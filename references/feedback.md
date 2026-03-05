# Feedback Log (Append Only)

Template:
- Date:
- Scenario:
- What worked:
- What was adjusted:
- New rule or edge case:
- Date: 2026-01-29
- Scenario: ANTA - Shopify Order Cancel邮件模版更新 (任务源+WBS)
- What worked: 提前确认任务源字段、优先级补齐、WBS 执行人按 ANTA 固定角色映射
- What was adjusted: 任务命名合并（开发与跟测 / 测试与回归验证）仅适用于小型简单任务
- New rule or edge case: 中大型任务仍需拆分开发与测试，不可合并
- Date: 2026-01-29
- Scenario: Other session missing app_token/table_id
- What worked: Add fixed app config + lookup steps
- What was adjusted: Skill now includes app-config.md with tokens
- New rule or edge case: Always check app-config.md before asking user for IDs
- Date: 2026-01-29
- Scenario: Add multi-app config (UED 项目管理/需求总表/项目大节点)
- What worked: Resolved app_token + table_id via wiki + appTable_list
- What was adjusted: app-config.md now contains three app sections
- New rule or edge case: Always read app-config.md; pick correct app by workflow context
- Date: 2026-01-29
- Scenario: Add entry links + relationship notes
- What worked: Included canonical wiki URLs for quick access
- What was adjusted: app-config now documents table relationships
- New rule or edge case: Keep entry links updated if view/table changes
- Date: 2026-01-29
- Scenario: Add detailed sync mapping + typical workflows
- What worked: Provided full mapping table and standard process checklist
- What was adjusted: SKILL.md references new files
- New rule or edge case: Keep mapping updated when field names change
- Date: 2026-01-29
- Scenario: Resolve user_id from name via history lookup
- What worked: Search WBS/项目库 records for matching name to get open_id
- What was adjusted: Add rule to resolve IDs via historical records before asking user
- New rule or edge case: If no match, fall back to contact_v3_user_batchGetId with email/phone
- Date: 2026-01-29
- Scenario: Create 人员映射 table for fast user_id resolution
- What worked: New table in UED 项目管理 to store name/email/open_id mapping
- What was adjusted: app-config updated with 人员映射 table_id
- New rule or edge case: Prefer 人员映射 lookup before API search
- Date: 2026-01-29
- Scenario: Skill upgrade doc sync requirement
- What worked: Added explicit doc sync rule in SKILL.md and README
- What was adjusted: New documentation sync rule is required on every upgrade
- New rule or edge case: Always update README.md + affected references + installed copy after skill changes
- Date: 2026-01-29
- Scenario: Enable name-based user lookup via contacts MCP
- What worked: Added contact_users_search to User ID Resolution
- What was adjusted: Prefer name search when contacts MCP is configured
- New rule or edge case: If contacts MCP missing, fall back to email/phone batchGetId
- Date: 2026-01-30
- Scenario: 姓名检索优先级与拼音/近似匹配
- What worked: 使用 contacts MCP 进行姓名/拼音/近似匹配检索
- What was adjusted: 将姓名检索设为第一优先级，历史映射与邮箱/手机作为后备
- New rule or edge case: 若 contacts MCP 未加载需提示新会话启动
- Date: 2026-01-30
- Scenario: UED 人员任务查询优先级
- What worked: UED 成员先查 WBS 排期
- What was adjusted: 非 UED 才查飞书任务（接口不可用需说明限制）
- New rule or edge case: WBS 为空时再考虑其他来源
- Date: 2026-01-30
- Scenario: 文档任务块无法从 docx rawContent 获取
- What worked: 识别任务块/表格在 rawContent 中缺失
- What was adjusted: 增加“需任务 API 或人工导出确认”的提示
- New rule or edge case: 不可直接断言“文档无日期”
2026-01-30 新建WBS：购买页 - 开发协助（父任务recv8PDe32OVMC，负责人贵权，8h，2026-01-30）
- 2026-01-30: Queried UED 需求总表 (tblesE69fcAUGRwD) for new demands since 2026-01-28 00:00 Asia/Shanghai; provided list to user.
- Date: 2026-01-30
- Scenario: 本周到期未完结任务清单（WBS）
- What worked: 明确使用结束日期范围 + 状态!=已完成 + Asia/Shanghai 周区间
- What was adjusted: 去除“创建时间范围”限制条件
- New rule or edge case: Bitable 日期字段可能不支持范围筛选，必要时拉未完成列表后本地过滤并在结束日期降序分页中提前停止

