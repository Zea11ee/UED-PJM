---
name: UED-PJM
description: Use when asked to work with Feishu Bitable UED 需求管理/任务源/WBS for demand lookup, syncing records, or scheduling with Beijing time and holiday/weekend constraints.
---

# UED-PJM

## Overview
Standardize the UED demand → parent task → WBS child task workflow in Feishu Bitable with correct field mapping, timezone handling, and scheduling constraints.

## MCP prerequisites（自动加载，操作前必须执行）
- 进入技能后立刻运行：`list_mcp_resources`（空也没关系），随后直接调用一次 `lark-mcp` 与 `lark-contacts-mcp` 的轻量接口以强制注册（例如最简 ping/查询；若无专用 ping，就执行一次空参数的联系人搜索/表结构读取再丢弃结果）。
- 资源列表为空或返回 `Method not found` 时也不要停；仍按默认已加载处理，继续尝试接口调用。只有在 **重复调用仍报 Method not found** 时，才向用户说明“当前环境缺少 lark-mcp / lark-contacts-mcp，需在本会话注册”并停止后续写入。
- 不再要求用户手动加载；技能执行时默认自动加载/探测 MCP 工具。

## 执行人选择准则（落库前必须判定或请用户确认）
- 负责人必须属于 **UED 部门**；非 UED 人选一律视为无效并需重新选择/确认。
- 优先按项目组/业务线的既定干系人列表（项目常驻 > 备份）选择。
- 如有相同项目/业务线的历史相似 WBS 记录，复用其负责人作为首选候选。
- 需求文本点名联系人（如 “联系 zane / david”）：仅在其属于 UED 时可作为首选；否则不直接指派，需确认。
- 默认不把“需求方”当执行人；缺少明确负责人时，列出推荐人选，请用户确认后再写入。
- 无法确定时：保持负责人为空/占位，不写入；或给出候选清单请用户确认。

## Core Workflow (Follow in order)
1. **Locate the correct app & tables**
   - Confirm app (e.g., “UED 项目管理”) and tables: 需求管理 / 任务源 / WBS.
   - List fields in each table before writing.

2. **Retrieve the demand record**
   - Search by 需求标题 (contains ok).
   - Collect required fields for mapping.
   - If the demand (or related task) contains links, **must** open and read the linked content. If that linked content contains more links, **penetrate one more time**. **Stop after 2 total hops** (original link + one nested link).
   - When presenting analysis, **always** include a brief “analysis logic” (method) and “references used” list.
   - Demand analysis must be written as a **senior DTC C-end product manager**: structured brief, clear and concise. **No free-form speculation**—every statement must cite its source sentence from the demand or linked content.
   - Analysis must include: similar past handling (if any), what tasks were done, total effort; proposed handling (understanding & split), dependencies (info/assets to collect), scope of website changes (pages/modules/features/interactions), impact scope (stores/country sites), phases & milestones (Hong Kong time, consider current time), systems/platforms/plugins, metrics & tracking, risks & mitigations. **Each bullet must include its source sentence**.

3. **Sync to 任务源 (父任务)**
   - Use `references/field-mapping.md`.
   - For DuplexLink fields, use **string record_id list** (not objects).

4. **Plan WBS 子任务**
   - Use historical similar demands if needed.
   - Convert all timestamps to Asia/Shanghai (see `references/timezone.md`).
   - Consider **date ranges** (启动–结束) and **预计工时** when checking load.
   - Respect weekends + company/holiday rules (see `references/holidays.md`).
   - Present draft plan for confirmation before writing.

5. **Create WBS 子任务**
   - Required fields: 任务名称 / 父任务 / 负责人 / 状态 / 预计工时 / 启动日期 / 结束日期.

6. **Record feedback**
   - Append adjustments to `references/feedback.md` after each run.

## Task Naming Rules
- Small/simple tasks may merge: “开发与跟测” / “测试与回归验证”.
- Medium/large tasks must split development and testing into separate tasks.

## App Selection Rules
- 需求收集/表单入口/汇总：使用「UED 需求总表」。
- 项目执行/任务源/WBS/项目库：使用「UED 项目管理」。
- 项目节奏与大节点：使用「UED 项目大节点」。

