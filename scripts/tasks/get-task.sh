#!/usr/bin/env bash
# Fetch task detail by GUID using user_access_token
# Env: TASK_GUID, USER_TOKEN
set -euo pipefail
curl -s "https://open.feishu.cn/open-apis/task/v2/tasks/${TASK_GUID}" \
  -H "Authorization: Bearer ${USER_TOKEN:-}" \
  -H "Content-Type: application/json"