- 2026-01-30 16:26 Created 任务源+WBS for RM202601291821, assigned to 黄镇蓝, 8h, scheduled 2026-01-30.
- 2026-01-30 16:30 Created 任务源+WBS for HSBUG202601301609; split into “开发排查&处理(3h)” and “测试跟测(2h)”, scheduled 2026-01-30; assignees 王佳丽 / 谢杜娓.
- 2026-01-30 16:40 线上问题创建规范：任务源标题不含编号，编号放“源编号/备注”；需求方填表单提交人。
- 2026-02-03 14:35 任务源创建时勿漏“源编号”（用需求编号/自动编号填入），否则后续联动/回填会空。
- 2026-02-03 15:20 任何落表操作前必须先出“父任务+WBS 草稿”给需求方确认；收到同意后再写入多维表格。

- 2026-01-30 18:03 创建WBS：Nubia情人节配置；父任务=托管标准化平台（nubia项目支持）；负责人=Tammy（周智莉）；日期=2026-02-03；工时=4h。
- Date: 2026-02-04
- Scenario: 项目管理表 SingleSelect 写入产生乱码选项
- What worked: 改用选项“名称”写入（如 P2、未启动），避免新增异常选项
- What was adjusted: 单选/多选字段在当前项目管理表均统一用名称字符串，不再写 option_id
- New rule or edge case: 若写入 option_id，Bitable 会把未知 id 当作新文本选项，需避免；如出现需立即改用名称并清理无效选项
- 2026-02-10: Node Ti2dwYWCviH6YKkRCa8clwRKnXc resolves to obj_type=sheet (spreadsheet). lark-mcp bitable APIs return 91402 NOTEXIST when app_token=OAl2sxWZ6hwcQytrZgScNc2jnLe; sheet endpoints not available in current MCP toolset.

## 2026-02-28
- 需求：2026年春促活动上线需求：落地页+周边图设计（RM202602241041）
- 父任务：recvcpV0kP3pm6（已存在）
- 操作：新增 11 条 WBS；保留既有“2026年春促活动 - KV+活动页 - 设计”不变。
- 关键修正：`Xiao` 执行人统一映射为 `肖荣健 (ou_7ef1de7929e2e2e31a0d82387a5bedff)`，非谢杜娓。
- 时间与工时：按用户确认，全部以 Asia/Shanghai 日期写入。

## 2026-02-28
- 需求：ANTA - 购买页新增支付方式展示（AT202602271910）
- 处理备注驱动拆分：PRD 2h、开发 3h、跟测验收 2h、测试 2h、产品验收上线 1h。
- 用户确认排期：PRD 2/28；开发与测试 3/4；其余保持。
- 新建父任务：recvcvJ9WEq2gq
- 新建WBS：recvcvJeIAgNU0 / recvcvJeIALBC2 / recvcvJeIAEOW5 / recvcvJeIAH4A1 / recvcvJeIAfh5O

## 2026-02-28
- 需求：2026年红魔中东斋月节促销活动上线需求：落地页+周边设计需求（RM202602241046）
- 用户调整：设计给麻吉；开发给徐炜健（3/10）；测试3/11；多语言改3/11；小婷任务名改“上线checklist与跟进”。
- 新建父任务：recvcvLxtHvO5V
- 新建WBS：recvcvLBMK7Tt0 / recvcvLBMKx67B / recvcvLBMKN2ng / recvcvLBMK91Eh / recvcvLBMKRiqx / recvcvLBMKhShd

## 2026-02-28
- 需求：红魔11 Air新颜色上线（RM202602271501）
- 用户确认：去掉炜健开发任务；保留父任务与其余WBS；3/11配置与多语言；3/30 EBO上线走查。
- 新建父任务：recvcvNNAiaRNu
- 新建WBS：recvcvNRhh8m41 / recvcvNRhh7ZK4 / recvcvNRhh2wSw / recvcvNRhhxq6P / recvcvNRhhvFhq / recvcvNRhh6DQx

## 2026-02-28
- 需求：红魔项目tech站点和GG站点跳转分离（RM202602271424）
- 用户要求：仅先安排1条WBS，3/2-3/3，小婷，产品PRD输出。
- 新建父任务：recvcvQQ4z0qgD
- 新建WBS：recvcvQSHzhuNi

## 2026-02-28
- 需求：红魔DTC站点运营商提示板块优化需求（RM202602261613）
- 用户要求：仅安排1条WBS（产品PRD），负责人小婷，3/4-3/5。
- 新建父任务：recvcvRIQr7qZN
- 新建WBS：recvcvRLEvDyxi

