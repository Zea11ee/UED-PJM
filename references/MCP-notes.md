# MCP 使用经验总结（UED-PJM）

## 常见问题与根因
- **Method not found / 未注册**：本会话未成功启动或注册 lark-mcp；tools/list 报 -32601 属于会话层问题，而非工具缺失。
- **启动慢/超时**：lark-mcp 通过 npx 远程拉起，网络或初始化慢时会导致刚开会话即调用接口出现错误。
- **跨会话不一致**：配置未同步或会话尚未加载最新 ~/.codex/config.*，导致有的会话正常、有的报错。

## 快速排查
1) 新会话先跑轻量调用确认：`docx_builtin_search` 或 `whoami`（如果有）以确保 mcp ready；若 -32601，则会话未注册。
2) 检查配置：~/.codex/config.json 与 ~/.codex/config.toml 是否包含 lark-mcp / lark-contacts-mcp，工具列表含 wiki/doc/sheets 等。
3) 如仍报错：重启 mcp 进程或重开会话；必要时用本地 dist 版 lark-mcp 代替 npx 启动以提高成功率。

## 稳定性建议
- 保持 config 同步（已含 wiki/doc/sheets）。
- 会话启动后先做一次探测调用再进入正式流程。
- 若网络不稳或 npx 启动频繁失败，可切换到本地源码版 lark-mcp（node dist）并在 config 中改为本地路径。

## 身份与权限（Sheet/Bitable）
- user_access_token 需对应有访问权限的用户；不可见时 API 可能直接 404 隐匿。
- tenant_access_token（应用身份）访问私有文档前，需把应用/机器人加为协作者并确认数据域一致。
- 数据域需匹配：国际区 token 访问中国区文档会 404；确保 app/用户与文档在同一域/租户。

## 复用
- 在 UED-PJM 流程中，若遇 MCP 报 -32601 或 404（隐藏资源），先用以上步骤确认注册、会话、数据域与访问主体，再继续需求处理。
