# kicad-mcp-pro Install Session

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Scope
- Installed only `kicad-mcp-pro`.
- Used isolated Python venv: `03_TOOLS\python_envs\kicad-mcp-pro`.
- Did not install dependencies for any other cloned repo.
- Did not configure MCP globally.
- Did not grant write or manufacturing authority.
- Did not modify real KiCad project files.

## Result
Status: INSTALLED.

Installed package:
- `kicad-mcp-pro` 3.1.8
- Source: local clone at `03_TOOLS\repos\kicad-mcp-pro`
- CLI: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe`

## Tests Run
- `kicad-mcp-pro --help`: passed.
- `kicad-mcp-pro version`: passed, returned `3.1.8`.
- `kicad-mcp-pro health --json`: passed with `status: ok`.
- `kicad-mcp-pro doctor --json`: passed with `status: degraded` because no active KiCad board/project was open.

KiCad CLI was found through explicit path:
`C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`

Doctor reported KiCad CLI version:
`9.0.7`

## MCP Startup Command
```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" serve --transport stdio --profile analysis
```

## Required Environment For Safe First Use
- `KICAD_MCP_PROFILE=analysis`
- `KICAD_MCP_TRANSPORT=stdio`
- `KICAD_MCP_WORKSPACE_ROOT=C:\Users\LJ\KICAD_ENGINE`
- `KICAD_MCP_KICAD_CLI=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- `KICAD_MCP_LOG_LEVEL=INFO`
- `KICAD_MCP_LOG_FORMAT=console`
- `KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false`

`KICAD_MCP_PROJECT_DIR` is intentionally omitted while `CURRENT_PROJECT` is `NONE`.

## Files Written Or Updated
- Created `03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml`.
- Updated `00_CODEX_START\TOOL_INDEX.md`.
- Wrote `02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md`.
- Wrote this session log.

## Risks
- `kicad-mcp-pro` exposes broad KiCad tooling when configured with wider profiles.
- Write/manufacturing tools must not be enabled until a disposable/sample project has passed validation.
- `doctor --json` is degraded until an active KiCad board/project is open and intentionally selected.
- KiCad CLI is still not on PATH; this install relies on explicit `KICAD_MCP_KICAD_CLI`.
- Do not store KiCad IPC tokens or auth tokens in memory/history/config snippets.

## Next Recommended Step
Create or select a disposable/sample KiCad project, copy it under `04_KICAD_PROJECTS\active`, set `CURRENT_PROJECT.md` only when explicitly asked, then test the MCP server in `analysis` profile against that sample before any real project connection.
