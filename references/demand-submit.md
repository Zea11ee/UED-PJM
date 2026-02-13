# UED 需求提交指南（UED 需求 Inbox）

表：UED 需求管理 / UED 需求 Inbox  
app_token: `X2zabbNYUaTlGgsgfKdcQSOCnaf`  
table_id: `tblesE69fcAUGRwD`

## 必填字段（提交时务必填）
- 需求标题 Request Title（Text）
- 归属项目 Associated Project（SingleSelect）
  - 选项：RedMagic / Hypershell / ANTA / Heyup / Nubia / Nothing / Galenic / Formovie / Eureka / Other / UED / 智能化运营 / 智能化建站
- 需求类型 Request Type（SingleSelect）
  - 综合需求 Complex / 设计需求 Design / 开发需求 Development / 方案需求 Solution / 测试需求 Test / 配置需求 Setup / 需求评估 Estimation
- 优先级 Priority（SingleSelect）
  - 很紧急很重要 / 很紧急不重要 / 不紧急很重要 / 不紧急不重要
- 需求背景 Background（Text）
- 需求目标 Objective（Text）
- 需求描述 Description（Text）
- 上线日期 Deadline（Date，毫秒时间戳，Asia/Shanghai）
- 需求方（User 单选）※须使用实际提单人 open_id，禁止留默认 LinkFlow

## 附件（选填）
- 附件（文件）Attachment (File)
- 附件（链接）Attachment (Link)

## 填写规则
- SingleSelect：用“名称”字符串，不要用 option_id，避免生成乱码选项。
- Date：毫秒时间戳（例：2026-02-13 00:00:00+08 → 1770912000000）。
- User：数组对象形式，例如 `"需求方":[{"id":"ou_xxx"}]`。
- 其他字段（状态、编号、工时、创建人等）为系统/回填，一般不手填。

## 常见错误与避免
- 需求方写成 LinkFlow：务必先 contacts-mcp 搜索 open_id，再写入 User 数组。
- 时间戳用秒级导致日期偏移：一律用毫秒。
- SingleSelect 用错 id：只写名称。

## 提交示例（接口）
```json
{
  "fields": {
    "需求标题 Request Title": "示例标题",
    "归属项目 Associated Project": "RedMagic",
    "需求类型 Request Type": "开发需求 Development",
    "优先级 Priority": "很紧急很重要 Urgent and Important",
    "需求背景 Background": "...",
    "需求目标 Objective": "...",
    "需求描述 Description": "...",
    "上线日期 Deadline": 1770912000000,
    "需求方": [{"id": "ou_xxx"}]
  }
}
```

## 建议流程（人工/工具）
1) contacts-mcp 搜索需求方，拿 open_id。
2) 准备毫秒时间戳（Asia/Shanghai）。
3) 填写必填字段，SingleSelect 用名称字符串。
4) 如有附件/链接，放对应字段；无则留空。
5) 用 `bitable_v1_appTableRecord_create` 落库；若需修正，用 `bitable_v1_appTableRecord_update`。

