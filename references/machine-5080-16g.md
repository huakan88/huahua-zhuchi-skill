# 机型档案 · RTX 5080 16GB（新机）

> 建立于 2026-11-14，所有数字均为本机实测，不是推算。
> 另一台 8GB 的档案见 `machine-5060-8g.md`；**两台的参数不可互套**。

## 识别

```powershell
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
# NVIDIA GeForce RTX 5080, 16303 MiB
Test-Path 'F:\AI\ComfyUI_windows_portable\python_embeded\python.exe'   # True
```

## 环境

| 项 | 值 |
|---|---|
| CPU / RAM | Ryzen 5 9600X / 32GB |
| 磁盘 | F 盘 NVMe（约 300GB 可用） |
| ComfyUI | `F:\AI\ComfyUI_windows_portable`，0.45.0 |
| Python | portable 3.13.14 |
| PyTorch | 2.14.1+cu130（cu130 已验证可用） |
| 引擎 | dynamic VRAM + `--fast-disk` + `--cache-none` |
| 启动 | `python_embeded\python.exe -s ComfyUI\main.py --fast-disk --cache-none --disable-partner-nodes --listen 127.0.0.1 --port 8188` |
| FFmpeg | `F:\AI\VideoTools\ffmpeg\ffmpeg-9.0.2-essentials_build\bin`（**9.x，无 `-vsync`**） |
| Real-ESRGAN | `F:\AI\VideoTools\esrgan\realesrgan-ncnn-vulkan.exe` |
| 口型 QC | `F:\AI\VideoTools\quality-python`（mediapipe 1.2.3）+ `face_landmarker.task` |

## 权重（GiB）

| 文件 | 体积 |
|---|---|
| `minimax_h3_image_pruned_w4a8` | 11.69 |
| `minimax_h3_fl2va_pruned_w6a8` | 14.89 |
| `qwen3vl_32b_minimax_h3_nvfp4_awq` | 14.61 |
| `minimax_h3_image_vae_fp16` | 1.09 |
| `minimax_h3_video_vae_int8_convrot` | 2.62 |
| `minimax_h3_audio_vae_fp32` | 0.56 |
| `seedvr2_3b_int8_convrot` | 3.22 |

合计约 **32.5GB**，正好压在「32GB RAM + 16GB VRAM」的总池上——这是能跑起来的原因，不是显卡特别快。

## 实测数据（2026-11-14）

| 项目 | 分辨率 | 步数 | 耗时 | 显存峰值 |
|---|---|---|---|---|
| H3-Image | 2048²（4MP） | 6 | 21.03 s | 15,475 MiB |
| H3-Image | 4096²（16MP） | 6 | 57.21 s | 15,500 MiB |
| H3 视频 | 864×480×124 | 20 | 120.9 s | 15,411 MiB |
| H3 视频 | 1344×768×124 | 20 | 515.0 s | 15,539 MiB |
| 图生视频 | 1344×768×124 | 20 | 535.2 s | 15,501 MiB |
| 主持人出画 | 576×1024 | 20 | 2.0–2.9 s/帧 | ~15.4G |
| 超分（批量） | 576→1080 | — | **0.79–0.92 s/帧** | — |
| 超分（逐帧） | 576→1080 | — | 2.8 s/帧 | — |
| 8G 预算压测 | 2048² | 6 | 39 s 后崩溃 | 10,165 MiB |

**关键结论**：显存峰值由**权重体积**决定，与分辨率关系很小（4MP 与 16MP 都是 15.5G）。所以「跑多大图」不是主要瓶颈，「能不能把权重塞进去」才是。

## 目录约定（本机）

```
F:\AI\Videos\<slug>-<date>\
├─ script/timeline.json        配音实测时间轴（from/frames/subs 全用绝对帧）
├─ audio/                      分段 wav + narration.wav + mix.wav
├─ gen/renoise-<id>.mp4        576×1024 原始出画
├─ gen_up/renoise-<id>.mp4     超分后 1080×1920（仅全屏段）
├─ qa/<id>/landmarks/          口型帧条与曲线
└─ remotion/                   Remotion 4.0.534 工程
```

## 踩过的坑（都在本机复现过）

1. **`-s 2` 出九宫格**：`realesrgan-ncnn-vulkan -s 2 -t 0` 输出 3×3 错位拼图 → 只用 `-s 4`。
2. **逐帧调用慢 3.5 倍**：改成目录批量（`upscale_batch.py`）。
3. **FFmpeg 9 没有 `-vsync`**：老脚本 `-vsync 0` 直接报错 → `-fps_mode passthrough`。
4. **Comfy 挂在临时终端会被会话重启带走**：用独立进程启动。
5. **`--reserve-vram 8` 不能模拟小卡**：它只是压预算，实测直接 OOM 崩进程。
6. **不写台词时首段会静嘴约 2 秒**：提示词里写 `Exact spoken dialogue: ...` + `never a fixed smile` 后消失。
7. **不锁构图时中段会推近切头顶**：写 `framing identical for the whole clip / whole head inside the frame / no zoom`。
8. **PowerShell `Set-Content` 会写 BOM**：手工改 `episode.json` 要用 Python 写 `encoding='utf-8'`，否则 Remotion 报 `Unexpected UTF-8 BOM`。

## 一期的时间预算（无样张验证）

| 环节 | 时间 |
|---|---|
| 配音（ViVi，逐句） | 1–2 分钟 |
| 出画（约 700 帧 @12 步） | ~18 分钟 |
| 全屏段批量超分（约 330 帧） | ~5 分钟 |
| Remotion 渲染 1080×1920 | 6–8 分钟 |
| 合计 | **30–35 分钟** |

对照：2026-11-14 第一期按旧方式（全部逐帧超分、含小窗段）用了约 90 分钟。
