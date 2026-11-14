---
name: huahua-zhuchi-skill
description: 做「一天一个 GitHub」竖版口播（花花出镜）时用：开场与收束真全屏数字人、中段 FullBleed 闪回、本机 H3 真对口、头/肩须有动感；口播先过眼。开工先认机型（RTX 5080 16GB / RTX 5060 8GB，参数不同不可互套）。多套定妆见 assets/looks。
---

# 一天一个 GitHub · 花花主持竖版

与口播全流程 skill（`skill-1791809256290`）配套；冲突时以用户当次指令为准。公共底座 `skill-1792547224096`。

## 系列
一天拆一个有意思的 GitHub：开场点题 → 亮点 → 怎么用 → 实测 → CTA。
`channelLabel` 默认「AI 速递 · 一天一个 GitHub」。**口播稿先交侃华过眼**再配音成片。
口播收束可自称「我是花花」；**禁止**把系列/角标写死成「花花聊科学 / 花花讲科学」。

## 机型档案（开工第一步：先识别，再选参数）

同一套 skill 跑在两台机器上，**参数、路径、耗时全都不同**。不许把一台机器的数字套到另一台上。

| 档案 | 显卡 | 显存 | 宿主 | ComfyUI | 启动方式 |
|---|---|---|---|---|---|
| **`5080-16G`**（新） | RTX 5080 | 16GB | 32GB RAM，F 盘 NVMe | `F:\AI\ComfyUI_windows_portable`（portable 0.45.0 / Py3.13 / torch2.14 cu130） | `.bat` 或 `main.py --fast-disk --cache-none`，默认 dynamic VRAM |
| **`5060-8G`**（旧 · TX-HK） | RTX 5060 | 8GB | E 盘 | `E:\minimax H3` + `venv` | **`start_h3_hangsafe.bat`**（t893 唯一默认） |

### 识别命令（两条都要看）

```powershell
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
Test-Path 'F:\AI\ComfyUI_windows_portable\python_embeded\python.exe'   # True → 5080-16G
Test-Path 'E:\minimax H3\venv\Scripts\python.exe'                      # True → 5060-8G
```

- `NVIDIA GeForce RTX 5080, 16303 MiB` → **`5080-16G`**
- 显卡名含 `5060` 或显存 ≈8GB → **`5060-8G`**
- 两条路径都为假 → **停机问华侃**，不要猜着跑。

### 两档的默认参数差异

| 项 | `5080-16G` | `5060-8G` |
|---|---|---|
| 出画分辨率 | **576×1024**（实测够用）；704×1280 可跑但更慢 | **704×1280 优先**，显存不够才 576×1024；7 秒以上片段会 OOM |
| 步数 | 20（交付档）；12 可提速（下限 ≥8，非 turbo） | ≥8，显存紧 ≥6 |
| 生成耗时 | **2.0–2.9 s/帧 @20 步**（实测 345 帧≈17 分钟） | 单段 7–12 分钟（裁剪 int8 小模型） |
| 超分 | **整目录批量** + `-s 4`，**0.79–0.92 s/帧**（见下节） | `upscale_segments.py`（逐帧） |
| 小窗段 | **不超分**（PiP 仅 304×410，576 宽原片够） | 同左 |
| 一期权预算 | 无样张验证时 **30–35 分钟** | 4 段约 25–35 分钟 + Remotion 10 分钟 |

> 详细档案：`references/machine-5080-16g.md`、`references/machine-5060-8g.md`。本文件正文里带「TX-HK」字样的规则默认只适用于 `5060-8G`。

## 定妆（多套）
资产目录：`assets/looks/<look-id>/`