## 2026-02-28
- 需求：ANTA搜索设计优化（AT202602121750）
- 用户要求：WBS 3条，均在3/6；设计联调0.5h、开发联调2h、测试1h。
- 新建父任务：recvcvUPBM6JRi
- 新建WBS：recvcvUSPwdXGg / recvcvUSPwlkIA / recvcvUSPwg18x

## 2026-02-28
- 需求：ANTA - AR试鞋 / 试装功能评估（AT202602271437）
- 用户要求：先仅安排1条产品调研PRD（3/6，8h，潘贵洪）。
- 新建父任务：recvcwmfmiIvx8
- 新建WBS：recvcwmihb1ivJ

## 2026-02-28
- 需求：中台问题反馈（UED202602261608）
- 用户调整：父任务UED负责人改周嵩；仅保留2条WBS（思雯开发修复3/9-3/10；周嵩设计验收3/11），其余后续补。
- 新建父任务：recvcwo4b2v2na
- 新建WBS：recvcwo6JQN5c5 / recvcwo6JQ9tlp

## 2026-02-28
- 主题：沉淀 UED-PJM 上次更新（2026-02-05）后的实战经验
- 动作：新增参考文档 `references/post-update-usage-lessons-20260205.md`，并在 `SKILL.md` 与 `README.md` 增加入口。
- 覆盖内容：协作节奏（先草案后落库）、活动类标准拆分链路、人员 ID 解析、排期工时估算、备注与外链处理、常见错误与 SOP。

## 2026-03-02
- 需求：ANTA - AR试鞋 / 试装功能评估（AT202602271437）
- 用户要求：仅保留贵洪1条调研任务，8h；并根据实际负载改期。
- 落库结果：更新现有WBS `recvcwmihb1ivJ` 启动/结束至 2026-03-03（Asia/Shanghai），工时保持8h。

## 2026-03-02
- 需求：创建 Skill，涵盖从素材解析、打标、简修到生成素材审计报告（AX202602102125）
- 用户要求：补建3条WBS（2/11与2/24历史已完成 + 3/9半天调整），任务名采用“skill 制作”。
- 落库结果：在父任务 `recvaPxm4A1mlr` 下创建
  - `recvcGbFCzRVjP` 素材处理Skill（1+2+4）制作（已完成，8h，2026-02-11）
  - `recvcGbI4EmcZq` 选图Skill（3，含选图+处理图）制作（已完成，8h，2026-02-24）
  - `recvcGbI4EtrfD` 素材处理/选图Skill联调修改调整（未启动，4h，2026-03-09）

## 2026-03-02
- 主题：WBS 展示格式规范补充
- 用户要求：WBS 在 CLI 中必须以表格形式展示（风格清晰，类似 Claude Code/OpenClaw 终端表格），不要纯文本段落。
- 更新内容：
  - `SKILL.md`：新增 WBS 表格展示硬性要求（Plan 阶段 + Session enforcement）
  - `references/workflows.md`：新增 WBS 展示格式小节
  - `README.md`：能力说明增加“WBS 终端表格展示”

## 2026-03-03
- 需求：红魔11 Pro&11 Air需要上传软件更新链接（RM202602281732）
- 用户要求：按固定轻量流程拆分并落库（设计0.5h透明底图 + Zendesk卡片新增上传1h）。
- 落库结果：
  - 父任务：`recvcNId53aDI2`（未启动，期望上线 2026-03-03）
  - WBS：`recvcNIh8NCJmH` 透明底产品图输出（黄钰，0.5h，2026-03-03）
  - WBS：`recvcNIh8N9y0H` Zendesk卡片新增并上传图片（洪贵权，1h，2026-03-03）

## 2026-03-03
- 需求：日本站点11Air“商品管理页”相关产品同步（手机&手机膜&手机壳）（RM202603021624）
- 用户要求：父任务+单条WBS，均给王小婷；WBS仅产品配置，0.5h，且昨日已完成；实际工时同步0.5h。
- 落库结果：
  - 父任务：`recvcNJpIhW9Dr`（已完成）
  - WBS：`recvcNJrKMC1aA` 日本站点11Air商品管理页相关产品同步 - 产品配置（已完成，预计0.5h，实际0.5h，2026-03-02）
- 备注：需求总表附件 file_token 不能直接写入项目管理表附件（跨表归属校验失败）；已在父任务描述中保留来源记录号 `recRC4Dvtc` 供追溯。

