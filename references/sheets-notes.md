# 飞书 Sheets 读写经验（持续更新）

> 适用场景：UED-PJM 工作流中需要读取/写入飞书电子表格（非多维表格）。

## 速查
- **range 必须用 sheet_id**：格式 `<sheetId>!A1:C5`，不要用 sheet 名。
- **获取 sheet_id**：`sheets.v3.spreadsheetSheet.query` → `sheet_id/title` 列表。
- **读单范围**：`GET /open-apis/sheets/v2/spreadsheets/{token}/values/{sheetId}!A1:C5`
  - 建议参数：`valueRenderOption=ToString&dateTimeRenderOption=FormattedString`。
- **批量读**：`GET .../values_batch_get?ranges=<sheetId>!A1:B5,<sheetId2>!C1:D3`。
- **写入**：`PUT /open-apis/sheets/v2/spreadsheets/{token}/values`，body：
  ```json
  {"valueRange":{"range":"<sheetId>!A20:A20","values":[["TEXT"]]}}
  ```
- **查找定位（不返回值）**：`POST .../sheets/{sheetId}/find`，传 `find_condition.range` 用 sheet_id。
- **token**：tenant_access_token 可读写（前提：应用在表上有协作权限；域/租户一致）。

## 推荐步骤（最小可用）
1) 取 tenant_access_token（app_id/app_secret）。
2) `sheets.v3.spreadsheetSheet.query` 拿到目标 sheet 的 `sheet_id`。
3) 读：`GET .../values/<sheet_id>!A1:C5`；批量读用 `values_batch_get`。
4) 写：`PUT .../values`，range 用 sheet_id。
5) 定位文本：`POST .../sheets/<sheet_id>/find` → `matched_cells`。

## 常见错误 & 解决
- 1310211 Wrong Sheet Id：range 里用了 sheet 名 / sheet_id 拼错；改为 `<sheetId>!…`。
- 1310202 Wrong Range：range 不合法或 JSON 体字段错；核对坐标与字段名。
- 404 page not found：使用了 v3 读值路径或错误的 URL；改用 v2 `values` / `values_batch_get`。
- MCP 工具缺读值：官方 lark-mcp 没有“读值”工具，需直接 REST/SDK。

## 实测参考（Working hours- UED, token XxJpsfIfUhAYTztvvP2cXMDznme）
- sheet_id 列表：Guide(0fUcBh)、Feb.25(5FtZuj)、…、汇总(nafF69)。
- 读 `0fUcBh!A1:C5` → 成功返回指南长文本。
- 写 `0fUcBh!A20:A20` = MCP-OK 成功；`find` 命中 A20；`values_batch_get` 读到写入值。

## 复制即用示例
```bash
APP_ID=cli_a846681bc822100c
APP_SECRET=i2aTic6I8lSGrCV2HvcoMgT6hqJjw1B1
SPREAD=XxJpsfIfUhAYTztvvP2cXMDznme
SHEET_ID=0fUcBh   # 先用 spreadsheetSheet.query 获取
TOKEN=$(curl -s -X POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
  -H 'Content-Type: application/json' \
  -d '{"app_id":"'$APP_ID'","app_secret":"'$APP_SECRET'"}' | python3 -c "import sys,json;print(json.load(sys.stdin)['tenant_access_token'])")

# 读
curl -s "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/${SPREAD}/values/${SHEET_ID}!A1:C5?valueRenderOption=ToString&dateTimeRenderOption=FormattedString" \
  -H "Authorization: Bearer $TOKEN"

# 写
curl -s -X PUT "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/${SPREAD}/values" \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"valueRange":{"range":"'${SHEET_ID}'!A20:A20","values":[["MCP-OK"]]}}'

# 查找
curl -s -X POST "https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/${SPREAD}/sheets/${SHEET_ID}/find" \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"find_condition":{"range":"'${SHEET_ID}'!A1:C30","match_case":false,"match_entire_cell":false,"search_by_regex":false,"include_formulas":false},"find":"MCP-OK"}'
```

## 维护约定
- 新的 Sheets 读写踩坑请追加到本文件，不要挤在 SKILL.md 正文。
- 若接口路径/域名变动，先在这里更新验证用的 curl，再同步 SKILL.md 的 Quick Reference。