| look-id | 服装 | 半身 | 七视 |
|---------|------|------|------|
| `look-00-body-base` | 黑蕾丝内衣换衣基准（不是裸体；七视下装肉色内裤） | `assets/looks/look-00-body-base/host_look.jpg` | `assets/looks/look-00-body-base/7view-sheet.jpg` |
| `look-01-white-tank`（**默认**） | 白罗纹背心 | `host_look.jpg` | `7view-sheet.jpg` |
| `look-02-black-turtleneck` | 黑高领 | 同上 | 同上 |
| `look-03-street-chic` | 年轻街头：奶茶染发 + 标准白棒球衫 jersey（罗纹领口+排扣开襟短款） | 同上 | 同上 |
| `look-04-blazer` | 西装外套 | 同上 | 同上 |
| `look-05-sexy-evening` | 黑缎绸吊带（性感女人味） | 同上 | 同上 |
| `look-06-lululemon-yoga` | 无 logo 贴身瑜伽（露腰 crop + 高腰裤） | 同上 | 同上 |
| `look-07-dress` | 日常优雅藕粉裙 + 半扎大波浪 | 同上 | 同上 |

### 硬锁
**定妆已锁定（侃华 2026-11-04）**：本套半身 + 七视「非常好，固定」。锁脸/锁头胸对照 look-01：`host_look-user-preferred-20261104.jpg`（= 同目录 `host_look.jpg`，md5 `67c564964aa0c4535cc7ec11da6ec20f`）。七视下装=肉色内裤；头大小/胸量对齐该 preferred。禁擅自改定妆；禁推仓除非项目总管放行。

1. **同一张花花脸**：禁换脸。现行 preferred：look-01 `host_look-user-preferred-20261104.jpg`（= `host_look.jpg`）。历史脸锁仍存 `host_look-canonical.jpg` / `host_ref-canonical.jpg`。
2. **左胸小痣（观众右侧）**：凡露锁骨/胸口的半身与七视正视/3/4 **必须保留**，绝不能少。
3. **半身统一模板**：每套只交付一张正视锁定图 `host_look.jpg`（头正直看镜头）；禁固定右歪头；勿再并存 natural 变体作交付；**头大小与胸量肉眼对齐 look-01 preferred**。
4. **七视先于 H3**：新 look / 换装须先有 `7view-sheet.jpg`（16:9 黑底横排 Front|3/4 F|Side L|3/4 B|Back|Side R|Top，中性站姿；**下装=肉色内裤**，非瑜伽裤/黑短裤）再喂本机 H3。

默认出画基准：`assets/looks/look-01-white-tank/host_look.jpg`（= preferred；路径可仍兼容旧名 vivi-zhuchi `host_look.jpg` 的用法：复制或软链到工程 assets）。

## 对口
- **本机 MiniMax H3** + lipsync_repair；|lag|≤2（corr&lt;0.4 勿采信）。
- 音频硬锚定（两台机通用）：`MiniMaxH3AddGuide(frame_idx=0)` 给音频条件，再用
  `VAEEncodeAudio → 零噪声 mask → LTXVConcatAVLatent` 把旁白 latent 冻结；导出后**重新 mux 原旁白**，不用模型重生成的声音。
- 提示词里**把实际台词写进去**（`Exact spoken dialogue: ...`）并加 `never a fixed smile`：`5080-16G` 实测这样首句就有口型；只靠音频不给文本时，首段出现过约 2 秒静嘴。
- 全屏段要写死「framing identical for the whole clip / whole head inside the frame / no zoom」：不写时模型会在中段推近，把头顶切掉。
- **禁** Grok i2v / 云端假对口交付。云端只配音/素材/Remotion。
- 布局改版可只重拼 Remotion，复用已过关 H3 与旁白。

## 超分（**交付必做**）

出画完 → 超分（**仅全屏段**）→ 再进 Remotion。

**`5080-16G`：整目录批量（3.5 倍速）**
```bash
python <skill>/scripts/upscale_batch.py --src gen/renoise-s02.mp4 --out gen_up/renoise-s02.mp4 --work tmp_up/s02
```
- 一次调用处理整段帧，实测 **0.79–0.92 s/帧**；逐帧调用是 **2.8 s/帧**，差别全在进程启动开销。
- **必须 `-s 4`**：本机这版 `realesrgan-ncnn-vulkan` 传 `-s 2` 会输出 **3×3 错位九宫格**（已实测踩坑，2026-11-14）。放大 4 倍后 Lanczos 缩到 1080×1920 即可，别指望降倍数提速。
- 小窗段（PiP）**不要超分**：窗口只有 304×410，576×1024 原片已经够，白跑一遍等于每人多花 10–25 分钟。

