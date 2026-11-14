#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""整目录批量超分（RTX 5080-16G 用；比逐帧调用快约 3.5 倍）。

为什么快：realesrgan-ncnn-vulkan 每启动一次就要重新初始化 GPU，逐帧调用时
**进程启动开销占大头**（实测 2.8 s/帧）；把整段帧交给一次目录调用后是 0.79–0.92 s/帧。

为什么必须 -s 4：本机这版 ncnn 二进制传 -s 2 会输出 3×3 错位九宫格
（2026-11-14 实测踩坑）。4 倍放大后用 Lanczos 缩到目标尺寸，别指望降倍数提速。

用法：
    python <skill>/scripts/upscale_batch.py --src gen/renoise-s2.mp4 --out gen_up/renoise-s2.mp4 --work tmp_up/s2

工具定位顺序：--esrgan / $HK_ESRGAN / <skill>/tools/esrgan/ / 工程 tools/esrgan/
FFmpeg：--ffmpeg / $HK_FFMPEG / PATH 上的 ffmpeg
"""
import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SKILL = Path(os.environ.get("HK_PRESET") or Path(__file__).resolve().parent.parent).resolve()
PROJ = Path(os.environ.get("HK_PROJECT") or Path.cwd()).resolve()


def find_esrgan(override=None):
    for candidate in ([override] if override else []) + [
        os.environ.get("HK_ESRGAN"),
        str(SKILL / "tools" / "esrgan" / "realesrgan-ncnn-vulkan.exe"),
        str(PROJ / "tools" / "esrgan" / "realesrgan-ncnn-vulkan.exe"),
    ]:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    sys.exit("找不到 realesrgan-ncnn-vulkan.exe；设 HK_ESRGAN 或跑 scripts/fetch_esrgan.py")


def find_ffmpeg(override=None):
    for candidate in ([override] if override else []) + [os.environ.get("HK_FFMPEG")]:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    found = shutil.which("ffmpeg")
    if not found:
        sys.exit("找不到 ffmpeg；设 HK_FFMPEG 或把 ffmpeg 放进 PATH")
    return Path(found)


def run(cmd):
    result = subprocess.run([str(c) for c in cmd], capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        print("FAIL:", " ".join(str(c) for c in cmd)[:200])
        print((result.stderr or result.stdout)[-800:])
        raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--work", type=Path, required=True)
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1920)
    ap.add_argument("--sharp", type=float, default=0.35)
    ap.add_argument("--crf", type=int, default=16)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--esrgan")
    ap.add_argument("--ffmpeg")
    a = ap.parse_args()

    esrgan, ffmpeg = find_esrgan(a.esrgan), find_ffmpeg(a.ffmpeg)
    if a.out.exists():
        sys.exit(f"输出已存在，不覆盖：{a.out}")
    if a.work.exists():
        shutil.rmtree(a.work)
    (a.work / "up").mkdir(parents=True)

    # -fps_mode passthrough 等价于 FFmpeg 9 之前的 -vsync 0
    run([ffmpeg, "-v", "error", "-y", "-i", a.src, "-fps_mode", "passthrough",
         "-frame_pts", "1", a.work / "%05d.png"])
    frames = sorted(a.work.glob("*.png"))
    if not frames:
        sys.exit("没有抽到帧")

    print(f"{len(frames)} 帧 → 批量 x4 (tile=0)", flush=True)
    started = time.time()
    run([esrgan, "-i", a.work, "-o", a.work / "up", "-n", "realesrgan-x4plus",
         "-s", "4", "-t", "0", "-f", "png"])
    spent = time.time() - started
    print(f"超分完成 {spent:.0f}s（{spent / len(frames):.2f} s/帧）", flush=True)

    vf = (f"scale={a.width}:{a.height}:flags=lanczos"
          + (f",cas=strength={a.sharp}" if a.sharp > 0 else "")
          + ",format=yuv420p")
    run([ffmpeg, "-v", "error", "-y", "-framerate", str(a.fps), "-i", a.work / "up" / "%05d.png",
         "-i", a.src, "-map", "0:v:0", "-map", "1:a:0", "-vf", vf,
         "-c:v", "libx264", "-crf", str(a.crf), "-preset", "slow",
         "-c:a", "copy", "-shortest", "-movflags", "+faststart", a.out])
    print(f"✓ {a.out}  {a.out.stat().st_size / 1048576:.2f} MB  {a.width}x{a.height}", flush=True)
    shutil.rmtree(a.work)


if __name__ == "__main__":
    main()
