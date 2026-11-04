---
name: huahua-zhuchi-skill
description: 做「一天一个 GitHub」竖版口播（花花出镜）时用：开场与收束真全屏数字人、中段 FullBleed 闪回、本机 H3 真对口、头/肩须有动感；口播先过眼。多套定妆见 assets/looks。
---

# 一天一个 GitHub · 花花主持竖版

与口播全流程 skill（`skill-1791809256290`）配套；冲突时以用户当次指令为准。公共底座 `skill-1792547224096`。

## 系列
一天拆一个有意思的 GitHub：开场点题 → 亮点 → 怎么用 → 实测 → CTA。
`channelLabel` 默认「AI 速递 · 一天一个 GitHub」。**口播稿先交侃华过眼**再配音成片。
口播收束可自称「我是花花」；**禁止**把系列/角标写死成「花花聊科学 / 花花讲科学」。

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
**定妆已锁定（侃华 2026-11-04）**：本套半身 + 七视「非常好，固定」。锁脸/锁头胸对照 look-01：`host_look-user-preferred-20261104.jpg`（= 同目录 `host_look.jpg`，md5 `44385332ae3f6a7e6aff9ca423f92ee1`）。七视下装=肉色内裤；头大小/胸量对齐该 preferred。禁擅自改定妆；禁推仓除非项目总管放行。

1. **同一张花花脸**：禁换脸。现行 preferred：look-01 `host_look-user-preferred-20261104.jpg`（= `host_look.jpg`）。历史脸锁仍存 `host_look-canonical.jpg` / `host_ref-canonical.jpg`。
2. **左胸小痣（观众右侧）**：凡露锁骨/胸口的半身与七视正视/3/4 **必须保留**，绝不能少。
3. **半身统一模板**：每套只交付一张正视锁定图 `host_look.jpg`（头正直看镜头）；禁固定右歪头；勿再并存 natural 变体作交付；**头大小与胸量肉眼对齐 look-01 preferred**。
4. **七视先于 H3**：新 look / 换装须先有 `7view-sheet.jpg`（16:9 黑底横排 Front|3/4 F|Side L|3/4 B|Back|Side R|Top，中性站姿；**下装=肉色内裤**，非瑜伽裤/黑短裤）再喂本机 H3。

默认出画基准：`assets/looks/look-01-white-tank/host_look.jpg`（= preferred；路径可仍兼容旧名 vivi-zhuchi `host_look.jpg` 的用法：复制或软链到工程 assets）。

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