## Routing Note (Timesheet)
- 工时导入、工时回填、L1/L2/L3 归并、对账校验、跨目标写入（Bitable/Sheets）不在本技能主流程内。
- 遇到上述需求时，切换到 `ued-timesheet-sync` 技能执行；本技能仅提供需求/WBS/排期与任务协同能力。

## User ID Resolution
- First try name-based search via contacts MCP (search supports中文/英文/拼音/近似匹配).
- If contacts MCP is missing or returns empty, look up historical records (WBS/项目库/任务源) and 人员映射表.
- If still missing, use contact_v3_user_batchGetId with email/phone.
- If still missing, ask user to provide email/phone.

## Task Query Priority
- If the person is UED部门：先查「UED 项目管理 → WBS」排期。
- 仅当查询对象非 UED 部门，或 WBS 为空时，才尝试飞书任务功能（若无接口需说明限制）。

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

## Contacts MCP Requirement
- 技能已内置自动探测/调用；即使 resources/list 为空也继续尝试。仅当连续调用依然返回 `Method not found` 时，才提示用户“当前会话未注册 lark-mcp / lark-contacts-mcp，需在本会话加载后再试”。旧会话 resume 可能缺少注册，需重新调用本技能以触发自动探测。

## App Config
- Default app_token/table_id are stored in `references/app-config.md`.
- If values change, follow the lookup steps in that file (wiki → app → table list).

## Quick Reference
- **Field mapping (simple):** `references/field-mapping.md`
- **Field mapping (detailed):** `references/sync-mapping.md`
- **Workflows (typical):** `references/workflows.md`
- **Guidance docs:** `references/docs.md`
- **Sheets 读写经验（飞书电子表格）:** `references/sheets-notes.md`
- **需求提交指南（Inbox 必填字段、填法）:** `references/demand-submit.md`
- **Timezone:** always Asia/Shanghai, never UTC
- **DuplexLink:** list of string record IDs only
- **Non-working days:** weekends + `references/holidays.md`

## Documentation Sync Rule
- After any skill upgrade, update `README.md` and any affected reference files.
- Keep the installed copy in `~/.codex/skills/UED-PJM` in sync.

## Detailed References
- Use `references/sync-mapping.md` for full field mapping and rules.
- Use `references/workflows.md` for typical end-to-end flows.

## Common Mistakes
- Off-by-one day from UTC timestamps → always convert to Beijing time.
- Writing DuplexLink as objects → must be string record_id list.
- Ignoring date ranges and hours → check overlaps, not just a single date.
- Updating the skill without updating `README.md` and relevant references.
- Attempting name search without the contacts MCP tool configured or loaded in a new session.
- Assuming docx rawContent includes Feishu task blocks/tables; it may not.
- Failing to **open/read linked content** in demand/task records (must penetrate links, up to 2 hops with one nested link).
- Reporting conclusions without stating analysis logic and references used.
- Including conclusions or scope without explicit source sentences from the demand/linked content.
- For SingleSelect/MultiSelect fields in 项目管理表，写入时用选项“名称”字符串而非 option_id；否则 Bitable 会把未知 id 当作新文本选项生成乱码。
- For SingleSelect/MultiSelect fields in 项目管理表，写入时用选项“名称”字符串而非 option_id；否则 Bitable 会将未知 id 作为新文本选项，产生乱码选项。

## Session enforcement additions (2026-02-05)
- **Never write without explicit confirmation.** Always present a full draft (fields + values) and wait for “确认/落库/执行”。If user reminder about process exists in session, force confirm-before-write for the whole session.
- **User-specified field scope only.** When presenting for confirmation:
  - 父任务（任务源）仅列：标题、源编号、归属项目（关联）、期望上线日期、优先级、状态、描述、附件、需求方、UED 负责人。不要手动写业务线/预计开始/预计交付/其他字段；不要新增选项。
  - 子任务（WBS）仅列：任务名称、父任务（关联）、负责人、状态、预计工时、启动日期、结束日期。其它字段不动；不要新增选项。
- **No new options/records.** For Single/MultiSelect or Lookup/DuplexLink, only use existing option text or record_id string list; never create new options.
- **People fields need IDs.** Always resolve to open_id/user_id via contacts search; never write plain names that Feishu无法识别。
- **Use source data first.** Demand IDs、归属项目等优先从需求/项目表查询，不要反复让用户提供现有信息。
- **Attachments.** If only a URL is given and no file_token, place in 描述; keep 附件字段空 unless file_token is available.
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
