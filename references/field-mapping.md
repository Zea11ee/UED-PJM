# Field Mapping (UED 需求管理 → 任务源 → WBS)

## 需求管理 → 任务源 (父任务)
- 需求标题 Request Title → 标题
- 需求编号 → 源编号
- 上线日期 Deadline → 期望上线日期
- 需求背景 Background + 需求目标 Objective + 需求描述 Description + 附件（链接）Attachment (Link) → 描述
- 附件（文件）Attachment (File) → 附件
- 需求方 → 需求方
- UED 负责人 → UED 负责人
- 归属项目 Associated Project → 归属项目 (DuplexLink to 项目库)

Notes:
- 描述字段建议按段落拼接，保留链接。
- DuplexLink 字段值必须是 string record_id 列表。

## 任务源 → WBS (子任务)
- 标题 → 任务名称 (prefix as needed, e.g. “需求 - 设计”)
- 父任务 → 父任务 (DuplexLink to 任务源)
- 负责人 → 负责人
- 期望上线日期 → 结束日期 (only if explicitly required)

## Key WBS Fields
- 任务名称
- 父任务
- 负责人
- 状态
- 预计工时 (h)
- 实际工时 (h)
- 启动日期
- 结束日期