## 2026-03-03
- 需求：红魔配件collection页面优化需求（RM202603021132）
- 用户要求：父任务+2条WBS；小婷产品配置（明天1d），炜健穿插0.5h处理filter dropdown默认展开。
- 落库结果：
  - 父任务：`recvcNLpJNzCBh`
  - WBS：`recvcNLsajnaye` 红魔配件collection页面优化 - 产品配置（王小婷，8h，2026-03-04）
  - WBS：`recvcNLsajF9h1` 红魔配件collection页面优化 - filter dropdown默认展开调整（徐炜健，0.5h，2026-03-04）

## 2026-03-03
- 需求：ANTA EU 导航栏产品新增标签需求（AT202602281220）
- 用户要求：开发安排东林在3.6；设计联调与开发并行同为3.6；PRD在开发前完成；后续测试/跟测/产品验收/上线走查也统一放到3.6。
- 落库结果：
  - 父任务：`recvcO3Q1RCAHt`
  - WBS：`recvcO3UfiufjK` 产品PRD（潘贵洪，1h，2026-03-05）
  - WBS：`recvcO3UfiEp5Y` 设计联调（周嵩，2h，2026-03-06）
  - WBS：`recvcO3UfiSxIw` 开发实现（廖东林，4h，2026-03-06）
  - WBS：`recvcO3Ufilhsl` 测试与回归（胡超，3h，2026-03-06）
  - WBS：`recvcO3UfifbX3` 跟测与验收（廖东林，4h，2026-03-06）
  - WBS：`recvcO3UfiZN77` 产品验收（潘贵洪，1h，2026-03-06）
  - WBS：`recvcO3UfiT77g` 上线走查（胡超，1h，2026-03-06）

## 2026-03-03
- 需求：ANTA EU 3月Kyrie BDay 活动需求（AT202602281210）
- 用户要求：设计负责人固定为刘佳莹；两阶段推进（Teasing 3/10，Launch 3/16）；刘佳莹任务可从3/4启动，Launch设计紧接Teasing处理。
- 落库结果：
  - 父任务：`recvcOkH9TWorQ`
  - WBS：`recvcOkKSWjhRH` 订阅与埋点配置（Teasing）（潘贵洪，2h，3/5）
  - WBS：`recvcOkKSW4OxD` Teasing落地页设计与配置（刘佳莹，12h，3/4-3/5）
  - WBS：`recvcOkKSWUPdV` Teasing KV与周边延展（刘佳莹，12h，3/6-3/9）
  - WBS：`recvcOkKSWg3qP` Launch设计素材（刘佳莹，8h，3/10）
  - WBS：`recvcOkKSWfnk9` Teasing上线走查（胡超，2h，3/10）
  - WBS：`recvcOkKSWDk3x` Launch上线走查（胡超，2h，3/16）

## 2026-03-03
- 主题：近期需求梳理经验沉淀到 UED-PJM skill
- 用户诉求：将最近多轮需求拆解与排期经验（类型化拆分、节点倒排、确认前不落库、去重回查、附件跨表降级）固化进技能文档。
- 更新文件：
  - `SKILL.md`：新增 WBS 规划规则与 Session enforcement 补充（去重、回查、跨表附件）。
  - `README.md`：补充能力说明（类型判定、节点倒排、绝对日期、去重回查）与限制（跨表附件 token）。
  - `references/post-update-usage-lessons-20260205.md`：新增“近期补充经验（2026-03-03）”。
  - `references/workflows.md`：新增“节点倒排与轻重拆分”“落库稳定性控制”流程段。

## 2026-03-03
- 主题：新增“项目知识库 + 人员档案库 + 案例记忆库”机制
- 用户诉求：
  - 减少每次梳理WBS时的全量历史检索成本。
  - 需求拆分并落库后，把有价值的模块/功能变化沉淀到项目知识库。
  - 维护人员档案（user_id/open_id/email/角色）以减少重复联系人查询，但保留 contacts MCP 能力与校验。
- 更新文件：
  - `SKILL.md`：新增 Knowledge Memory Priority、落库后强制更新项目KB/人员档案。
  - `README.md`：能力与限制新增知识库机制说明。
  - `references/workflows.md`：主流程新增“先读KB、落库后反写KB”。
  - `references/people-resolution.md`：新增档案库联动规则。
  - `references/docs.md`：新增本地知识库索引。
  - 新增 `references/project-kb/`（README、模板、ANTA/REDMAGIC/HYPERSHELL）。
  - 新增 `references/case-kb/`（README、活动双阶段模板、轻量配置模板）。
  - 新增 `references/people-profiles.md`（人员档案表）。

