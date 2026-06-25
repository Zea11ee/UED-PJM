---
name: UED-PJM
description: Use when asked to work with Feishu Bitable UED 需求管理/任务源/WBS for demand lookup, syncing records, or scheduling with Beijing time and holiday/weekend constraints.
---

# UED-PJM

## Overview
Standardize the UED demand → parent task → WBS child task workflow in Feishu Bitable with correct field mapping, timezone handling, and scheduling constraints.

## Execution Layer

Default Feishu execution layer is the official `lark-cli`.

Use these domains by default:
- `lark-cli base` for UED 项目管理 / 任务源 / WBS / 需求管理 / 项目大节点
- `lark-cli contact` for people lookup and ID resolution
- `lark-cli task` for Feishu task querying when the request is outside UED WBS-first scope
- `lark-cli calendar` for schedule conflict checks or time-window verification
- `lark-cli wiki` / `docx` / `drive` for linked content resolution when records contain wiki/doc links

Old MCP-based paths are compatibility fallback only. New execution paths should default to `lark-cli`.

## Identity Rules

Distinguish clearly between `bot` execution and `user` execution.

- Use `bot` when working with app-accessible Base data and project-system records.
- Use `user` only when the target API or data scope truly requires user identity.
- In multi-user bot products such as LinkFlow, do not treat a single container-level `lark-cli auth login` as the shared identity for all users.
- If this skill is running behind LinkFlow, user-scoped operations should continue to rely on LinkFlow's own OAuth / token-store model.

## 执行人选择准则（落库前必须判定或请用户确认）
- 负责人必须属于 **UED 部门**；非 UED 人选一律视为无效并需重新选择/确认。
- 优先按项目组/业务线的既定干系人列表（项目常驻 > 备份）选择。
- 如有相同项目/业务线的历史相似 WBS 记录，复用其负责人作为首选候选。
- 需求文本点名联系人（如 “联系 zane / david”）：仅在其属于 UED 时可作为首选；否则不直接指派，需确认。
- 默认不把“需求方”当执行人；缺少明确负责人时，列出推荐人选，请用户确认后再写入。
- 无法确定时：保持负责人为空/占位，不写入；或给出候选清单请用户确认。

## Core Workflow (Follow in order)
1. **Locate the correct app & tables**
   - Confirm app (e.g. `UED 项目管理`) and target tables: `需求管理` / `任务源` / `WBS`.
   - Use `lark-cli base +table-list` and `+field-list` before any write.
   - Never guess table names or field names.

2. **Retrieve the demand record**
   - Search demand records with `lark-cli base +record-list` or `+record-get`.
   - Collect all required fields for mapping and planning.
   - If the demand (or related task) contains links, resolve them with `lark-cli wiki` / `docx` / `drive`.
   - If that linked content contains more links, penetrate one more time.
   - Stop after 2 total hops.
   - When presenting analysis, always include:
     - analysis logic
     - references used
     - source sentences for key conclusions
   - Demand analysis must be written as a senior DTC C-end product manager: structured brief, clear and concise.
   - Analysis must include: similar past handling (if any), what tasks were done, total effort; proposed handling (understanding & split), dependencies (info/assets to collect), scope of website changes (pages/modules/features/interactions), impact scope (stores/country sites), phases & milestones (Hong Kong time, consider current time), systems/platforms/plugins, metrics & tracking, risks & mitigations. Each bullet must include its source sentence.

3. **Resolve people and ownership**
   - First use local people cache and historical records.
   - Then use `lark-cli contact +search-user` / `+get-user` when IDs are missing or ambiguous.
   - Do not write plain names into people fields when IDs are required.

4. **Sync to 任务源 (父任务)**
   - Use `references/field-mapping.md`.
   - Write through `lark-cli base +record-upsert`.
   - For DuplexLink fields, use string `record_id` list only.
   - After creating/upserting a parent task, determine the parent `record_id` from an explicit `record_id` field or by re-querying `任务源` with stable keys such as `源编号 + 标题`.
   - Do not regex the first `rec*` token from a whole CLI/JSON response; linked fields may contain project or lookup record IDs before the newly created parent task ID.
   - Before creating WBS, verify the parent record table/context and expected fields (`标题`, `源编号`, `归属项目`). If WBS were linked to the wrong record, update their `父任务` link in place instead of deleting/recreating them.

