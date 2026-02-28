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
