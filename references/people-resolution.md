# 人员解析（open_id / user_id）

## 使用顺序
1) lark-contacts-mcp 名称搜索（中文/英文/拼音/近似匹配）。
2) 历史记录匹配（WBS/项目库/任务源/人员映射表）。
3) contact_v3_user_batchGetId（email/phone）。
4) 仍缺失 → 向需求方要 email/phone。

## 档案库联动
- 常用人员缓存维护在 `people-profiles.md`（name/open_id/user_id/email/role/project）。
- 调度顺序：先读档案库做快速匹配，再用 contacts MCP 校验/补全。
- contacts MCP 必须可用；档案库仅用于提效，不替代实时查询。

## 写入规则
- People 字段必须写 open_id/user_id，禁止只写姓名。
- 负责人必须属于 UED 部门；非 UED 需确认或置空。
- 需求文本点名但非 UED：不得直接指派，需确认。
- 默认不把“需求方”当执行人；无法判定时列候选、待确认。

## 常用对象（便于对照）
- 详见 `people-profiles.md`。

## 失效场景提示
- 多租户/同名：联系人 UI 可见但 API 403/404，需要确认租户与授权账号一致。
- user_access_token 过期：401/99991677 → 刷新/重新登录。
