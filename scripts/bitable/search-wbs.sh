#!/usr/bin/env bash
# Minimal WBS search by owner + status != 已完成
# Env: APP_TOKEN (bitable app token), TABLE_ID (WBS table), OWNER_OPEN_ID
set -euo pipefail
json=$(cat <<EOF
{
  "field_names": ["任务名称","负责人","状态","结束日期"],
  "filter": {
    "conjunction": "and",
    "conditions": [
      {"field_name":"负责人","operator":"contains","value":["${OWNER_OPEN_ID:-}"]},
      {"field_name":"状态","operator":"isNot","value":["已完成"]},
      {"field_name":"结束日期","operator":"isNotEmpty","value":[]}
    ]
  },
  "sort": [{"field_name":"结束日期","desc":false}],
  "automatic_fields": true
}
EOF
)
curl -s -X POST "https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/records/search" \
  -H "Content-Type: application/json" \
  -d "$json"