**`5060-8G`：沿用逐帧脚本**
```bash
python <skill>/scripts/upscale_segments.py s1 s7 s16     # 指定段
python <skill>/scripts/upscale_segments.py --all          # 全部出画段
```

**两台通用**
- 出画 576×1024 → Real-ESRGAN `x4plus` + **`-t 0`** → lanczos 1080×1920 → `cas=0.35` → CRF16，音轨一并 mux。
- 输出在 `gen_up/renoise-<id>.mp4`，**已是 1080×1920**。包装层 **1:1 直接铺，不要再缩放**。
- **三个坑**：① tile 不关会拼成错位碎块 → 必须 `-t 0`；② `realesr-animevideov3` 用在真人脸上出描边 → 只用 `x4plus`；③ x4plus 磨毛孔 → 接 `cas=0.35`，别上强锐化。
- **FFmpeg 9 起 `-vsync` 已移除**，老脚本里的 `-vsync 0` 要换成 `-fps_mode passthrough`（等价）。
- 超分后重跑一次 `sync_pic.py` / `qc_landmarks.py`：确认没把口型弄糊。
- Real-ESRGAN 装在 `tools/esrgan/`（**不入 Git 仓**）；换机器跑 `python <skill>/scripts/fetch_esrgan.py`。

## 画面（handraw v3/v4）
| 段 | 布局 |
|----|------|
| 开场 | 数字人**真全屏**（禁椭圆大窗叠底） |
| 正文 | 证据卡 + 左下椭圆 pip |
| 中段 | ≥1–2 处素材 **FullBleed**（dh 可 hide） |
| **收束** | 与开场同：**真全屏**；CTA/仓库字轻叠 |

头或肩须有可见动感（优先 H3 头动；必要时仅数字人层极轻微动）。禁底板 Ken Burns/pan/sin。−16 LUFS。

## 参考工程
`/workspace/handraw-style-vertical-2026-10-31/`（Vertical：`dh: fullscreen|pip|hide`，`kind: fullbleed`）。

---

# 本机硬规补丁（装仓后保留 · 勿丢）

## 画质标杆（华侃 2026-11-01 · 硬节）
**人像自然度 / 清晰度基准片**：`/workspace/shared/content/huahua-debug-2026-11-01/athenaion-vertical.norm.mp4`（早期 athenaion 成片，look-01）。开场/收束真全屏人物须达到该片的皮肤质感、发丝边缘、口型区清晰度与整体自然度；近期偏糊、偏蜡、偏软的交付不合格。

对照诊断与门禁：`/workspace/shared/content/huahua-debug-2026-11-01/DIAGNOSIS.md`、`QUALITY-GATE.md`；并排图 `contact-early-vs-recent.jpg`。

### 衣柜不砍
look-00～look-07 **全部保留**。本节能改的是**画质与生成/编码参数**，不是衣服套数。

### 默认 H3 交付档

**`5080-16G`（新机 · 实测）**

| 项 | 交付默认 | 说明 |
|----|----------|------|
| 分辨率 | **576×1024** 出画 → 批量超分 1080×1920 | 704×1280 可跑但更慢；原生 1344×768 已实测可跑（515 秒/5 秒片） |
| 步数 | **20**（交付）/ **12**（提速，下限 ≥8） | 不挂 turbo LoRA |
| 生成耗时 | 2.0–2.9 s/帧 @20 步 | 345 帧段约 17 分钟 |
| 超分 | 批量目录模式，`-s 4`，0.79–0.92 s/帧 | **仅全屏段**；小窗跳过 |
| 显存 | 峰值 15.0–15.2G（4MP/16MP/480p/1MP 视频都在这个区间） | 卡的是权重体积，不是分辨率 |
| 成片 | 1080×1920、8 Mbps、−16 LUFS、真峰 ≤−2 dBTP | 验收脚本 `verify_final.py` |

**`5060-8G`（旧机 · TX-HK）**

