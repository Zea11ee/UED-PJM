# UED-PJM Scripts

示例脚本分域存放，便于按需复用：
- sheets/   飞书电子表格读写示例
- bitable/  Bitable 查询/写入示例
- tasks/    任务接口示例
- project-kb/  项目知识库自动沉淀脚本

约定：
- 仅放最小可运行示例（环境变量/占位 token 标注清晰）。
- 脚本命名：功能-语言，如 `read-range.sh`, `batch-insert.py`。
- 更新脚本后，在 README 或脚本头部写运行方式和必需环境变量。

## Project KB 自动追加
- 脚本：`project-kb/append_project_kb_entry.py`
- 用途：在父任务/WBS 落库并回查成功后，自动向 `references/project-kb/<PROJECT>.md` 追加一条变更事件（默认去重）。
- 示例：
  `python3 scripts/project-kb/append_project_kb_entry.py --project ANTA --demand-id ANTA-20260304-01 --module PDP --change 新增支付方式展示 --status 已排期 --parent-record-id rec_parent --wbs-record-ids rec_wbs1,rec_wbs2`
