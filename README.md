# UED-PJM

UED-PJM standardizes UED demand execution in Feishu Bitable:
`Demand -> Parent Task (任务源) -> WBS`.

Chinese guide: see `README.zh.md`.

## What's New (2026-02-28)
- Added post-update operating lessons since 2026-02-05:
  `references/post-update-usage-lessons-20260205.md`.
- Synced the latest field-scope and confirm-before-write enforcement in `SKILL.md`.
- Appended recent real-world execution logs in `references/feedback.md`.

## Repository Structure
- `SKILL.md`: workflow, rules, and execution constraints.
- `references/`: mappings, workflows, date/time, people resolution, and run feedback.
- `scripts/`: minimal examples for Bitable/Sheets/Tasks.
- `README.zh.md`: Chinese installation and usage guide.

## Installation (Codex Skill)
1. Copy this skill to local Codex skills directory.
```bash
mkdir -p ~/.codex/skills/UED-PJM
cp -R ./* ~/.codex/skills/UED-PJM/
```
2. Configure MCP servers in `~/.codex/config.json` (or your Codex config path):
  - `lark-mcp` (required)
  - `lark-contacts-mcp` (required for robust name-based assignee resolution)
3. Restart Codex CLI.

## Minimal MCP Example
```json
{
  "mcpServers": {
    "lark-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@larksuiteoapi/lark-mcp",
        "mcp",
        "-a",
        "$LARK_APP_ID",
        "-s",
        "$LARK_APP_SECRET",
        "-t",
        "preset.default,preset.im.default,preset.base.default,preset.base.batch,preset.doc.default,preset.calendar.default",
        "--oauth"
      ]
    },
    "lark-contacts-mcp": {
      "command": "node",
      "args": ["/path/to/lark-contacts-mcp/dist/index.js"]
    }
  }
}
```

## Usage
1. Load the skill in session.
2. Query and analyze demand content (including linked docs, up to 2-hop penetration).
3. Draft parent task and WBS first.
4. Wait for explicit confirmation (`确认/落库/执行`) before any write.
5. Write records and append feedback.

## Core Operating Rules
- Timezone is always `Asia/Shanghai`.
- Person fields must use resolved IDs (open_id/user_id), not plain text names.
- SingleSelect/MultiSelect should be written with option names, not option_id.
- DuplexLink must be a string `record_id[]`.
- Do not write fields outside allowed scope for parent/WBS in confirmation flow.

## Limitations
- Cannot read Feishu Base automations/workflows through public APIs.
- If MCP registration fails repeatedly (`Method not found`), writes must stop.
- Feishu task blocks may not appear in raw doc content and need task APIs/manual check.

## Update Policy
- Keep `SKILL.md`, `README.md`, `README.zh.md`, and affected files in `references/` in sync.
- For each meaningful run/update, append concise logs to `references/feedback.md`.