## 2026-03-04
- 主题：落库后自动追加项目KB条目（默认开启）
- 用户诉求：将“需求落库→项目知识沉淀”从手工步骤升级为默认自动动作。
- 更新内容：
  - 新增脚本 `scripts/project-kb/append_project_kb_entry.py`：
    - 按项目自动定位/创建 `references/project-kb/<PROJECT>.md`；
    - 追加“已确认变更事件”表格行；
    - 默认按 `需求编号 + 页面/模块 + 功能/交互变化` 去重。
  - `SKILL.md`：Step 6 改为默认执行脚本，并在 Session enforcement 增加 default-on 约束。
  - `references/workflows.md`：外部需求与已有任务源流程均改为脚本自动沉淀。
  - `README.md`：能力补充“Post-write project KB auto append”。
  - `scripts/README.md` 与 `references/project-kb/README.md`：新增脚本使用说明。

## 2026-03-04
- 需求：线上环境跨国家切换后筛选侧边栏丢失（QXBUG202603041450）
- 用户要求：开发负责人改为 Dina（林梓仪）并直接落库。
- 落库结果：
  - 父任务：`recvcSAD1ZFdiQ`（LiberNovo，P2，未启动，期望上线 2026-03-05）
  - WBS：`recvcSAFI7Ksvp` 备件集合页筛选侧边栏丢失 - 开发处理（林梓仪，3h，2026-03-04）
  - WBS：`recvcSAFI719Vx` 备件集合页筛选侧边栏丢失 - 复现与跟测（周小莉，2h，2026-03-04）
- 知识沉淀：
  - 已自动追加项目KB：`references/project-kb/LIBERNOVO.md`
  - 事件行：`2026-03-04 | QXBUG202603041450 | 备件集合页 | 跨国家站点切换后筛选侧边栏丢失修复（US→DE） | 已排期 | recvcSAD1ZFdiQ / recvcSAFI7Ksvp / recvcSAFI719Vx`

## 2026-03-05
- 需求：ANTA EU 非可售国家跳转到EU站（AT202602261117）新增开发排查子任务
- 用户要求：仅在该父任务下新增1条开发排查WBS，负责人东林，排期 2026-03-02 ~ 2026-03-05，预计 6h。
- 落库结果：
  - 父任务：`recvcvcyS5RkPX`（复用）
  - WBS：`recvcXrLrXxcku` ANTA EU 非可售国家跳转到EU站 - 开发排查（廖东林，未启动，6h，2026-03-02~2026-03-05）
- 知识沉淀：
  - 已自动追加项目KB：`references/project-kb/ANTA.md`
  - 事件行：`2026-03-05 | AT202602261117 | 国家跳转逻辑 | 新增开发排查子任务（东林，3.2-3.5，6h） | 已排期 | recvcvcyS5RkPX / recvcXrLrXxcku`

## 2026-03-05
- 需求：红魔FAQ板块内容统一配置功能需求（RM202603031834）
- 用户要求：最小工作项拆分并按依赖顺序排期；工时调整为 PRD 3h、开发 4h、测试 2h、测试反馈修改 2h、回归 1h、上线 1h；去除配置与产品验收任务。
- 落库结果：
  - 父任务：`recvcXFNyDoZs9`（RedMagic，P2，未启动，期望上线 2026-03-19）
  - WBS：`recvcXFRkyVWRG` FAQ统一配置 - PRD（王小婷，3h，2026-03-10）
  - WBS：`recvcXFRkyxwCL` FAQ统一配置 - 开发（徐炜健，4h，2026-03-11）
  - WBS：`recvcXFRky7FIu` FAQ统一配置 - 测试（肖荣健，2h，2026-03-12）
  - WBS：`recvcXFRkyVjOZ` FAQ统一配置 - 测试反馈修改（徐炜健，2h，2026-03-13）
  - WBS：`recvcXFRkylRF8` FAQ统一配置 - 回归验证（肖荣健，1h，2026-03-16）
  - WBS：`recvcXFRkyEOno` FAQ统一配置 - 上线走查（肖荣健，1h，2026-03-19）
- 知识沉淀：
  - 已自动追加项目KB：`references/project-kb/REDMAGIC.md`
  - 事件行：`2026-03-05 | RM202603031834 | FAQ板块 | 新增metaobject统一配置（含多语言）并保留主产品自定义覆盖 | 已排期 | recvcXFNyDoZs9 / recvcXFRkyVWRG / recvcXFRkyxwCL / recvcXFRky7FIu / recvcXFRkyVjOZ / recvcXFRkylRF8 / recvcXFRkyEOno`
