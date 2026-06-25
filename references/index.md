# UED-PJM 知识索引

本页面是 UED-PJM 技能的统一知识入口。查询时先读本页，再进入对应子页面。

---

## 项目知识

按项目沉淀的特有知识（默认分工、排期偏好、常见模块、历史变更）：

- [ANTA](project-kb/ANTA.md) — ANTA 项目知识
- [REDMAGIC](project-kb/REDMAGIC.md) — RedMagic 项目知识
- [HYPERSHELL](project-kb/HYPERSHELL.md) — Hypershell 项目知识
- [LIBERNOVO](project-kb/LIBERNOVO.md) — LiberNovo 项目知识

新项目首次处理后，应建立对应项目页。

---

## 需求拆分模板

按需求类型沉淀的可复用拆分模式：

- [活动双阶段](case-kb/campaign-two-phase.md) — Teasing + Launch 两阶段活动需求
- [轻量配置](case-kb/lightweight-config.md) — 纯配置或轻量调整类需求
- [问题修复](case-kb/bug-fix.md) — Bug Fix / Incident 紧急修复
- [产品调研](case-kb/research-evaluation.md) — 前期调研、可行性评估
- [商品同步](case-kb/product-sync.md) — 商品上架、SKU 配置

查询时先按需求类型匹配模板，再叠加项目知识。

---

## 稳定规则

从 feedback.md 提炼的稳定规则（被重复验证 ≥3 次）：

- [任务拆分规则](rules/task-split.md) — 中大型任务必须拆分开发与测试
- [Bitable 字段写入规则](rules/bitable-field-write.md) — 单选/多选字段用名称不用 option_id
- [确认后落库规则](rules/confirm-before-write.md) — 任何落表操作前必须先出草稿确认

新规则从 feedback.md 积累，被重复使用 ≥3 次后提炼到此处。

---

## 人员

- [人员档案](people-profiles.md) — 人员 ID/邮箱/角色/项目缓存

人员解析优先查档案，缺失时再查 lark-cli contact。

---

## 待补空白

以下知识尚未建立独立页面，遇到相关需求时应考虑补充：

- [ ] 问题修复类需求模板（case-kb）
- [ ] 人员排期冲突处理规则（rules）
- [ ] 跨表附件 token 处理规则（rules）
- [ ] 周末/节假日排期边界规则（rules）

---

## 使用说明

### Query 优先级

```
1. index.md（本页）
2. project-kb/{PROJECT}.md
3. case-kb/{template}.md
4. rules/{rule}.md
5. people-profiles.md
6. feedback.md
7. Bitable 历史记录
8. 在线数据源
```

### Ingest 规则

| 场景 | 动作 |
|------|------|
| 新项目首次出现 | 建 `project-kb/{PROJECT}.md` |
| feedback.md 经验被用 ≥3 次 | 提炼到 `rules/` |
| 需求落库完成 | 自动追加项目 KB（脚本已有） |
| 新人员解析成功 | 更新 `people-profiles.md` |

### Weekly Lint Checklist

每周检查一次：

1. `project-kb/` 是否覆盖近 30 天内处理过的所有项目？
2. `people-profiles.md` 是否有超过 60 天未更新的条目？
3. `feedback.md` 是否有被重复使用 ≥3 次但未提炼成规则的经验？
4. 本页是否覆盖所有 `rules/`、`project-kb/`、`case-kb/` 文件？

---

## 维护记录

- 2026-04-11：创建索引页，初始化规则目录