5. **Plan WBS 子任务**
   - 先判定需求类型再拆解：轻量配置/联调类、活动两阶段类（Teasing/Launch）、问题修复类。
   - Use historical similar demands if needed.
   - 里程碑驱动任务用倒排：先锁上线节点，再反推 PRD/设计/开发/测试/走查。
   - 默认依赖顺序：PRD 完成早于开发；设计联调与开发可并行；上线走查绑定上线当天。
   - Convert all timestamps to Asia/Shanghai.
   - “今天/明天/后天”等相对日期，落库前必须转换为绝对日期（YYYY-MM-DD）。
   - Consider date ranges and estimated hours when checking load.
   - Respect weekends + company/holiday rules.
   - 轻量任务（通常 <=2h）优先最小 WBS 集合，避免过度拆分。
   - Present draft plan for confirmation before writing.
   - Parent task and WBS drafts must be shown in a clear terminal table format.
   - WBS table must include: 序号 / 任务名称 / 负责人 / 状态 / 预计工时 / 启动日期 / 结束日期.

6. **Create or update WBS 子任务**
   - Use `lark-cli base +record-upsert`.
   - Required fields:
     - 任务名称
     - 父任务
     - 负责人
     - 状态
     - 预计工时
     - 启动日期
     - 结束日期

7. **Verify and record feedback**
   - Re-query parent task and WBS after write.
   - Return record IDs.
   - Append adjustments to `references/feedback.md` after each run.
   - If tasks were confirmed and written, **default run**:
     `python3 scripts/project-kb/append_project_kb_entry.py --project "<PROJECT>" --demand-id "<需求编号/源编号>" --module "<页面/模块>" --change "<新增/调整功能点>" --status "已排期" --parent-record-id "<parent_rec_id>" --wbs-record-ids "<wbs_rec_a,wbs_rec_b>"`.
   - The script inserts one project-KB event row and auto-deduplicates by `需求编号 + 页面/模块 + 功能/交互变化`.
   - If new people were resolved, append/refresh profile rows in `references/people-profiles.md`.

## Task Naming Rules
- Small/simple tasks may merge: “开发与跟测” / “测试与回归验证”.
- Medium/large tasks must split development and testing into separate tasks.

## App Selection Rules
- 需求收集/表单入口/汇总：使用「UED 需求总表」。
- 项目执行/任务源/WBS/项目库：使用「UED 项目管理」。
- 项目节奏与大节点：使用「UED 项目大节点」。

## Routing Note (Timesheet)
- 工时导入、工时回填、L1/L2/L3 归并、对账校验、跨目标写入（Bitable/Sheets）不在本技能主流程内。
- 遇到上述需求时，切换到 `UED-Worktime` 技能执行；本技能仅提供需求/WBS/排期与任务协同能力。

## User ID Resolution
- First try `references/people-profiles.md` (people cache) by exact name/alias match.
- If cache miss, cache row missing IDs, write fails, or same-name ambiguity exists, then use `lark-cli contact +search-user` (supports 中文/英文/拼音/近似匹配).
- If still missing, look up historical records (WBS/项目库/任务源) and 人员映射表.
- If still missing, use contact_v3_user_batchGetId with email/phone.
- If still missing, ask user to provide email/phone.

## Knowledge Memory Priority
- Before broad history search, read `references/project-kb/<PROJECT>.md` and `references/case-kb` (if available) to reuse known patterns.
- After confirmed write, persist high-value conclusions in project KB:
  - Use line format: `YYYY-MM-DD | 需求编号 | 页面/模块 | 新增/调整功能点 | 状态(已排期/已上线) | 关联任务ID`.
  - Only record likely-to-land decisions (already split to WBS and confirmed).
- Maintain people cache in `references/people-profiles.md` (name/open_id/user_id/email/role/project).
- Official contact lookup remains the default live path: people cache is acceleration, not source of truth.

## Task Query Priority
- If the person is UED部门：先查「UED 项目管理 → WBS」排期。
- 仅当查询对象非 UED 部门、用户明确要求飞书任务、或 WBS 为空时，才尝试飞书任务功能。
- When Feishu Task is needed, prefer `lark-cli task`.

## Personnel Current Task Query (WBS)
When the user asks “某人目前/当前/手上/在做/待处理的任务有哪些”:
- Default table: `UED 项目管理 → WBS`.
- Resolve the person to open_id/user_id first; do not filter people fields by plain display name only.
- Read WBS with full pagination. Do not stop at the first page, a single view, or the first matching batch.
- Default logical filter:
  - `负责人` contains the person
  - `状态` is not `已完成`
  - `状态` is not `废弃`
- Do not treat “手上任务” as `状态=未启动`; include `进行中` and any other non-closed status.
- If the result contains many stale records, group output into:
  - 当前/近期：`状态=进行中`, or start/end date is near today or in the future
  - 历史未清理：end date is far before today or dates are empty
