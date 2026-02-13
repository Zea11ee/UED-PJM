# UED-PJM 技能包（本地版）

这是 UED-PJM 的完整技能文件（SKILL + 参考文档 + 示例脚本），用于标准化 UED 需求收集、需求→任务源→WBS 的协同，以及飞书 Bitable/电子表格相关操作。

## 目录
- `SKILL.md`：技能主入口（流程与规则）
- `references/`：参考与经验沉淀
  - `demand-submit.md`：UED 需求 Inbox 提交字段、选项、填法、常见错误
  - `sheets-notes.md`：飞书电子表格读写经验
  - `bitable-notes.md`：Bitable 查询/写入要点
  - `task-notes.md`：任务接口与权限
  - `people-resolution.md`：人员解析规则与常用 open_id
  - `MCP-notes.md` 等：MCP 启动/排障、时间/假期、字段映射、工作流等
- `scripts/`：按域分组的最小示例脚本
  - `sheets/read-range.sh`、`bitable/search-wbs.sh`、`tasks/get-task.sh` 等

## 主要能力（摘要）
- 需求 → 父任务 → WBS 的标准流程，包含字段映射、日期/工时规则、周到期未完结查询、写入前确认
- 人员解析：联系人搜索、历史记录匹配、邮箱/手机号解析 user_id
- Bitable 操作：字段读取、过滤查询、单/批写入
- 飞书电子表格读写：基于 sheet_id 的 range 读写、查找、常见错误处理
- 任务接口：权限与常见错误、排查要点

## 提交/使用注意
- SingleSelect 填“名称”字符串，避免新增乱码选项
- Date 用毫秒时间戳（Asia/Shanghai）
- User 字段必须用 open_id 对象数组，禁止用默认 LinkFlow
- 写入前遵循 SKILL.md 的“确认后落库”规则

## 同步到本地 Codex
将本仓库内容拷贝到 `~/.codex/skills/UED-PJM/` 后，重启 Codex CLI 即可生效。

