# UED-PJM

## Overview
UED-PJM documents the standard workflow for UED demand intake, parent task sync, and WBS scheduling using Feishu Bitable (via lark-mcp).

## Capabilities (Current)
### Feishu Bitable (lark-mcp)
- List Base tables
- Read table fields (schema)
- Search records (filters + sorting)
- Create records (single/batch)
- Update records (single/batch)
- Create Base app and tables (when needed)

### UED Project Workflow (UED-PJM)
- Demand -> parent task -> WBS child task mapping and sync
- Field mapping with DuplexLink record_id list format
- Draft WBS plan based on historical similar demands
- Beijing time scheduling with weekend/holiday constraints
- Weekly “本周到期未完结” query in WBS (status != 已完成, end date within current week, Asia/Shanghai)
- Load checking using date ranges + estimated hours
- Pre-write field review for approval
- Link penetration for demand/task records (open linked content, up to 2 hops)
- Demand analysis must include analysis logic + references used
- Demand analysis must be structured DTC PM brief with per-bullet source sentences, no speculation
- Feedback capture into references/feedback.md

### People Resolution
- Resolve open_id/user_id by contacts MCP name search (中文/英文/拼音/近似)
- Resolve open_id/user_id by matching historical records
- Resolve user_id via email/phone (contact_v3_user_batchGetId)
- Maintain reusable personnel mapping table

### Guidance Docs
- UED 项目指导手册（飞书文档）用于流程/规范检索与沉淀
- Sheets 读写与踩坑：references/sheets-notes.md（飞书电子表格读/写/查找的实测经验与命令模板）
- Bitable 操作要点：references/bitable-notes.md
- 任务接口与权限：references/task-notes.md
- 人员解析：references/people-resolution.md
- 需求提交指南：references/demand-submit.md

### Collaboration (IM/Docs/Calendar)
- Send Feishu messages (user/group)
- List chat members and fetch chat history
- Search/read doc contents
- Create/update calendar events and freebusy checks

## Limitations
- Cannot read Feishu Base automation/workflow configuration (no public API)
- Feishu 任务功能接口不可用时，无法直接读取任务块/任务列表
- docx 原始内容可能不包含任务块/表格，需要任务 API 或人工确认
- 启用技能时自动探测/调用 lark-mcp 与 lark-contacts-mcp（资源列表为空也继续）；若反复调用仍报 Method not found，需在当前会话注册后再试
- Link penetration depth is capped at 2 hops

## Update Policy
- When UED-PJM is upgraded, update this README.md and any affected reference files
- Keep the capability list and limitations in sync with actual tool access
