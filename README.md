# 一天一个 GitHub · 花花主持竖版

Skill id：`huahua-zhuchi-skill`（https://github.com/huakan88/huahua-zhuchi-skill）

## 何时用
「一天一个 GitHub」竖版口播、花花出镜：开场/收束真全屏数字人、中段 FullBleed、本机 H3 真对口。

## 机型档案（开工先认机）
同一套 skill 跑两台机器，**参数不可互套**；SKILL.md 开头有识别命令与差异表。

| 档案 | 显卡 | ComfyUI | 参考 |
|---|---|---|---|
| `5080-16G` | RTX 5080 16GB / 32GB RAM | `F:\AI\ComfyUI_windows_portable` | `references/machine-5080-16g.md` |
| `5060-8G` | RTX 5060 8GB（TX-HK） | `E:\minimax H3` + `start_h3_hangsafe.bat` | `references/machine-5060-8g.md` |

关键差异：5080 用 **576×1024 出画 + 目录批量超分（0.79–0.92 s/帧）**，一期约 30–35 分钟；
5060 用 704×1280 优先、逐帧超分，单段 7–12 分钟。

## 定妆资产 `assets/looks/`
每套统一交付：
- `host_look.jpg` — **唯一**半身正视锁定图（头正直看镜头）
- `7view-sheet.jpg` — 16:9 七视图（黑底横排 Front|3/4 F|Side L|3/4 B|Back|Side R|Top）

| 目录 | 说明 |
|------|------|
| `look-00-body-base/` | 黑蕾丝内衣换衣基准（不是裸体）；七视下装肉色内裤 |
| `look-01-white-tank/` | **默认**。`host_look-user-preferred-20261104.jpg` = `host_look.jpg`（md5 `67c564964aa0c4535cc7ec11da6ec20f`）；另含 `host_look-canonical.jpg` / `host_ref-canonical.jpg` 历史脸锁 |
| `look-02-black-turtleneck/` | 黑高领 |
| `look-03-street-chic/` | 年轻街头（奶茶染发 + 标准白棒球衫 jersey） |
| `look-04-blazer/` | 西装外套 |
| `look-05-sexy-evening/` | 黑缎绸吊带（性感女人味） |
| `look-06-lululemon-yoga/` | 无 logo 贴身瑜伽套装（露腰 crop + 高腰裤） |
| `look-07-dress/` | 日常优雅藕粉裙 + 半扎大波浪 |

**硬锁（侃华 2026-11-04 已锁定）**：同一张脸，脸锁 preferred；左胸小痣（观众右）露胸口必留；头大小/胸量对齐 look-01 preferred；七视下装=肉色内裤；半身禁固定右歪头；七视先于本机 H3 真对口。

## 仓库内容
- `SKILL.md` — 完整流程与硬规则
- `assets/looks/` — look-00 换衣基准 + look-01～07 定妆（半身+七视）
- 本 README

成片与中间产物不放本仓。其他 Agent 可直接 clone / 引用本仓 `assets/looks/<look>/host_look.jpg`。