| 项 | 交付默认 | 禁止当交付默认 |
|----|----------|----------------|
| 分辨率 | 优先 **704×1280**（32 倍数，接近定妆 720×1280）；显存不够再用 **576×1024** | 再降到 384×576；用低分辨率出片后靠 Remotion 硬拉到 1080 当「修好了」 |
| 步数 / 模式 | **非 turbo**，`h3_steps` **≥8**（显存紧时 ≥6） | **turbo 4 步**当交付默认（仅草稿/试口型） |
| 原生片编码 | H3 落盘视频码率对标早期 ≈**1.9 Mbps@576×1024**（同分辨率勿压到 ~1.0 Mbps） | 过度压 raw gen |
| 帧率 | H3 与成片尽量同 fps；竖片 30fps 时优先 H3 24→注意不要二次柔化 | 多次转码放大 |
| 定妆 | `host_look.jpg` 保持清晰（现库 720×1280）；禁用发糊/过压 JPEG 当参考 | 低清 look 喂 H3 |
| 构图（开场/收束全屏） | 脸在画面中占比接近标杆（早期 selfie / 半身近景）；少留无效头顶空 | 头很小+大片墙面导致脸区像素不够 |
| Remotion | 成片视频码率对标标杆 ≈**4.3 Mbps@1080×1920**（≥4 Mbps）；DH `objectFit:cover` 只放大一次 | 成片压到 ~1.8 Mbps；576→1080 后再导出降码率；双重缩放+锐化堆积 |
| Prompt | 保留 `realistic skin pores` / `without beauty-filter smoothing` | 美颜/磨皮措辞 |

**草稿可**用 turbo 4 · 576×1024 试片；**过目审 / 上传前**必须按交付档重出或证明标杆对齐。

## 交付策略（t636u · 二选一）
开渲前选定其一，中途勿擅自改档：
1. **严格 skill**：全程交付档（优先 704×1280、非 turbo、`h3_steps`≥8、成片≥4Mbps）。
2. **先初步再超清**：初稿可低精度；**大头像（开场/收束全屏）超清重出或超分到标杆**；**小头像（缩小叠画）保持低精度即可**。超分不得当作「糊片硬拉」的唯一交付手段。

未点名策略时默认 **① 严格 skill**。华侃 t631u：本机只需 H3 数字人；demo/合片可上线。

## 真实感硬要求 + 本批制作规范（华侃 2026-11-01 t503u · **硬规，以后必须照做**）
华侃明确：这一次对**真实感**要求更强，是硬要求，不是建议。CF长风、ai-topic 两支重做所总结的规范如下，后续花花主持每一支都按此执行。

### A. 真实感（验收第一条）
- 人物必须像真人拍摄：皮肤有毛孔与自然起伏，不蜡、不塑料、不磨皮；发丝、睫毛、齿缝、唇缘可分；口型区不抹糊。
- 对照标杆 `athenaion-vertical.norm.mp4`：开场/收束真全屏抽 2 帧并排对比，皮肤/发丝/唇缘达不到 → **不交，返工**。
- 口型必须对准文字（H3 真对口 + 出片前验收，对不上就返工）；头/肩有自然动感。
- 提示词保留 `realistic skin pores`、`without beauty-filter smoothing`，禁美颜/磨皮措辞；构图用近景半身（selfie 式），脸占比接近标杆。
- 超分/修复只可作为**可选补充**：任何超分、人脸修复（GFPGAN/CodeFormer 类）如带来蜡感、塑料皮、唇区抹糊、帧间闪烁，一律不采用；**不得只靠超分把低清片当交付**。

### B. 生成与出片参数（交付档，不可降）
- H3：**不挂 turbo LoRA**（workflow 里不得出现 turbo_4step 等；sched/guider 直连 unet），`steps≥8`（显存紧 ≥6），优先 **704×1280**，否则 576×1024 且 raw 码率≈早期 1.9Mbps。
- 成片：Remotion 1080×1920，视频 **≥4 Mbps**（标杆 ~4.3；<2.5 必重导出），只放大一次，禁导出后再放大/叠锐化。
- turbo 4 / 低清只许草稿（试口型与节奏），**过目审、上传前必须交付档重出**。
- h3gen 已 patch：standard 不挂 LoRA（备份 `h3gen.py.bak_no_turbo`）；每次出片前先查 workflow 里没有 turbo 字符串。

### C. 执行纪律