- `任务源` is only parent-context supplement for this query. Do not use parent tasks as the primary task list unless WBS is empty.
- State the query basis in the answer: source table, person, closed statuses excluded, and whether stale records were separated.

## Weekly Due-but-Not-Complete (WBS)
When user asks for “本周到期未完结”:
- Table: UED 项目管理 → WBS
- Timezone: Asia/Shanghai
- Week range: Monday 00:00:00 to Sunday 23:59:59 of the current week (based on Beijing time)
- Filters (logical):
  - 状态 != 已完成
  - 结束日期 in current week range
  - 结束日期 must exist
- Note: Bitable Date field range filters may not be supported; if so, fetch 未完成 records and filter by 结束日期 locally, then stop paging once 结束日期 < week start (when sorted desc by 结束日期).

## CLI Command Discipline

When using `lark-cli`:
- prefer shortcuts when the domain skill defines them
- prefer atomic commands over generic raw API calls
- read table/field structure before record writes
- use `schema` before raw API methods when parameter structure is unclear
- never guess field names, option values, or record IDs
- dry-run / draft first, then confirm, then write, then verify

## Fallback Policy

The default execution path is official `lark-cli`.

Fallbacks are allowed only when:
- the current environment does not have usable `lark-cli`
- the required domain command is not available yet
- there is a temporary compatibility gap during migration

Do not expand new UED-PJM capabilities on top of old MCP-first patterns unless there is a specific migration reason.

## App Config
- Default app_token/table_id are stored in `references/app-config.md`.
- If values change, follow the lookup steps in that file (wiki → app → table list).

## Execution Quick Map
- table / field / record read-write -> `lark-cli base`
- people lookup / ID resolution -> `lark-cli contact`
- task query outside UED WBS-first scope -> `lark-cli task`
- schedule conflict / time-window verification -> `lark-cli calendar`
- wiki / doc link resolution -> `lark-cli wiki` / `docx` / `drive`

## Quick Reference
- **知识索引（统一入口）:** `references/index.md`
- **稳定规则（从 feedback 提炼）:** `references/rules/`
- **Field mapping (simple):** `references/field-mapping.md`
- **Field mapping (detailed):** `references/sync-mapping.md`
- **Workflows (typical):** `references/workflows.md`
- **Post-update 实战经验（2026-02-05 基线）:** `references/post-update-usage-lessons-20260205.md`
- **项目知识库（按项目沉淀）:** `references/project-kb/README.md`
- **案例记忆库（按需求类型模板）:** `references/case-kb/README.md`
- **人员档案库（ID/邮箱/角色）:** `references/people-profiles.md`
- **Guidance docs:** `references/docs.md`
- **Sheets 读写经验（飞书电子表格）:** `references/sheets-notes.md`
- **需求提交指南（Inbox 必填字段、填法）:** `references/demand-submit.md`
- **Official Feishu execution layer:** `lark-cli` domains (`base` / `contact` / `task` / `calendar` / `wiki` / `docx` / `drive`)
- **Timezone:** always Asia/Shanghai, never UTC
- **DuplexLink:** list of string record IDs only
- **Non-working days:** weekends + `references/holidays.md`

## Documentation Sync Rule
- After any skill upgrade, update `README.md` and any affected reference files.
- Keep the installed copy in `~/.codex/skills/UED-PJM` in sync.

## Detailed References
- Use `references/sync-mapping.md` for full field mapping and rules.
- Use `references/workflows.md` for typical end-to-end flows.
- Use `references/post-update-usage-lessons-20260205.md` for practical execution patterns, common pitfalls, and SOP since 2026-02-05.

## Common Mistakes
- Off-by-one day from UTC timestamps → always convert to Beijing time.
- Writing DuplexLink as objects → must be string record_id list.
- Ignoring date ranges and hours → check overlaps, not just a single date.
- Updating the skill without updating `README.md` and relevant references.
- Treating old MCP registration as mandatory when official `lark-cli` is already available.
- Assuming docx rawContent includes Feishu task blocks/tables; it may not.
- Failing to **open/read linked content** in demand/task records (must penetrate links, up to 2 hops with one nested link).
- Reporting conclusions without stating analysis logic and references used.
- Including conclusions or scope without explicit source sentences from the demand/linked content.
- For SingleSelect/MultiSelect fields in 项目管理表，写入时用选项“名称”字符串而非 option_id；否则 Bitable 会把未知 id 当作新文本选项生成乱码。
- For SingleSelect/MultiSelect fields in 项目管理表，写入时用选项“名称”字符串而非 option_id；否则 Bitable 会将未知 id 作为新文本选项，产生乱码选项。
- Using `lark-cli auth login` from a single shared runtime as if it represented every LinkFlow user.
- Guessing wiki token as base token instead of resolving `obj_token` first.
- Skipping `field-list` / `table-get` before `base +record-upsert`.
- Extracting a parent task ID by matching the first `rec*` in `record-upsert` output; always parse the explicit returned record ID or re-query `任务源` by stable keys before writing WBS.

