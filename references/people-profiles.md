# 人员档案库（People Profiles）

> 目的：减少重复联系人检索成本。  
> 原则：本文件用于加速匹配，最终写入前仍需具备并可调用 contacts MCP 做校验。

## 字段说明
- `姓名`：中文名
- `常用称呼`：英文名/昵称
- `角色`：在项目协作中的常见角色
- `项目`：常见参与项目
- `open_id` / `user_id`：用于 Feishu 人员字段写入
- `邮箱`：已知邮箱
- `最后更新`：最近校验日期

## 档案
| 姓名 | 常用称呼 | 角色 | 项目 | open_id | user_id | 邮箱 | 最后更新 |
|---|---|---|---|---|---|---|---|
| 王小婷 | Ada | 产品/项目负责人 | RedMagic | `ou_e760b3dc2ba3db6ff73f8a8ad01a3ee4` | `g47924fg` | `ada.wang@fstln.io` | 2026-03-03 |
| 潘贵洪 | David | 产品/配置 | ANTA/Hypershell | `ou_9aeceff4aa19503f3789100f197ab44b` | `d459e2db` | `david.pan@fstln.io` | 2026-03-03 |
| 刘佳莹 | Vicky | 设计 | ANTA | `ou_3c9f893887c9ddd409a142ba16566397` | `b1aba19g` | `vicky.liu@fstln.io` | 2026-03-03 |
| 周嵩 | Gavin | 设计 | ANTA/Hypershell | `ou_92b220f85a0b8a99622ae1aec26d30bf` | `g8a79646` | `gavinzhou@fstln.io` | 2026-03-03 |
| 廖东林 | Cotton | 开发 | ANTA | `ou_eb832378558cf77dc33771c49856e812` | `gfbc4e16` | `cotton@fstln.io` | 2026-03-03 |
| 徐炜健 | Roy | 开发 | RedMagic | `ou_1a2a93cdde80f254698149073ab08ab7` | `cd1bgaf4` | `roy.xu@fstln.io` | 2026-03-03 |
| 黄钰 | Maggie/麻吉 | 设计 | RedMagic | `ou_c037869f3e214afb423a9181bd29dc8d` | `3c8a81ab` | `maggie@fstln.io` | 2026-03-03 |
| 胡超 | Stan | 测试 | ANTA/RedMagic | `ou_4690ebb5dbef1124f951c2b48fb491f9` | `2558384e` | `stan@fstln.io` | 2026-03-03 |
| 周智莉 | Tammy | 多语言配置 | ANTA | `ou_9e033cd187e9e8bde488098bbbf493f7` | `2fg326e3` | `tammy.zhou@fstln.io` | 2026-03-03 |
| 严思雯 | Winsy | 开发 | RedMagic | `ou_c43a94c7a227ef1431dc47345f74ad24` | `e878b5ab` | `winsy@fstln.io` | 2026-03-03 |
| 肖荣健 | Xiao | 测试 | RedMagic/Hypershell | `ou_7ef1de7929e2e2e31a0d82387a5bedff` | `58585f94` | （待补） | 2026-03-03 |
| 刘思 | Sally | 需求方 | ANTA | `ou_879809a9accf24e7e139c111a68bbc93` | `8g27fg1f` | `sally.liu@fstln.io` | 2026-03-03 |
| 钟文清 | Nina | 需求方 | RedMagic | `ou_d6f78d98bce590648aba613ea66291ad` | `42fb7616` | `nina@fstln.io` | 2026-03-03 |
| 倪芷贝 | Betty | 需求方 | RedMagic | `ou_2fa483b5571ea6c81073fe1fc62e942a` | `ba2bec5d` | `betty.ni@fstln.io` | 2026-03-03 |
| 林梓仪 | Dina | 开发 | LiberNovo | `ou_e630d84ff5e303da9e740db0d8297efc` | `geg6afg2` | `dina.lin@fstln.io` | 2026-03-04 |
| 洪贵权 | Guiquan | 开发/配置 | LiberNovo/ANTA | `ou_fe96bca0fd49dc83c23e779c31ca4cf1` | `g5af3782` | `guiquan@fstln.io` | 2026-03-04 |
| 周小莉 | Anne | 测试 | LiberNovo | `ou_5f78e8226a8f82481058222560f48e2b` | `72d7fda9` | `anne.zhou@fstln.io` | 2026-03-04 |

## 维护规则
1. 每次新需求中出现新同学，先补档案再落任务。
2. 若人员字段写入失败，优先以 contacts MCP 结果覆盖本地档案。
3. 同名冲突时，以 `open_id` 为唯一键，不以姓名判重。