**`5080-16G`**
- ComfyUI 在 `F:\AI\ComfyUI_windows_portable`，用 portable 的 `python_embeded\python.exe -s ComfyUI\main.py --fast-disk --cache-none --disable-partner-nodes --listen 127.0.0.1 --port 8188`。
- **用独立进程启动**（`Start-Process` 或常驻窗口），别只挂在临时终端里：会话一重启，Comfy 会跟着退出，白等一轮。
- 16GB + 32GB RAM，权重约 32.5GB 总量，**必须靠 dynamic VRAM + `--fast-disk` 分层**；峰值 15.0–15.2G 是正常状态，不要因为“顶满”去重启。
- 别用 `--reserve-vram 8` 之类的压力参数做“模拟小卡”：实测会直接把进程跑崩（9.9G 峰值处 OOM），那不是 8G 卡的真实表现。
- 配音、素材、Remotion 仍可云端；**数字人对口必须本机**。

**`5060-8G`（TX-HK）**
- Comfy 必须用 `E:\minimax H3\venv` + **`start_h3_hangsafe.bat`** 启动（t893 唯一默认；不要用 pybase 3.13，勿再直跑旧 nosage/t874 bat）。
- 开跑前查 `nvidia-smi`：排队≠在跑；**GPU-Util 长时间 0% 即假跑**，要查掉线/崩溃，而不是干等。
- 配音用线上 **ViVi**，**不要预加载 VoxCPM / TTS 服务占显存**（8GB 卡，H3 与 Vox 争显存会让 Comfy 不稳）；除非华侃点名用 huakan 克隆音色。
- Comfy 已在稳定跑时**不要杀、不要重启**；只杀确认无用的 TTS 进程。
- 本机显卡仅 8GB、装的是裁剪 int8 小模型，不是 65GB 全量版，排期按此估算（单段约 7–12 分钟，一支 4 段约 25–35 分钟 + Remotion ~10 分钟）。

### D. 交付前自检（缺一不交）
1. workflow 无 turbo；steps≥8；分辨率 704×1280 或已书面说明。
2. 开场/收束抽帧对标杆并排：真实感 OK。
3. 口型对齐验收通过；ViVi 读音准、有情绪。
4. 成片码率≥4Mbps@1080；无「内容由数字人演绎」类角标；缩小画幅无框、露上半身。
5. 回报只给：成片路径 + 码率 + 一句话结果。

## 构图长期规则（本机补丁）
穿搭出镜一律严格模仿最早白背心标杆片 athenaion——只换衣服，构图/近景比例/暖侧光/微侧头/说话表情/叠画方式照抄。详见 `/workspace/shared/content/STANDING-huahua-framing.md`。

缩小叠画：用框子框住、不抠像；框内背景与数字人原背景一致（白底）；开场收束真全屏。


## 配音（华侃 2026-11-01）
- 系列固定 **ViVi**，不必每次再问。
- 普通话必须读准（勿把「满」念成「蛮」等错读）。
- 语气要有感情、有情绪起伏，不要平铺太满。

### VoxCPM 禁令（华侃 2026-11-01 t510u · **硬规**）
- **除非华侃明确点名要用 huakan 克隆音色**，否则 **一律禁止** 启动 / 预加载 / 占用显存的 VoxCPM（含 `tts_server.py --preload`、任何本机 Vox 进程）。
- 花花系列配音默认 **线上 ViVi**；开 H3 / Comfy 前必须确认无 Vox 进程（`nvidia-smi` / 任务管理器）。发现占用 → 先杀再渲。
- 本条写入后仍违规视为交付事故。

## t520u 缩小叠画硬规（2026-11-01）
- 缩小后的数字人不得有任何框：含透明底板、遮罩、空白边；需抠像/裁到人物轮廓后直接叠在画面上。
- 缩小尺寸 = 此前缩小尺寸的 1/2；仍须半身、露上半身。

## 【最新·t99u 2026-11-01】缩小叠画规则（覆盖此前「无框/抠像」）
- 数字人缩小后用框子框住再叠画面，不要抠像（抠图显傻）。
- 框内背景保持与数字人原背景一致（如白底）。
- 仍尽量露出上半身；开场收束仍真全屏。已交片不重做除非点名。
