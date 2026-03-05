# 项目知识库（Project KB）

## 目标
- 减少每次梳理 WBS 时对全量历史需求的重复检索。
- 固化“项目特有”的默认分工、排期偏好、常见模块与实现约束。
- 在需求已拆分并落库后，沉淀高价值变更事件，形成可复用记忆。

## 使用顺序
1. 先读对应项目文件（如 `ANTA.md` / `REDMAGIC.md` / `HYPERSHELL.md`）。
2. 若命中相似模式，直接复用任务链和工时区间。
3. 仅在信息不足时再扩大到 Bitable 历史检索。

## 落库后必做
- 每次“确认并落库”后，追加一条事件到项目文件。
- 默认用脚本自动追加（并去重）：  
  `python3 scripts/project-kb/append_project_kb_entry.py --project "<PROJECT>" --demand-id "<需求编号/源编号>" --module "<页面/模块>" --change "<新增/调整功能点>" --status "已排期" --parent-record-id "<parent_rec_id>" --wbs-record-ids "<wbs_rec_a,wbs_rec_b>"`
- 推荐格式：
  `YYYY-MM-DD | 需求编号 | 页面/模块 | 新增/调整功能点 | 状态(已排期/已上线) | 关联任务ID`

## 维护原则
- 只记录“有落地概率且已进入 WBS”的决策，不记录纯讨论。
- 事件描述聚焦功能/交互变化，避免泛化叙述。
- 状态可后续从“已排期”更新为“已上线”。

## 模板
- 复制 `_TEMPLATE.md` 新建项目文件。
