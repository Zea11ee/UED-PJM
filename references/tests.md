# RED Baseline Tests (No Skill)

These scenarios document expected failure modes when the UED-PJM skill is not used.

## Pressure Scenarios

### Scenario A: 时间紧 + 表名相似 + 字段不一致
- Prompt: “立刻把 UED 需求管理的记录同步到 任务源 并创建 WBS 子任务。”
- Pressures: time pressure, ambiguous tables, field name mismatches.
- Baseline failures observed/expected:
  - Uses wrong table (e.g., similar “UED 需求总表（Test）”)
  - Field name mismatch (e.g., uses “标题” when actual is “任务名称”)
  - Skips field list lookup

### Scenario B: 时区误差 + 日期边界
- Prompt: “根据 WBS 排期，给出 2/6 的任务安排。”
- Pressures: timezone ambiguity, date boundary (00:00), scheduling urgency.
- Baseline failures observed/expected:
  - Interprets Unix ms as UTC date and shifts by -1 day
  - Schedules on wrong day (e.g., 1/29 shown as 1/28)

### Scenario C: 关联字段类型 + 批量创建
- Prompt: “把归属项目关联到项目库，并一次性建 3 条 WBS 子任务。”
- Pressures: data integrity, duplex link format, batch speed.
- Baseline failures observed/expected:
  - Writes DuplexLink as object array instead of string record_id list
  - Batch create succeeds partially without validation

### Scenario D: 节假日/周末规则
- Prompt: “结合公司假期安排排期。”
- Pressures: holiday awareness, weekends, local rules.
- Baseline failures observed/expected:
  - Ignores company holiday (e.g., 2/2)
  - Schedules tasks on weekend

### Scenario E: 人员姓名检索 + 工具未加载
- Prompt: “用姓名查刘博的 user_id。”
- Pressures: missing contacts MCP tool, name-only input, urgency.
- Baseline failures observed/expected:
  - 未优先调用 contacts 搜索接口，直接走历史映射或要求邮箱
  - 忽略会话未加载 lark-contacts-mcp（旧会话 resume 不会生效）

### Scenario F: UED 成员任务查询优先级
- Prompt: “查询刘博/贵权今天的任务安排。”
- Pressures: UED 内部人员、需要即时排期。
- Baseline failures observed/expected:
  - 未优先查 UED WBS，直接尝试 Feishu 任务
  - 忽略“非 UED 才查飞书任务”的优先级规则

### Scenario G: 文档含任务块/表格无法直接读取
- Prompt: “读取工作进度总表并提取 1 月日期条目。”
- Pressures: 文档内为飞书任务块/表格，原始 docx 输出不完整。
- Baseline failures observed/expected:
  - 误以为文档没有日期内容
  - 未提示需要通过任务 API/人工确认或提供导出

## Baseline Failure Notes (from prior runs)
- Off-by-one day due to UTC vs Asia/Shanghai conversion.
- DuplexLink field requires list of string IDs; object list fails.
- Date-based planning mistakenly treated as single point, not date range.

## GREEN Verification Status
- Subagent execution not available in this environment.
- Manual checklist review only; scenario replays with skill still needed.
- Pending: run Scenario A–D with skill to verify compliance.

## GREEN Replays (With Skill) — Manual Simulation

### Scenario A
- Action: list tables/fields before write; confirm correct table; map fields via field-mapping.
- Expected pass: no wrong-table writes; no field-name mismatch.

### Scenario B
- Action: convert all Unix ms to Asia/Shanghai before reasoning; explicitly note Beijing date.
- Expected pass: no -1 day error.

### Scenario C
- Action: for DuplexLink fields, write string record_id list; validate before batch create.
- Expected pass: no DuplexLink format errors.

### Scenario D
- Action: exclude weekends + company holidays from scheduling; ask for missing holiday list.
- Expected pass: no weekend/holiday scheduling.

### Scenario E
- Action: verify contacts MCP loaded; call name search first (supports拼音/近似匹配); fall back to mapping/email only if search unavailable or empty.
- Expected pass: name-based lookup attempted before mapping; explicit note if tool not loaded.

### Scenario F
- Action: if person is UED member, check WBS first; only if non-UED or WBS empty, then check Feishu tasks (if available).
- Expected pass: WBS-first for UED; no premature Feishu task lookup.

### Scenario G
- Action: note docx rawContent may omit task blocks; request export/alternative source or use task API (if available).
- Expected pass: no false “no dates” conclusion; explicit limitation and next step.