## Session enforcement additions (2026-02-05)
- **Never write without explicit confirmation.** Always present a full draft (fields + values) and wait for “确认/落库/执行”。If user reminder about process exists in session, force confirm-before-write for the whole session.
- **WBS display must be table-first.** For draft/review messages, render WBS in terminal-style table (readable in CLI, aligned columns). Do not output plain paragraph list unless user explicitly asks.
- **User-specified field scope only.** When presenting for confirmation:
  - 父任务（任务源）仅列：标题、源编号、归属项目（关联）、期望上线日期、优先级、状态、描述、附件、需求方、UED 负责人。不要手动写业务线/预计开始/预计交付/其他字段；不要新增选项。
  - 子任务（WBS）仅列：任务名称、父任务（关联）、负责人、状态、预计工时、启动日期、结束日期。其它字段不动；不要新增选项。
- **No new options/records.** For Single/MultiSelect or Lookup/DuplexLink, only use existing option text or record_id string list; never create new options.
- **People fields need IDs.** Always resolve to open_id/user_id via contacts search; never write plain names that Feishu无法识别。
- **Use source data first.** Demand IDs、归属项目等优先从需求/项目表查询，不要反复让用户提供现有信息。
- **Dedupe before create.** 落库前先按“源编号”查询任务源，存在则更新/补WBS，不重复创建父任务。
- **Post-write verification.** 写入后必须回查父任务与WBS（按源编号/父任务关联）并返回 record_id。
- **Project KB update after write.** 需求落库后，必须将有价值的模块/功能变化追加到对应项目知识库。
- **Project KB append is default-on.** 落库并完成回查后，默认调用 `scripts/project-kb/append_project_kb_entry.py` 自动追加事件。
- **People profile upkeep.** 新解析到的人员信息（open_id/user_id/email/角色）应补充到人员档案库；档案缺失或冲突时再触发官方通讯录查询。
- **Attachments.** If only a URL is given and no file_token, place in 描述; keep 附件字段空 unless file_token is available.
- **Cross-base attachments.** 不同 Base/表的附件 file_token 可能不可直接复用；写入失败时将来源记录号/链接落到描述并继续流程。
- **Timezone.** All dates are Asia/Shanghai; convert timestamps accordingly.
- **Date filtering (Bitable API).** Supported operators for Date fields: `is`, `isGreater`, `isLess`, `isEmpty`, `isNotEmpty`. Value formats:
  - Exact date: `["ExactDate","<ms_timestamp>"]` (ms since epoch; converted to local 00:00 of doc timezone).
  - Today: `["Today"]` (only with `is`).
  - Current week: `["CurrentWeek"]` (only with `is`).
  - Last 7 days: `["TheLastWeek"]` (only with `is`).
  - Empty / Not empty: `[]` with `isEmpty` / `isNotEmpty`.
  - `isGreater`/`isLess` only accept `ExactDate`; timestamps must be ms.
  - Example: `{"field_name":"提交时间","operator":"isGreater","value":["ExactDate","1771862400000"]}`.
- **Error handling.** If API returns field/permission/datetime format errors, re-check `field_name`, `operator`, timestamp format, and fall back to per-record `update` when batch fails.

## Weekly Lint Checklist

每周检查一次知识健康度：

1. **项目覆盖**：`project-kb/` 是否覆盖近 30 天内处理过的所有项目？缺失则新建项目页。
2. **人员时效**：`people-profiles.md` 是否有超过 60 天未更新的条目？过期则标记或触发重新解析。
3. **规则提炼**：`feedback.md` 是否有被重复使用 ≥3 次但未提炼成规则的经验？符合则迁移到 `rules/`。
4. **索引完整**：`index.md` 是否覆盖所有 `rules/`、`project-kb/`、`case-kb/` 文件？缺失则补充链接。
5. **规则冲突**：`rules/` 中的规则是否与 SKILL.md 主流程或其他规则冲突？冲突则更新或标注废弃。
