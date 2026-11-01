---
name: huahua-zhuchi-skill
description: >-
  做「一天一个 GitHub」竖版口播（花花出镜）时用：开场与收束真全屏数字人、中段 FullBleed 闪回、本机 H3
  真对口、头/肩须有动感；口播先过眼。多套定妆见 assets/looks（默认 look-01 白背心）。
---
# 一天一个 GitHub · 花花主持竖版

与口播全流程 skill（`skill-1791809256290`）配套；冲突时以用户当次指令为准。公共底座 `skill-1792547224096`。

## 系列
一天拆一个有意思的 GitHub：开场点题 → 亮点 → 怎么用 → 实测 → CTA。
`channelLabel` 默认「AI 速递 · 一天一个 GitHub」。**口播稿先交侃华过眼**再配音成片。
口播收束可自称「我是花花」；**禁止**把系列/角标写死成「花花聊科学 / 花花讲科学」。

## 定妆（多套）
资产目录：`assets/looks/<look-id>/`

**默认出画是 look-01 白罗纹背心**：`assets/looks/look-01-white-tank/host_look.jpg`。旧工程若仍找 `vivi-zhuchi` / `host_look.jpg`，从该文件复制或软链，不要另造一张脸。

每套已入库 look 只有两张交付图（look-01 另附历史脸锁，见下）：

- `host_look.jpg` — **一张**正视半身（头正直看镜头）
- `7view-sheet.jpg` — 16:9 黑底横排七视：Front | 3/4 F | Side L | 3/4 B | Back | Side R | Top，中性站姿

| look-id | 路径 | 服装 | 状态 |
|---------|------|------|------|
| `look-00-body-base` | `assets/looks/look-00-body-base/` | **性感内衣**换衣基准 | **待替换**（目录在，图未入库） |
| `look-01-white-tank`（**默认**） | `assets/looks/look-01-white-tank/` | 白罗纹背心 | 已入库 |
| `look-02-black-turtleneck` | `assets/looks/look-02-black-turtleneck/` | 黑高领 | 已入库 |
| `look-03-street-chic` | `assets/looks/look-03-street-chic/` | 年轻街头：奶茶染发 + 白短外套/白 Tee | 已入库 |
| `look-04-blazer` | `assets/looks/look-04-blazer/` | 西装外套 | 已入库 |
| `look-05-sexy-evening` | `assets/looks/look-05-sexy-evening/` | 黑缎绸吊带 | 已入库 |
| `look-06-lululemon-yoga` | `assets/looks/look-06-lululemon-yoga/` | 无 logo 贴身瑜伽（露腰 crop + 高腰裤） | 已入库 |
| `look-07-dress` | `assets/looks/look-07-dress/` | 日常优雅藕粉裙 + 半扎大波浪 | 已入库 |

look-01 历史脸锁（只作参考，交付仍用 `host_look.jpg`）：

- `assets/looks/look-01-white-tank/host_look-canonical.jpg`
- `assets/looks/look-01-white-tank/host_ref-canonical.jpg`

### look-00（待替换）
侃华改口：**不要裸体，也不要肉色无缝连体。** look-00 改为性感内衣换衣基准。

本仓没有收录旧版肉色无缝半身，也没有灰 mocap 七视。真裸被图像策略拦截；肉色无缝是被否决的替代，不是情色裸图，也不再使用。父代理随后附上 lingerie 的 `host_look.jpg` 与 `7view-sheet.jpg` 后，再放入 `assets/looks/look-00-body-base/`。图到位前不要用 look-00 出画，默认 look-01。

### 硬锁
1. **同一张花花脸**：禁换脸。历史脸锁参考仅 look-01 的两张 canonical。
2. **左胸小痣（观众右侧）**：凡露锁骨/胸口的半身与七视正视/3/4 **必须保留**，绝不能少。
3. **每套只一张正视 `host_look.jpg`**：头正直看镜头；禁固定右歪头；勿再并存 natural 变体作交付。
4. **七视先于 H3 / Ref2VA**：新 look / 换装须先有 `7view-sheet.jpg`，再喂本机 H3 或 Ref2VA。没有七视不要开对口或换装。

## 对口
- TX-HK **本机 MiniMax H3** + lipsync_repair；|lag|≤2（corr&lt;0.4 勿采信）。
- **禁** Grok i2v / 云端假对口交付。云端只配音/素材/Remotion。
- 布局改版可只重拼 Remotion，复用已过关 H3 与旁白。

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
