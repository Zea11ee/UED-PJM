#!/usr/bin/env bash
# Read a range from a Feishu sheet using sheet_id in range (<sheet_id>!A1:C5)
# Env: APP_ID, APP_SECRET, SPREAD (spreadsheet_token), SHEET_ID, RANGE (e.g., 0fUcBh!A1:C5)
set -euo pipefail
TOKEN=$(curl -s -X POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
  -H 'Content-Type: application/json' \
  -d '{"app_id":"'"${APP_ID:-}"'","app_secret":"'"${APP_SECRET:-}"'"}' | python3 -c "import sys,json;print(json.load(sys.stdin)['tenant_access_token'])")
curl -s "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/${SPREAD}/values/${RANGE}?valueRenderOption=ToString&dateTimeRenderOption=FormattedString" \
  -H "Authorization: Bearer $TOKEN"
