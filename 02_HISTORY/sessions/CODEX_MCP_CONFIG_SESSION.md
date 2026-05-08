# Codex MCP Config Session

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Scope
- Configured project-scoped Codex MCP in `.codex\config.toml`.
- Used `kicad-mcp-pro` only.
- Used analysis profile only.
- Did not modify `C:\Users\LJ\.codex\config.toml`.
- Did not enable manufacturing/export authority.
- Did not enable experimental tools.
- Did not enable parallel MCP calls.
- Did not edit KiCad project files.

## Backup
Existing project-scoped config was backed up to:

`99_BACKUPS\pre_codex_edits\codex_config_20260430_154315.toml`

## MCP Server
Server name:

`kicad_mcp_pro_analysis`

Command:

`C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe`

Args:

`serve --transport stdio --profile analysis`

Environment:
- `KICAD_MCP_PROFILE=analysis`
- `KICAD_MCP_TRANSPORT=stdio`
- `KICAD_MCP_WORKSPACE_ROOT=C:\Users\LJ\KICAD_ENGINE`
- `KICAD_MCP_PROJECT_DIR=C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active`
- `KICAD_MCP_OUTPUT_DIR=C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis`
- `KICAD_MCP_KICAD_CLI=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- `KICAD_MCP_LOG_LEVEL=INFO`
- `KICAD_MCP_LOG_FORMAT=console`
- `KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false`

## Verification
- `.codex\config.toml` parsed successfully with Python `tomllib`.
- `kicad-mcp-pro health --json` returned `status: ok`.
- `codex mcp list` showed `kicad_mcp_pro_analysis` as enabled.

## Limitations
- `KICAD_MCP_PROJECT_DIR` points to the active-projects root, not to one selected project.
- `CURRENT_PROJECT.md` still says `NONE`, so Codex must not edit KiCad project files.
- Analysis profile is configured, but any write/destructive/manufacturing tool use still requires manual approval, active project selection, and backup gates.
- No final fabrication/export gate is configured.
