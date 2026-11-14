# 机型档案 · RTX 5060 8GB（旧机 · TX-HK）

> 这是 SKILL.md 正文里带「TX-HK」字样的规则所对应的机器。
> 新机（RTX 5080 16GB）见 `machine-5080-16g.md`；**参数不可互套**。

## 识别

```powershell
Test-Path 'E:\minimax H3\venv\Scripts\python.exe'   # True → 本机
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader   # 显存 ≈8GB
```

## 环境

| 项 | 值 |
|---|---|
| 显卡 | NVIDIA RTX 5060，8GB |
| ComfyUI | `E:\minimax H3`（含 `venv`） |
| 启动 | **`start_h3_hangsafe.bat`**（t893 唯一默认；不要用 pybase 3.13，勿再直跑旧 nosage/t874 bat） |
| 模型 | 裁剪 int8 小模型，**不是** 65GB 全量版 |

## 关键限制

- **704×1280 在 7 秒以上片段会 torch OOM** → 优先 576×1024。
- 显存只有 8GB：**不要预加载 VoxCPM / 其它 TTS 服务**，会和 H3 抢显存把 Comfy 拖不稳。
- Comfy 稳定运行时不要杀、不要重启；只杀确认无用的 TTS 进程。
- 开跑前查 `nvidia-smi`：**GPU-Util 长时间 0% 即假跑**，要去查掉线/崩溃，不要干等。

## 排期基线

- 单段出画约 **7–12 分钟**。
- 一支 4 段约 **25–35 分钟**，加 Remotion 约 10 分钟。

## 超分

沿用逐帧脚本（本机验证过的路径）：

```bash
python <skill>/scripts/upscale_segments.py s1 s7 s16
python <skill>/scripts/upscale_segments.py --all
```

- 参数与两台通用：`x4plus` + `-t 0` → lanczos 1080×1920 → `cas=0.35` → CRF16。
- 若该机 FFmpeg 升级到 9.x，脚本里的 `-vsync 0` 会报错，需换成 `-fps_mode passthrough`；
  不想动脚本时直接用 `upscale_batch.py`（同样参数，只是改成目录批量）。

## 与 5080 的差异速查

| 项 | 5060-8G | 5080-16G |
|---|---|---|
| 交付分辨率 | 704×1280 优先，显存不够才 576×1024 | 576×1024 出画 + 超分 |
| 704×1280 可行性 | 7 秒以上会 OOM | 可跑（更慢） |
| 超分方式 | 逐帧 `upscale_segments.py` | 目录批量 `upscale_batch.py` |
| 启动方式 | `start_h3_hangsafe.bat` | `main.py --fast-disk --cache-none` |
| 服务器 | E 盘 | F 盘 portable |
