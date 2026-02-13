# 同步字段对应关系图（详细版）

## A. 需求总表 → 项目管理（任务源）

| 源表字段（UED 需求总表） | 目标表字段（项目管理/任务源） | 类型 | 规则/说明 |
|---|---|---|---|
| 需求标题 Request Title | 标题 | Text | 原样复制 |
| 需求编号 | 源编号 | Text | 原样复制 |
| 归属项目 Associated Project | 归属项目 | DuplexLink | 需解析项目库 record_id，写入 string id 列表 |
| 上线日期 Deadline | 期望上线日期 | DateTime | Unix ms(UTC)→北京时区；存时间戳 |
| 需求背景 Background | 描述 | Text | 与目标/描述/附件链接拼接 |
| 需求目标 Objective | 描述 | Text | 与背景/描述/附件链接拼接 |
| 需求描述 Description | 描述 | Text | 与背景/目标/附件链接拼接 |
| 附件（链接）Attachment (Link) | 描述 | Text | 追加到描述末尾（保留链接） |
| 附件（文件）Attachment (File) | 附件 | Attachment | 原样复制（附件 token） |
| 需求方 | 需求方 | User | 原样复制（open_id） |
| UED 负责人 | UED 负责人 | User | 原样复制（open_id） |
| 优先级 | 优先级 | SingleSelect | 若缺失需提醒补齐 |

拼接描述建议模板：
- 需求背景\n需求目标\n需求描述\n[附件链接]


## B. 项目管理（任务源） → WBS（子任务）

| 源表字段（任务源） | 目标表字段（WBS） | 类型 | 规则/说明 |
|---|---|---|---|
| 标题 | 任务名称 | Text | 可加前缀/后缀（如“需求-开发”） |
| 任务源 record_id | 父任务 | DuplexLink | 写入 string id 列表 |
| 负责人 | 负责人 | User | 指定执行人 open_id |
| 优先级 | 优先级 | Lookup | WBS 为 lookup 时无需写 |
| 期望上线日期 | 结束日期 | DateTime | 仅在需要时同步 |
| 备注 | 描述/备注 | Text | 需要时补充 |

## C. 同步检查要点
- 字段名严格匹配，先 list 字段再写入。
- DuplexLink 必须是 string record_id 列表。
- 日期字段必须按 Asia/Shanghai 转换。
