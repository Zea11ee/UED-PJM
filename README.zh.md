# UED-PJM 技能包（中文说明）

UED-PJM 用于标准化飞书 Bitable 的 UED 需求执行链路：
`需求 -> 父任务（任务源）-> WBS`。

English guide: see `README.md`.

## 最近更新（2026-02-28）
- 新增“上次更新后实战经验”文档：  
  `references/post-update-usage-lessons-20260205.md`
- `SKILL.md` 同步最新规则（先确认后落库、字段范围约束、人员 ID 解析等）。
- `references/feedback.md` 补充近期实操记录。

## 目录说明
- `SKILL.md`：技能主流程与执行约束。
- `references/`：字段映射、流程、日期与人员规则、经验反馈。
- `scripts/`：最小化脚本示例。
- `README.md`：英文安装与使用说明。

## 安装（Codex 技能）
1. 复制技能到本地目录：
```bash
mkdir -p ~/.codex/skills/UED-PJM
cp -R ./* ~/.codex/skills/UED-PJM/
```
2. 配置 MCP（`~/.codex/config.json` 或实际配置路径）：
  - `lark-mcp`（必需）
  - `lark-contacts-mcp`（建议必配，用于姓名解析与人员映射）
3. 重启 Codex CLI。

## MCP 配置最小示例
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

## 使用说明
1. 会话中加载 UED-PJM 技能。
2. 读取需求正文与备注，必要时穿透链接（最多 2 跳）。
3. 先输出父任务与 WBS 草案。
4. 收到明确“确认/落库/执行”后再写入。
5. 落库后回传记录 ID，并追加反馈记录。

## 核心约束
- 时区统一 `Asia/Shanghai`。
- 人员字段必须写 open_id/user_id，不能只写姓名文本。
- 单选/多选字段写“选项名称”而非 option_id。
- DuplexLink 写字符串 `record_id[]`。
- 仅在允许字段范围内写入父任务/WBS。

## 已知限制
- 无法通过公开 API 读取 Base 自动化/工作流配置。
- MCP 若持续 `Method not found`，应停止写入并先排查注册。
- 文档 rawContent 可能不含任务块，需任务 API 或人工核对。

## 维护策略
- 保持 `SKILL.md`、`README.md`、`README.zh.md` 与 `references/` 同步更新。
- 每次关键实操后在 `references/feedback.md` 追加简要记录。
