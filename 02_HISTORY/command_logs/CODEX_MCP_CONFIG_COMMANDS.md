# Codex MCP Config Commands

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

Scope: Configure project-scoped Codex MCP for `kicad-mcp-pro` in analysis/safe mode only.

Global config rule: `C:\Users\LJ\.codex\config.toml` was checked for existence but not modified.

## Startup And Input Reads

```powershell
Get-Content -LiteralPath 'AGENTS.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\START_HERE.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\SESSION_START_CHECKLIST.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\WORKFLOW_RULES.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\SAFETY_RULES.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\REPO_MAP.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\TOOL_INDEX.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\MEMORY_INDEX.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\HISTORY_INDEX.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\PROJECT_INDEX.md' -Raw
Get-Content -LiteralPath '00_CODEX_START\CURRENT_PROJECT.md' -Raw
Get-Content -LiteralPath '01_MEMORY\GLOBAL_MEMORY.md' -Raw
Get-Content -LiteralPath '01_MEMORY\CODING_AND_SCRIPTING_RULES.md' -Raw
Get-Content -LiteralPath '03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml' -Raw
```

Result: startup files and the draft snippet were read. `CURRENT_PROJECT.md` still reports `Active project name: NONE`.

## Existing Config Inspection

```powershell
Get-Content -LiteralPath '.codex\config.toml' -Raw
```

Result:
```text
# Codex workspace-local configuration placeholder.
# MCP servers are intentionally not configured during bootstrap.
# Add tool and MCP configuration only after reviewing 00_CODEX_START/TOOL_INDEX.md.
```

```powershell
Test-Path -LiteralPath 'C:\Users\LJ\.codex\config.toml'
```

Result:
```text
True
```

```powershell
Get-Date -Format 'yyyyMMdd_HHmmss'
```

Result:
```text
20260430_154257
```

```powershell
Get-ChildItem -LiteralPath '.codex' -Force | Select-Object Mode,Length,Name
```

Result: `.codex\config.toml` existed and `.codex\prompts` existed.

## Backup

```powershell
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$backupDir = '99_BACKUPS\pre_codex_edits'
$backupPath = Join-Path -Path $backupDir -ChildPath "codex_config_$timestamp.toml"
New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
Copy-Item -LiteralPath '.codex\config.toml' -Destination $backupPath
Write-Output $backupPath
Get-Item -LiteralPath $backupPath | Select-Object FullName,Length
```

Result:
```text
99_BACKUPS\pre_codex_edits\codex_config_20260430_154315.toml
C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\codex_config_20260430_154315.toml  Length: 204
```

## Config Edit

Edit method: `apply_patch`.

Changed file:
```text
.codex\config.toml
```

Configured MCP server:
```text
kicad_mcp_pro_analysis
```

Command:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe
```

Args:
```text
serve --transport stdio --profile analysis
```

Environment:
```text
KICAD_MCP_PROFILE=analysis
KICAD_MCP_TRANSPORT=stdio
KICAD_MCP_WORKSPACE_ROOT=C:\Users\LJ\KICAD_ENGINE
KICAD_MCP_PROJECT_DIR=C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active
KICAD_MCP_OUTPUT_DIR=C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis
KICAD_MCP_KICAD_CLI=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
KICAD_MCP_LOG_LEVEL=INFO
KICAD_MCP_LOG_FORMAT=console
KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false
```

## Validation

```powershell
py -3.12 - <<'PY'
...
PY
```

Result: failed because Bash-style heredoc syntax is invalid in PowerShell. No files were changed by this failed parse attempt.

```powershell
New-Item -ItemType Directory -Force -Path '05_OUTPUTS\kicad-mcp-pro-analysis' | Select-Object FullName
```

Result:
```text
C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis
```

```powershell
@'
import pathlib, tomllib
path = pathlib.Path('.codex/config.toml')
with path.open('rb') as f:
    data = tomllib.load(f)
print('TOML_OK')
print(sorted(data.get('mcp_servers', {}).keys()))
print(data['mcp_servers']['kicad_mcp_pro_analysis']['env']['KICAD_MCP_PROFILE'])
'@ | py -3.12 -
```

Result:
```text
TOML_OK
['kicad_mcp_pro_analysis']
analysis
```

```powershell
$env:KICAD_MCP_PROFILE='analysis'
$env:KICAD_MCP_TRANSPORT='stdio'
$env:KICAD_MCP_WORKSPACE_ROOT='C:\Users\LJ\KICAD_ENGINE'
$env:KICAD_MCP_PROJECT_DIR='C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active'
$env:KICAD_MCP_OUTPUT_DIR='C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis'
$env:KICAD_MCP_KICAD_CLI='C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
$env:KICAD_MCP_LOG_LEVEL='INFO'
$env:KICAD_MCP_LOG_FORMAT='console'
$env:KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS='false'
& '03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe' health --json
```

Result: `status: ok`; profile `analysis`; project dir `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active`; output dir `C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis`; KiCad CLI found.

```powershell
Get-Item -LiteralPath 'C:\Users\LJ\.codex\config.toml' | Select-Object FullName,Length,LastWriteTime
```

Result: global config exists at length 1198 with last write time `4/30/2026 2:19:22 PM`; it was not modified by this task.

```powershell
codex mcp list
```

Result: Codex listed `kicad_mcp_pro_analysis` as enabled with command `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe` and args `serve --transport stdio --profile analysis`.

```powershell
codex mcp --help
```

Result: Codex MCP management help printed successfully.

```powershell
Get-Content -LiteralPath '.codex\config.toml' -Raw
```

Result: project-scoped config contained the `kicad_mcp_pro_analysis` server in analysis mode.
