# Visual Review Tools Install Commands

Date: 2026-04-30
Scope: inspect, install/test or document blockers for InteractiveHtmlBom, PcbDraw, and KiCanvas.
Rules: do not modify real KiCad projects; do not generate final manufacturing outputs; install one tool at a time; record every command.


## Read startup file: AGENTS.md

Command:
```powershell
Get-Content -LiteralPath "AGENTS.md" -Raw
```
Exit code: 0
Output:
```text
# AGENTS.md

Strict operating rules for Codex and other AI agents in this KiCad engineering workspace.

## Mandatory Startup Order
At the start of every session, Codex must read this `AGENTS.md` file first.

After reading `AGENTS.md`, Codex must read the following files in this exact order before touching KiCad project files:
1. `00_CODEX_START/START_HERE.md`
2. `00_CODEX_START/SESSION_START_CHECKLIST.md`
3. `00_CODEX_START/WORKFLOW_RULES.md`
4. `00_CODEX_START/SAFETY_RULES.md`
5. `00_CODEX_START/REPO_MAP.md`
6. `00_CODEX_START/TOOL_INDEX.md`
7. `00_CODEX_START/MEMORY_INDEX.md`
8. `00_CODEX_START/HISTORY_INDEX.md`
9. `00_CODEX_START/PROJECT_INDEX.md`
10. `00_CODEX_START/CURRENT_PROJECT.md`

After the startup files are read, Codex must review relevant project memory and history before touching KiCad files.

## Workspace Boundaries
- Active KiCad projects belong under `04_KICAD_PROJECTS/active/`.
- Templates belong under `04_KICAD_PROJECTS/templates/`.
- External tool repositories belong under `03_TOOLS/repos/`.
- Generated release outputs belong under `05_OUTPUTS/`.
- Datasheets and reference documents belong under `06_DATASHEETS/`.
- Backups before automated edits belong under `99_BACKUPS/pre_codex_edits/`.
- MCP server configuration is intentionally deferred.

## Hard Restrictions
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP servers yet.
- Do not modify KiCad files unless the active project is identified in `00_CODEX_START/CURRENT_PROJECT.md`.
- Do not edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing output files unless the active project is identified.
- Do not store passwords, API keys, license keys, private tokens, or credentials in memory or history.

## Required Before KiCad Edits
Before editing KiCad project files, Codex must:
- Confirm the active project name and active project path.
- Confirm that the target files are inside the active project folder.
- Create or confirm a backup in `99_BACKUPS/pre_codex_edits/`.
- State the active project, path, files likely to change, verification plan, and rollback plan.
- Check relevant memory and history for prior constraints, decisions, review notes, and open issues.

## Verification Requirements
- After schematic changes, run ERC or explain why ERC could not be run.
- After PCB changes, run DRC or explain why DRC could not be run.
- Treat manufacturing output as not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Separate review findings from direct edits unless the user explicitly asks for fixes.

## Memory And History Rules
- Durable design decisions go in `01_MEMORY/`, not command logs.
- Commands, command results, failed attempts, and verification outputs go in `02_HISTORY/`.
- After meaningful work, write a session log in `02_HISTORY/sessions/` or project-specific history.
- Project-specific durable decisions belong in `01_MEMORY/projects/PROJECT_NAME/PROJECT_MEMORY.md`.
- Project-specific history belongs in `02_HISTORY/project_history/PROJECT_NAME/`.

## Primary Directive
Assist with KiCad design, review, verification, documentation, and release preparation while preserving project files unless the user explicitly asks for edits and the startup gates above are satisfied.


```

## Read startup file: 00_CODEX_START\START_HERE.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\START_HERE.md" -Raw
```
Exit code: 0
Output:
```text
# Start Here

This is the first startup instruction file after the root `AGENTS.md`.

## Required Startup Sequence
Codex must complete the full startup sequence before touching KiCad project files:
1. Read root `AGENTS.md`.
2. Read every file in `00_CODEX_START/` in the order listed by `AGENTS.md`.
3. Identify the active project from `CURRENT_PROJECT.md`.
4. Review relevant `01_MEMORY/` files.
5. Review relevant `02_HISTORY/` files.
6. Only then inspect or edit KiCad project files.

## Session Rule
If the active project is `NONE`, Codex may organize instructions, memory, history, indexes, and workspace documentation, but must not edit KiCad project files.

## Deferred Setup
Do not install tools, clone repositories, or configure MCP servers during startup.

## First Action Checklist
- Confirm the workspace root.
- Confirm the active project.
- Confirm the task mode.
- Confirm whether KiCad files are in scope.
- If KiCad files are in scope, verify that backups and a rollback plan exist before edits.


```

## Read startup file: 00_CODEX_START\SESSION_START_CHECKLIST.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\SESSION_START_CHECKLIST.md" -Raw
```
Exit code: 0
Output:
```text
# Session Start Checklist

Use this checklist at the beginning of every Codex session.

## Read Order
- Confirm root `AGENTS.md` has been read.
- Confirm `START_HERE.md` has been read.
- Continue through the remaining `00_CODEX_START/` files in the order required by `AGENTS.md`.

## Project Identification
- Read `CURRENT_PROJECT.md`.
- State the active project name.
- State the active project path.
- State the current task mode.
- If the active project is `NONE`, do not touch KiCad project files.

## Context Review
- Read relevant global memory files in `01_MEMORY/`.
- Read relevant project memory under `01_MEMORY/projects/PROJECT_NAME/` when an active project exists.
- Read relevant session logs, reviews, command logs, ERC/DRC reports, and fabrication reviews under `02_HISTORY/`.

## Before KiCad File Access
- Confirm files are under the active project path.
- Confirm whether the task is design, review, verification, tooling, documentation, or release preparation.
- Identify files likely to change.
- Prepare the verification plan.
- Prepare the rollback plan.
- Create or confirm a backup in `99_BACKUPS/pre_codex_edits/` before edits.

## Session Close
- Record meaningful work in `02_HISTORY/sessions/` or project-specific history.
- Put durable decisions in `01_MEMORY/`.
- Put commands and command results in `02_HISTORY/`.
- Do not record secrets or credentials.


```

## Read startup file: 00_CODEX_START\WORKFLOW_RULES.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\WORKFLOW_RULES.md" -Raw
```
Exit code: 0
Output:
```text
# Workflow Rules

## Startup Workflow
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Identify the active project.
4. Review relevant memory and history.
5. State scope before touching KiCad files.

## Work Boundaries
- Work only in the active project folder for project-specific work.
- Keep active KiCad projects in `04_KICAD_PROJECTS/active/`.
- Keep templates in `04_KICAD_PROJECTS/templates/`.
- Keep external repositories in `03_TOOLS/repos/`.
- Keep generated outputs in `05_OUTPUTS/` unless a project explicitly tracks them.
- Keep datasheets and reference files in `06_DATASHEETS/`.
- Keep pre-edit backups in `99_BACKUPS/pre_codex_edits/`.

## Before Design Changes
Codex must state:
- Active project name.
- Active project path.
- Files likely to change.
- Verification plan.
- Rollback plan.

## Work Products
- Durable design decisions go in `01_MEMORY/`.
- Commands and command results go in `02_HISTORY/command_logs/`.
- Session summaries go in `02_HISTORY/sessions/`.
- Design reviews go in `02_HISTORY/design_reviews/`.
- ERC/DRC reports go in `02_HISTORY/erc_drc_reports/`.
- Fabrication reviews go in `02_HISTORY/fabrication_reviews/`.
- Project-specific history goes in `02_HISTORY/project_history/PROJECT_NAME/`.

## Tooling Limits
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP yet.
- If a requested check cannot run because tooling is missing, explain the limitation and record it in history when relevant.


```

## Read startup file: 00_CODEX_START\SAFETY_RULES.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\SAFETY_RULES.md" -Raw
```
Exit code: 0
Output:
```text
# Safety Rules

## Protected Files
Do not edit these files unless the active project is identified and the user task explicitly requires it:
- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`
- Symbol libraries
- Footprint libraries
- Manufacturing output files

## Required Before Protected Edits
- Confirm the active project name is not `NONE`.
- Confirm the active project path is not `NONE`.
- Confirm the target files are inside the active project path.
- Create or confirm a backup in `99_BACKUPS/pre_codex_edits/`.
- State files likely to change.
- State the verification plan.
- State the rollback plan.

## Verification Gates
- After schematic changes, run ERC or explain why ERC could not be run.
- After PCB changes, run DRC or explain why DRC could not be run.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.

## Review Discipline
- Verify connector pinouts, polarity, voltage ratings, current ratings, thermal limits, and mechanical constraints against datasheets.
- Keep review findings separate from edits unless the user asks for implementation.
- Do not overwrite user work.
- Do not revert unrelated changes.

## Secret Handling
Do not store passwords, API keys, license keys, private tokens, or credentials in:
- `01_MEMORY/`
- `02_HISTORY/`
- Project notes
- Generated reports


```

## Read startup file: 00_CODEX_START\REPO_MAP.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\REPO_MAP.md" -Raw
```
Exit code: 0
Output:
```text
# Repository Map

All external repositories belong in:

`03_TOOLS\repos`

## Current State
- Approved open-source KiCad/Codex support repositories are cloned under `03_TOOLS\repos`.
- Dependencies are not installed.
- Repositories have not been modified after cloning.
- MCP is not configured.
- Do not pull changes unless explicitly requested.
- Last inspection: 2026-04-30. All seven requested repositories already existed and were inspected without recloning or pulling.

## Repository Records

### kicad-mcp-pro
- Local path: `03_TOOLS\repos\kicad-mcp-pro`
- Source URL: `https://github.com/oaslananka/kicad-mcp-pro.git`
- Current branch: `main`
- Latest commit: `9991061561d1e3551dee03a525c06bf2e2cbaf02`
- Latest commit subject: `chore: sync uv lock for 3.1.8`
- Purpose: MCP-assisted KiCad automation support.
- Status: cloned, not installed, MCP not configured.
- Last inspected: 2026-04-30.

### kicad-happy
- Local path: `03_TOOLS\repos\kicad-happy`
- Source URL: `https://github.com/aklofas/kicad-happy.git`
- Current branch: `main`
- Latest commit: `2a7dc4147a8edbbe3694498ff1ba9f06e37244cb`
- Latest commit subject: `fix: handle dict format in power_rails list (#16)`
- Purpose: KiCad helper automation and scripting support.
- Status: cloned, not installed.
- Last inspected: 2026-04-30.

### KiCAD-MCP-Server
- Local path: `03_TOOLS\repos\KiCAD-MCP-Server`
- Source URL: `https://github.com/mixelpixx/KiCAD-MCP-Server.git`
- Current branch: `main`
- Latest commit: `d3c01e20bd3af96eaaebcdb84baa7ec9908b31e4`
- Latest commit subject: `Merge pull request #139 from mixelpixx/fix/post-pr88-regressions`
- Purpose: MCP server for KiCad integration experiments.
- Status: cloned, not installed, MCP not configured.
- Last inspected: 2026-04-30.

### KiBot
- Local path: `03_TOOLS\repos\KiBot`
- Source URL: `https://github.com/INTI-CMNB/KiBot.git`
- Current branch: `master`
- Latest commit: `367a2e04122aa46413a30e61cb213bfe7223c8c8`
- Latest commit subject: `[DOCs] Updated tags`
- Purpose: Repeatable KiCad checks, exports, and release generation.
- Status: cloned, not installed.
- Last inspected: 2026-04-30.

### InteractiveHtmlBom
- Local path: `03_TOOLS\repos\InteractiveHtmlBom`
- Source URL: `https://github.com/openscopeproject/InteractiveHtmlBom.git`
- Current branch: `master`
- Latest commit: `8c13013fc5233cfa31698a777813e87502bdb625`
- Latest commit subject: `Fix dnp detection for kicad variants`
- Purpose: Interactive HTML BOM generation.
- Status: cloned, not installed.
- Last inspected: 2026-04-30.

### PcbDraw
- Local path: `03_TOOLS\repos\PcbDraw`
- Source URL: `https://github.com/yaqwsx/PcbDraw.git`
- Current branch: `master`
- Latest commit: `9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f`
- Latest commit subject: `Normalize package name and fix build command`
- Purpose: PCB rendering for documentation and visual review.
- Status: cloned, not installed.
- Last inspected: 2026-04-30.

### kicanvas
- Local path: `03_TOOLS\repos\kicanvas`
- Source URL: `https://github.com/theacodes/kicanvas.git`
- Current branch: `main`
- Latest commit: `b031159eb74aaa7eef2b026fd85d35bc05ff2095`
- Latest commit subject: `fix: file loading fails when path contains URL-encoded characters (#192)`
- Purpose: Browser-based KiCad visualization.
- Status: cloned, not installed.
- Last inspected: 2026-04-30.

## Future Repository Records
When the user explicitly authorizes adding another repository, document:
- Repository name.
- Repository URL.
- Local path under `03_TOOLS\repos`.
- Purpose.
- Install date.
- Required environment.
- Command entry points.
- Known limitations.
- Related history log.


```

## Read startup file: 00_CODEX_START\TOOL_INDEX.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\TOOL_INDEX.md" -Raw
```
Exit code: 0
Output:
```text
# Tool Index

This file tracks intended and available KiCad-related tools. `CLONED_NOT_INSTALLED` means the source repository is present locally, but dependencies have not been installed and setup scripts have not been run.

## Startup Tooling Rule
- Do not install tools unless explicitly requested.
- Do not clone additional repositories unless explicitly requested.
- Do not configure MCP unless explicitly requested.
- Before using any tool, confirm it exists locally and record important command results in `02_HISTORY/`.
- Do not give an MCP server write or manufacturing authority until tested on non-critical sample files.
- Last inspection: 2026-04-30. All cloned support repositories remained `CLONED_NOT_INSTALLED`; no dependencies were installed and no setup scripts were run.
- Install plan: `03_TOOLS\tool_logs\INSTALL_PLAN.md`.
- Local environment check: `03_TOOLS\tool_logs\LOCAL_ENVIRONMENT_CHECK.md`.
- Current local blockers: KiCad 9.0.7 is installed at `C:\Program Files\KiCad\9.0\bin`, but `kicad` and `kicad-cli` are not on PATH. Python 3.12.10 is available through `py`, and pip 25.0.1 is available through `py -m pip`, but `python` and `pip` are not on PATH. Node `v22.15.0`, npm `10.9.2`, Git `2.52.0.windows.1`, PowerShell `5.1.26100.8115`, and Codex CLI `0.80.0` are available.

## Tool Records

### KiCad
- Status: INSTALLED_NOT_ON_PATH
- Location: `C:\Program Files\KiCad\9.0\bin\kicad.exe`
- Version: 9.0.7 from Windows file metadata.
- Purpose: KiCad schematic, PCB, library, and fabrication workflow.
- Notes: `kicad --version` is not callable from PATH. Do not assume PATH-based KiCad automation works until PATH is fixed or full executable paths are validated.

### kicad-cli
- Status: INSTALLED_NOT_ON_PATH
- Location: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- Version: 9.0.7 from Windows file metadata.
- Purpose: Command-line ERC, DRC, exports, and automation.
- Notes: `kicad-cli version` is not callable from PATH. A full-path version probe timed out during the 2026-04-30 environment check; validate CLI execution before using ERC, DRC, or export automation.

### Codex CLI/App
- Status: INSTALLED
- Location: `C:\Users\LJ\AppData\Roaming\npm\codex.cmd`; VS Code extension binary also present at `c:\Users\LJ\.vscode\extensions\openai.chatgpt-26.422.71525-win32-x64\bin\windows-x86_64\codex.exe`
- Version: `codex-cli 0.80.0`
- Purpose: AI-assisted workspace operations and documentation.
- Notes: Follow `AGENTS.md` and startup instructions.

## Local Runtime Tools
- PowerShell: `5.1.26100.8115` at `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe`.
- Python launcher: `py` at `C:\Users\LJ\AppData\Local\Microsoft\WindowsApps\py.exe`; `py --version` reports Python 3.12.10.
- Python command: `python` is not on PATH.
- pip command: `pip` is not on PATH; `py -m pip --version` reports pip 25.0.1 for Python 3.12.
- Node: `v22.15.0` at `C:\Program Files\nodejs\node.exe`.
- npm: `10.9.2` at `C:\Program Files\nodejs\npm.cmd`.
- Git: `git version 2.52.0.windows.1` at `C:\Program Files\Git\cmd\git.exe`.

## Workspace PowerShell Automation Scripts
- Status: CREATED_SYNTAX_CHECKED_NOT_PROJECT_TESTED.
- Location: `03_TOOLS\scripts`.
- Created: 2026-04-30.
- Last revalidated: 2026-04-30 15:32:27 -04:00.
- Session log: `02_HISTORY\sessions\KICAD_VERIFICATION_SCRIPTS_CREATED.md`.
- Safety posture: scripts accept `-ProjectPath`, fail when the project path is missing, resolve or require `kicad-cli`, create timestamped folders, write logs, do not delete source files, and mark generated manufacturing-style exports as not final.
- Test status: PowerShell parser checks passed for all scripts. Scripts were not run against any real KiCad project.
- KiCad CLI note: scripts first try PATH, then search `C:\Program Files\KiCad` for `kicad-cli.exe`, and also accept explicit `-KiCadCliPath`.

### Verification Script Entries
- `run_erc.ps1`: runs KiCad schematic ERC and writes a timestamped report folder.
- `run_drc.ps1`: runs KiCad PCB DRC and writes a timestamped report folder.
- `export_gerbers.ps1`: exports Gerbers into a timestamped not-final output folder.
- `export_drill.ps1`: exports drill files into a timestamped not-final output folder.
- `export_step.ps1`: exports STEP into a timestamped not-final output folder.
- `export_bom.ps1`: exports BOM into a timestamped BOM/output folder for review.
- `full_verify_project.ps1`: locates project files, runs backup, ERC, DRC, BOM, Gerber, drill, and STEP child scripts, and writes a verification summary.
- `backup_kicad_project.ps1`: copies KiCad project source files and local libraries into `99_BACKUPS\pre_codex_edits\PROJECT_NAME_TIMESTAMP`.
- `find_kicad_project_files.ps1`: inventories KiCad project, schematic, PCB, symbol, and footprint files.
- `kicad_automation_common.ps1`: shared helper used by the entry scripts.

### kicad-mcp-pro
- Status: INSTALLED_PROJECT_SCOPED_CODEX_CONFIGURED_ANALYSIS_ONLY
- Location: `03_TOOLS\repos\kicad-mcp-pro`
- Environment: `03_TOOLS\python_envs\kicad-mcp-pro`
- CLI: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe`
- Source URL: `https://github.com/oaslananka/kicad-mcp-pro.git`
- Branch: `main`
- Commit: `9991061561d1e3551dee03a525c06bf2e2cbaf02`
- Purpose: MCP-assisted KiCad automation support.
- Installed version: 3.1.8.
- Install method used: local clone installed into dedicated Python 3.12 venv with `python -m pip install 03_TOOLS\repos\kicad-mcp-pro`.
- Runtime requirements: Python >=3.12; `uv`/`uvx` recommended; KiCad/`kicad-cli` for real workflows. Repo dev scripts require Node >=24.11.0 and npm >=11.6.1.
- Safe tests run: `--help`, `version`, `health --json`, and `doctor --json` with `KICAD_MCP_PROFILE=analysis`.
- Test result: installed and healthy; `doctor --json` reported `status: degraded` only because no active KiCad board/project was open. KiCad CLI was found through explicit path `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` and reported version 9.0.7.
- MCP startup command: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe serve --transport stdio --profile analysis`.
- Draft Codex config: `03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml`.
- Active project-scoped Codex config: `.codex\config.toml`.
- MCP server name: `kicad_mcp_pro_analysis`.
- Project-scoped env: `KICAD_MCP_PROFILE=analysis`, `KICAD_MCP_TRANSPORT=stdio`, `KICAD_MCP_WORKSPACE_ROOT=C:\Users\LJ\KICAD_ENGINE`, `KICAD_MCP_PROJECT_DIR=C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active`, `KICAD_MCP_OUTPUT_DIR=C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis`, `KICAD_MCP_KICAD_CLI=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`, `KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false`.
- Project-scoped config backup: `99_BACKUPS\pre_codex_edits\codex_config_20260430_154315.toml`.
- Command log: `02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md`.
- Config command log: `02_HISTORY\command_logs\CODEX_MCP_CONFIG_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md`.
- Config session log: `02_HISTORY\sessions\CODEX_MCP_CONFIG_SESSION.md`.
- Initial authority: analysis-only; no write or manufacturing authority.
- Notes: MCP config was applied only to the workspace-local `.codex\config.toml`; global `C:\Users\LJ\.codex\config.toml` was not modified. Manufacturing/export authority and experimental tools remain disabled. Write/destructive tools still require manual approval and active project backup gates.

### kicad-happy
- Status: INSTALLED_ANALYSIS_ONLY
- Location: `03_TOOLS\repos\kicad-happy`
- Environment: `03_TOOLS\python_envs\kicad-happy`
- Runner: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-happy\Scripts\python.exe`
- Source URL: `https://github.com/aklofas/kicad-happy.git`
- Branch: `main`
- Commit: `2a7dc4147a8edbbe3694498ff1ba9f06e37244cb`
- Purpose: AI-assisted KiCad design review using skill guidance and deterministic Python analyzers for schematics, PCB layout, cross-domain checks, EMC, thermal review, Gerber review, and fabrication release gating.
- Install method used: dedicated Python 3.12 venv created with the Windows Python launcher. No pip dependencies were installed because core analyzers are documented as Python stdlib-only.
- Runtime requirements: Python 3.10+ for core analyzers. KiCad install is not required for saved-file analysis. Optional KiDoc rendering, SPICE, distributor, and datasheet workflows have additional requirements and were not installed or configured.
- Safe tests run: analyzer `--help` checks for schematic, PCB, Gerber, cross-analysis, thermal, EMC, and fab release gate scripts; one `analyze_schematic.py --schema` smoke test.
- Exact analysis runner pattern: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-happy\Scripts\python.exe C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-happy\skills\kicad\scripts\analyze_schematic.py <copied-or-approved-project-file.kicad_sch> --output <05_OUTPUTS\kicad-happy\PROJECT_TIMESTAMP\schematic.json>`.
- Usage guide: `03_TOOLS\tool_logs\KICAD_HAPPY_USAGE_GUIDE.md`.
- Command log: `02_HISTORY\command_logs\KICAD_HAPPY_INSTALL_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KICAD_HAPPY_INSTALL_SESSION.md`.
- Initial authority: read-only, analysis-only.
- Notes: Do not run against production/current projects until explicitly approved. Do not globally install Codex skills, configure GitHub Actions, run optional KiDoc dependency installs, or use distributor/API-key flows unless requested.

### KiCAD-MCP-Server
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\repos\KiCAD-MCP-Server`
- Source URL: `https://github.com/mixelpixx/KiCAD-MCP-Server.git`
- Branch: `main`
- Commit: `d3c01e20bd3af96eaaebcdb84baa7ec9908b31e4`
- Purpose: MCP server for KiCad integration experiments.
- Install method: staged manual install after approval; do not run `setup-windows.ps1` until approved.
- Runtime requirements: KiCad 9.0+ with Python/`pcbnew`; Node.js 18+; Python >=3.9/3.10+ depending on path; npm dependencies and Python requirements.
- Safe first test: KiCad bundled Python `pcbnew` import check, then `npm run build` after dependency install.
- Initial authority: analysis-only/read-only; write-capable only after disposable-project validation.
- Notes: Dependencies are not installed. MCP is not configured.

### KiBot
- Status: INSTALLED_OUTPUT_AUTOMATION_NOT_PROJECT_TESTED
- Location: `03_TOOLS\repos\KiBot`
- Environment: `03_TOOLS\python_envs\kibot`
- CLI: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe`
- Source URL: `https://github.com/INTI-CMNB/KiBot.git`
- Branch: `master`
- Commit: `367a2e04122aa46413a30e61cb213bfe7223c8c8`
- Purpose: Deterministic KiCad ERC/DRC, fabrication export, documentation, BOM, and release-output automation.
- Installed version: 1.8.5.
- Install method used: KiCad 9.0 bundled Python 3.11 created the dedicated venv at `03_TOOLS\python_envs\kibot`; KiBot and Python dependencies were installed into that venv.
- Runtime requirements: KiCad 9.0.7 is available at `C:\Program Files\KiCad\9.0\bin`; KiBot commands must run with KiCad `bin` on `PATH` and KiCad `site-packages`/`bin` on `PYTHONPATH` so `pcbnew` is available.
- Installed Python packages: `kibot`, `kiauto`, `pyyaml`, `xlsxwriter`, `colorama`, `requests`, `qrcodegen`, `markdown2`, `lark`, `psutil`, `xvfbwrapper`, and `lxml`.
- Safe tests run: Python import of KiBot and KiCad `pcbnew`, `kibot --version`, `kibot --help`, `kibot --help-list-outputs`, `kibot --help-preflights`, and template output listing.
- Exact command pattern:
  `powershell -NoProfile -Command "$env:PATH='C:\Program Files\KiCad\9.0\bin;' + $env:PATH; $env:PYTHONPATH='C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'; & 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe' -c '<project.kibot.yaml>' -b '<board.kicad_pcb>' -e '<schematic.kicad_sch>' -d '<output_dir>' -A"`
- Starter config template: `04_KICAD_PROJECTS\templates\kibot_default.kibot.yaml`.
- Command log: `02_HISTORY\command_logs\KIBOT_INSTALL_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KIBOT_INSTALL_SESSION.md`.
- Initial authority: output-only automation into approved output folders.
- Notes: Windows support is documented as experimental by KiBot. Do not run on real projects until an active project is selected, backups are confirmed, and outputs are directed to `05_OUTPUTS` or project `reports`/`fabrication` folders. Do not treat generated outputs as final until full workspace fabrication checks pass.

### InteractiveHtmlBom
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\repos\InteractiveHtmlBom`
- Source URL: `https://github.com/openscopeproject/InteractiveHtmlBom.git`
- Branch: `master`
- Commit: `8c13013fc5233cfa31698a777813e87502bdb625`
- Purpose: Interactive HTML BOM generation.
- Install method: Python venv or KiCad plugin path after approval.
- Runtime requirements: Python >=3.8; `wxpython>=4.0`; `jsonschema>=4.1`; KiCad/Pcbnew context for real board extraction.
- Safe first test: `generate_interactive_bom --help`.
- Initial authority: read-only analysis with generated output only.
- Notes: Dependencies are not installed.

### PcbDraw
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\repos\PcbDraw`
- Source URL: `https://github.com/yaqwsx/PcbDraw.git`
- Branch: `master`
- Commit: `9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f`
- Purpose: PCB rendering for documentation and visual review.
- Install method: Python venv or KiCad Command Prompt install after approval.
- Runtime requirements: Python >=3.9; KiCad 9+; Inkscape 1.x or librsvg; Python packages from `setup.py`.
- Safe first test: `pcbdraw --help`.
- Initial authority: read-only rendering with output only.
- Notes: Dependencies are not installed.

### KiCanvas
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\repos\kicanvas`
- Source URL: `https://github.com/theacodes/kicanvas.git`
- Branch: `main`
- Commit: `b031159eb74aaa7eef2b026fd85d35bc05ff2095`
- Purpose: Browser-based KiCad visualization.
- Install method: npm project install/build after approval, or use bundled viewer artifact if provided.
- Runtime requirements: Node/npm for local build; docs require Python packages only for documentation build. KiCad 6+ file formats; KiCad 5 unsupported.
- Safe first test: `npm run lint:types` after dependency install.
- Initial authority: read-only visualization.
- Notes: Dependencies are not installed.


```

## Read startup file: 00_CODEX_START\MEMORY_INDEX.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\MEMORY_INDEX.md" -Raw
```
Exit code: 0
Output:
```text
# Memory Index

Memory files store durable preferences, constraints, and design decisions. They are not command logs.

## Required Memory Files
- `01_MEMORY\GLOBAL_MEMORY.md`
- `01_MEMORY\DESIGN_RULES_MEMORY.md`
- `01_MEMORY\COMPONENT_PREFERENCES.md`
- `01_MEMORY\FAB_HOUSE_PREFERENCES.md`
- `01_MEMORY\projects\PROJECT_NAME\PROJECT_MEMORY.md`

## Use Rules
- Read relevant memory before touching KiCad files.
- Store durable decisions in memory.
- Do not store command transcripts in memory.
- Do not store passwords, API keys, license keys, private tokens, or credentials in memory.

## Scope
- `GLOBAL_MEMORY.md`: workspace-wide durable context.
- `DESIGN_RULES_MEMORY.md`: electrical, PCB, fabrication, and review rules that apply across projects.
- `COMPONENT_PREFERENCES.md`: preferred parts, alternates, sourcing constraints, and avoided components.
- `FAB_HOUSE_PREFERENCES.md`: manufacturer capabilities, process preferences, and release requirements.
- `projects\PROJECT_NAME\PROJECT_MEMORY.md`: durable project-specific decisions and constraints.


```

## Read startup file: 00_CODEX_START\HISTORY_INDEX.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\HISTORY_INDEX.md" -Raw
```
Exit code: 0
Output:
```text
# History Index

History files store session records, command results, reviews, and generated reports. They are not durable design memory.

## Required History Areas
- `sessions`
- `command_logs`
- `design_reviews`
- `erc_drc_reports`
- `fabrication_reviews`
- `project_history`

## Folder Map
- `02_HISTORY\sessions\`: session summaries and meaningful work records.
- `02_HISTORY\command_logs\`: commands run, important outputs, failures, and environment observations.
- `02_HISTORY\design_reviews\`: schematic, PCB, component, and architecture review notes.
- `02_HISTORY\erc_drc_reports\`: ERC and DRC outputs or explanations when checks could not run.
- `02_HISTORY\fabrication_reviews\`: release readiness, Gerber, drill, BOM, placement, and fab package review notes.
- `02_HISTORY\project_history\PROJECT_NAME\`: project-specific history and milestone notes.

## Use Rules
- After meaningful work, write a session log.
- Record commands and results in history, not memory.
- Record ERC/DRC results or reasons they could not run.
- Do not store passwords, API keys, license keys, private tokens, or credentials in history.


```

## Read startup file: 00_CODEX_START\PROJECT_INDEX.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\PROJECT_INDEX.md" -Raw
```
Exit code: 0
Output:
```text
# Project Index

KiCad projects belong in:

`04_KICAD_PROJECTS\active`

## Current State
- No active project is selected unless `CURRENT_PROJECT.md` says otherwise.
- Do not edit KiCad project files when the active project is `NONE`.

## Project Record Fields
For each active project, record:
- Project name.
- Project path.
- Status.
- Board purpose.
- KiCad version.
- Important electrical constraints.
- Important mechanical constraints.
- Fabrication constraints.
- Related project memory file.
- Latest review or verification report.

## Project Work Rule
Before touching project files, confirm the target path is inside the active project path listed in `CURRENT_PROJECT.md`.


```

## Read startup file: 00_CODEX_START\CURRENT_PROJECT.md

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\CURRENT_PROJECT.md" -Raw
```
Exit code: 0
Output:
```text
Active project name: NONE
Active project path: NONE
Current task mode: NONE
Current priority: NONE

# Current Project

This file controls whether Codex may inspect or edit KiCad project files.

## Rules
- If active project name is `NONE`, do not edit KiCad project files.
- If active project path is `NONE`, do not edit KiCad project files.
- Before protected edits, confirm backups in `99_BACKUPS/pre_codex_edits/`.
- Before design changes, state the files likely to change, verification plan, and rollback plan.

## Update Fields When Selecting A Project
- Active project name.
- Active project path.
- Current task mode.
- Current priority.
- Allowed edit boundaries.
- Required verification.
- Relevant memory files.
- Relevant history files.


```

## Read visual-tool relevant memory and install plan context

Command:
```powershell
Get-Content memory files and Select-String install plan for InteractiveHtmlBom, PcbDraw, KiCanvas
```
Exit code: 0
Output:
```text
# Global Memory

Durable workspace-wide rules for AI-assisted KiCad engineering.

## Workspace Purpose
- This workspace is for AI-assisted KiCad design, review, verification, and fabrication prep.
- Codex should operate from `KICAD_ENGINE` unless working inside a specific project.
- Preserve clean separation between tools, projects, memory, history, outputs, datasheets, and backups.

## Trust And Verification
- Never trust AI-only review for fabrication.
- Always verify with KiCad ERC/DRC and visual review.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Treat missing or blocked verification as a release blocker, not a minor note.

## Workspace Separation
- Tools and tool repositories belong in `03_TOOLS/`.
- Active projects belong in `04_KICAD_PROJECTS/active/`.
- Durable decisions belong in `01_MEMORY/`.
- Session notes, command logs, reviews, and reports belong in `02_HISTORY/`.
- Generated outputs belong in `05_OUTPUTS/` or approved project output folders.
- Datasheets belong in `06_DATASHEETS/` or approved project datasheet folders.
- Backups before edits belong in `99_BACKUPS/pre_codex_edits/`.

## Current Durable State
- Workspace bootstrapped.
- No active project selected unless `00_CODEX_START/CURRENT_PROJECT.md` says otherwise.
- No external repositories installed by bootstrap.
- No MCP tools configured by bootstrap.
- Do not install tools, clone repositories, or configure MCP unless explicitly requested.

# Coding And Scripting Rules

Durable rules for scripts and automation used in this KiCad workspace.

## Safety
- Scripts must be safe to run repeatedly.
- Scripts must not delete source project files.
- Scripts must fail safely if KiCad CLI is missing.
- Scripts must not hardcode secrets.
- Do not store passwords, API keys, license keys, private tokens, or credentials in scripts, memory, history, or generated reports.

## File Placement
- General scripts belong in `03_TOOLS/scripts/`.
- Project-specific scripts belong inside the relevant project only when the project intentionally owns them.
- Generated files go to outputs, reports, or fabrication folders.
- Do not write generated files over source `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing packages unless explicitly requested and backed up.

## PowerShell Rules
- PowerShell scripts must use quoted paths.
- Prefer `-LiteralPath` for filesystem operations.
- Avoid path assumptions; resolve workspace-relative paths before acting.

## Logging
- Log commands and results.
- Command logs belong in `02_HISTORY/command_logs/`.
- Verification outputs belong in `02_HISTORY/erc_drc_reports/` or project-specific history.
- Session summaries belong in `02_HISTORY/sessions/`.

## KiCad CLI Behavior
- Check for `kicad-cli` before running ERC, DRC, export, or render commands.
- If `kicad-cli` is missing, report the missing dependency and stop without pretending checks passed.
- Record failed or blocked checks in history when they affect release readiness.

## Repeatability
- Prefer deterministic command arguments and explicit output paths.
- Prefer dated or versioned output directories for generated release artifacts.
- Do not silently overwrite previous verification or fabrication outputs.


> 03_TOOLS\tool_logs\INSTALL_PLAN.md:1:# KiCad Tool Install Plan
  03_TOOLS\tool_logs\INSTALL_PLAN.md:2:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:3:Date: 2026-04-30
  03_TOOLS\tool_logs\INSTALL_PLAN.md:4:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:5:## Scope
  03_TOOLS\tool_logs\INSTALL_PLAN.md:6:This plan covers the cloned repositories in `03_TOOLS\repos`. It is an 
installation plan only.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:10:## Local Prerequisite Snapshot
  03_TOOLS\tool_logs\INSTALL_PLAN.md:11:- Git: available, `git version 2.52.0.windows.1`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:12:- Python launcher: available, `py` reports `Python 3.12.10`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:13:- `python`: missing from PATH
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:14:- Node.js: available, `v22.15.0`
  03_TOOLS\tool_logs\INSTALL_PLAN.md:15:- npm: available, `10.9.2`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:16:- KiCad / `kicad`: missing from PATH
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:17:- `kicad-cli`: missing from PATH
  03_TOOLS\tool_logs\INSTALL_PLAN.md:18:- Docker: missing from PATH
  03_TOOLS\tool_logs\INSTALL_PLAN.md:19:- `uv` / `uvx`: missing from PATH
  03_TOOLS\tool_logs\INSTALL_PLAN.md:20:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:21:## Global Blockers
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:22:- KiCad and `kicad-cli` are not available on PATH. This blocks real 
ERC/DRC/export checks and blocks tools that need KiCad Python or `pcbnew`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:23:- `uv` / `uvx` are missing. This blocks the documented quick path for 
`kicad-mcp-pro`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:24:- `python` is missing, but `py -3.12` is available. Windows commands should 
prefer `py -3.12` unless a tool specifically needs KiCad's bundled Python.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:25:- Docker is missing. This blocks Docker-based KiBot evaluation and 
Freerouting/Docker optional flows.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:26:- No MCP server should be connected to Codex or granted write/manufacturing 
authority until tested on non-critical sample files.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:27:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:28:## Recommended Install Order
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:29:1. Baseline prerequisites: identify/install KiCad with `kicad-cli`, confirm 
KiCad Python/`pcbnew`, and decide whether `python` should be added to PATH.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:30:2. `kicad-happy`: lowest risk, read-only deterministic analysis scripts, no 
required dependencies beyond Python 3.10+.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:31:3. `kicanvas`: browser-based viewer, Node/npm dependency only, read-only 
visualization.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:32:4. `InteractiveHtmlBom`: Python tool/plugin for BOM generation; needs Python 
venv and likely KiCad/Pcbnew context for real projects.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:33:5. `PcbDraw`: Python CLI rendering tool; requires KiCad 9+, Inkscape 1.x or 
librsvg, and likely `kicad-cli` for rendering workflows.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:34:6. `KiBot`: broad fabrication/export automation; install only after KiCad CLI 
works and output-folder rules are settled.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:35:7. `kicad-mcp-pro`: MCP server; evaluate in analysis-only profile first after 
`uvx` or venv install is available.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:36:8. `KiCAD-MCP-Server`: broad MCP server with write/export capabilities; 
evaluate last, on a disposable sample project only.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:37:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:38:## Repository Plans
  03_TOOLS\tool_logs\INSTALL_PLAN.md:39:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:40:### kicad-happy
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:41:- Repo name: `kicad-happy`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:42:- Repo path: `03_TOOLS\repos\kicad-happy`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:43:- Purpose: AI-assisted KiCad design review skills and deterministic Python 
analyzers for schematics, PCBs, Gerbers, datasheets, BOM, EMC, SPICE, and documentation support.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:44:- Inspected files: `README.md`, `install-guidance.md`, `how-it-works.md`, 
`VALIDATION.md`, `github-action.md`, skill scripts.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:45:- Install method: Prefer Codex skill installation only after approval. Before 
skill installation, evaluate standalone scripts from the local clone against a disposable or copied test project.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:46:- Dependencies: Python 3.10+; core analysis scripts are documented as 
stdlib-only. Optional flows can need ngspice, poppler-utils, distributor credentials, or a project-local KiDoc venv 
for PDF/DOCX/ODT output.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:47:- Python venv needed: No for core read-only analyzers; yes for optional 
KiDoc/report-generation dependencies.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:48:- Node/npm needed: No for local Python analyzers.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:49:- KiCad CLI needed: No for core parsing; it reads saved `.kicad_sch` / 
`.kicad_pcb` files directly.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:50:- MCP used: No.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:51:- Risks: Skills may encourage broad AI review; AI review is not fabrication 
authority. Some BOM/datasheet scripts can write when explicit `--write` flags are used. Windows symlink installs may 
require PowerShell 7 plus Developer Mode or admin rights.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:52:- Safe test command: `py -3.12 
"03_TOOLS\repos\kicad-happy\skills\kicad\scripts\analyze_schematic.py" "<copied-test-project>\board.kicad_sch" 
--output "05_OUTPUTS\tool_tests\kicad-happy\schematic.json"`
  03_TOOLS\tool_logs\INSTALL_PLAN.md:53:- Initial capability: read-only, analysis-only.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:54:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:55:### kicanvas
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:56:- Repo name: `kicanvas`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:57:- Repo path: `03_TOOLS\repos\kicanvas`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:58:- Purpose: Browser-based viewer for KiCad schematics and boards.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:59:- Inspected files: `README.md`, `package.json`, `docs\requirements.txt`, 
`docs\docs\development.md`, `docs\docs\embedding.md`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:60:- Install method: Node/npm project evaluation after approval, likely `npm ci` 
followed by local build/serve commands. For embedding use, the docs describe copying a bundled `kicanvas.js`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:61:- Dependencies: Node/npm development dependencies from `package.json`; docs 
use Python packages `mkdocs`, `pymdown-extensions`, and `mkdocs-material`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:62:- Python venv needed: Only for documentation build, not for viewer runtime 
evaluation.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:63:- Node/npm needed: Yes.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:64:- KiCad CLI needed: No.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:65:- MCP used: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:66:- Risks: Cannot parse KiCad 5 files per README; KiCad 6+ only. Running `npm 
ci` creates `node_modules` in the repo unless a separate worktree/install strategy is chosen. `npm run build` writes 
build outputs.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:67:- Safe test command: after approved npm install, run `npm run lint:types` from 
`03_TOOLS\repos\kicanvas`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:68:- Initial capability: read-only visualization.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:69:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:70:### InteractiveHtmlBom
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:71:- Repo name: `InteractiveHtmlBom`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:72:- Repo path: `03_TOOLS\repos\InteractiveHtmlBom`
  03_TOOLS\tool_logs\INSTALL_PLAN.md:73:- Purpose: Generate interactive HTML BOM output for electronics projects.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:74:- Inspected files: `README.md`, `pyproject.toml`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:75:- Install method: Python venv or KiCad plugin-oriented install after approval; 
README points to the project wiki for full install instructions.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:76:- Dependencies: Python >=3.8, `wxpython>=4.0`, `jsonschema>=4.1`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:77:- Python venv needed: Yes, unless installed into KiCad's Python/plugin 
environment.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:78:- Node/npm needed: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:79:- KiCad CLI needed: No for the package entry point itself, but real KiCad PCB 
data access depends on KiCad/Pcbnew context.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:80:- MCP used: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:81:- Risks: `wxpython` installation on Windows can be sensitive to Python version 
and wheels. Plugin use may require KiCad user plugin paths. Generated BOM must be treated as not final until full 
fabrication review is complete.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:82:- Safe test command: after approved install, run `generate_interactive_bom 
--help`.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:83:- Initial capability: read-only analysis with output generation only into 
`05_OUTPUTS` or project `bom`/`reports` folders.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:84:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:85:### PcbDraw
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:86:- Repo name: `PcbDraw`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:87:- Repo path: `03_TOOLS\repos\PcbDraw`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:88:- Purpose: Generate 2D board renderings and visual documentation from KiCad 
board files.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:89:- Inspected files: `README.md`, `doc\installation.md`, `doc\pcbdraw.md`, 
`setup.py`, `setup.cfg`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:90:- Install method: Python venv or KiCad Command Prompt install after approval. 
On Windows, docs say to use the KiCad Command Prompt, not an ordinary command prompt.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:91:- Dependencies: Python >=3.9; Python packages include `numpy`, `lxml`, 
`mistune>=3.0`, `pybars3`, `pyyaml`, `svgpathtools==1.4.1`, `Pillow>=9.0`, `click>=7.1`; requires Inkscape 1.x or 
librsvg.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:92:- Python venv needed: Yes, but it must be able to access KiCad's Python/board 
libraries where required.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:93:- Node/npm needed: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:94:- KiCad CLI needed: Yes for rendering workflows that call `kicad-cli pcb 
render`; docs require KiCad 9 or newer.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:95:- MCP used: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:96:- Risks: Windows needs KiCad Command Prompt; ordinary PowerShell may not 
expose KiCad Python paths. Inkscape 0.9x is explicitly unsupported. Rendering can be blocked until KiCad 9+ and 
Inkscape/librsvg are installed.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:97:- Safe test command: after approved install, run `pcbdraw --help`; after KiCad 
9+ is available, render only a copied/sample `.kicad_pcb` into `05_OUTPUTS\tool_tests\PcbDraw`.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:98:- Initial capability: read-only rendering, output-only.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:99:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:100:### KiBot
  03_TOOLS\tool_logs\INSTALL_PLAN.md:101:- Repo name: `KiBot`
  03_TOOLS\tool_logs\INSTALL_PLAN.md:102:- Repo path: `03_TOOLS\repos\KiBot`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:103:- Purpose: Scriptable KiCad fabrication/documentation generation, ERC/DRC, 
output automation, and CI workflows.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:104:- Inspected files: `README.md`, `setup.py`, `setup.cfg`, `kibot\__init__.py`, 
`docs\source\installation.rst`, `docs\source\dependencies.rst`, `docs\source\configuration\quick_start.rst`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:105:- Install method: Prefer Docker image for full dependency coverage when 
Docker is available, or Python venv install after KiCad is installed and `pcbnew` accessibility is understood. On 
Windows, docs recommend WSL2/Linux-like environment for non-Docker local use.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:106:- Dependencies: Python package requires Python >=3.8 and `kiauto`, `pyyaml`, 
`xlsxwriter`, `colorama`, `requests`, `qrcodegen`, `markdown2`, `lark`; many optional external tools exist for 
specific outputs.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:107:- Python venv needed: Yes for local install; venv may need 
`--system-site-packages` or explicit KiCad Python paths to access `pcbnew`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:108:- Node/npm needed: No.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:109:- KiCad CLI needed: Yes for meaningful KiCad automation, ERC/DRC, and exports.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:110:- MCP used: No.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:111:- Risks: Broad output generation can overwrite release artifacts if paths are 
not constrained. Some features can auto-download dependencies. Docker is currently missing. Windows local use is 
higher friction than Linux/WSL2. KiBot should only write into `05_OUTPUTS` or project fabrication/report folders.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:112:- Safe test command: after approved install, run `kibot --version` and `kibot 
--help`; later run `kibot --quick-start` only in a disposable copy of a project.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:113:- Initial capability: output-only automation; no source project edits.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:114:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:115:### kicad-mcp-pro
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:116:- Repo name: `kicad-mcp-pro`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:117:- Repo path: `03_TOOLS\repos\kicad-mcp-pro`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:118:- Purpose: Model Context Protocol server for KiCad schematic, PCB, 
validation, DFM, simulation, and release workflows.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:119:- Inspected files: `README.md`, `docs\installation.md`, 
`docs\client-configuration.md`, `docs\development.md`, `pyproject.toml`, `package.json`, `mcp.json`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:120:- Install method: Prefer `uvx kicad-mcp-pro` for isolated runtime after 
`uv`/`uvx` is installed, or install into a dedicated Python venv. Do not configure MCP until standalone health/doctor 
checks pass.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:121:- Dependencies: Python >=3.12; core dependencies include `authlib`, `anyio`, 
`kicad-sch-api`, `kicad-python`, `mcp[cli]`, `pydantic`, `pydantic-settings`, `rich`, `structlog`, `typer`; optional 
extras include HTTP, components, freerouting/Docker, simulation, and VCS. Dev scripts specify Node >=24.11.0 and npm 
>=11.6.1.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:122:- Python venv needed: Yes if not using `uvx`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:123:- Node/npm needed: No for runtime; yes for repo dev hooks/checks. Current 
Node 22/npm 10 do not meet repo dev engine constraints.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:124:- KiCad CLI needed: Yes for deeper `doctor`/CLI diagnostics and real KiCad 
workflows; `health --json` is documented as safe without KiCad running.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:125:- MCP used: Yes.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:126:- Risks: MCP exposes write/manufacturing-capable workflows depending on 
profile. Must start with `KICAD_MCP_PROFILE=analysis` or the narrowest available profile and a disposable project. Do 
not use manufacturing/export profiles until ERC/DRC and backup rules are proven.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:127:- Safe test command: after approved `uvx` or venv setup, run `kicad-mcp-pro 
health --json`, then `kicad-mcp-pro doctor --json`.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:128:- Initial capability: analysis-only; no write or manufacturing authority.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:129:
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:130:### KiCAD-MCP-Server
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:131:- Repo name: `KiCAD-MCP-Server`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:132:- Repo path: `03_TOOLS\repos\KiCAD-MCP-Server`
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:133:- Purpose: MCP server for AI-assisted KiCad project, schematic, PCB, library, 
export, and routing workflows.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:134:- Inspected files: `README.md`, `setup-windows.ps1`, 
`docs\WINDOWS_TROUBLESHOOTING.md`, `scripts\install-linux.sh`, `requirements.txt`, `requirements-dev.txt`, 
`pyproject.toml`, `package.json`.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:135:- Install method: Manual staged install only after prerequisites are 
confirmed. Do not run `setup-windows.ps1` until explicitly approved because it installs dependencies, builds the 
project, and generates MCP configuration.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:136:- Dependencies: KiCad 9.0+ with Python/`pcbnew`; Node.js 18+; Python >=3.9 by 
`pyproject.toml`, while Windows troubleshooting says to use KiCad 9's bundled Python 3.11 / Python 3.10+; Python 
packages include `kicad-skip`, `Pillow`, `cairosvg`, `colorlog`, `pydantic`, `requests`, `python-dotenv`; Node 
dependencies include `@modelcontextprotocol/sdk`, `dotenv`, `express`, `zod`, TypeScript tooling.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:137:- Python venv needed: Yes or KiCad bundled Python; must preserve access to 
`pcbnew` via KiCad Python or `PYTHONPATH`.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:138:- Node/npm needed: Yes. Current Node 22/npm 10 satisfy the documented Node 
18+ requirement.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:139:- KiCad CLI needed: Yes for real use; KiCad 9+ and `pcbnew` are central 
requirements.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:140:- MCP used: Yes.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:141:- Risks: Very broad tool surface includes project creation, schematic/PCB 
edits, exports, Freerouting, and JLCPCB-related flows. Setup scripts install dependencies and write configuration. 
Windows path escaping and `PYTHONPATH` are common failure points. Must not connect to active projects until tested on 
a disposable sample project.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:142:- Safe test command: after approved dependency install and build, run KiCad 
Python import check with KiCad's bundled Python, then `npm run build`; only then start the server against a disposable 
project.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:143:- Initial capability: analysis-only/read-only. Write-capable only after 
explicit approval and sample-project validation.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:144:
  03_TOOLS\tool_logs\INSTALL_PLAN.md:145:## Deferred Items
  03_TOOLS\tool_logs\INSTALL_PLAN.md:146:- No install commands should run until the user approves a specific tool.
> 03_TOOLS\tool_logs\INSTALL_PLAN.md:147:- Before any MCP configuration, create a disposable test KiCad project and 
define allowed read/write boundaries.
  03_TOOLS\tool_logs\INSTALL_PLAN.md:148:- Before any fabrication/export tool is used on a real project, enforce the 
workspace backup and verification rules from `AGENTS.md`.



```

## Confirm current project remains NONE

Command:
```powershell
Get-Content -LiteralPath "00_CODEX_START\CURRENT_PROJECT.md" -Raw
```
Exit code: 0
Output:
```text
Active project name: NONE
Active project path: NONE
Current task mode: NONE
Current priority: NONE

# Current Project

This file controls whether Codex may inspect or edit KiCad project files.

## Rules
- If active project name is `NONE`, do not edit KiCad project files.
- If active project path is `NONE`, do not edit KiCad project files.
- Before protected edits, confirm backups in `99_BACKUPS/pre_codex_edits/`.
- Before design changes, state the files likely to change, verification plan, and rollback plan.

## Update Fields When Selecting A Project
- Active project name.
- Active project path.
- Current task mode.
- Current priority.
- Allowed edit boundaries.
- Required verification.
- Relevant memory files.
- Relevant history files.


```

## InteractiveHtmlBom: repo status

Command:
```powershell
git -C "03_TOOLS\repos\InteractiveHtmlBom" status --short --branch; git rev-parse; git log -1
```
Exit code: 0
Output:
```text
## master...origin/master
master
8c13013fc5233cfa31698a777813e87502bdb625
Fix dnp detection for kicad variants

```

## InteractiveHtmlBom: list root files and manifests

Command:
```powershell
Get-ChildItem root; rg --files manifest/doc files
```
Exit code: 0
Output:
```text
d--h-- 1 .git
d----- 1 .github
d----- 1 icons
d----- 1 InteractiveHtmlBom
d----- 1 tests
-a---- 109 .gitignore
-a---- 787 .jsbeautifyrc
-a---- 9955 DATAFORMAT.md
-a---- 1083 LICENSE
-a---- 6061 make_release.py
-a---- 2177 pyproject.toml
-a---- 2184 README.md
-a---- 234429 settings_dialog.fbp
-a---- 40 __init__.py
--- manifests/docs ---
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\LICENSE
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\README.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\DATAFORMAT.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\tests\test_module.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\stats-36px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\plugin_icon_big.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\plugin.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\io-36px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\copy-48px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\btn-question.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\btn-plus.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\btn-minus.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\btn-arrow-up.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\btn-arrow-down.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-ungrouped-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-top-bot-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-only-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-netlist-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-left-right-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\bom-grouped-32px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\baseline-settings-20px.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\errors.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\util.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\table-util.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\split.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\render.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\pep.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\lz-string.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\ibom.js
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\ibom.html
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\ibom.css
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\Run.bat
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\icon.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\genericjson.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\fusion_eagle.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\easyeda.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\common.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog_test.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\compat.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\i18n\language_zh.bat
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\i18n\language_en.bat
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\xmlparser.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\sexpressions.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\parser_base.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\netlistparser.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\schema\genericjsonpcbdata_v1.schema
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\fontparser.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\config.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\ibom.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\lzstring.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\units.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\newstroke_font.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\dialog_base.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\__init__.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\settings_dialog.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\bitmaps\btn-question.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\bitmaps\btn-plus.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\bitmaps\btn-minus.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\bitmaps\btn-arrow-up.png
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\bitmaps\btn-arrow-down.png

```

## InteractiveHtmlBom: read README and pyproject

Command:
```powershell
Get-Content README.md and pyproject.toml
```
Exit code: 0
Output:
```text
--- README.md ---
# Interactive HTML BOM plugin for KiCad
## Supports EasyEDA, Eagle, Fusion360 and Allegro PCB designer

![icon](https://i.imgur.com/js4kDOn.png)

This plugin generates a convenient Bill of Materials (BOM) listing with the
ability to visually correlate and easily search for components and their placements
on the PCB. It is particularly useful when hand-soldering a prototype, as it allows
users to quickly find locations of components groups on the board. It is also possible
to reverse lookup the component group by clicking on a footprint on the board drawing.

The plugin utilizes Pcbnew python API to read PCB data and render silkscreen, fab layer,
footprint pads, text, and drawings. BOM table fields and grouping is fully configurable,
additional columns, such as a manufacturer ID, can be added in Schematic editor and
imported either through the netlist file, XML file generated by Eeschema's internal
BOM tool, or from board file itself.

There is an option to include tracks/zones data as well as netlist information allowing
dynamic highlight of nets on the board.

For full description of functionality see [wiki](https://github.com/openscopeproject/InteractiveHtmlBom/wiki).

Generated html page is fully self contained, doesn't need internet connection to work
and can be packaged with documentation of your project or hosted anywhere on the web.

[A demo is worth a thousand words.](https://openscopeproject.org/InteractiveHtmlBomDemo/)

## Installation and Usage

See [project wiki](https://github.com/openscopeproject/InteractiveHtmlBom/wiki/Installation) for instructions.

## License and credits

Plugin code is licensed under MIT license, see `LICENSE` for more info.

Html page uses [Split.js](https://github.com/nathancahill/Split.js),
[PEP.js](https://github.com/jquery/PEP) and (stripped down)
[lz-string.js](https://github.com/pieroxy/lz-string) libraries that get embedded into
generated bom page.

`units.py` is borrowed from [KiBom](https://github.com/SchrodingersGat/KiBoM)
plugin (MIT license).

`svgpath.py` is heavily based on
[svgpathtools](https://github.com/mathandy/svgpathtools) module (MIT license).

--- pyproject.toml ---
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "InteractiveHtmlBom"
dynamic = ["version"]
description = 'Generate Interactive Html BOM for your electronics projects'
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
keywords = ["ibom", "KiCad", "Eagle", "EasyEDA"]
authors = [{ name = "qu1ck", email = "anlutsenko@gmail.com" }]
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
  "Topic :: Utilities",
]
dependencies = [
  "wxpython>=4.0",
  "jsonschema>=4.1",
]

[project.scripts]
generate_interactive_bom = "InteractiveHtmlBom.generate_interactive_bom:main"

[project.urls]
Documentation = "https://github.com/openscopeproject/InteractiveHtmlBom/wiki"
Issues = "https://github.com/openscopeproject/InteractiveHtmlBom/issues"
Source = "https://github.com/openscopeproject/InteractiveHtmlBom"

[tool.hatch.version]
path = "InteractiveHtmlBom/version.py"
pattern = "LAST_TAG = 'v(?P<version>[^']+)'"

[tool.hatch.envs.default]
system-packages = true
dependencies = [
  "coverage[toml]>=6.5",
  "pytest",
  "pytest-sugar"
]
[tool.hatch.envs.default.scripts]
test = "pytest {args:tests}"
test-cov = "coverage run -m pytest {args:tests}"
cov-report = ["- coverage combine", "coverage report"]
cov = ["test-cov", "cov-report"]

[[tool.hatch.envs.all.matrix]]
python = ["3.8", "3.9", "3.10", "3.11", "3.12"]

[tool.hatch.envs.types]
dependencies = ["mypy>=1.0.0"]
[tool.hatch.envs.types.scripts]
check = "mypy --install-types --non-interactive {args:InteractiveHtmlBom}"

[tool.coverage.run]
source_pkgs = ["InteractiveHtmlBom", "tests"]
branch = true
parallel = true
omit = ["src/InteractiveHtmlBom/__about__.py"]

[tool.coverage.paths]
InteractiveHtmlBom = [
  "InteractiveHtmlBom",
]
tests = ["tests", "*/InteractiveHtmlBom/tests"]

[tool.coverage.report]
exclude_lines = ["no cov", "if __name__ == .__main__.:", "if TYPE_CHECKING:"]

--- LICENSE ---
MIT License

Copyright (c) 2018 qu1ck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


```

## InteractiveHtmlBom: extract install/dependency/CLI notes

Command:
```powershell
rg -n "install|pip|python|wxPython|wxpython|jsonschema|generate_interactive_bom|KiCad|pcbnew|plugin|command|usage|Windows|CLI|--help" repo
```
Exit code: 0
Output:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:10:requires-python = ">=3.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:12:keywords = ["ibom", "KiCad", "Eagle", "EasyEDA"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:23:  "wxpython>=4.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:24:  "jsonschema>=4.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:28:generate_interactive_bom = "InteractiveHtmlBom.generate_interactive_bom:main"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:53:python = ["3.8", "3.9", "3.10", "3.11", "3.12"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\pyproject.toml:58:check = "mypy --install-types --non-interactive {args:InteractiveHtmlBom}"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\README.md:1:# Interactive HTML BOM plugin for KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\README.md:6:This plugin generates a convenient Bill of Materials (BOM) listing with the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\README.md:12:The plugin utilizes Pcbnew python API to read PCB data and render silkscreen, fab layer,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\README.md:42:plugin (MIT license).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\DATAFORMAT.md:3:This document describes pcbdata json structure that plugin
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:1:#!/usr/bin/env python3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:10:6. Copy `InteractiveHtmlBom` into tmp/plugins,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:17:10.Zip plugin code into InteractiveHtmlBom.zip suitable for manual install.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:115:        # 6. Copy InteractiveHtmlBom into tmp/plugins excluding patterns
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:116:        plugins_dir = tmp_path / "plugins"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:118:            root / "InteractiveHtmlBom", plugins_dir)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:119:        print("Copied InteractiveHtmlBom into tmp/plugins (excluded __pycache__ and .ini files)")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:140:        # 10. Create "normal" zip of just plugin code
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:141:        shutil.move(plugins_dir, tmp_path / "InteractiveHtmlBom")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\make_release.py:154:        print("ERROR: git command failed:\n", e.output, file=sys.stderr)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\settings_dialog.py:44:    # hack for new wxFormBuilder generating code incompatible with old wxPython
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\settings_dialog.py:48:            # wxPython 4
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\settings_dialog.py:51:            # wxPython 3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\dialog\dialog_base.py:555:        self.fieldsGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridCellClicked )
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\lzstring.py:279:            # python dont support bit operation with NaN like javascript
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:1:#!/usr/bin/python3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:9:# Works if this script is executed without installing the module
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:18:# python 2 and 3 compatibility hack
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:32:        print("wxpython is required unless INTERACTIVE_HTML_BOM_NO_DISPLAY "
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:52:            description='KiCad InteractiveHtmlBom plugin CLI.',
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py:56:                        help="KiCad PCB file")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\genericjson.py:4:from jsonschema import validate, ValidationError
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\newstroke_font.py:4: * This program source code file is part of KiCad, a free EDA CAD application.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\newstroke_font.py:7: * Copyright (C) 1992-2010 KiCad Developers, see change_log.txt for contributors.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\newstroke_font.py:28:This file is copied from KiCad source tree and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\newstroke_font.py:29:slightly modified to be valid python by qu1ck.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\__init__.py:2:import pcbnew
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad_extra\__init__.py:13:if hasattr(pcbnew, 'FOOTPRINT'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\config.py:344:                            help='KiCad board variant, empty is default '
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\core\config.py:345:                                 'variant. (Only for KiCad v10+)')
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:369:    command = None
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:374:            # New command.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:375:            command = elements.pop()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:376:            absolute = command in UPPERCASE
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:377:            command = command.upper()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:379:            # If this element starts with numbers, it is an implicit command
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:380:            # and we don't change the command. Check that it's allowed:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:381:            if command is None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:383:                    "Unallowed implicit command in %s, position %s" % (
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:386:        if command == 'M':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:387:            # Moveto command.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:401:            # Implicit moveto commands are treated as lineto commands.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:402:            # So we set command to lineto here, in case there are
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:403:            # further implicit commands after this moveto.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:404:            command = 'L'
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:406:        elif command == 'Z':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:411:            command = None
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:413:        elif command == 'L':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:422:        elif command == 'H':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:430:        elif command == 'V':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:438:        elif command == 'C':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:453:        elif command == 'S':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:468:        elif command == 'Q':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:483:        elif command == 'T':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\svgpath.py:496:        elif command == 'A':
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:4:import pcbnew
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:16:if hasattr(pcbnew, 'Version'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:17:    version = pcbnew.Version().split('.')
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:32:            self.board = pcbnew.LoadBoard(self.file_name)  # type: pcbnew.BOARD
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:38:            # type: list[pcbnew.MODULE]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:41:            # type: list[pcbnew.FOOTPRINT]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:56:        # type: (pcbnew.FOOTPRINT) -> dict
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:126:        # type: (pcbnew.PCB_SHAPE) -> tuple
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:137:        # type: (pcbnew.PCB_SHAPE) -> dict | None
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:139:            pcbnew.S_SEGMENT: "segment",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:140:            pcbnew.S_CIRCLE: "circle",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:141:            pcbnew.S_ARC: "arc",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:142:            pcbnew.S_POLYGON: "polygon",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:143:            pcbnew.S_CURVE: "curve",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:144:            pcbnew.S_RECT: "rect",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:210:                    "Polygons not supported for KiCad 4, skipping")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:247:        # type: (pcbnew.SHAPE_LINE_CHAIN) -> list
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:261:        # type: (pcbnew.SHAPE_POLY_SET) -> list
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:270:        # type: (pcbnew.PCB_TEXT) -> dict
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:290:            # type: pcbnew.SHAPE_COMPOUND
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:295:                if s.Type() == pcbnew.SH_LINE_CHAIN:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:297:                elif s.Type() == pcbnew.SH_SEGMENT:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:352:        # type: (pcbnew.PCB_DIMENSION_BASE) -> dict
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:357:            if s.Type() == pcbnew.SH_SEGMENT:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:361:            elif s.Type() == pcbnew.SH_CIRCLE:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:376:        # type: (pcbnew.BOARD_ITEM) -> list
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:384:              and hasattr(pcbnew, "VECTOR_SHAPEPTR")):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:405:            if d.GetLayer() == pcbnew.Edge_Cuts:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:444:                fields = f.GetFields()  # type: list[pcbnew.PCB_FIELD]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:454:        # type: (pcbnew.PAD) -> bool
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:455:        if hasattr(pcbnew, 'PAD_ATTRIB_PTH'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:456:            through_hole_attributes = [pcbnew.PAD_ATTRIB_PTH,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:457:                                       pcbnew.PAD_ATTRIB_NPTH]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:459:            through_hole_attributes = [pcbnew.PAD_ATTRIB_STANDARD,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:460:                                       pcbnew.PAD_ATTRIB_HOLE_NOT_PLATED]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:464:        # type: (pcbnew.PAD) -> list[dict]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:466:        outer_layers = [(pcbnew.F_Cu, "F"), (pcbnew.B_Cu, "B")]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:468:            padstack = pad.Padstack()  # type: pcbnew.PADSTACK
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:470:            if hasattr(pcbnew, "UNCONNECTED_LAYER_MODE_REMOVE_ALL"):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:471:                ULMRA = pcbnew.UNCONNECTED_LAYER_MODE_REMOVE_ALL
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:496:            pad_layer = layers_set[0] if layers_set else pcbnew.F_Cu
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:502:        # type: (pcbnew.PAD, int) -> dict | None
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:510:            pcbnew.PAD_SHAPE_RECT: "rect",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:511:            pcbnew.PAD_SHAPE_OVAL: "oval",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:512:            pcbnew.PAD_SHAPE_CIRCLE: "circle",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:514:        if hasattr(pcbnew, "PAD_SHAPE_TRAPEZOID"):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:515:            shape_lookup[pcbnew.PAD_SHAPE_TRAPEZOID] = "trapezoid"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:516:        if hasattr(pcbnew, "PAD_SHAPE_ROUNDRECT"):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:517:            shape_lookup[pcbnew.PAD_SHAPE_ROUNDRECT] = "roundrect"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:518:        if hasattr(pcbnew, "PAD_SHAPE_CUSTOM"):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:519:            shape_lookup[pcbnew.PAD_SHAPE_CUSTOM] = "custom"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:520:        if hasattr(pcbnew, "PAD_SHAPE_CHAMFERED_RECT"):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:521:            shape_lookup[pcbnew.PAD_SHAPE_CHAMFERED_RECT] = "chamfrect"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:537:            polygon_set = pcbnew.SHAPE_POLY_SET()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:575:                pcbnew.PAD_DRILL_SHAPE_CIRCLE: "circle",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:576:                pcbnew.PAD_DRILL_SHAPE_OBLONG: "oblong"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:599:            if hasattr(pcbnew, 'MODULE'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:600:                f_copy = pcbnew.MODULE(f)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:602:                f_copy = pcbnew.FOOTPRINT(f)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:607:                    pcbnew.EDA_ANGLE(0, pcbnew.TENTHS_OF_A_DEGREE_T))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:629:                if d.GetLayer() not in [pcbnew.F_Cu, pcbnew.B_Cu]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:633:                        "layer": "F" if d.GetLayer() == pcbnew.F_Cu else "B",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:667:                    pcbnew.F_Cu: "F",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:668:                    pcbnew.B_Cu: "B"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:678:        result = {pcbnew.F_Cu: [], pcbnew.B_Cu: []}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:689:                for layer in [pcbnew.F_Cu, pcbnew.B_Cu]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:693:                if track.GetLayer() in [pcbnew.F_Cu, pcbnew.B_Cu]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:714:            'F': result.get(pcbnew.F_Cu),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:715:            'B': result.get(pcbnew.B_Cu)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:719:        # type: (list[pcbnew.ZONE]) -> dict
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:720:        result = {pcbnew.F_Cu: [], pcbnew.B_Cu: []}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:727:                      if layer in [pcbnew.F_Cu, pcbnew.B_Cu]]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:749:            'F': result.get(pcbnew.F_Cu),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:750:            'B': result.get(pcbnew.B_Cu)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:755:        # type: (pcbnew.NETINFO_LIST) -> list
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:761:        # type: (pcbnew.FOOTPRINT, list) -> Component
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:772:        if hasattr(pcbnew, 'FP_EXCLUDE_FROM_BOM'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:777:            elif footprint.GetAttributes() & pcbnew.FP_EXCLUDE_FROM_BOM:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:779:        elif hasattr(pcbnew, 'MOD_VIRTUAL'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:780:            if footprint.GetAttributes() == pcbnew.MOD_VIRTUAL:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:783:            pcbnew.F_Cu: 'F',
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:784:            pcbnew.B_Cu: 'B',
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:827:                hasattr(pcbnew, "ExpandTextVars")):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:829:            title = pcbnew.ExpandTextVars(title, project)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:830:            revision = pcbnew.ExpandTextVars(revision, project)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:831:            company = pcbnew.ExpandTextVars(company, project)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:832:            file_date = pcbnew.ExpandTextVars(file_date, project)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:862:                    drawings, pcbnew.F_SilkS, pcbnew.B_SilkS),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:864:                    drawings, pcbnew.F_Fab, pcbnew.B_Fab),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:882:                self.logger.info("Zones not supported for KiCad 4, skipping")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:918:class InteractiveHtmlBomPlugin(pcbnew.ActionPlugin, object):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:924:        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\ecad\kicad.py:939:        board = pcbnew.GetBoard()  # type: pcbnew.BOARD
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\__init__.py:1:from .InteractiveHtmlBom import plugin
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp:26:    <property name="python_disconnect_events">0</property>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp:27:    <property name="python_disconnect_mode">source_name</property>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp:28:    <property name="python_image_path_wrapper_function_name"></property>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp:29:    <property name="python_indent_with_spaces">1</property>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\settings_dialog.fbp:30:    <property name="python_skip_events">1</property>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\Run.bat:50:set pyFilePath=%FilePath%generate_interactive_bom.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\Run.bat:59:python %pyFilePath% %pathofEDASourceFile% %option%
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\i18n\language_zh.bat:1:::This file needs to be in 'UTF-8 encoding' AND 'Windows CR LF' to work.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\version.py:10:    plugin_path = os.path.realpath(os.path.dirname(__file__))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\version.py:15:            cwd=plugin_path)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:12:    # https://kicad.mmccoo.com/2017/03/05/adding-your-own-command-buttons-to-the-pcbnew-gui/
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:13:    def find_pcbnew_window():
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:14:        windows = wx.GetTopLevelWindows()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:15:        pcbneww = [w for w in windows if "pcbnew" in w.GetTitle().lower()]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:16:        if len(pcbneww) != 1:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:18:        return pcbneww[0]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:21:        plugin.Run()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:29:    from pcbnew import ID_H_TOOLBAR
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:32:        pcbnew_window = find_pcbnew_window()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:33:        if not pcbnew_window:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:36:        top_tb = pcbnew_window.FindWindowById(ID_H_TOOLBAR)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:46:if (not os.environ.get('INTERACTIVE_HTML_BOM_CLI_MODE', False) and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:47:    not os.path.basename(sys.argv[0]).startswith('generate_interactive_bom')):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:50:    plugin = InteractiveHtmlBomPlugin()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:51:    plugin.register()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:53:    # Add a button the hacky way if plugin button is not supported
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:54:    # in pcbnew, unless this is linux.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\__init__.py:55:    if not plugin.pcbnew_icon_support and not sys.platform.startswith('linux'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\icons\plugin.svg:15:   sodipodi:docname="plugin.svg"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\pep.js:15:this.observer&&v.canTarget(a)&&this.observer.observe(a,C)},enableOnSubtree:function(a){this.watchSubtree(a),a===document&&"complete"!==document.readyState?this.installOnLoad():this.installNewSubtree(a)},installNewSubtree:function(a){w(this.findElements(a),this.addElement,this)},findElements:function(a){return a.querySelectorAll?a.querySelectorAll(B):[]},removeElement:function(a){this.removeCallback(a)},addElement:function(a){this.addCallback(a)},elementChanged:function(a,b){this.changedCallback(a,b)},concatLists:function(a,b){return a.concat(y(b))},
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\pep.js:16:installOnLoad:function(){document.addEventListener("readystatechange",function(){"complete"===document.readyState&&this.installNewSubtree(document)}.bind(this))},isElement:function(a){return a.nodeType===Node.ELEMENT_NODE},flattenMutationTree:function(a){
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\render.js:14:  // This approximates pcbnew behavior with how text tilts depending on horizontal justification
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\render.js:56:  // KiCad ignores last empty line.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom\InteractiveHtmlBom\web\util.js:3:var storagePrefix = 'KiCad_HTML_BOM__' + pcbdata.metadata.title + '__' +

```

## InteractiveHtmlBom create or reuse isolated KiCad Python venv

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -m venv 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom'
```
Exit code: 0
Output:
```text
```

## InteractiveHtmlBom venv Python version

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\python.exe' --version
```
Exit code: 0
Output:
```text
Python 3.11.5

```

## InteractiveHtmlBom install from local repo

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\python.exe' -m pip install --disable-pip-version-check --no-compile --no-cache-dir 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom'
```
Exit code: 0
Output:
```text
Processing c:\users\lj\kicad_engine\03_tools\repos\interactivehtmlbom
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting jsonschema>=4.1 (from InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for jsonschema>=4.1 from https://files.pythonhosted.org/packages/69/90/f63fb5873511e014207a475e2bb4e8b2e570d655b00ac19a9a0ca0a385ee/jsonschema-4.26.0-py3-none-any.whl.metadata
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting wxpython>=4.0 (from InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for wxpython>=4.0 from https://files.pythonhosted.org/packages/dd/95/5b4928819f161fb4cb38a5b5a001abb8d66500b2399bf20f914215e8e17e/wxpython-4.2.5-cp311-cp311-win_amd64.whl.metadata
  Downloading wxpython-4.2.5-cp311-cp311-win_amd64.whl.metadata (3.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=4.1->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for attrs>=22.2.0 from https://files.pythonhosted.org/packages/64/b4/17d4b0b2a2dc85a6df63d1157e028ed19f90d4cd97c36717afef2bc2f395/attrs-26.1.0-py3-none-any.whl.metadata
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.1->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for jsonschema-specifications>=2023.03.6 from https://files.pythonhosted.org/packages/41/45/1a4ed80516f02155c51f51e8cedb3c1902296743db0bbc66608a0db2814f/jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.1->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for referencing>=0.28.4 from https://files.pythonhosted.org/packages/2c/58/ca301544e1fa93ed4f80d724bf5b194f6e4b945841c5bfd555878eea9fcb/referencing-0.37.0-py3-none-any.whl.metadata
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.1->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for rpds-py>=0.25.0 from https://files.pythonhosted.org/packages/fa/5b/e7b7aa136f28462b344e652ee010d4de26ee9fd16f1bfd5811f5153ccf89/rpds_py-0.30.0-cp311-cp311-win_amd64.whl.metadata
  Downloading rpds_py-0.30.0-cp311-cp311-win_amd64.whl.metadata (4.2 kB)
Collecting numpy (from wxpython>=4.0->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for numpy from https://files.pythonhosted.org/packages/bd/63/05d193dbb4b5eec1eca73822d80da98b511f8328ad4ae3ca4caf0f4db91d/numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata
  Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
Collecting typing-extensions>=4.4.0 (from referencing>=0.28.4->jsonschema>=4.1->InteractiveHtmlBom==2.11.1)
  Obtaining dependency information for typing-extensions>=4.4.0 from https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl.metadata
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
   ---------------------------------------- 90.6/90.6 kB 5.4 MB/s eta 0:00:00
Downloading wxpython-4.2.5-cp311-cp311-win_amd64.whl (16.6 MB)
   ---------------------------------------- 16.6/16.6 MB 16.4 MB/s eta 0:00:00
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
   ---------------------------------------- 67.5/67.5 kB ? eta 0:00:00
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-0.30.0-cp311-cp311-win_amd64.whl (236 kB)
   ---------------------------------------- 236.0/236.0 kB ? eta 0:00:00
Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl (12.6 MB)
   ---------------------------------------- 12.6/12.6 MB 72.5 MB/s eta 0:00:00
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
   ---------------------------------------- 44.6/44.6 kB ? eta 0:00:00
Building wheels for collected packages: InteractiveHtmlBom
  Building wheel for InteractiveHtmlBom (pyproject.toml): started
  Building wheel for InteractiveHtmlBom (pyproject.toml): finished with status 'done'
  Created wheel for InteractiveHtmlBom: filename=interactivehtmlbom-2.11.1-py3-none-any.whl size=150884 sha256=907c0d88f760a0395aa3c2b2f523fd7286bc50111199a92622ecd918777a7da2
  Stored in directory: C:\Users\LJ\AppData\Local\Temp\pip-ephem-wheel-cache-lcdd87on\wheels\c3\dd\1c\e4b4a2599118337d52294d67149b14cb7a5755b71ec4b9da1a
Successfully built InteractiveHtmlBom
Installing collected packages: typing-extensions, rpds-py, numpy, attrs, wxpython, referencing, jsonschema-specifications, jsonschema, InteractiveHtmlBom
Successfully installed InteractiveHtmlBom-2.11.1 attrs-26.1.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 numpy-2.4.4 referencing-0.37.0 rpds-py-0.30.0 typing-extensions-4.15.0 wxpython-4.2.5

```

## InteractiveHtmlBom pip freeze after install attempt

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\python.exe' -m pip freeze
```
Exit code: 0
Output:
```text
attrs==26.1.0
InteractiveHtmlBom @ file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/InteractiveHtmlBom
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
numpy==2.4.4
referencing==0.37.0
rpds-py==0.30.0
typing_extensions==4.15.0
wxPython==4.2.5

```

## InteractiveHtmlBom git status after install attempt

```powershell
git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\InteractiveHtmlBom' status --short
```
Exit code: 0
Output:
```text
```

## InteractiveHtmlBom safe help command

```powershell
C:\Users\LJ\.codex\tmp\arg0\codex-arg0Hv0gW1;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code;C:\Program Files\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Kraken Desktop\;C:\Users\LJ\AppData\Local\Microsoft\WindowsApps;C:\Program Files\sf\bin;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files (x86)\sf\bin;C:\Program Files\Java\jdk-24\\bin;C:\Users\LJ\Downloads\apache-ant-1.10.15-bin\apache-ant-1.10.15\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\nodejs\;C:\Program Files\Git\cmd;C:\Users\LJ\Documents\Rider InterLock App\Tools\;C:\Program Files\GitHub CLI\;C:\Users\LJ\AppData\Local\Microsoft\WindowsApps;C:\Program Files\sf\bin;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files (x86)\sf\bin;C:\Program Files\Java\jdk-24\\bin;C:\Users\LJ\AppData\Roaming\npm;C:\Users\LJ\AppData\Local\Microsoft\WinGet\Packages\lucasg.Dependencies_Microsoft.Winget.Source_8wekyb3d8bbwe;C:\Users\LJ\AppData\Local\Programs\Ollama;C:\Users\LJ\AppData\Local\GitHubDesktop\bin;c:\Users\LJ\.vscode\extensions\openai.chatgpt-26.422.71525-win32-x64\bin\windows-x86_64='C:\Program Files\KiCad\9.0\bin;' + C:\Users\LJ\.codex\tmp\arg0\codex-arg0Hv0gW1;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code;C:\Program Files\Common Files\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Kraken Desktop\;C:\Users\LJ\AppData\Local\Microsoft\WindowsApps;C:\Program Files\sf\bin;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files (x86)\sf\bin;C:\Program Files\Java\jdk-24\\bin;C:\Users\LJ\Downloads\apache-ant-1.10.15-bin\apache-ant-1.10.15\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\nodejs\;C:\Program Files\Git\cmd;C:\Users\LJ\Documents\Rider InterLock App\Tools\;C:\Program Files\GitHub CLI\;C:\Users\LJ\AppData\Local\Microsoft\WindowsApps;C:\Program Files\sf\bin;C:\Users\LJ\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files (x86)\sf\bin;C:\Program Files\Java\jdk-24\\bin;C:\Users\LJ\AppData\Roaming\npm;C:\Users\LJ\AppData\Local\Microsoft\WinGet\Packages\lucasg.Dependencies_Microsoft.Winget.Source_8wekyb3d8bbwe;C:\Users\LJ\AppData\Local\Programs\Ollama;C:\Users\LJ\AppData\Local\GitHubDesktop\bin;c:\Users\LJ\.vscode\extensions\openai.chatgpt-26.422.71525-win32-x64\bin\windows-x86_64; ='C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'; ='1'; & 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\generate_interactive_bom.exe' --help
```
Exit code: 0
Output:
```text
usage: generate_interactive_bom [-h] [--show-dialog]
                                [--kicad-variant KICAD_VARIANT] [--version]
                                [--dark-mode] [--hide-pads]
                                [--show-fabrication] [--hide-silkscreen]
                                [--highlight-pin1 [{none,all,selected}]]
                                [--no-redraw-on-drag]
                                [--board-rotation BOARD_ROTATION]
                                [--offset-back-rotation]
                                [--checkboxes CHECKBOXES]
                                [--mark-when-checked MARK_WHEN_CHECKED]
                                [--bom-view {bom-only,left-right,top-bottom}]
                                [--layer-view {F,FB,B}] [--no-compression]
                                [--no-browser] [--dest-dir DEST_DIR]
                                [--name-format NAME_FORMAT] [--include-tracks]
                                [--include-nets] [--sort-order SORT_ORDER]
                                [--blacklist BLACKLIST]
                                [--no-blacklist-virtual]
                                [--blacklist-empty-val]
                                [--netlist-file NETLIST_FILE]
                                [--extra-data-file EXTRA_DATA_FILE]
                                [--extra-fields EXTRA_FIELDS]
                                [--show-fields SHOW_FIELDS]
                                [--group-fields GROUP_FIELDS]
                                [--normalize-field-case]
                                [--variant-field VARIANT_FIELD]
                                [--variants-whitelist VARIANTS_WHITELIST]
                                [--variants-blacklist VARIANTS_BLACKLIST]
                                [--dnp-field DNP_FIELD]
                                file

KiCad InteractiveHtmlBom plugin CLI.

positional arguments:
  file                  KiCad PCB file

options:
  -h, --help            show this help message and exit
  --show-dialog         Shows config dialog. All flags except --kicad-variant
                        will be ignored. (default: False)
  --kicad-variant KICAD_VARIANT
                        KiCad board variant, empty is default variant. (Only
                        for KiCad v10+) (default: )
  --version             show program's version number and exit
  --dark-mode           Default to dark mode. (default: False)
  --hide-pads           Hide footprint pads by default. (default: False)
  --show-fabrication    Show fabrication layer by default. (default: False)
  --hide-silkscreen     Hide silkscreen by default. (default: False)
  --highlight-pin1 [{none,all,selected}]
                        Highlight first pin. (default: none)
  --no-redraw-on-drag   Do not redraw pcb on drag by default. (default: False)
  --board-rotation BOARD_ROTATION
                        Board rotation in degrees (-180 to 180). Will be
                        rounded to multiple of 5. (default: 0)
  --offset-back-rotation
                        Offset the back of the pcb by 180 degrees (default:
                        False)
  --checkboxes CHECKBOXES
                        Comma separated list of checkbox columns. (default:
                        Sourced,Placed)
  --mark-when-checked MARK_WHEN_CHECKED
                        Name of the checkbox column used to mark components
                        when checked. (default: )
  --bom-view {bom-only,left-right,top-bottom}
                        Default BOM view. (default: left-right)
  --layer-view {F,FB,B}
                        Default layer view. (default: FB)
  --no-compression      Disable compression of pcb data. (default: False)
  --no-browser          Do not launch browser. (default: False)
  --dest-dir DEST_DIR   Destination directory for bom file relative to pcb
                        file directory. (default: bom)
  --name-format NAME_FORMAT
                        Output file name format supports substitutions: %f :
                        original pcb file name without extension. %p :
                        pcb/project title from pcb metadata. %c : company from
                        pcb metadata. %r : revision from pcb metadata. %v :
                        pcb variant. %V : pcb variant or 'default', if empty.
                        %d : pcb date from metadata if available, file
                        modification date otherwise. %D : bom generation date.
                        %T : bom generation time. Extension .html will be
                        added automatically. (default: ibom)
  --include-tracks      Include track/zone information in output. F.Cu and
                        B.Cu layers only. (default: False)
  --include-nets        Include netlist information in output. (default:
                        False)
  --sort-order SORT_ORDER
                        Default sort order for components. Must contain "~"
                        once. (default:
                        C,R,L,D,U,Y,X,F,SW,A,~,HS,CNN,J,P,NT,MH)
  --blacklist BLACKLIST
                        List of comma separated blacklisted components or
                        prefixes with *. E.g. "X1,MH*" (default: )
  --no-blacklist-virtual
                        Do not blacklist virtual components. (default: False)
  --blacklist-empty-val
                        Blacklist components with empty value. (default:
                        False)
  --netlist-file NETLIST_FILE
                        (Deprecated) Path to netlist or xml file. (default:
                        None)
  --extra-data-file EXTRA_DATA_FILE
                        Path to netlist or xml file. (default: None)
  --extra-fields EXTRA_FIELDS
                        Passing --extra-fields "X,Y" is a shortcut for --show-
                        fields and --group-fields with values
                        "Value,Footprint,X,Y" (default: None)
  --show-fields SHOW_FIELDS
                        List of fields to show in the BOM. (default:
                        Value,Footprint)
  --group-fields GROUP_FIELDS
                        Fields that components will be grouped by. (default:
                        Value,Footprint)
  --normalize-field-case
                        Normalize extra field name case. E.g. "MPN" , "mpn"
                        will be considered the same field. (default: False)
  --variant-field VARIANT_FIELD
                        Name of the extra field that stores board variant for
                        component. (default: None)
  --variants-whitelist VARIANTS_WHITELIST
                        List of board variants to include in the BOM. Use
                        "<empty>" to denote not set or empty value. (default:
                        )
  --variants-blacklist VARIANTS_BLACKLIST
                        List of board variants to exclude from the BOM. Use
                        "<empty>" to denote not set or empty value. (default:
                        )
  --dnp-field DNP_FIELD
                        Name of the extra field that indicates do not populate
                        status. Components with this field not empty will be
                        excluded. (default: )

```

## InteractiveHtmlBom entry point detection

```powershell
Test-Path 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\generate_interactive_bom.exe'; Get-Command 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\generate_interactive_bom.exe'
```
Exit code: 0
Output:
```text
True

CommandType     Name                                               Version    Source                                   
-----------     ----                                               -------    ------                                   
Application     generate_interactive_bom.exe                       0.0.0.0    C:\Users\LJ\KICAD_ENGINE\03_TOOLS\pyth...



```

## PcbDraw git status branch commit

```powershell
git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' status --short --branch; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' branch --show-current; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' rev-parse HEAD; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' log -1 --pretty=%s
```
Exit code: 0
Output:
```text
## master...origin/master
master
9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f
Normalize package name and fix build command

```

## PcbDraw root file inventory

```powershell
Get-ChildItem -Force 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' | Select-Object Mode,Length,Name
```
Exit code: 0
Output:
```text

Mode   Length Name              
----   ------ ----              
d--h--        .git              
d-----        .github           
d-----        doc               
d-----        examples          
d-----        pcbdraw           
d-----        test              
-a---- 34     .gitattributes    
-a---- 1193   .gitignore        
-a---- 132    .gitmodules       
-a---- 1089   LICENSE           
-a---- 350    Makefile          
-a---- 153    MANIFEST.in       
-a---- 352491 promo_pcbdraw.png 
-a---- 113638 promo_populate.jpg
-a---- 1583   README.md         
-a---- 163    setup.cfg         
-a---- 1319   setup.py          
-a---- 88954  versioneer.py     



```

## PcbDraw install docs and manifests inventory

```powershell
Get-ChildItem -Path 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' -Recurse -File -Include README*,*.md,pyproject.toml,setup.py,setup.cfg,requirements*.txt,package.json | Select-Object FullName
```
Exit code: 0
Output:
```text

FullName                                                                        
--------                                                                        
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md                      
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md             
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\library.md                  
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md                  
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\populate.md                 
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\populate\source_html.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\populate\source_md.md  
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md              
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md                       
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.cfg                       
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py                        



```

## PcbDraw read README and install docs

```powershell
Get-Content README.md, doc\\installation.md, setup.py, setup.cfg
```
Exit code: 0
Output captured but omitted from command log for brevity.

## PcbDraw rg dependency and command notes

```powershell
rg -n --glob '!*.svg' --glob '!*.html' --glob '!*.png' --glob '!*.jpg' --glob '!*.pdf' 'install|pip|python|KiCad|pcbnew|Inkscape|librsvg|rsvg|entry_points|console_scripts|pcbdraw|render|version' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw'
```
Exit code: 0
Output:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:9:you just have to install KiCAD and then install PcbDraw via Pip:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:12:pip install PcbDraw # Use pip or pip3 based on your distribution
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:15:If you would like to use the upstream (unstable) version of PcbDraw, you can
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:16:install it directly from GitHub:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:19:pip3 install git+https://github.com/yaqwsx/PcbDraw@master
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:22:PcbDraw also requires either Inkscape 1.x or librsvg installed to perform
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:23:conversion from vector to raster images. The executables `inkscape` or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:24:`rsvg-convert` have to be in PATH. Optionally, you can specify environmental
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:30:On Windows, you have to install KiCAD 9 or newer and also Inkscape 1.x. PcbDraw
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:31:doesn't work with Inkscape 0.9x. To install PcbDraw on Windows, you have to open
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:48:pip install PcbDraw
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:54:pcbdraw --help
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\installation.md:65:container](https://github.com/yaqwsx/KiKit/blob/master/doc/installation.md#running-kikit-via-docker)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:5:PcbDraw uses either Inkscape or librsvg (`rsvg-convert`) to convert generated
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:6:SVG files into PNG files. If neither is available, conversion will fail.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:8:We recommend installing librsvg as it is faster. On Debian/Ubuntu:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:11:sudo apt install librsvg2-bin
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:14:Alternatively, install Inkscape 1.x. Make sure the `inkscape` or `rsvg-convert`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:17:## PcbDraw doesn't work with my KiCAD version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:19:PcbDraw requires KiCAD 9 or newer. Older versions (v5, v6, v7, v8) are no
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:20:longer supported. If you need support for older versions, use PcbDraw v1.1.x
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\faq.md:28:option or create them using the `pcbdraw libtemplate` command. See the [library
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\Makefile:9:	python3 setup.py sdist bdist_wheel
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\Makefile:11:install: package
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\Makefile:12:	pip3 install --no-deps --force dist/*.whl
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\Makefile:23:	cd pcbdraw && mypy .
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:9:To render the board invoke:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:12:pcbdraw plot examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:15:To render board, but e.g. change colors of LEDs:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:18:pcbdraw plot --remap examples/resources/remap.json examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:21:To render the back side:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:24:pcbdraw plot --back examples/resources/ArduinoLearningKitStarter.kicad_pcb back.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:30:pcbdraw plot --style oshpark-purple examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:33:To render only the board without components:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:36:pcbdraw plot --filter "" examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:39:To render board with only `L_R1` and `L_Y1`:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:42:pcbdraw plot --filter L_R1,L_Y1 examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:45:To render board and highlight `L_R1` and `L_Y1`:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:48:pcbdraw plot --highlight L_R1,L_Y1 examples/resources/ArduinoLearningKitStarter.kicad_pcb front.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\readme.md:63:pcbdraw populate examples/populate/source_html.md html_demo
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\library.md:10:given footprint is used for rendering. The lookup order is the same you
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:4:import versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:10:    name="pcbdraw",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:11:    version=versioneer.get_version(),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:12:    cmdclass=versioneer.get_cmdclass(),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:13:    python_requires=">=3.9",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:26:    install_requires=[
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:37:        "versioneer"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:44:    entry_points = {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:45:        "console_scripts": [
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.py:46:            "pcbdraw=pcbdraw.ui:run"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md:6:![example](promo_pcbdraw.png)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md:21:And, also, as a bonus it allows you to programmatically obtain 3D-rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md:27:`pcbdraw`. It also requires Inkscape 1 or librsvg installed. Read more details
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md:28:in the [installation guide](doc/installation.md).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\README.md:34:- [usage of PcbDraw](doc/pcbdraw.md)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.cfg:1:[versioneer]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.cfg:4:versionfile_source = pcbdraw/_version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\setup.cfg:5:versionfile_build = pcbdraw/_version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\MANIFEST.in:1:recursive-include pcbdraw/resources *
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\MANIFEST.in:3:recursive-include pcbdraw/templates *include versioneer.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\MANIFEST.in:4:include pcbdraw/_version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\MANIFEST.in:5:include versioneer.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:4:"""The Versioneer - like a rocketeer, but for versions.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:9:* like a rocketeer, but for versions!
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:10:* https://github.com/python-versioneer/python-versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:17:This is a tool for managing a recorded version number in setuptools-based
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:18:python projects. The goal is to remove the tedious and error-prone "update
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:19:the embedded version string" step from your release process. Making a new
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:20:release should be as easy as recording a new tag in your version-control
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:26:Versioneer provides two installation modes. The "classic" vendored mode installs
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:27:a copy of versioneer into your repository. The experimental build-time dependency mode
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:32:* `pip install versioneer` to somewhere in your $PATH
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:33:   * A [conda-forge recipe](https://github.com/conda-forge/versioneer-feedstock) is
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:34:     available, so you can also use `conda install -c conda-forge versioneer`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:35:* add a `[tool.versioneer]` section to your `pyproject.toml` or a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:36:  `[versioneer]` section to your `setup.cfg` (see [Install](INSTALL.md))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:37:   * Note that you will need to add `tomli; python_version < "3.11"` to your
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:39:* run `versioneer install --vendor` in your source tree, commit the results
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:40:* verify version information with `python setup.py version`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:44:* `pip install versioneer` to somewhere in your $PATH
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:45:   * A [conda-forge recipe](https://github.com/conda-forge/versioneer-feedstock) is
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:46:     available, so you can also use `conda install -c conda-forge versioneer`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:47:* add a `[tool.versioneer]` section to your `pyproject.toml` or a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:48:  `[versioneer]` section to your `setup.cfg` (see [Install](INSTALL.md))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:49:* add `versioneer` (with `[toml]` extra, if configuring in `pyproject.toml`)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:53:  requires = ["setuptools", "versioneer[toml]"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:56:* run `versioneer install --no-vendor` in your source tree, commit the results
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:57:* verify version information with `python setup.py version`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:63:* a version-control system checkout (mostly used by developers)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:69:Within each source tree, the version identifier (either a string or a number,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:76:* a `_version.py` created by some earlier build step
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:78:For released software, the version identifier is closely related to a VCS
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:79:tag. Some projects use tag names that include more than just the version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:81:needs to strip the tag prefix to extract the version identifier. For
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:82:unreleased software (between tags), the version identifier should provide
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:84:giving them an idea of roughly how old the tree is (after version 1.2, before
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:85:version 1.3). Many VCS systems can report a description that captures this,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:91:The version identifier is used for multiple purposes:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:93:* to allow the module to self-identify its version: `myproject.__version__`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:98:Versioneer works by adding a special `_version.py` file into your source
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:99:tree, where your `__init__.py` can import it. This `_version.py` knows how to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:100:dynamically ask the VCS tool for version information at import time.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:102:`_version.py` also contains `$Revision$` markers, and the installation
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:103:process marks `_version.py` to have this marker rewritten with a tag name
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:105:contain enough information to get the proper version.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:107:To allow `setup.py` to compute a version too, a `versioneer.py` is added to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:110:compute the version when invoked, and changes `setup.py build` and `setup.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:111:sdist` to replace `_version.py` with a small static file that contains just
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:112:the generated version data.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:116:See [INSTALL.md](./INSTALL.md) for detailed installation instructions.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:120:Code which uses Versioneer can learn about its version string at runtime by
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:121:importing `_version` from your main `__init__.py` file and running the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:122:`get_versions()` function. From the "outside" (e.g. in `setup.py`), you can
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:123:import the top-level `versioneer.py` and run `get_versions()`.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:125:Both functions return a dictionary with different flavors of version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:128:* `['version']`: A condensed version string, rendered using the selected
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:129:  style. This is the most commonly used value for the project's version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:145:* `['error']`: if the version string could not be computed, this will be set
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:148:  creating tarballs with a version string of "unknown".
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:153:developers). `version` is suitable for display in an "about" box or a CLI
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:154:`--version` output: it can be easily compared against release notes and lists
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:157:The installer adds the following text to your `__init__.py` to place a basic
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:158:version in `YOURPROJECT.__version__`:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:160:    from ._version import get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:161:    __version__ = get_versions()['version']
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:162:    del get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:167:rendered into a version string.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:171:version" section with more detail for in-between builds. For Git, this is
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:185:to return a version of "0+unknown". To investigate the problem, run `setup.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:186:version`, which will run the version-lookup code in a verbose mode, and will
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:187:display the full contents of `get_versions()` (including the `error` string,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:194:[issues page](https://github.com/python-versioneer/python-versioneer/issues).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:206:  distributions (and upload multiple independently-installable tarballs).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:211:should get the right version string. However `pip` and `setuptools` have bugs
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:212:and implementation details which frequently cause `pip install .` from a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:213:subproject directory to fail to find a correct version string (so it usually
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:216:`pip install --editable .` should work correctly. `setup.py install` might
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:220:some later version.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:222:[Bug #38](https://github.com/python-versioneer/python-versioneer/issues/38) is tracking
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:224:[PR #61](https://github.com/python-versioneer/python-versioneer/pull/61) describes the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:226:[pip PR#3176](https://github.com/pypa/pip/pull/3176) and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:227:[pip PR#3615](https://github.com/pypa/pip/pull/3615) contain work to improve
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:228:pip to let Versioneer work correctly.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:233:### Editable installs with setuptools <= 18.5
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:235:`setup.py develop` and `pip install --editable .` allow you to install a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:237:test) without re-installing after every change.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:239:"Entry-point scripts" (`setup(entry_points={"console_scripts": ..})`) are a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:240:convenient way to specify executable scripts that should be installed along
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:241:with the python package.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:246:script, which must be resolved by re-installing the package. This happens
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:247:when the install happens with one version, then the egg_info data is
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:248:regenerated while a different version is checked out. Many setup.py commands
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:249:cause egg_info to be rebuilt (including `sdist`, `wheel`, and installing into
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:252:[Bug #83](https://github.com/python-versioneer/python-versioneer/issues/83) describes
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:253:this one, but upgrading to a newer version of setuptools should probably
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:261:* install the new Versioneer (`pip install -U versioneer` or equivalent)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:265:* re-run `versioneer install --[no-]vendor` in your source tree, to replace
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:266:  `SRC/_version.py`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:271:This tool is designed to make it easily extended to other version-control
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:273:src/git/ . The top-level `versioneer.py` script is assembled from these
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:274:components by running make-versioneer.py . In the future, make-versioneer.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:275:will take a VCS name as an argument, and will construct a version of
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:276:`versioneer.py` that is specific to the given VCS. It might also take the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:278:installation by editing setup.py . Alternatively, it might go the other
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:287:  versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:288:* [versioningit](https://github.com/jwodder/versioningit) - a PEP 518-based setuptools
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:294:domain. The `_version.py` that it creates is also in the public domain.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:298:[pypi-image]: https://img.shields.io/pypi/v/versioneer.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:299:[pypi-url]: https://pypi.python.org/pypi/versioneer/
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:301:https://img.shields.io/travis/com/python-versioneer/python-versioneer.svg
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:302:[travis-url]: https://travis-ci.com/github/python-versioneer/python-versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:324:if sys.version_info >= (3, 11):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:339:    versionfile_source: str
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:340:    versionfile_build: Optional[str]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:349:    directory that contains setup.py, setup.cfg, and versioneer.py .
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:354:    versioneer_py = os.path.join(root, "versioneer.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:358:        or os.path.exists(versioneer_py)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:360:        # allow 'python path/to/setup.py COMMAND'
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:364:        versioneer_py = os.path.join(root, "versioneer.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:368:        or os.path.exists(versioneer_py)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:372:               "its immediate directory (like 'python setup.py COMMAND'), "
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:374:               "(like 'python path/to/setup.py COMMAND').")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:377:        # Certain runtime workflows (setup.py install/develop in a setuptools
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:378:        # tree) execute all dependencies in a single python process, so
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:379:        # "versioneer" may be imported multiple times, and python's shared
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:382:        # versioneer.py was first imported, even in later projects.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:385:        vsr_dir = os.path.normcase(os.path.splitext(versioneer_py)[0])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:387:            print("Warning: build in %s is using versioneer.py from %s"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:388:                  % (os.path.dirname(my_path), versioneer_py))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:397:    # configparser.NoSectionError (if it lacks a [versioneer] section), or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:399:    # the top of versioneer.py for instructions on writing your setup.cfg .
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:408:            section = pp['tool']['versioneer']
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:416:        parser.get("versioneer", "VCS")  # raise error if missing
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:418:        section = parser["versioneer"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:427:    cfg.versionfile_source = cast(str, section.get("versionfile_source"))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:428:    cfg.versionfile_build = section.get("versionfile_build")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:474:        # This hides the console window if pythonw.exe is used
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:509:# This file helps to compute a version number in source trees obtained from
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:513:# that just contains the computed version number.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:516:# Generated by versioneer-0.29
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:517:# https://github.com/python-versioneer/python-versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:519:"""Git implementation of _version.py."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:531:    """Get the keywords needed to look up the version information."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:533:    # setup.py/versioneer.py will grep for the variable names, so they must
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:534:    # each be defined on a line of their own. _version.py will just call
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:550:    versionfile_source: str
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:556:    # these strings are filled in when 'setup.py versioneer' creates
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:557:    # _version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:563:    cfg.versionfile_source = "%(VERSIONFILE_SOURCE)s"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:601:        # This hides the console window if pythonw.exe is used
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:635:def versions_from_parentdir(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:640:    """Try to determine the version from the parent directory name.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:643:    the project name and a version string. We will also support searching up
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:651:            return {"version": dirname[len(parentdir_prefix):],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:664:def git_get_keywords(versionfile_abs: str) -> Dict[str, str]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:665:    """Extract version information from the given file."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:666:    # the code embedded in _version.py can just fetch the value of these
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:667:    # keywords. When used from setup.py, we don't want to import _version.py,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:669:    # _version.py.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:672:        with open(versionfile_abs, "r") as fobj:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:692:def git_versions_from_keywords(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:697:    """Get version information from git keywords."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:699:        raise NotThisMethod("Short version file found")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:710:        # discover which version we're using, or to work around using an
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:725:        # a heuristic: assume all version tags have a digit. The old git %%d
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:747:            return {"version": r,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:751:    # no suitable tags, so version is "0+unknown", but full hex is still there
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:754:    return {"version": "0+unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:766:    """Get version from 'git describe' in the root of the source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:769:    expanded, and _version.py hasn't already been rewritten with a short
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:770:    version string, meaning we're inside a checked out source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:777:    # It may be intended to be passed to the Versioneer-versioned project,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:778:    # but that should not change where we get our version from.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:887:    # commit date: see ISO-8601 comment in git_versions_from_keywords()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:904:def render_pep440(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:905:    """Build up version string, with post-release "local version identifier".
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:914:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:916:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:917:            rendered += "%%d.g%%s" %% (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:919:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:922:        rendered = "0+untagged.%%d.g%%s" %% (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:925:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:926:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:929:def render_pep440_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:939:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:942:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:943:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:944:            rendered += "%%d.g%%s" %% (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:946:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:949:        rendered = "0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:951:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:952:        rendered += "+untagged.%%d.g%%s" %% (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:955:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:956:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:960:    """Split pep440 version string at the post-release segment.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:963:    post-release version number (or -1 if no post-release segment is present).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:969:def render_pep440_pre(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:978:            tag_version, post_version = pep440_split_post(pieces["closest-tag"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:979:            rendered = tag_version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:980:            if post_version is not None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:981:                rendered += ".post%%d.dev%%d" %% (post_version + 1, pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:983:                rendered += ".post0.dev%%d" %% (pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:985:            # no commits, use the tag as the version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:986:            rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:989:        rendered = "0.post0.dev%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:990:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:993:def render_pep440_post(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1004:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1006:            rendered += ".post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1008:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1009:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1010:            rendered += "g%%s" %% pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1013:        rendered = "0.post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1015:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1016:        rendered += "+g%%s" %% pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1017:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1020:def render_pep440_post_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1029:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1031:            rendered += ".post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1033:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1034:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1035:            rendered += "g%%s" %% pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1037:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1040:        rendered = "0.post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1042:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1043:        rendered += "+g%%s" %% pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1045:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1046:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1049:def render_pep440_old(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1058:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1060:            rendered += ".post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1062:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1065:        rendered = "0.post%%d" %% pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1067:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1068:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1071:def render_git_describe(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1080:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1082:            rendered += "-%%d-g%%s" %% (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1085:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1087:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1088:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1091:def render_git_describe_long(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1101:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1102:        rendered += "-%%d-g%%s" %% (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1105:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1107:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1108:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1111:def render(pieces: Dict[str, Any], style: str) -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1112:    """Render the given version pieces into the requested style."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1114:        return {"version": "unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1124:        rendered = render_pep440(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1126:        rendered = render_pep440_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1128:        rendered = render_pep440_pre(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1130:        rendered = render_pep440_post(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1132:        rendered = render_pep440_post_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1134:        rendered = render_pep440_old(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1136:        rendered = render_git_describe(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1138:        rendered = render_git_describe_long(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1142:    return {"version": rendered, "full-revisionid": pieces["long"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1147:def get_versions() -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1148:    """Get version information or return default if unable to do so."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1149:    # I am in _version.py, which lives at ROOT/VERSIONFILE_SOURCE. If we have
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1158:        return git_versions_from_keywords(get_keywords(), cfg.tag_prefix,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1165:        # versionfile_source is the relative path from the top of the source
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1168:        for _ in cfg.versionfile_source.split('/'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1171:        return {"version": "0+unknown", "full-revisionid": None,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1178:        return render(pieces, cfg.style)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1184:            return versions_from_parentdir(cfg.parentdir_prefix, root, verbose)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1188:    return {"version": "0+unknown", "full-revisionid": None,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1190:            "error": "unable to compute version", "date": None}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1195:def git_get_keywords(versionfile_abs: str) -> Dict[str, str]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1196:    """Extract version information from the given file."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1197:    # the code embedded in _version.py can just fetch the value of these
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1198:    # keywords. When used from setup.py, we don't want to import _version.py,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1200:    # _version.py.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1203:        with open(versionfile_abs, "r") as fobj:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1223:def git_versions_from_keywords(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1228:    """Get version information from git keywords."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1230:        raise NotThisMethod("Short version file found")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1241:        # discover which version we're using, or to work around using an
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1256:        # a heuristic: assume all version tags have a digit. The old git %d
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1278:            return {"version": r,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1282:    # no suitable tags, so version is "0+unknown", but full hex is still there
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1285:    return {"version": "0+unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1297:    """Get version from 'git describe' in the root of the source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1300:    expanded, and _version.py hasn't already been rewritten with a short
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1301:    version string, meaning we're inside a checked out source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1308:    # It may be intended to be passed to the Versioneer-versioned project,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1309:    # but that should not change where we get our version from.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1418:    # commit date: see ISO-8601 comment in git_versions_from_keywords()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1428:def do_vcs_install(versionfile_source: str, ipy: Optional[str]) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1429:    """Git-specific installation logic for Versioneer.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1431:    For Git, this means creating/changing .gitattributes to mark _version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1437:    files = [versionfile_source]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1445:            versioneer_file = os.path.relpath(my_path)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1447:            versioneer_file = "versioneer.py"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1448:        files.append(versioneer_file)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1453:                if line.strip().startswith(versionfile_source):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1461:            fobj.write(f"{versionfile_source} export-subst\n")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1466:def versions_from_parentdir(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1471:    """Try to determine the version from the parent directory name.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1474:    the project name and a version string. We will also support searching up
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1482:            return {"version": dirname[len(parentdir_prefix):],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1495:# This file was generated by 'versioneer.py' (0.29) from
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1502:version_json = '''
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1507:def get_versions():
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1508:    return json.loads(version_json)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1512:def versions_from_file(filename: str) -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1513:    """Try to determine the version from _version.py if present."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1518:        raise NotThisMethod("unable to read _version.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1519:    mo = re.search(r"version_json = '''\n(.*)'''  # END VERSION_JSON",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1522:        mo = re.search(r"version_json = '''\r\n(.*)'''  # END VERSION_JSON",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1525:        raise NotThisMethod("no version_json in _version.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1529:def write_to_version_file(filename: str, versions: Dict[str, Any]) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1530:    """Write the given version number to the given _version.py file."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1531:    contents = json.dumps(versions, sort_keys=True,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1536:    print("set %s to '%s'" % (filename, versions["version"]))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1546:def render_pep440(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1547:    """Build up version string, with post-release "local version identifier".
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1556:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1558:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1559:            rendered += "%d.g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1561:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1564:        rendered = "0+untagged.%d.g%s" % (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1567:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1568:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1571:def render_pep440_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1581:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1584:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1585:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1586:            rendered += "%d.g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1588:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1591:        rendered = "0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1593:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1594:        rendered += "+untagged.%d.g%s" % (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1597:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1598:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1602:    """Split pep440 version string at the post-release segment.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1605:    post-release version number (or -1 if no post-release segment is present).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1611:def render_pep440_pre(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1620:            tag_version, post_version = pep440_split_post(pieces["closest-tag"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1621:            rendered = tag_version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1622:            if post_version is not None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1623:                rendered += ".post%d.dev%d" % (post_version + 1, pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1625:                rendered += ".post0.dev%d" % (pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1627:            # no commits, use the tag as the version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1628:            rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1631:        rendered = "0.post0.dev%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1632:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1635:def render_pep440_post(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1646:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1648:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1650:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1651:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1652:            rendered += "g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1655:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1657:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1658:        rendered += "+g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1659:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1662:def render_pep440_post_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1671:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1673:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1675:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1676:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1677:            rendered += "g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1679:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1682:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1684:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1685:        rendered += "+g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1687:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1688:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1691:def render_pep440_old(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1700:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1702:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1704:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1707:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1709:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1710:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1713:def render_git_describe(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1722:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1724:            rendered += "-%d-g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1727:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1729:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1730:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1733:def render_git_describe_long(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1743:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1744:        rendered += "-%d-g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1747:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1749:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1750:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1753:def render(pieces: Dict[str, Any], style: str) -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1754:    """Render the given version pieces into the requested style."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1756:        return {"version": "unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1766:        rendered = render_pep440(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1768:        rendered = render_pep440_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1770:        rendered = render_pep440_pre(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1772:        rendered = render_pep440_post(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1774:        rendered = render_pep440_post_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1776:        rendered = render_pep440_old(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1778:        rendered = render_git_describe(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1780:        rendered = render_git_describe_long(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1784:    return {"version": rendered, "full-revisionid": pieces["long"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1793:def get_versions(verbose: bool = False) -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1794:    """Get the project version from whatever source is available.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1796:    Returns dict with two keys: 'version' and 'full'.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1798:    if "versioneer" in sys.modules:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1800:        del sys.modules["versioneer"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1805:    assert cfg.VCS is not None, "please set [versioneer]VCS= in setup.cfg"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1809:    assert cfg.versionfile_source is not None, \
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1810:        "please set versioneer.versionfile_source"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1811:    assert cfg.tag_prefix is not None, "please set versioneer.tag_prefix"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1813:    versionfile_abs = os.path.join(root, cfg.versionfile_source)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1815:    # extract version from first of: _version.py, VCS command (e.g. 'git
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1825:            keywords = get_keywords_f(versionfile_abs)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1828:                print("got version from expanded keyword %s" % ver)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1834:        ver = versions_from_file(versionfile_abs)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1836:            print("got version from file %s %s" % (versionfile_abs, ver))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1845:            ver = render(pieces, cfg.style)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1847:                print("got version from VCS %s" % ver)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1854:            ver = versions_from_parentdir(cfg.parentdir_prefix, root, verbose)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1856:                print("got version from parentdir %s" % ver)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1862:        print("unable to compute version")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1864:    return {"version": "0+unknown", "full-revisionid": None,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1865:            "dirty": None, "error": "unable to compute version",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1869:def get_version() -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1870:    """Get the short version string for this project."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1871:    return get_versions()["version"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1880:    if "versioneer" in sys.modules:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1881:        del sys.modules["versioneer"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1882:        # this fixes the "python setup.py develop" case (also 'install' and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1883:        # 'easy_install .'), in which subdependencies of the main project are
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1884:        # built (using setup.py bdist_egg) in the same python process. Assume
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1885:        # a main project A and a dependency B, which use different versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1888:        # with the wrong versioneer. Setuptools wraps the sub-dep builds in a
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1890:        # parent is protected against the child's "import versioneer". By
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1892:        # happens, we protect the child from the parent's versioneer too.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1893:        # Also see https://github.com/python-versioneer/python-versioneer/issues/52
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1897:    # we add "version" to setuptools
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1900:    class cmd_version(Command):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1901:        description = "report generated version string"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1912:            vers = get_versions(verbose=True)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1913:            print("Version: %s" % vers["version"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1919:    cmds["version"] = cmd_version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1925:    #  distutils/install -> distutils/build ->..
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1926:    #  setuptools/bdist_wheel -> distutils/install ->..
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1927:    #  setuptools/bdist_egg -> distutils/install_lib -> build_py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1928:    #  setuptools/install -> bdist_egg ->..
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1930:    #  pip install:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1933:    #   then does setup.py bdist_wheel, or sometimes setup.py install
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1936:    # pip install -e . and setuptool/editable_wheel will invoke build_py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1949:            versions = get_versions()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1952:                # During editable installs `.py` and data files are
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1955:            # now locate _version.py in the new build/ directory and replace
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1957:            if cfg.versionfile_build:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1958:                target_versionfile = os.path.join(self.build_lib,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1959:                                                  cfg.versionfile_build)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1960:                print("UPDATING %s" % target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1961:                write_to_version_file(target_versionfile, versions)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1973:            versions = get_versions()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1977:                # build/lib<..> dir with no _version.py to write to.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1978:                # As in place builds will already have a _version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1981:            # now locate _version.py in the new build/ directory and replace
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1983:            if not cfg.versionfile_build:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1985:            target_versionfile = os.path.join(self.build_lib,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1986:                                              cfg.versionfile_build)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1987:            if not os.path.exists(target_versionfile):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1988:                print(f"Warning: {target_versionfile} does not exist, skipping "
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1989:                      "version update. This can happen if you are running build_ext "
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1992:            print("UPDATING %s" % target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:1993:            write_to_version_file(target_versionfile, versions)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2001:        #   "version": versioneer.get_version().split("+", 1)[0], # FILEVERSION
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2002:        #   "product_version": versioneer.get_version(),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2009:                versions = get_versions()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2010:                target_versionfile = cfg.versionfile_source
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2011:                print("UPDATING %s" % target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2012:                write_to_version_file(target_versionfile, versions)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2015:                os.unlink(target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2016:                with open(cfg.versionfile_source, "w") as f:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2023:                             "VERSIONFILE_SOURCE": cfg.versionfile_source,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2038:                versions = get_versions()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2039:                target_versionfile = cfg.versionfile_source
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2040:                print("UPDATING %s" % target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2041:                write_to_version_file(target_versionfile, versions)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2044:                os.unlink(target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2045:                with open(cfg.versionfile_source, "w") as f:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2052:                             "VERSIONFILE_SOURCE": cfg.versionfile_source,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2071:            self.filelist.append('versioneer.py')
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2072:            if cfg.versionfile_source:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2073:                # There are rare cases where versionfile_source might not be
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2075:                self.filelist.append(cfg.versionfile_source)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2101:            versions = get_versions()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2102:            self._versioneer_generated_versions = versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2104:            # version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2105:            self.distribution.metadata.version = versions["version"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2112:            # now locate _version.py in the new base_dir directory
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2115:            target_versionfile = os.path.join(base_dir, cfg.versionfile_source)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2116:            print("UPDATING %s" % target_versionfile)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2117:            write_to_version_file(target_versionfile,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2118:                                  self._versioneer_generated_versions)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2128: [versioneer]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2131: versionfile_source = src/myproject/_version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2132: versionfile_build = myproject/_version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2138: import versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2139: setup(version=versioneer.get_version(),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2140:       cmdclass=versioneer.get_cmdclass(), ...)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2142:Please read the docstring in ./versioneer.py for configuration instructions,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2143:edit setup.cfg, and re-run the installer or 'python versioneer.py setup'.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2147:# See the docstring in versioneer.py for instructions. Note that you must
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2148:# re-run 'versioneer.py setup' after changing this section, and commit the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2151:[versioneer]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2154:#versionfile_source =
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2155:#versionfile_build =
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2162:from ._version import get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2163:__version__ = get_versions()['version']
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2164:del get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2169:__version__ = {0}.get_versions()['version']
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2174:    """Do main VCS-independent setup function for installing Versioneer."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2181:            print("Adding sample versioneer config to setup.cfg",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2188:    print(" creating %s" % cfg.versionfile_source)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2189:    with open(cfg.versionfile_source, "w") as f:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2195:                        "VERSIONFILE_SOURCE": cfg.versionfile_source,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2198:    ipy = os.path.join(os.path.dirname(cfg.versionfile_source),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2207:        module = os.path.splitext(os.path.basename(cfg.versionfile_source))[0]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2224:    # .gitattributes to mark _version.py for export-subst keyword
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2226:    do_vcs_install(cfg.versionfile_source, maybe_ipy)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2237:            if "import versioneer" in line:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2239:            if "versioneer.get_cmdclass()" in line:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2241:            if "versioneer.get_version()" in line:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2242:                found.add("get_version")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2243:            if "versioneer.VCS" in line:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2245:            if "versioneer.versionfile_source" in line:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2253:        print(" import versioneer")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2254:        print(" setup( version=versioneer.get_version(),")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2255:        print("        cmdclass=versioneer.get_cmdclass(),  ...)")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2259:        print("You should remove lines like 'versioneer.VCS = ' and")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\versioneer.py:2260:        print("'versioneer.versionfile_source = ' . This configuration")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_read_resistance.py:1:from pcbdraw.unit import read_resistance
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:4:from pcbdraw.convert_common import chooseInkscapeCandidate
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:6:def detectInkscape() -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:8:    Return path to working Inkscape >v1.0 executable
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:15:    candidates.append("inkscape") # Inkscape in path
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:16:    return chooseInkscapeCandidate(candidates)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:18:def rsvgSvgToPng(inputFilename: str, outputFilename: str, dpi: int) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:19:    tool = os.environ.get("PCBDRAW_RSVG", "rsvg-convert")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_unix.py:34:        reportError("rsvg-convert is not available. Please make sure it is installed.\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:9:def get_board_path(version: str) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:10:    return os.path.join(RESOURCES_DIR, f"ArduinoLearningKitStarter-v{version}.kicad_pcb")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:14:    """Detect which boards can actually be loaded by the installed KiCAD."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:21:            import pcbnew
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:22:            b = pcbnew.LoadBoard(path)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\conftest.py:35:    """Parametrized fixture providing board paths for each available KiCAD version."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:11:# imagemagick) to do the conversion. However, imagemagick is really hard to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:13:# that has several conversion strategies that reflect the platform. We also try
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:17:    from pcbdraw.convert_windows import detectInkscape
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:19:    from pcbdraw.convert_unix import detectInkscape, rsvgSvgToPng
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:23:    A strategy to convert an SVG file into a PNG file using Inkscape
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:25:    command = [detectInkscape(), "--export-type=png", f"--export-dpi={dpi}",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:28:        raise RuntimeError(f"Cannot convert {inputFilename} to {outputFilename}. Inkscape failed with:\n"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:33:        # Inkscape doesn't respect error codes
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:46:            "Inkscape": inkscapeSvgToPng
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:50:            "RSVG": rsvgSvgToPng, # We prefer it over Inkscape as it is much faster
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert.py:51:            "Inkscape": inkscapeSvgToPng
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:1:"""Integration tests for pcbdraw plot command. Requires KiCAD installation."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:11:        import pcbnew
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:17:requires_kicad = pytest.mark.skipif(not _has_kicad(), reason="KiCAD not installed")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:22:    """Test SVG generation from pcbdraw plot."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:27:            ["pcbdraw", "plot", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:49:            ["pcbdraw", "plot", "--side", "back", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:59:            ["pcbdraw", "plot", "--style", "oshpark-purple", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:74:            ["pcbdraw", "plot", "--no-components", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:82:            ["pcbdraw", "plot", "--mirror", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:90:    """Test bitmap (PNG/JPG) generation from pcbdraw plot."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:95:            ["pcbdraw", "plot", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:105:            ["pcbdraw", "plot", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:117:            ["pcbdraw", "plot", "--remap", remap_path, board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:126:    """Test 3D rendering via kicad-cli."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:128:    def test_render_front(self, board_path, tmp_path):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:129:        output = tmp_path / "render.png"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:131:            ["pcbdraw", "render", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:138:    def test_render_back(self, board_path, tmp_path):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:139:        output = tmp_path / "render.png"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:141:            ["pcbdraw", "render", "--side", "back", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:147:    def test_render_transparent(self, board_path, tmp_path):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:148:        output = tmp_path / "render.png"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:150:            ["pcbdraw", "render", "--transparent", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:156:    def test_render_normal_quality(self, board_path, tmp_path):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:157:        output = tmp_path / "render.png"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\test_plot_integration.py:159:            ["pcbdraw", "render", "--renderer", "normal", board_path, str(output)],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:3:PcbDraw allows you to convert KiCad board files into a nice looking
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:8:  easily select board style and also, render resistor values color bands.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:9:- rendering them. This invokes `kicad-cli pcb render` to produce a 3D image of
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:14:Board plotting is available under the `pcbdraw plot <input_file> <output_file>`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:31:- `--side [front|back]` Specify which side of the PCB to render
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:37:- `-v, --vcuts KICAD LAYER` If layer is specified, renders V-cuts from it
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:54:The styles can be installed in various locations. PcbDraw will
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:59:- the user local data directory. The script adds `share/pcbdraw`. As an
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:61:  `~/.local/share/pcbdraw/styles`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:62:- the system data directory. The script adds `share/pcbdraw`. As an example, on
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:63:  Linux systems the path for styles will be: `/usr/share/pcbdraw/styles`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:100:Board rendering is available under the `pcbdraw render <input_file> <output_file>`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:101:command. It uses `kicad-cli pcb render` to produce 3D images of the board. The
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:105:- `--side [front|back]` Specify which side to render
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:106:- `--renderer [raytrace|normal]` Specify what renderer to use
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\pcbdraw.md:114:The board thickness and color is also taken from the board file. The rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\resources\ArduinoLearningKitStarter.kicad_pcb:1:(kicad_pcb (version 20211014) (generator pcbnew)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\examples\resources\ArduinoLearningKitStarter.kicad_pcb:61:      (dxfusepcbnewfont true)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:4:def isValidInkscape(executable: str) -> bool:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:6:        out = subprocess.check_output([executable, "--version"]).decode("utf-8")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:8:        if parts[0] != "Inkscape":
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:10:        version = parts[1].split(".")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:11:        return int(version[0]) == 1
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:17:def chooseInkscapeCandidate(candidates: List[str]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:19:        if isValidInkscape(candidate):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:21:    raise RuntimeError("No Inkscape executable found. Please check:\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:22:                       "- if Inkscape is installed\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:23:                       "- if it is version at least 1.0\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:24:                       "If the conditions above are true, please ensure Inkscape is in PATH or\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_common.py:25:                       "ensure there is environmental variable 'PCBDRAW_INKSCAPE' pointing to the Inkscape executable\n\n" +
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\__init__.py:2:from ._version import get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\__init__.py:3:__version__ = get_versions()['version'] # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\__init__.py:4:del get_versions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\__init__.py:6:from . import _version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\__init__.py:7:__version__ = _version.get_versions()['version']
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\populate.md:13:Populate is invoked via `pcbdraw populate <specification> <output_directory>`.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\populate.md:38:- `[[front | R1,R2 ]]` will render front side of the board and adds R1 and R2.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\doc\populate.md:39:- `[[back | ]]` will render the back side and no components will be added
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:4:from mistune.renderers.markdown import MarkdownRenderer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:6:from pcbdraw.populate import (
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:10:    pcbdraw_plugin,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:48:        renderer = Renderer(mistune.HTMLRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:50:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:62:        renderer = Renderer(mistune.HTMLRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:64:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:72:        renderer = Renderer(mistune.HTMLRenderer, ["C1", "C2"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:74:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:82:        renderer = Renderer(mistune.HTMLRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:84:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:90:        renderer = Renderer(mistune.HTMLRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:92:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:97:        renderer = Renderer(mistune.HTMLRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:99:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:110:        renderer = Renderer(MarkdownRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:112:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:120:        renderer = Renderer(MarkdownRenderer, [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_populate.py:122:        result = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1:#!/usr/bin/env python3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:31:from pcbdraw.unit import read_resistance
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:34:import pcbnew  # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:318:    share = os.path.join('share', 'pcbdraw')
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:469:        """<?xml version="1.0"?>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:471:        <svg xmlns="http://www.w3.org/2000/svg" version="1.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:493:                # that some KiCAD versions emit for Edge.Cuts
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:614:    orientation: pcbnew.EDA_ANGLE
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:650:def collect_holes(board: pcbnew.BOARD) -> List[Hole]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:663:    via_type = pcbnew.PCB_VIA
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:670:            orientation=pcbnew.EDA_ANGLE(0, pcbnew.DEGREES_T),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:677:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:687:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:691:        if plotter.render_back:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:693:                PlotAction("board", [pcbnew.Edge_Cuts], self._process_baselayer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:694:                PlotAction("clad", [pcbnew.B_Mask], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:695:                PlotAction("pads", [pcbnew.B_Cu], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:696:                PlotAction("pads-mask", [pcbnew.B_Mask], self._process_mask),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:697:                PlotAction("silk", [pcbnew.B_SilkS], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:698:                PlotAction("outline", [pcbnew.Edge_Cuts], self._process_outline)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:701:                to_plot.insert(2, PlotAction("copper", [pcbnew.B_Cu], self._process_layer))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:704:                PlotAction("board", [pcbnew.Edge_Cuts], self._process_baselayer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:705:                PlotAction("clad", [pcbnew.F_Mask], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:706:                PlotAction("pads", [pcbnew.F_Cu], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:707:                PlotAction("pads-mask", [pcbnew.F_Mask], self._process_mask),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:708:                PlotAction("silk", [pcbnew.F_SilkS], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:709:                PlotAction("outline", [pcbnew.Edge_Cuts], self._process_outline)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:712:                to_plot.insert(2, PlotAction("copper", [pcbnew.F_Cu], self._process_layer))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:849:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1017:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1031:    layer: int = pcbnew.Cmts_User
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1033:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1052:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1054:        if plotter.render_back:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1055:            plan = [PlotAction("paste", [pcbnew.B_Paste], self._process_paste)]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1057:            plan = [PlotAction("paste", [pcbnew.F_Paste], self._process_paste)]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1077:    def __init__(self, board: Union[str, pcbnew.BOARD]):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1080:            self.board: pcbnew.BOARD = board if isinstance(board, pcbnew.BOARD) else pcbnew.LoadBoard(board)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1083:        self.render_back: bool = False
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1123:        self._setup_document(self.render_back, self.mirror)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1125:            plotter.render(self)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1128:        self._shrink_svg(self._document, self.margin, self.render_back ^ self.mirror)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1142:        The position is adjusted based on what side we are rendering
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1144:        render_back = not self.render_back if invert_side else self.render_back
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1146:            if (str(footprint.GetLayerName()) in ["Back", "B.Cu"] and not render_back) or \
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1147:               (str(footprint.GetLayerName()) in ["Top", "F.Cu"]  and     render_back):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1190:        Add global installation paths to the search path for libraries.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1265:            pctl = pcbnew.PLOT_CONTROLLER(self.board)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1274:            popt.SetTextMode(pcbnew.PLOT_TEXT_MODE_STROKE)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1282:                pctl.OpenPlotfile(action.name, pcbnew.PLOT_FORMAT_SVG, action.name)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1294:        return int(pcbnew.FromMM(x))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1297:        return float(pcbnew.ToMM(x))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1362:    def _setup_document(self, render_back: bool, mirror: bool) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\plot.py:1370:        if(render_back ^ mirror):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:1:#!/usr/bin/env python3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:19:from mistune.renderers.markdown import MarkdownRenderer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:21:from .pcbnew_common import fakeKiCADGui
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:27:def parse_pcbdraw(inline: Any, m: re.Match[str], state: Any) -> int:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:28:    text = m.group("pcbdraw_content")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:32:        "type": "pcbdraw",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:41:    r"(?P<pcbdraw_content>[\s\S]+?\|[\s\S]+?)"  # side| component
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:46:def pcbdraw_plugin(md: mistune.Markdown) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:47:    md.inline.register("pcbdraw", PCBDRAW_PATTERN, parse_pcbdraw, before="link")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:52:    Create a renderer instance that tracks assembly steps.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:64:    """Common state tracking for both HTML and Markdown renderers."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:101:    def handle_pcbdraw(self, side: str, components: List[str]) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:123:    def pcbdraw(self, text: str, side: str = "", components: Optional[List[str]] = None) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:124:        self.handle_pcbdraw(side, components or [])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:177:    def pcbdraw(self, token: Dict[str, Any], state: Any) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:179:        self.handle_pcbdraw(attrs.get("side", ""), attrs.get("components", []))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:211:            self.render_token(child, state)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:216:        text = self.render_children(token, state)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:237:def parse_content(renderer: Any, content: str) -> List[Dict[str, Any]]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:239:        renderer=renderer,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:240:        plugins=[pcbdraw_plugin, plugin_table, plugin_footnotes],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:243:    return renderer.output()  # type: ignore[no-any-return]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:372:        renderer = Renderer(mistune.HTMLRenderer, header.get("initial_components", []))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:383:        renderer = Renderer(MarkdownRenderer, header.get("initial_components", []))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\populate.py:385:    parsed_content = parse_content(renderer, content)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:10:from . import __version__
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:16:from .pcbnew_common import fakeKiCADGui
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:97:    help="Specify which side of the PCB to render")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:105:    help="If layer specified, renders V-cuts from it")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:150:    plotter.render_back = side == "back"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:247:    help="Specify which side to render")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:248:@click.option("--renderer", type=click.Choice(["raytrace", "normal"]), default="raytrace",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:249:    help="Specify what renderer to use")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:260:def render(input: str, output: str, side: str, renderer: str, projection: str,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:263:    Create a rendered image of the PCB using kicad-cli's 3D renderer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:265:    from .renderer import RenderAction, Side, renderBoard
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:269:        raytraced=renderer == "raytrace",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:276:    image = renderBoard(input, plan)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:280:@click.version_option(__version__)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\ui.py:287:run.add_command(render)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:2:3D board rendering using kicad-cli.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:4:Replaces the old GUI-automation approach (xvfb + xdotool + pcbnew).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:5:Requires KiCAD 9+ which ships kicad-cli with `pcb render` support.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:48:        "kicad-cli not found. Please install KiCAD 9 or newer.\n"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:49:        "kicad-cli is required for 3D rendering."
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:55:    Detect the board region in the rendered image using edge detection.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:73:    Make the background of a rendered board image transparent.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:89:def renderBoard(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:97:    behavior of the old GUI-automation renderer.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:104:        output = os.path.join(tmp, "render.png")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:107:            cli, "pcb", "render",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\renderer.py:132:                f"kicad-cli pcb render failed (exit code {result.returncode}):\n{stderr}"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_plot_units.py:1:"""Unit tests for pure functions in pcbdraw.plot (no KiCAD dependency)."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_plot_units.py:7:from pcbdraw.plot import (
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_plot_units.py:189:class TestUnitConversions:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\units\test_plot_units.py:278:        """KiCad 7.0.1+ emits closed polygon paths like 'M x,y x,y Z'."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:2:# This file helps to compute a version number in source trees obtained from
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:6:# that just contains the computed version number.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:9:# Generated by versioneer-0.29
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:10:# https://github.com/python-versioneer/python-versioneer
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:12:"""Git implementation of _version.py."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:24:    """Get the keywords needed to look up the version information."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:26:    # setup.py/versioneer.py will grep for the variable names, so they must
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:27:    # each be defined on a line of their own. _version.py will just call
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:43:    versionfile_source: str
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:49:    # these strings are filled in when 'setup.py versioneer' creates
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:50:    # _version.py
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:56:    cfg.versionfile_source = "pcbdraw/_version.py"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:94:        # This hides the console window if pythonw.exe is used
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:128:def versions_from_parentdir(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:133:    """Try to determine the version from the parent directory name.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:136:    the project name and a version string. We will also support searching up
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:144:            return {"version": dirname[len(parentdir_prefix):],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:157:def git_get_keywords(versionfile_abs: str) -> Dict[str, str]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:158:    """Extract version information from the given file."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:159:    # the code embedded in _version.py can just fetch the value of these
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:160:    # keywords. When used from setup.py, we don't want to import _version.py,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:162:    # _version.py.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:165:        with open(versionfile_abs, "r") as fobj:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:185:def git_versions_from_keywords(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:190:    """Get version information from git keywords."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:192:        raise NotThisMethod("Short version file found")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:203:        # discover which version we're using, or to work around using an
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:218:        # a heuristic: assume all version tags have a digit. The old git %d
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:240:            return {"version": r,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:244:    # no suitable tags, so version is "0+unknown", but full hex is still there
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:247:    return {"version": "0+unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:259:    """Get version from 'git describe' in the root of the source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:262:    expanded, and _version.py hasn't already been rewritten with a short
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:263:    version string, meaning we're inside a checked out source tree.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:270:    # It may be intended to be passed to the Versioneer-versioned project,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:271:    # but that should not change where we get our version from.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:380:    # commit date: see ISO-8601 comment in git_versions_from_keywords()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:397:def render_pep440(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:398:    """Build up version string, with post-release "local version identifier".
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:407:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:409:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:410:            rendered += "%d.g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:412:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:415:        rendered = "0+untagged.%d.g%s" % (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:418:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:419:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:422:def render_pep440_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:432:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:435:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:436:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:437:            rendered += "%d.g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:439:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:442:        rendered = "0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:444:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:445:        rendered += "+untagged.%d.g%s" % (pieces["distance"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:448:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:449:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:453:    """Split pep440 version string at the post-release segment.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:456:    post-release version number (or -1 if no post-release segment is present).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:462:def render_pep440_pre(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:471:            tag_version, post_version = pep440_split_post(pieces["closest-tag"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:472:            rendered = tag_version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:473:            if post_version is not None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:474:                rendered += ".post%d.dev%d" % (post_version + 1, pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:476:                rendered += ".post0.dev%d" % (pieces["distance"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:478:            # no commits, use the tag as the version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:479:            rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:482:        rendered = "0.post0.dev%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:483:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:486:def render_pep440_post(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:497:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:499:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:501:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:502:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:503:            rendered += "g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:506:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:508:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:509:        rendered += "+g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:510:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:513:def render_pep440_post_branch(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:522:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:524:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:526:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:527:            rendered += plus_or_dot(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:528:            rendered += "g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:530:                rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:533:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:535:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:536:        rendered += "+g%s" % pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:538:            rendered += ".dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:539:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:542:def render_pep440_old(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:551:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:553:            rendered += ".post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:555:                rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:558:        rendered = "0.post%d" % pieces["distance"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:560:            rendered += ".dev0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:561:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:564:def render_git_describe(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:573:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:575:            rendered += "-%d-g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:578:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:580:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:581:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:584:def render_git_describe_long(pieces: Dict[str, Any]) -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:594:        rendered = pieces["closest-tag"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:595:        rendered += "-%d-g%s" % (pieces["distance"], pieces["short"])
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:598:        rendered = pieces["short"]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:600:        rendered += "-dirty"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:601:    return rendered
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:604:def render(pieces: Dict[str, Any], style: str) -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:605:    """Render the given version pieces into the requested style."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:607:        return {"version": "unknown",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:617:        rendered = render_pep440(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:619:        rendered = render_pep440_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:621:        rendered = render_pep440_pre(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:623:        rendered = render_pep440_post(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:625:        rendered = render_pep440_post_branch(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:627:        rendered = render_pep440_old(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:629:        rendered = render_git_describe(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:631:        rendered = render_git_describe_long(pieces)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:635:    return {"version": rendered, "full-revisionid": pieces["long"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:640:def get_versions() -> Dict[str, Any]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:641:    """Get version information or return default if unable to do so."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:642:    # I am in _version.py, which lives at ROOT/VERSIONFILE_SOURCE. If we have
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:651:        return git_versions_from_keywords(get_keywords(), cfg.tag_prefix,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:658:        # versionfile_source is the relative path from the top of the source
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:661:        for _ in cfg.versionfile_source.split('/'):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:664:        return {"version": "0+unknown", "full-revisionid": None,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:671:        return render(pieces, cfg.style)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:677:            return versions_from_parentdir(cfg.parentdir_prefix, root, verbose)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:681:    return {"version": "0+unknown", "full-revisionid": None,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\_version.py:683:            "error": "unable to compute version", "date": None}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:2:import pcbnew  # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:3:from pcbnew import BOX2I  # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:9:def getBBoxWithoutContours(edge: pcbnew.EDA_SHAPE) -> pcbnew.BOX2I:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:16:def findBoundingBox(edges: List[pcbnew.EDA_SHAPE]) -> pcbnew.BOX2I:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:27:def findBoardBoundingBox(board: pcbnew.BOARD) -> BOX2I:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:36:def collectEdges(board: pcbnew.BOARD, layerName: str) -> List[pcbnew.EDA_SHAPE]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:42:        if isinstance(edge, pcbnew.PCB_DIMENSION_BASE):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:47:def combineBoundingBoxes(a: pcbnew.BOX2I, b: pcbnew.BOX2I) -> pcbnew.BOX2I:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_common.py:53:    return BOX2I(pcbnew.VECTOR2I(x1, y1), pcbnew.VECTOR2I(x2 - x1, y2 - y1))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\mypy.ini:4:    | ^_version.py$
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:5:from pcbdraw.convert_common import chooseInkscapeCandidate
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:7:def detectInkscape() -> str:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:9:    Return path to working Inkscape >v1.0 executable
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:16:    candidates.append("inkscape") # Inkscape in path
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:17:    candidates += readInkscapeFromStartMenu()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:19:    return chooseInkscapeCandidate(candidates)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:21:def readInkscapeFromStartMenu() -> List[str]:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:25:                            "Programs", "Inkscape", "Inkscape.lnk")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:30:                # The .com version provides CLI interface
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\convert_windows.py:38:    print(detectInkscape())
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:2:Thin compatibility shim for KiCAD 9 and 10 pcbnew API differences.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:4:Replaces pcbnewTransition. Only supports KiCAD 9 and 10.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:7:import pcbnew  # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:9:KICAD_VERSION = tuple(int(x) for x in pcbnew.GetMajorMinorVersion().split("."))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:13:        f"PcbDraw requires KiCAD 9 or newer, found {pcbnew.GetMajorMinorVersion()}"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:18:    """Resolve a pcbnew attribute that may have been renamed between v9 and v10."""
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:19:    v = getattr(pcbnew, name, None)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\pcbnew_compat.py:22:    return getattr(pcbnew, fallback)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:1:#!/usr/bin/env python3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:4:import pcbnew  # type: ignore
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:12:def loadFootprint(footprintPath: Union[str, Path]) -> pcbnew.FOOTPRINT:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:15:    return pcbnew.FootprintLoad(lib, foot)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:17:def buildFootprintBoardFromFile(footprintPath: str) -> pcbnew.BOARD:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:24:    board = pcbnew.BOARD()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:25:    footprint.SetPosition(pcbnew.VECTOR2I(0, 0))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:32:def buildFootprintBoardFromFootprint(footprint: pcbnew.FOOTPRINT) -> pcbnew.BOARD:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:40:        newFootprint = pcbnew.Cast_to_BOARD_ITEM(footprint).Duplicate()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:41:    board = pcbnew.BOARD()
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:42:    if newFootprint.GetLayer() == pcbnew.B_Cu:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:43:        newFootprint.Flip(pcbnew.VECTOR2I(0, 0), True)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:44:    newFootprint.SetPosition(pcbnew.VECTOR2I(0, 0))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:50:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:54:            PlotAction("copper", [pcbnew.F_Cu], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:55:            PlotAction("crt", [pcbnew.F_CrtYd], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:56:            PlotAction("fab", [pcbnew.F_Fab], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:57:            PlotAction("cmt", [pcbnew.Cmts_User], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:58:            PlotAction("edge", [pcbnew.Edge_Cuts], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:59:            PlotAction("silk", [pcbnew.F_SilkS], self._process_layer)]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:66:    def render(self, plotter: PcbPlotter) -> None:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:70:            PlotAction("copper", [pcbnew.B_Cu], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:71:            PlotAction("crt", [pcbnew.B_CrtYd], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:72:            PlotAction("fab", [pcbnew.B_Fab], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:73:            PlotAction("cmt", [pcbnew.Cmts_User], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:74:            PlotAction("edge", [pcbnew.Edge_Cuts], self._process_layer),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:75:            PlotAction("silk", [pcbnew.B_SilkS], self._process_layer)]
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:95:def run_footprint_impl(footprint: Union[str, Path, pcbnew.FOOTPRINT],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:100:    if isinstance(footprint, pcbnew.FOOTPRINT):
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\pcbdraw\create_template.py:146:    boardObj = pcbnew.LoadBoard(board)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pcb:2:	(version 20260206)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pcb:3:	(generator "pcbnew")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pcb:4:	(generator_version "10.0")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pcb:77:			(dxfusepcbnewfont yes)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_prl:67:    "version": 5
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:59:        "version": 2
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:237:      "version": 0
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:252:    "version": 3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:277:      "version": 5
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:283:  "pcbnew": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v10.kicad_pro:303:      "version": 0
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pcb:2:	(version 20241229)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pcb:3:	(generator "pcbnew")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pcb:4:	(generator_version "9.0")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pcb:67:			(dxfusepcbnewfont yes)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_prl:65:    "version": 5
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pro:57:        "version": 2
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pro:234:    "version": 3
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pro:258:      "version": 4
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\ArduinoLearningKitStarter-v9.kicad_pro:264:  "pcbnew": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw\test\resources\conn.kicad_pcb:1:(kicad_pcb (version 20171130) (host pcbnew 5.1.9-73d0e3b20d~88~ubuntu20.04.1)

```

## PcbDraw renderer availability checks

```powershell
where.exe inkscape; inkscape --version; where.exe rsvg-convert; rsvg-convert --version
```
Exit code: 1
Output:
```text
```
Errors:
```text
where.exe : INFO: Could not find files for the given pattern(s).
At line:73 char:5
+     where.exe inkscape
+     ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (INFO: Could not...ven pattern(s).:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
inkscape : The term 'inkscape' is not recognized as the name of a cmdlet, function, script file, or operable program. 
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:74 char:5
+     inkscape --version
+     ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (inkscape:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 

```

## PcbDraw create or reuse isolated KiCad Python venv

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -m venv 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw'
```
Exit code: 0
Output:
```text
```

## PcbDraw venv Python version

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\python.exe' --version
```
Exit code: 0
Output:
```text
Python 3.11.5

```

## PcbDraw install from local git clone without modifying source checkout

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\python.exe' -m pip install --disable-pip-version-check --no-compile --no-cache-dir 'git+file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw'
```
Exit code: 0
Output:
```text
Collecting git+file:/C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw
  Cloning file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw to c:\users\lj\appdata\local\temp\pip-req-build-5ex1lvza
  Resolved file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw to commit 9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Installing backend dependencies: started
  Installing backend dependencies: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting numpy (from pcbdraw==1.2.0)
  Obtaining dependency information for numpy from https://files.pythonhosted.org/packages/bd/63/05d193dbb4b5eec1eca73822d80da98b511f8328ad4ae3ca4caf0f4db91d/numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata
  Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
Collecting lxml (from pcbdraw==1.2.0)
  Obtaining dependency information for lxml from https://files.pythonhosted.org/packages/02/05/d60c732b56da5085175c07c74b2df4e6d181b0c9a61e1691474f06ef4b39/lxml-6.1.0-cp311-cp311-win_amd64.whl.metadata
  Downloading lxml-6.1.0-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
Collecting mistune>=3.0 (from pcbdraw==1.2.0)
  Obtaining dependency information for mistune>=3.0 from https://files.pythonhosted.org/packages/9b/f7/4a5e785ec9fbd65146a27b6b70b6cdc161a66f2024e4b04ac06a67f5578b/mistune-3.2.0-py3-none-any.whl.metadata
  Downloading mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting pybars3 (from pcbdraw==1.2.0)
  Downloading pybars3-0.9.7.tar.gz (29 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting pyyaml (from pcbdraw==1.2.0)
  Obtaining dependency information for pyyaml from https://files.pythonhosted.org/packages/da/e3/ea007450a105ae919a72393cb06f122f288ef60bba2dc64b26e2646fa315/pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata
  Downloading pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata (2.4 kB)
Collecting svgpathtools==1.4.1 (from pcbdraw==1.2.0)
  Obtaining dependency information for svgpathtools==1.4.1 from https://files.pythonhosted.org/packages/d3/ff/fc1a3a943934b6d484584882091fd7d21ec2f201e075f1380fa0da39aa5b/svgpathtools-1.4.1-py2.py3-none-any.whl.metadata
  Downloading svgpathtools-1.4.1-py2.py3-none-any.whl.metadata (21 kB)
Collecting Pillow>=9.0 (from pcbdraw==1.2.0)
  Obtaining dependency information for Pillow>=9.0 from https://files.pythonhosted.org/packages/69/42/836b6f3cd7f3e5fa10a1f1a5420447c17966044c8fbf589cc0452d5502db/pillow-12.2.0-cp311-cp311-win_amd64.whl.metadata
  Downloading pillow-12.2.0-cp311-cp311-win_amd64.whl.metadata (9.0 kB)
Collecting click>=7.1 (from pcbdraw==1.2.0)
  Obtaining dependency information for click>=7.1 from https://files.pythonhosted.org/packages/ae/44/c1221527f6a71a01ec6fbad7fa78f1d50dfa02217385cf0fa3eec7087d59/click-8.3.3-py3-none-any.whl.metadata
  Downloading click-8.3.3-py3-none-any.whl.metadata (2.6 kB)
Collecting svgwrite (from svgpathtools==1.4.1->pcbdraw==1.2.0)
  Obtaining dependency information for svgwrite from https://files.pythonhosted.org/packages/84/15/640e399579024a6875918839454025bb1d5f850bb70d96a11eabb644d11c/svgwrite-1.4.3-py3-none-any.whl.metadata
  Downloading svgwrite-1.4.3-py3-none-any.whl.metadata (8.8 kB)
Collecting colorama (from click>=7.1->pcbdraw==1.2.0)
  Obtaining dependency information for colorama from https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl.metadata
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting PyMeta3>=0.5.1 (from pybars3->pcbdraw==1.2.0)
  Downloading PyMeta3-0.5.1.tar.gz (29 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Downloading svgpathtools-1.4.1-py2.py3-none-any.whl (63 kB)
   ---------------------------------------- 63.1/63.1 kB ? eta 0:00:00
Downloading click-8.3.3-py3-none-any.whl (110 kB)
   ---------------------------------------- 110.5/110.5 kB ? eta 0:00:00
Downloading mistune-3.2.0-py3-none-any.whl (53 kB)
   ---------------------------------------- 53.6/53.6 kB ? eta 0:00:00
Downloading pillow-12.2.0-cp311-cp311-win_amd64.whl (7.1 MB)
   ---------------------------------------- 7.1/7.1 MB 56.6 MB/s eta 0:00:00
Downloading lxml-6.1.0-cp311-cp311-win_amd64.whl (4.0 MB)
   ---------------------------------------- 4.0/4.0 MB 87.3 MB/s eta 0:00:00
Downloading numpy-2.4.4-cp311-cp311-win_amd64.whl (12.6 MB)
   ---------------------------------------- 12.6/12.6 MB 81.8 MB/s eta 0:00:00
Downloading pyyaml-6.0.3-cp311-cp311-win_amd64.whl (158 kB)
   ---------------------------------------- 158.8/158.8 kB ? eta 0:00:00
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading svgwrite-1.4.3-py3-none-any.whl (67 kB)
   ---------------------------------------- 67.1/67.1 kB ? eta 0:00:00
Building wheels for collected packages: pcbdraw, pybars3, PyMeta3
  Building wheel for pcbdraw (pyproject.toml): started
  Building wheel for pcbdraw (pyproject.toml): finished with status 'done'
  Created wheel for pcbdraw: filename=pcbdraw-1.2.0-py3-none-any.whl size=566492 sha256=760c5ca73e942b2b53ae8d9fb17a21e311114a97059a53cc34c6ba89598946cf
  Stored in directory: C:\Users\LJ\AppData\Local\Temp\pip-ephem-wheel-cache-zim6dh26\wheels\7e\ec\c0\9fb9be56b903160271d073369211c075aca6fb79c99c8012e2
  Building wheel for pybars3 (pyproject.toml): started
  Building wheel for pybars3 (pyproject.toml): finished with status 'done'
  Created wheel for pybars3: filename=pybars3-0.9.7-py3-none-any.whl size=14176 sha256=9f6618951cf8736bc3561bd872b7dc2af2f28f082ad14d9dd9759337ea5fea6b
  Stored in directory: C:\Users\LJ\AppData\Local\Temp\pip-ephem-wheel-cache-zim6dh26\wheels\64\b1\3d\cfac19f3ddd92f19e630a97106a66d1a92ffd30e4e95ca5e45
  Building wheel for PyMeta3 (pyproject.toml): started
  Building wheel for PyMeta3 (pyproject.toml): finished with status 'done'
  Created wheel for PyMeta3: filename=pymeta3-0.5.1-py3-none-any.whl size=16556 sha256=bc153d595ed6449a7109c705da116dab3dd46590a30a69c02fb4bcd3048bd459
  Stored in directory: C:\Users\LJ\AppData\Local\Temp\pip-ephem-wheel-cache-zim6dh26\wheels\67\18\5a\5a3a19ff18c8118a8dd11204dcde08349c2bbbdd77ac45b6a7
Successfully built pcbdraw pybars3 PyMeta3
Installing collected packages: PyMeta3, svgwrite, pyyaml, pybars3, Pillow, numpy, mistune, lxml, colorama, svgpathtools, click, pcbdraw
Successfully installed Pillow-12.2.0 PyMeta3-0.5.1 click-8.3.3 colorama-0.4.6 lxml-6.1.0 mistune-3.2.0 numpy-2.4.4 pcbdraw-1.2.0 pybars3-0.9.7 pyyaml-6.0.3 svgpathtools-1.4.1 svgwrite-1.4.3

```
Errors:
```text
python.exe :   Running command git clone --filter=blob:none --quiet 
file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw 'C:\Users\LJ\AppData\Local\Temp\pip-req-build-5ex1lvza'
At line:82 char:5
+     & (Join-Path $EnvDir 'Scripts\python.exe') -m pip install --disab ...
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (  Running comma...build-5ex1lvza':String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
  warning: filtering not recognized by server, ignoring
  Running command git submodule update --init --recursive -q

```

## PcbDraw pip freeze after install attempt

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\python.exe' -m pip freeze
```
Exit code: 0
Output:
```text
click==8.3.3
colorama==0.4.6
lxml==6.1.0
mistune==3.2.0
numpy==2.4.4
pcbdraw @ git+file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw@9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f
pillow==12.2.0
pybars3==0.9.7
PyMeta3==0.5.1
PyYAML==6.0.3
svgpathtools==1.4.1
svgwrite==1.4.3

```

## PcbDraw git status after install attempt

```powershell
git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\PcbDraw' status --short
```
Exit code: 0
Output:
```text
```

## PcbDraw safe help command

```powershell
$env:PATH = 'C:\Program Files\KiCad\9.0\bin;' + $env:PATH
$env:PYTHONPATH = 'C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe' --help
```
Exit code: 1
Output:
```text
```
Errors:
```text
pcbdraw.exe : Traceback (most recent call last):
At line:94 char:5
+     & (Join-Path $EnvDir 'Scripts\pcbdraw.exe') --help
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Traceback (most recent call last)::String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe\__main__.py", line 4, in <module>
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Lib\site-packages\pcbdraw\ui.py", line 11, in <module>
    from .convert import save
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Lib\site-packages\pcbdraw\convert.py", line 17, in 
<module>
    from pcbdraw.convert_windows import detectInkscape
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Lib\site-packages\pcbdraw\convert_windows.py", line 3, 
in <module>
    import LnkParse3 # type: ignore
    ^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'LnkParse3'

```

## PcbDraw entry point detection

```powershell
Test-Path 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe'; Get-Command 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe'
```
Exit code: 1
Output:
```text
True

CommandType     Name                                               Version    Source                                   
-----------     ----                                               -------    ------                                   
Application     pcbdraw.exe                                        0.0.0.0    C:\Users\LJ\KICAD_ENGINE\03_TOOLS\pyth...



```

## PcbDraw install missing Windows dependency LnkParse3

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\python.exe' -m pip install --disable-pip-version-check --no-compile --no-cache-dir LnkParse3
```
Exit code: 0
Output:
```text
Collecting LnkParse3
  Obtaining dependency information for LnkParse3 from https://files.pythonhosted.org/packages/47/7f/3998a1902e88b556679118cdc052fd87ee180b8782c925585e77a176371a/lnkparse3-1.6.0-py3-none-any.whl.metadata
  Downloading lnkparse3-1.6.0-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: pyyaml in c:\users\lj\kicad_engine\03_tools\python_envs\pcbdraw\lib\site-packages (from LnkParse3) (6.0.3)
Downloading lnkparse3-1.6.0-py3-none-any.whl (52 kB)
   ---------------------------------------- 52.6/52.6 kB 2.6 MB/s eta 0:00:00
Installing collected packages: LnkParse3
Successfully installed LnkParse3-1.6.0

```

## PcbDraw safe help command after LnkParse3 install

```powershell
$env:PATH = 'C:\Program Files\KiCad\9.0\bin;' + $env:PATH
$env:PYTHONPATH = 'C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe' --help
```
Exit code: 0
Output:
```text
Usage: pcbdraw [OPTIONS] COMMAND [ARGS]...

  PcbDraw generates images of KiCAD PCBs

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  libtemplate  Create footprint templates
  plot         Create a stylized drawing of the PCB.
  populate     Create assembly step-by-step guides
  render       Create a rendered image of the PCB using kicad-cli's 3D...

```

## PcbDraw pip freeze after LnkParse3 install

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\python.exe' -m pip freeze
```
Exit code: 0
Output:
```text
certifi==2025.11.12
charset-normalizer==3.4.4
click==8.3.3
colorama==0.4.6
idna==3.11
LnkParse3==1.6.0
lxml==6.1.0
mistune==3.2.0
numpy==2.3.5
pcbdraw @ git+file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/PcbDraw@9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f
pillow==12.0.0
pybars3==0.9.7
PyMeta3==0.5.1
PyYAML==6.0.3
requests==2.32.5
six==1.17.0
svgpathtools==1.4.1
svgwrite==1.4.3
urllib3==2.6.2

```

## PcbDraw version check

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe' --version
```
Exit code: 1
Output:
```text
```
Errors:
```text
pcbdraw.exe : Traceback (most recent call last):
At line:51 char:127
+ ... ure -Script { & (Join-Path $EnvDir 'Scripts\pcbdraw.exe') --version }
+                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Traceback (most recent call last)::String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe\__main__.py", line 4, in <module>
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Lib\site-packages\pcbdraw\ui.py", line 8, in <module>
    from .create_template import libtemplate
  File "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Lib\site-packages\pcbdraw\create_template.py", line 4, 
in <module>
    import pcbnew  # type: ignore
    ^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pcbnew'

```

## PcbDraw renderer availability follow-up

```powershell
where.exe rsvg-convert; Test-Path 'C:\Program Files\Inkscape\bin\inkscape.exe'; Test-Path 'C:\Program Files\Inkscape\inkscape.exe'; Get-ChildItem 'C:\Program Files','C:\Program Files (x86)' -Directory -Filter 'Inkscape*' -ErrorAction SilentlyContinue
```
Exit code: 1
Output:
```text
True
False


    Directory: C:\Program Files


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d-----          1/3/2026  12:01 PM                Inkscape                                                             



```
Errors:
```text
where.exe : INFO: Could not find files for the given pattern(s).
At line:53 char:5
+     where.exe rsvg-convert
+     ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (INFO: Could not...ven pattern(s).:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 

```

## PcbDraw version check with KiCad Python environment

```powershell
$env:PATH = 'C:\Program Files\KiCad\9.0\bin;' + $env:PATH
$env:PYTHONPATH = 'C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe' --version
```
Exit code: 0
Output:
```text
pcbdraw, version 1.2.0

```

## PcbDraw inspect existing Inkscape installation path

```powershell
Get-ChildItem -LiteralPath 'C:\Program Files\Inkscape' -Force; Get-ChildItem -Path 'C:\Program Files\Inkscape' -Recurse -Filter 'inkscape*.exe' -ErrorAction SilentlyContinue | Select-Object FullName
```
Exit code: 0
Output:
```text


    Directory: C:\Program Files\Inkscape


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d-----          1/3/2026  12:01 PM                bin                                                                  
d-----          1/3/2026  12:01 PM                etc                                                                  
d-----          1/3/2026  12:01 PM                include                                                              
d-----          1/3/2026  12:01 PM                lib                                                                  
d-----          1/3/2026  12:02 PM                share                                                                
-a----         5/13/2025  10:50 PM          29776 NEWS.md                                                              
-a----         5/13/2025  10:50 PM           1699 README.md                                                            
-a----         5/13/2025  10:50 PM             28 Run Inkscape !.bat                                                   
-a----         5/13/2025  10:50 PM             40 Run Inkscape and create debug trace.bat                              
-a----         5/13/2025  10:50 PM             55 Run Inkscape with GTK Inspector.bat                                  

FullName : C:\Program Files\Inkscape\bin\inkscape.exe




```

## PcbDraw Inkscape full-path version check

```powershell
& 'C:\Program Files\Inkscape\bin\inkscape.exe' --version
```
Exit code: 0
Output:
```text
```

## PcbDraw Inkscape file metadata version check

```powershell
(Get-Item 'C:\Program Files\Inkscape\bin\inkscape.exe').VersionInfo | Select-Object ProductVersion,FileVersion,FileDescription
```
Exit code: 0
Output:
```text

ProductVersion FileVersion FileDescription                
-------------- ----------- ---------------                
1.4.2          1.4.2       Inkscape vector graphics editor



```

## KiCanvas git status branch commit

```powershell
git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' status --short --branch; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' branch --show-current; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' rev-parse HEAD; git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' log -1 --pretty=%s
```
Exit code: 0
Output:
```text
## main...origin/main
main
b031159eb74aaa7eef2b026fd85d35bc05ff2095
fix: file loading fails when path contains URL-encoded characters (#192)

```

## KiCanvas root file inventory

```powershell
Get-ChildItem -Force 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' | Select-Object Mode,Length,Name
```
Exit code: 0
Output:
```text

Mode   Length Name              
----   ------ ----              
d--h--        .git              
d-----        .github           
d-----        .vscode           
d-----        assets            
d-----        debug             
d-----        docs              
d-----        scripts           
d-----        src               
d-----        test              
d-----        third_party       
-a---- 1143   .eslintrc.cjs     
-a---- 95     .gitignore        
-a---- 173    .prettierignore   
-a---- 484    .prettierrc       
-a---- 3447   CODE_OF_CONDUCT.md
-a---- 2179   LICENSE.md        
-a---- 319214 package-lock.json 
-a---- 2148   package.json      
-a---- 3755   README.md         
-a---- 3754   tsconfig.json     



```

## KiCanvas install docs and manifests inventory

```powershell
Get-ChildItem -Path 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' -Recurse -File -Include README*,*.md,package.json,package-lock.json,pnpm-lock.yaml,yarn.lock,pyproject.toml,requirements*.txt | Select-Object FullName
```
Exit code: 0
Output:
```text

FullName                                                                                              
--------                                                                                              
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\is-this-in-latin-.md          
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\my-file-looks-wrong--.md      
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\my-file-won-t-load-.md        
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\oh-boy--do-i-have-an-idea-.md 
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\this-doesn-t-work-right--.md  
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\.github\ISSUE_TEMPLATE\this-made-my-browser-mad---.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md                             
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md                               
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md                                    
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\index.md                                   
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md                                 
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md                                 
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\requirements.txt                                
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt                     
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\THIRD_PARTY_README.md          
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\CODE_OF_CONDUCT.md                                   
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\LICENSE.md                                           
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json                                    
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json                                         
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md                                            



```

## KiCanvas read README and package manifests

```powershell
Get-Content README.md, package.json, package-lock.json, docs/package.json
```
Exit code: 0
Output captured but omitted from command log for brevity.

## KiCanvas rg dependency build and command notes

```powershell
rg -n --glob '!*.svg' --glob '!*.html' --glob '!*.png' --glob '!*.jpg' --glob '!*.pdf' 'install|npm|pnpm|yarn|node|build|dev|serve|test|lint|KiCad|kicanvas|package|dist|browser' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas'
```
Exit code: 0
Output:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\LICENSE.md:11:to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\LICENSE.md:26:This notice must be included in any distributions of this project or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\LICENSE.md:34:- Newstroke by Vladimir Uryvaev, Lingdong Huang, Adobe, and KiCad contributors. Originally licensed under Creative Commons CC0 1.0, amended with an MIT-like license, and utilizes glyphs that are licensed under the SIL Open Font License Version 1.1.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:2:    "name": "kicanvas",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:7:        "test": "tests"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:9:    "devDependencies": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:12:        "@typescript-eslint/eslint-plugin": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:13:        "@typescript-eslint/parser": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:14:        "@web/dev-server-esbuild": "^1.0.4",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:15:        "@web/test-runner": "^0.20.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:17:        "esbuild": "^0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:18:        "esbuild-plugin-copy": "^2.1.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:19:        "eslint": "^8.53.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:20:        "eslint-config-prettier": "^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:21:        "eslint-plugin-mocha": "^10.2.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:29:        "test:watch": "web-test-runner --config scripts/web-test-runner.config.mjs --watch",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:30:        "test:coverage": "web-test-runner --config scripts/web-test-runner.config.mjs --coverage",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:31:        "test": "web-test-runner --config scripts/web-test-runner.config.mjs",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:32:        "lint:eslint": "eslint --config .eslintrc.cjs src/ --ext .js,.ts",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:33:        "lint:types": "tsc -p tsconfig.json",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:34:        "lint:prettier": "prettier . --check",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:35:        "lint": "npm run lint:eslint && npm run lint:types && npm run lint:prettier",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:37:        "serve": "node scripts/serve.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:38:        "build:no-check": "node scripts/build.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:39:        "build:font": "node scripts/build-font.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:40:        "build:sprites": "node scripts/build-sprites.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:41:        "build": "tsc -p tsconfig.json && node scripts/build.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:42:        "clean": "rm -rf build && rm -rf debug/kicanvas"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:46:        "url": "git+https://github.com/theacodes/kicanvas.js.git"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:51:        "url": "https://github.com/theacodes/kicanvas.js/issues"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json:53:    "homepage": "https://github.com/theacodes/kicanvas.js#readme"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2:    "name": "kicanvas",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6:    "packages": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:8:            "name": "kicanvas",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:11:            "devDependencies": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:14:                "@typescript-eslint/eslint-plugin": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:15:                "@typescript-eslint/parser": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:16:                "@web/dev-server-esbuild": "^1.0.4",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:17:                "@web/test-runner": "^0.20.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:19:                "esbuild": "^0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:20:                "esbuild-plugin-copy": "^2.1.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:21:                "eslint": "^8.53.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:22:                "eslint-config-prettier": "^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:23:                "eslint-plugin-mocha": "^10.2.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:31:        "node_modules/@babel/code-frame": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:33:            "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:35:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:43:                "node": ">=6.9.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:46:        "node_modules/@babel/helper-validator-identifier": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:48:            "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:50:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:53:                "node": ">=6.9.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:56:        "node_modules/@emmetio/extract-abbreviation": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:58:            "resolved": "https://registry.npmjs.org/@emmetio/extract-abbreviation/-/extract-abbreviation-0.1.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:60:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:63:        "node_modules/@esbuild/aix-ppc64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:65:            "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:70:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:77:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:80:        "node_modules/@esbuild/android-arm": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:82:            "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:87:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:94:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:97:        "node_modules/@esbuild/android-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:99:            "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:104:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:111:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:114:        "node_modules/@esbuild/android-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:116:            "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:121:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:128:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:131:        "node_modules/@esbuild/darwin-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:133:            "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:138:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:145:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:148:        "node_modules/@esbuild/darwin-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:150:            "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:155:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:162:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:165:        "node_modules/@esbuild/freebsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:167:            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:172:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:179:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:182:        "node_modules/@esbuild/freebsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:184:            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:189:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:196:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:199:        "node_modules/@esbuild/linux-arm": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:201:            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:206:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:213:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:216:        "node_modules/@esbuild/linux-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:218:            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:223:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:230:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:233:        "node_modules/@esbuild/linux-ia32": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:235:            "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:240:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:247:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:250:        "node_modules/@esbuild/linux-loong64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:252:            "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:257:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:264:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:267:        "node_modules/@esbuild/linux-mips64el": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:269:            "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:274:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:281:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:284:        "node_modules/@esbuild/linux-ppc64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:286:            "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:291:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:298:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:301:        "node_modules/@esbuild/linux-riscv64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:303:            "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:308:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:315:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:318:        "node_modules/@esbuild/linux-s390x": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:320:            "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:325:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:332:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:335:        "node_modules/@esbuild/linux-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:337:            "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:342:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:349:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:352:        "node_modules/@esbuild/netbsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:354:            "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:359:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:366:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:369:        "node_modules/@esbuild/netbsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:371:            "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:376:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:383:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:386:        "node_modules/@esbuild/openbsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:388:            "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:393:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:400:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:403:        "node_modules/@esbuild/openbsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:405:            "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:410:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:417:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:420:        "node_modules/@esbuild/openharmony-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:422:            "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:427:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:434:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:437:        "node_modules/@esbuild/sunos-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:439:            "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:444:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:451:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:454:        "node_modules/@esbuild/win32-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:456:            "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:461:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:468:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:471:        "node_modules/@esbuild/win32-ia32": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:473:            "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:478:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:485:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:488:        "node_modules/@esbuild/win32-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:490:            "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:495:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:502:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:505:        "node_modules/@eslint-community/eslint-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:507:            "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:509:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:512:                "eslint-visitor-keys": "^3.4.3"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:515:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:518:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:521:                "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:524:        "node_modules/@eslint-community/regexpp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:526:            "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:528:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:531:                "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:534:        "node_modules/@eslint/eslintrc": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:536:            "resolved": "https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-2.1.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:538:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:552:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:555:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:558:        "node_modules/@eslint/eslintrc/node_modules/brace-expansion": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:560:            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:562:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:569:        "node_modules/@eslint/eslintrc/node_modules/minimatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:571:            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:573:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:579:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:582:        "node_modules/@eslint/js": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:584:            "resolved": "https://registry.npmjs.org/@eslint/js/-/js-8.57.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:586:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:589:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:592:        "node_modules/@hapi/bourne": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:594:            "resolved": "https://registry.npmjs.org/@hapi/bourne/-/bourne-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:596:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:599:        "node_modules/@humanwhocodes/config-array": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:601:            "resolved": "https://registry.npmjs.org/@humanwhocodes/config-array/-/config-array-0.13.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:603:            "deprecated": "Use @eslint/config-array instead",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:604:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:612:                "node": ">=10.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:615:        "node_modules/@humanwhocodes/config-array/node_modules/brace-expansion": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:617:            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:619:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:626:        "node_modules/@humanwhocodes/config-array/node_modules/minimatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:628:            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:630:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:636:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:639:        "node_modules/@humanwhocodes/module-importer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:641:            "resolved": "https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:643:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:646:                "node": ">=12.22"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:653:        "node_modules/@humanwhocodes/object-schema": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:655:            "resolved": "https://registry.npmjs.org/@humanwhocodes/object-schema/-/object-schema-2.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:657:            "deprecated": "Use @eslint/object-schema instead",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:658:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:661:        "node_modules/@jridgewell/gen-mapping": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:663:            "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:665:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:672:        "node_modules/@jridgewell/resolve-uri": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:674:            "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:676:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:679:                "node": ">=6.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:682:        "node_modules/@jridgewell/source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:684:            "resolved": "https://registry.npmjs.org/@jridgewell/source-map/-/source-map-0.3.11.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:686:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:693:        "node_modules/@jridgewell/sourcemap-codec": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:695:            "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:697:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:700:        "node_modules/@jridgewell/trace-mapping": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:702:            "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:704:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:711:        "node_modules/@mdn/browser-compat-data": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:713:            "resolved": "https://registry.npmjs.org/@mdn/browser-compat-data/-/browser-compat-data-4.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:715:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:718:        "node_modules/@nodelib/fs.scandir": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:720:            "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:722:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:725:                "@nodelib/fs.stat": "2.0.5",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:729:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:732:        "node_modules/@nodelib/fs.stat": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:734:            "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:736:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:739:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:742:        "node_modules/@nodelib/fs.walk": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:744:            "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:746:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:749:                "@nodelib/fs.scandir": "2.1.5",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:753:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:756:        "node_modules/@open-wc/semantic-dom-diff": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:758:            "resolved": "https://registry.npmjs.org/@open-wc/semantic-dom-diff/-/semantic-dom-diff-0.20.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:760:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:764:                "@web/test-runner-commands": "^0.9.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:767:        "node_modules/@puppeteer/browsers": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:769:            "resolved": "https://registry.npmjs.org/@puppeteer/browsers/-/browsers-2.11.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:771:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:783:                "browsers": "lib/cjs/main-cli.js"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:786:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:789:        "node_modules/@rollup/plugin-node-resolve": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:791:            "resolved": "https://registry.npmjs.org/@rollup/plugin-node-resolve/-/plugin-node-resolve-15.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:793:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:803:                "node": ">=14.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:814:        "node_modules/@rollup/pluginutils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:816:            "resolved": "https://registry.npmjs.org/@rollup/pluginutils/-/pluginutils-5.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:818:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:826:                "node": ">=14.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:837:        "node_modules/@rollup/pluginutils/node_modules/picomatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:839:            "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:841:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:844:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:850:        "node_modules/@rollup/rollup-android-arm-eabi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:852:            "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:857:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:864:        "node_modules/@rollup/rollup-android-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:866:            "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:871:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:878:        "node_modules/@rollup/rollup-darwin-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:880:            "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:885:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:892:        "node_modules/@rollup/rollup-darwin-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:894:            "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:899:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:906:        "node_modules/@rollup/rollup-freebsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:908:            "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-arm64/-/rollup-freebsd-arm64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:913:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:920:        "node_modules/@rollup/rollup-freebsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:922:            "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-x64/-/rollup-freebsd-x64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:927:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:934:        "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:936:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:941:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:948:        "node_modules/@rollup/rollup-linux-arm-musleabihf": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:950:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-musleabihf/-/rollup-linux-arm-musleabihf-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:955:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:962:        "node_modules/@rollup/rollup-linux-arm64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:964:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:969:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:976:        "node_modules/@rollup/rollup-linux-arm64-musl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:978:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:983:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:990:        "node_modules/@rollup/rollup-linux-loong64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:992:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-gnu/-/rollup-linux-loong64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:997:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1004:        "node_modules/@rollup/rollup-linux-ppc64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1006:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-gnu/-/rollup-linux-ppc64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1011:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1018:        "node_modules/@rollup/rollup-linux-riscv64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1020:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1025:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1032:        "node_modules/@rollup/rollup-linux-riscv64-musl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1034:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-musl/-/rollup-linux-riscv64-musl-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1039:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1046:        "node_modules/@rollup/rollup-linux-s390x-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1048:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-s390x-gnu/-/rollup-linux-s390x-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1053:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1060:        "node_modules/@rollup/rollup-linux-x64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1062:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1067:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1074:        "node_modules/@rollup/rollup-linux-x64-musl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1076:            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1081:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1088:        "node_modules/@rollup/rollup-openharmony-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1090:            "resolved": "https://registry.npmjs.org/@rollup/rollup-openharmony-arm64/-/rollup-openharmony-arm64-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1095:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1102:        "node_modules/@rollup/rollup-win32-arm64-msvc": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1104:            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1109:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1116:        "node_modules/@rollup/rollup-win32-ia32-msvc": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1118:            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1123:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1130:        "node_modules/@rollup/rollup-win32-x64-gnu": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1132:            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-gnu/-/rollup-win32-x64-gnu-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1137:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1144:        "node_modules/@rollup/rollup-win32-x64-msvc": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1146:            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1151:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1158:        "node_modules/@tootallnate/quickjs-emscripten": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1160:            "resolved": "https://registry.npmjs.org/@tootallnate/quickjs-emscripten/-/quickjs-emscripten-0.23.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1162:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1165:        "node_modules/@types/accepts": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1167:            "resolved": "https://registry.npmjs.org/@types/accepts/-/accepts-1.3.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1169:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1172:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1175:        "node_modules/@types/babel__code-frame": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1177:            "resolved": "https://registry.npmjs.org/@types/babel__code-frame/-/babel__code-frame-7.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1179:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1182:        "node_modules/@types/body-parser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1184:            "resolved": "https://registry.npmjs.org/@types/body-parser/-/body-parser-1.19.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1186:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1190:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1193:        "node_modules/@types/chai": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1195:            "resolved": "https://registry.npmjs.org/@types/chai/-/chai-4.3.20.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1197:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1200:        "node_modules/@types/co-body": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1202:            "resolved": "https://registry.npmjs.org/@types/co-body/-/co-body-6.1.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1204:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1207:                "@types/node": "*",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1211:        "node_modules/@types/command-line-args": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1213:            "resolved": "https://registry.npmjs.org/@types/command-line-args/-/command-line-args-5.2.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1215:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1218:        "node_modules/@types/connect": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1220:            "resolved": "https://registry.npmjs.org/@types/connect/-/connect-3.4.38.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1222:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1225:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1228:        "node_modules/@types/content-disposition": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1230:            "resolved": "https://registry.npmjs.org/@types/content-disposition/-/content-disposition-0.5.9.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1232:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1235:        "node_modules/@types/convert-source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1237:            "resolved": "https://registry.npmjs.org/@types/convert-source-map/-/convert-source-map-2.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1239:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1242:        "node_modules/@types/cookies": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1244:            "resolved": "https://registry.npmjs.org/@types/cookies/-/cookies-0.9.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1246:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1252:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1255:        "node_modules/@types/debounce": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1257:            "resolved": "https://registry.npmjs.org/@types/debounce/-/debounce-1.2.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1259:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1262:        "node_modules/@types/estree": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1264:            "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1266:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1269:        "node_modules/@types/express": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1271:            "resolved": "https://registry.npmjs.org/@types/express/-/express-5.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1273:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1277:                "@types/express-serve-static-core": "^5.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1278:                "@types/serve-static": "^2"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1281:        "node_modules/@types/express-serve-static-core": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1283:            "resolved": "https://registry.npmjs.org/@types/express-serve-static-core/-/express-serve-static-core-5.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1285:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1288:                "@types/node": "*",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1294:        "node_modules/@types/http-assert": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1296:            "resolved": "https://registry.npmjs.org/@types/http-assert/-/http-assert-1.5.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1298:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1301:        "node_modules/@types/http-errors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1303:            "resolved": "https://registry.npmjs.org/@types/http-errors/-/http-errors-2.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1305:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1308:        "node_modules/@types/istanbul-lib-coverage": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1310:            "resolved": "https://registry.npmjs.org/@types/istanbul-lib-coverage/-/istanbul-lib-coverage-2.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1312:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1315:        "node_modules/@types/istanbul-lib-report": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1317:            "resolved": "https://registry.npmjs.org/@types/istanbul-lib-report/-/istanbul-lib-report-3.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1319:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1325:        "node_modules/@types/istanbul-reports": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1327:            "resolved": "https://registry.npmjs.org/@types/istanbul-reports/-/istanbul-reports-3.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1329:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1335:        "node_modules/@types/keygrip": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1337:            "resolved": "https://registry.npmjs.org/@types/keygrip/-/keygrip-1.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1339:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1342:        "node_modules/@types/koa": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1344:            "resolved": "https://registry.npmjs.org/@types/koa/-/koa-2.15.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1346:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1356:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1359:        "node_modules/@types/koa-compose": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1361:            "resolved": "https://registry.npmjs.org/@types/koa-compose/-/koa-compose-3.2.9.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1363:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1369:        "node_modules/@types/mocha": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1371:            "resolved": "https://registry.npmjs.org/@types/mocha/-/mocha-10.0.10.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1373:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1376:        "node_modules/@types/node": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1378:            "resolved": "https://registry.npmjs.org/@types/node/-/node-24.10.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1380:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1386:        "node_modules/@types/parse5": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1388:            "resolved": "https://registry.npmjs.org/@types/parse5/-/parse5-6.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1390:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1393:        "node_modules/@types/qs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1395:            "resolved": "https://registry.npmjs.org/@types/qs/-/qs-6.14.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1397:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1400:        "node_modules/@types/range-parser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1402:            "resolved": "https://registry.npmjs.org/@types/range-parser/-/range-parser-1.2.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1404:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1407:        "node_modules/@types/resolve": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1409:            "resolved": "https://registry.npmjs.org/@types/resolve/-/resolve-1.20.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1411:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1414:        "node_modules/@types/send": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1416:            "resolved": "https://registry.npmjs.org/@types/send/-/send-1.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1418:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1421:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1424:        "node_modules/@types/serve-static": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1426:            "resolved": "https://registry.npmjs.org/@types/serve-static/-/serve-static-2.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1428:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1432:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1435:        "node_modules/@types/ws": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1437:            "resolved": "https://registry.npmjs.org/@types/ws/-/ws-7.4.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1439:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1442:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1445:        "node_modules/@types/yauzl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1447:            "resolved": "https://registry.npmjs.org/@types/yauzl/-/yauzl-2.10.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1449:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1453:                "@types/node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1456:        "node_modules/@typescript-eslint/eslint-plugin": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1458:            "resolved": "https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1460:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1463:                "@eslint-community/regexpp": "^4.10.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1464:                "@typescript-eslint/scope-manager": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1465:                "@typescript-eslint/type-utils": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1466:                "@typescript-eslint/utils": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1467:                "@typescript-eslint/visitor-keys": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1473:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1477:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1480:                "@typescript-eslint/parser": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1481:                "eslint": "^8.57.0 || ^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1485:        "node_modules/@typescript-eslint/eslint-plugin/node_modules/ignore": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1487:            "resolved": "https://registry.npmjs.org/ignore/-/ignore-7.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1489:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1492:                "node": ">= 4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1495:        "node_modules/@typescript-eslint/parser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1497:            "resolved": "https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1499:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1502:                "@typescript-eslint/scope-manager": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1503:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1504:                "@typescript-eslint/typescript-estree": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1505:                "@typescript-eslint/visitor-keys": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1509:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1513:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1516:                "eslint": "^8.57.0 || ^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1520:        "node_modules/@typescript-eslint/project-service": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1522:            "resolved": "https://registry.npmjs.org/@typescript-eslint/project-service/-/project-service-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1524:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1527:                "@typescript-eslint/tsconfig-utils": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1528:                "@typescript-eslint/types": "^8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1532:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1536:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1542:        "node_modules/@typescript-eslint/scope-manager": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1544:            "resolved": "https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1546:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1549:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1550:                "@typescript-eslint/visitor-keys": "8.49.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1553:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1557:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1560:        "node_modules/@typescript-eslint/tsconfig-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1562:            "resolved": "https://registry.npmjs.org/@typescript-eslint/tsconfig-utils/-/tsconfig-utils-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1564:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1567:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1571:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1577:        "node_modules/@typescript-eslint/type-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1579:            "resolved": "https://registry.npmjs.org/@typescript-eslint/type-utils/-/type-utils-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1581:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1584:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1585:                "@typescript-eslint/typescript-estree": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1586:                "@typescript-eslint/utils": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1591:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1595:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1598:                "eslint": "^8.57.0 || ^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1602:        "node_modules/@typescript-eslint/types": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1604:            "resolved": "https://registry.npmjs.org/@typescript-eslint/types/-/types-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1606:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1609:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1613:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1616:        "node_modules/@typescript-eslint/typescript-estree": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1618:            "resolved": "https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1620:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1623:                "@typescript-eslint/project-service": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1624:                "@typescript-eslint/tsconfig-utils": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1625:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1626:                "@typescript-eslint/visitor-keys": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1634:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1638:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1644:        "node_modules/@typescript-eslint/utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1646:            "resolved": "https://registry.npmjs.org/@typescript-eslint/utils/-/utils-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1648:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1651:                "@eslint-community/eslint-utils": "^4.7.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1652:                "@typescript-eslint/scope-manager": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1653:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1654:                "@typescript-eslint/typescript-estree": "8.49.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1657:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1661:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1664:                "eslint": "^8.57.0 || ^9.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1668:        "node_modules/@typescript-eslint/visitor-keys": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1670:            "resolved": "https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-8.49.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1672:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1675:                "@typescript-eslint/types": "8.49.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1676:                "eslint-visitor-keys": "^4.2.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1679:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1683:                "url": "https://opencollective.com/typescript-eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1686:        "node_modules/@typescript-eslint/visitor-keys/node_modules/eslint-visitor-keys": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1688:            "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-4.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1690:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1693:                "node": "^18.18.0 || ^20.9.0 || >=21.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1696:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1699:        "node_modules/@ungap/structured-clone": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1701:            "resolved": "https://registry.npmjs.org/@ungap/structured-clone/-/structured-clone-1.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1703:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1706:        "node_modules/@web/browser-logs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1708:            "resolved": "https://registry.npmjs.org/@web/browser-logs/-/browser-logs-0.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1710:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1716:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1719:        "node_modules/@web/config-loader": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1721:            "resolved": "https://registry.npmjs.org/@web/config-loader/-/config-loader-0.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1723:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1726:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1729:        "node_modules/@web/dev-server": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1731:            "resolved": "https://registry.npmjs.org/@web/dev-server/-/dev-server-0.4.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1733:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1739:                "@web/dev-server-core": "^0.7.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1740:                "@web/dev-server-rollup": "^0.6.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1752:                "wds": "dist/bin.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1753:                "web-dev-server": "dist/bin.js"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1756:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1759:        "node_modules/@web/dev-server-core": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1761:            "resolved": "https://registry.npmjs.org/@web/dev-server-core/-/dev-server-core-0.7.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1763:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1786:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1789:        "node_modules/@web/dev-server-esbuild": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1791:            "resolved": "https://registry.npmjs.org/@web/dev-server-esbuild/-/dev-server-esbuild-1.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1793:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1796:                "@mdn/browser-compat-data": "^4.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1797:                "@web/dev-server-core": "^0.7.4",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1798:                "esbuild": "^0.25.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1803:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1806:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/aix-ppc64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1808:            "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1813:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1820:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1823:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/android-arm": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1825:            "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1830:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1837:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1840:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/android-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1842:            "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1847:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1854:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1857:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/android-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1859:            "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1864:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1871:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1874:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/darwin-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1876:            "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1881:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1888:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1891:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/darwin-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1893:            "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1898:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1905:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1908:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/freebsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1910:            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1915:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1922:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1925:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/freebsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1927:            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1932:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1939:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1942:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-arm": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1944:            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1949:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1956:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1959:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1961:            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1966:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1973:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1976:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-ia32": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1978:            "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1983:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1990:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1993:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-loong64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:1995:            "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2000:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2007:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2010:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-mips64el": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2012:            "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2017:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2024:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2027:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-ppc64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2029:            "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2034:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2041:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2044:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-riscv64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2046:            "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2051:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2058:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2061:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-s390x": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2063:            "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2068:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2075:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2078:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/linux-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2080:            "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2085:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2092:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2095:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/netbsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2097:            "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2102:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2109:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2112:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/openbsd-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2114:            "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2119:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2126:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2129:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/sunos-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2131:            "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2136:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2143:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2146:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/win32-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2148:            "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2153:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2160:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2163:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/win32-ia32": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2165:            "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2170:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2177:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2180:        "node_modules/@web/dev-server-esbuild/node_modules/@esbuild/win32-x64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2182:            "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2187:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2194:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2197:        "node_modules/@web/dev-server-esbuild/node_modules/esbuild": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2199:            "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.25.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2201:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2205:                "esbuild": "bin/esbuild"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2208:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2211:                "@esbuild/aix-ppc64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2212:                "@esbuild/android-arm": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2213:                "@esbuild/android-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2214:                "@esbuild/android-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2215:                "@esbuild/darwin-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2216:                "@esbuild/darwin-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2217:                "@esbuild/freebsd-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2218:                "@esbuild/freebsd-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2219:                "@esbuild/linux-arm": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2220:                "@esbuild/linux-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2221:                "@esbuild/linux-ia32": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2222:                "@esbuild/linux-loong64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2223:                "@esbuild/linux-mips64el": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2224:                "@esbuild/linux-ppc64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2225:                "@esbuild/linux-riscv64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2226:                "@esbuild/linux-s390x": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2227:                "@esbuild/linux-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2228:                "@esbuild/netbsd-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2229:                "@esbuild/netbsd-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2230:                "@esbuild/openbsd-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2231:                "@esbuild/openbsd-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2232:                "@esbuild/openharmony-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2233:                "@esbuild/sunos-x64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2234:                "@esbuild/win32-arm64": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2235:                "@esbuild/win32-ia32": "0.25.12",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2236:                "@esbuild/win32-x64": "0.25.12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2239:        "node_modules/@web/dev-server-rollup": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2241:            "resolved": "https://registry.npmjs.org/@web/dev-server-rollup/-/dev-server-rollup-0.6.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2243:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2246:                "@rollup/plugin-node-resolve": "^15.0.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2247:                "@web/dev-server-core": "^0.7.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2254:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2257:        "node_modules/@web/parse5-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2259:            "resolved": "https://registry.npmjs.org/@web/parse5-utils/-/parse5-utils-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2261:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2268:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2271:        "node_modules/@web/test-runner": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2273:            "resolved": "https://registry.npmjs.org/@web/test-runner/-/test-runner-0.20.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2275:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2278:                "@web/browser-logs": "^0.4.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2280:                "@web/dev-server": "^0.4.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2281:                "@web/test-runner-chrome": "^0.18.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2282:                "@web/test-runner-commands": "^0.9.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2283:                "@web/test-runner-core": "^0.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2284:                "@web/test-runner-mocha": "^0.9.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2296:                "web-test-runner": "dist/bin.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2297:                "wtr": "dist/bin.js"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2300:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2303:        "node_modules/@web/test-runner-chrome": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2305:            "resolved": "https://registry.npmjs.org/@web/test-runner-chrome/-/test-runner-chrome-0.18.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2307:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2310:                "@web/test-runner-core": "^0.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2311:                "@web/test-runner-coverage-v8": "^0.8.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2316:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2319:        "node_modules/@web/test-runner-commands": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2321:            "resolved": "https://registry.npmjs.org/@web/test-runner-commands/-/test-runner-commands-0.9.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2323:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2326:                "@web/test-runner-core": "^0.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2330:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2333:        "node_modules/@web/test-runner-core": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2335:            "resolved": "https://registry.npmjs.org/@web/test-runner-core/-/test-runner-core-0.13.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2337:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2347:                "@web/browser-logs": "^0.4.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2348:                "@web/dev-server-core": "^0.7.3",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2368:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2371:        "node_modules/@web/test-runner-coverage-v8": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2373:            "resolved": "https://registry.npmjs.org/@web/test-runner-coverage-v8/-/test-runner-coverage-v8-0.8.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2375:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2378:                "@web/test-runner-core": "^0.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2385:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2388:        "node_modules/@web/test-runner-mocha": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2390:            "resolved": "https://registry.npmjs.org/@web/test-runner-mocha/-/test-runner-mocha-0.9.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2392:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2395:                "@web/test-runner-core": "^0.13.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2398:                "node": ">=18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2401:        "node_modules/accepts": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2403:            "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2405:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2412:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2415:        "node_modules/acorn": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2417:            "resolved": "https://registry.npmjs.org/acorn/-/acorn-8.15.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2419:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2425:                "node": ">=0.4.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2428:        "node_modules/acorn-jsx": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2430:            "resolved": "https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2432:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2438:        "node_modules/agent-base": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2440:            "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-7.1.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2442:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2445:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2448:        "node_modules/ajv": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2450:            "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2452:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2465:        "node_modules/ansi-escapes": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2467:            "resolved": "https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2469:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2475:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2481:        "node_modules/ansi-escapes/node_modules/type-fest": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2483:            "resolved": "https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2485:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2488:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2494:        "node_modules/ansi-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2496:            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2498:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2501:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2504:        "node_modules/ansi-styles": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2506:            "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2508:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2514:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2520:        "node_modules/anymatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2522:            "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2524:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2531:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2534:        "node_modules/argparse": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2536:            "resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2538:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2541:        "node_modules/array-back": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2543:            "resolved": "https://registry.npmjs.org/array-back/-/array-back-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2545:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2548:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2551:        "node_modules/array-union": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2553:            "resolved": "https://registry.npmjs.org/array-union/-/array-union-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2555:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2558:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2561:        "node_modules/ast-types": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2563:            "resolved": "https://registry.npmjs.org/ast-types/-/ast-types-0.13.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2565:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2571:                "node": ">=4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2574:        "node_modules/astral-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2576:            "resolved": "https://registry.npmjs.org/astral-regex/-/astral-regex-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2578:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2581:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2584:        "node_modules/async": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2586:            "resolved": "https://registry.npmjs.org/async/-/async-3.2.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2588:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2591:        "node_modules/b4a": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2593:            "resolved": "https://registry.npmjs.org/b4a/-/b4a-1.7.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2595:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2606:        "node_modules/balanced-match": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2608:            "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2610:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2613:        "node_modules/bare-events": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2615:            "resolved": "https://registry.npmjs.org/bare-events/-/bare-events-2.8.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2617:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2628:        "node_modules/bare-fs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2630:            "resolved": "https://registry.npmjs.org/bare-fs/-/bare-fs-4.5.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2632:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2654:        "node_modules/bare-os": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2656:            "resolved": "https://registry.npmjs.org/bare-os/-/bare-os-3.6.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2658:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2665:        "node_modules/bare-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2667:            "resolved": "https://registry.npmjs.org/bare-path/-/bare-path-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2669:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2676:        "node_modules/bare-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2678:            "resolved": "https://registry.npmjs.org/bare-stream/-/bare-stream-2.7.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2680:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2699:        "node_modules/bare-url": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2701:            "resolved": "https://registry.npmjs.org/bare-url/-/bare-url-2.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2703:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2710:        "node_modules/basic-ftp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2712:            "resolved": "https://registry.npmjs.org/basic-ftp/-/basic-ftp-5.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2714:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2717:                "node": ">=10.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2720:        "node_modules/binary-extensions": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2722:            "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2724:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2727:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2733:        "node_modules/boolbase": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2735:            "resolved": "https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2737:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2740:        "node_modules/brace-expansion": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2742:            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2744:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2750:        "node_modules/braces": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2752:            "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2754:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2760:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2763:        "node_modules/buffer-crc32": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2765:            "resolved": "https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2767:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2770:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2773:        "node_modules/buffer-from": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2775:            "resolved": "https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2777:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2780:        "node_modules/bytes": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2782:            "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2784:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2787:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2790:        "node_modules/cache-content-type": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2792:            "resolved": "https://registry.npmjs.org/cache-content-type/-/cache-content-type-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2794:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2801:                "node": ">= 6.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2804:        "node_modules/call-bind-apply-helpers": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2806:            "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2808:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2815:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2818:        "node_modules/call-bound": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2820:            "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2822:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2829:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2835:        "node_modules/callsites": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2837:            "resolved": "https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2839:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2842:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2845:        "node_modules/camel-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2847:            "resolved": "https://registry.npmjs.org/camel-case/-/camel-case-4.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2849:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2856:        "node_modules/camelcase": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2858:            "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-6.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2860:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2863:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2869:        "node_modules/chai": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2871:            "resolved": "https://registry.npmjs.org/chai/-/chai-6.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2873:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2876:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2879:        "node_modules/chalk": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2881:            "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2883:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2890:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2896:        "node_modules/chalk-template": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2898:            "resolved": "https://registry.npmjs.org/chalk-template/-/chalk-template-0.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2900:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2906:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2912:        "node_modules/cheerio": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2914:            "resolved": "https://registry.npmjs.org/cheerio/-/cheerio-1.0.0-rc.10.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2916:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2928:                "node": ">= 6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2934:        "node_modules/cheerio-select": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2936:            "resolved": "https://registry.npmjs.org/cheerio-select/-/cheerio-select-1.6.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2938:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2951:        "node_modules/chokidar": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2953:            "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-4.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2955:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2961:                "node": ">= 14.16.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2967:        "node_modules/chrome-launcher": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2969:            "resolved": "https://registry.npmjs.org/chrome-launcher/-/chrome-launcher-0.15.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2971:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2974:                "@types/node": "*",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2983:                "node": ">=12.13.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2986:        "node_modules/chromium-bidi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2988:            "resolved": "https://registry.npmjs.org/chromium-bidi/-/chromium-bidi-11.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2990:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:2997:                "devtools-protocol": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3000:        "node_modules/clean-css": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3002:            "resolved": "https://registry.npmjs.org/clean-css/-/clean-css-5.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3004:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3010:                "node": ">= 10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3013:        "node_modules/clean-css/node_modules/source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3015:            "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3017:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3020:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3023:        "node_modules/cli-cursor": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3025:            "resolved": "https://registry.npmjs.org/cli-cursor/-/cli-cursor-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3027:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3033:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3036:        "node_modules/cliui": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3038:            "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3040:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3048:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3051:        "node_modules/cliui/node_modules/wrap-ansi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3053:            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3055:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3063:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3069:        "node_modules/clone": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3071:            "resolved": "https://registry.npmjs.org/clone/-/clone-2.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3073:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3076:                "node": ">=0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3079:        "node_modules/co": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3081:            "resolved": "https://registry.npmjs.org/co/-/co-4.6.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3083:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3087:                "node": ">= 0.12.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3090:        "node_modules/co-body": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3092:            "resolved": "https://registry.npmjs.org/co-body/-/co-body-6.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3094:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3104:                "node": ">=8.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3107:        "node_modules/color-convert": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3109:            "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3111:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3117:                "node": ">=7.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3120:        "node_modules/color-name": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3122:            "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3124:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3127:        "node_modules/command-line-args": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3129:            "resolved": "https://registry.npmjs.org/command-line-args/-/command-line-args-5.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3131:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3140:                "node": ">=4.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3143:        "node_modules/command-line-usage": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3145:            "resolved": "https://registry.npmjs.org/command-line-usage/-/command-line-usage-7.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3147:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3156:                "node": ">=12.20.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3159:        "node_modules/command-line-usage/node_modules/array-back": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3161:            "resolved": "https://registry.npmjs.org/array-back/-/array-back-6.2.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3163:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3166:                "node": ">=12.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3169:        "node_modules/command-line-usage/node_modules/typical": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3171:            "resolved": "https://registry.npmjs.org/typical/-/typical-7.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3173:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3176:                "node": ">=12.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3179:        "node_modules/commander": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3181:            "resolved": "https://registry.npmjs.org/commander/-/commander-10.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3183:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3186:                "node": ">=14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3189:        "node_modules/concat-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3191:            "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3193:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3196:        "node_modules/content-disposition": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3198:            "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3200:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3206:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3209:        "node_modules/content-type": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3211:            "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3213:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3216:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3219:        "node_modules/convert-source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3221:            "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3223:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3226:        "node_modules/cookies": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3228:            "resolved": "https://registry.npmjs.org/cookies/-/cookies-0.9.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3230:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3237:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3240:        "node_modules/cross-spawn": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3242:            "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3244:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3252:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3255:        "node_modules/css-select": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3257:            "resolved": "https://registry.npmjs.org/css-select/-/css-select-4.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3259:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3272:        "node_modules/css-what": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3274:            "resolved": "https://registry.npmjs.org/css-what/-/css-what-6.2.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3276:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3279:                "node": ">= 6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3285:        "node_modules/data-uri-to-buffer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3287:            "resolved": "https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-6.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3289:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3292:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3295:        "node_modules/debounce": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3297:            "resolved": "https://registry.npmjs.org/debounce/-/debounce-1.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3299:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3302:        "node_modules/debug": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3304:            "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3306:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3312:                "node": ">=6.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3320:        "node_modules/deep-equal": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3322:            "resolved": "https://registry.npmjs.org/deep-equal/-/deep-equal-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3324:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3327:        "node_modules/deep-is": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3329:            "resolved": "https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3331:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3334:        "node_modules/deepmerge": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3336:            "resolved": "https://registry.npmjs.org/deepmerge/-/deepmerge-4.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3338:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3341:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3344:        "node_modules/default-gateway": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3346:            "resolved": "https://registry.npmjs.org/default-gateway/-/default-gateway-6.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3348:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3354:                "node": ">= 10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3357:        "node_modules/define-lazy-prop": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3359:            "resolved": "https://registry.npmjs.org/define-lazy-prop/-/define-lazy-prop-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3361:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3364:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3367:        "node_modules/degenerator": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3369:            "resolved": "https://registry.npmjs.org/degenerator/-/degenerator-5.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3371:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3379:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3382:        "node_modules/delegates": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3384:            "resolved": "https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3386:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3389:        "node_modules/depd": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3391:            "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3393:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3396:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3399:        "node_modules/dependency-graph": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3401:            "resolved": "https://registry.npmjs.org/dependency-graph/-/dependency-graph-0.11.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3403:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3406:                "node": ">= 0.6.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3409:        "node_modules/destroy": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3411:            "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3413:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3416:                "node": ">= 0.8",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3417:                "npm": "1.2.8000 || >= 1.4.16"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3420:        "node_modules/devtools-protocol": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3422:            "resolved": "https://registry.npmjs.org/devtools-protocol/-/devtools-protocol-0.0.1534754.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3424:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3427:        "node_modules/diff": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3429:            "resolved": "https://registry.npmjs.org/diff/-/diff-5.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3430:            "integrity": "sha512-uIFDxqpRZGZ6ThOk84hEfqWoHx2devRFvpTZcTHur85vImfaxUbTW9Ryh4CpCuDnToOP1CEtXKIgytHBPVff5A==",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3431:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3434:                "node": ">=0.3.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3437:        "node_modules/dir-glob": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3439:            "resolved": "https://registry.npmjs.org/dir-glob/-/dir-glob-3.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3441:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3447:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3450:        "node_modules/doctrine": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3452:            "resolved": "https://registry.npmjs.org/doctrine/-/doctrine-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3454:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3460:                "node": ">=6.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3463:        "node_modules/dom-serializer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3465:            "resolved": "https://registry.npmjs.org/dom-serializer/-/dom-serializer-1.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3467:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3478:        "node_modules/dom-serializer/node_modules/entities": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3480:            "resolved": "https://registry.npmjs.org/entities/-/entities-2.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3482:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3488:        "node_modules/domelementtype": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3490:            "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-2.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3492:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3501:        "node_modules/domhandler": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3503:            "resolved": "https://registry.npmjs.org/domhandler/-/domhandler-4.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3505:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3511:                "node": ">= 4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3517:        "node_modules/domutils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3519:            "resolved": "https://registry.npmjs.org/domutils/-/domutils-2.8.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3521:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3532:        "node_modules/dot-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3534:            "resolved": "https://registry.npmjs.org/dot-case/-/dot-case-3.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3536:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3543:        "node_modules/dunder-proto": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3545:            "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3547:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3555:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3558:        "node_modules/ee-first": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3560:            "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3562:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3565:        "node_modules/emoji-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3567:            "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3569:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3572:        "node_modules/encodeurl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3574:            "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3576:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3579:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3582:        "node_modules/end-of-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3584:            "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3586:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3592:        "node_modules/entities": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3594:            "resolved": "https://registry.npmjs.org/entities/-/entities-4.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3596:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3599:                "node": ">=0.12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3605:        "node_modules/errorstacks": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3607:            "resolved": "https://registry.npmjs.org/errorstacks/-/errorstacks-2.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3609:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3612:        "node_modules/es-define-property": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3614:            "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3616:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3619:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3622:        "node_modules/es-errors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3624:            "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3626:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3629:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3632:        "node_modules/es-module-lexer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3634:            "resolved": "https://registry.npmjs.org/es-module-lexer/-/es-module-lexer-1.7.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3636:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3639:        "node_modules/es-object-atoms": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3641:            "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3643:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3649:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3652:        "node_modules/esbuild": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3654:            "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3656:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3660:                "esbuild": "bin/esbuild"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3663:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3666:                "@esbuild/aix-ppc64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3667:                "@esbuild/android-arm": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3668:                "@esbuild/android-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3669:                "@esbuild/android-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3670:                "@esbuild/darwin-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3671:                "@esbuild/darwin-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3672:                "@esbuild/freebsd-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3673:                "@esbuild/freebsd-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3674:                "@esbuild/linux-arm": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3675:                "@esbuild/linux-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3676:                "@esbuild/linux-ia32": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3677:                "@esbuild/linux-loong64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3678:                "@esbuild/linux-mips64el": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3679:                "@esbuild/linux-ppc64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3680:                "@esbuild/linux-riscv64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3681:                "@esbuild/linux-s390x": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3682:                "@esbuild/linux-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3683:                "@esbuild/netbsd-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3684:                "@esbuild/netbsd-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3685:                "@esbuild/openbsd-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3686:                "@esbuild/openbsd-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3687:                "@esbuild/openharmony-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3688:                "@esbuild/sunos-x64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3689:                "@esbuild/win32-arm64": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3690:                "@esbuild/win32-ia32": "0.27.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3691:                "@esbuild/win32-x64": "0.27.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3694:        "node_modules/esbuild-plugin-copy": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3696:            "resolved": "https://registry.npmjs.org/esbuild-plugin-copy/-/esbuild-plugin-copy-2.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3698:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3707:                "esbuild": ">= 0.14.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3710:        "node_modules/esbuild-plugin-copy/node_modules/chokidar": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3712:            "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3714:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3726:                "node": ">= 8.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3735:        "node_modules/esbuild-plugin-copy/node_modules/glob-parent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3737:            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3739:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3745:                "node": ">= 6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3748:        "node_modules/esbuild-plugin-copy/node_modules/readdirp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3750:            "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3752:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3758:                "node": ">=8.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3761:        "node_modules/esbuild/node_modules/@esbuild/netbsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3763:            "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3768:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3775:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3778:        "node_modules/esbuild/node_modules/@esbuild/openbsd-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3780:            "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3785:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3792:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3795:        "node_modules/esbuild/node_modules/@esbuild/openharmony-arm64": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3797:            "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3802:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3809:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3812:        "node_modules/escalade": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3814:            "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3816:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3819:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3822:        "node_modules/escape-html": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3824:            "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3826:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3829:        "node_modules/escape-string-regexp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3831:            "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3833:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3836:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3842:        "node_modules/escodegen": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3844:            "resolved": "https://registry.npmjs.org/escodegen/-/escodegen-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3846:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3858:                "node": ">=6.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3864:        "node_modules/escodegen/node_modules/source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3866:            "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3868:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3872:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3875:        "node_modules/eslint": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3877:            "resolved": "https://registry.npmjs.org/eslint/-/eslint-8.57.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3879:            "deprecated": "This version is no longer supported. Please see https://eslint.org/version-support for other options.",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3880:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3883:                "@eslint-community/eslint-utils": "^4.2.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3884:                "@eslint-community/regexpp": "^4.6.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3885:                "@eslint/eslintrc": "^2.1.4",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3886:                "@eslint/js": "8.57.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3889:                "@nodelib/fs.walk": "^1.2.8",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3897:                "eslint-scope": "^7.2.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3898:                "eslint-visitor-keys": "^3.4.3",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3923:                "eslint": "bin/eslint.js"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3926:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3929:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3932:        "node_modules/eslint-config-prettier": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3934:            "resolved": "https://registry.npmjs.org/eslint-config-prettier/-/eslint-config-prettier-9.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3936:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3939:                "eslint-config-prettier": "bin/cli.js"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3942:                "eslint": ">=7.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3945:        "node_modules/eslint-plugin-mocha": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3947:            "resolved": "https://registry.npmjs.org/eslint-plugin-mocha/-/eslint-plugin-mocha-10.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3949:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3952:                "eslint-utils": "^3.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3957:                "node": ">=14.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3960:                "eslint": ">=7.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3963:        "node_modules/eslint-scope": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3965:            "resolved": "https://registry.npmjs.org/eslint-scope/-/eslint-scope-7.2.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3967:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3974:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3977:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3980:        "node_modules/eslint-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3982:            "resolved": "https://registry.npmjs.org/eslint-utils/-/eslint-utils-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3984:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3987:                "eslint-visitor-keys": "^2.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3990:                "node": "^10.0.0 || ^12.0.0 || >= 14.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3996:                "eslint": ">=5"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:3999:        "node_modules/eslint-utils/node_modules/eslint-visitor-keys": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4001:            "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4003:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4006:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4009:        "node_modules/eslint-visitor-keys": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4011:            "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4013:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4016:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4019:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4022:        "node_modules/eslint/node_modules/brace-expansion": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4024:            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4026:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4033:        "node_modules/eslint/node_modules/minimatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4035:            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4037:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4043:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4046:        "node_modules/espree": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4048:            "resolved": "https://registry.npmjs.org/espree/-/espree-9.6.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4050:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4055:                "eslint-visitor-keys": "^3.4.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4058:                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4061:                "url": "https://opencollective.com/eslint"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4064:        "node_modules/esprima": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4066:            "resolved": "https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4068:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4075:                "node": ">=4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4078:        "node_modules/esquery": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4080:            "resolved": "https://registry.npmjs.org/esquery/-/esquery-1.6.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4082:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4088:                "node": ">=0.10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4091:        "node_modules/esrecurse": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4093:            "resolved": "https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4095:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4101:                "node": ">=4.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4104:        "node_modules/estraverse": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4106:            "resolved": "https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4108:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4111:                "node": ">=4.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4114:        "node_modules/estree-walker": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4116:            "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4118:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4121:        "node_modules/esutils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4123:            "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4125:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4128:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4131:        "node_modules/etag": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4133:            "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4135:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4138:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4141:        "node_modules/events-universal": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4143:            "resolved": "https://registry.npmjs.org/events-universal/-/events-universal-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4145:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4151:        "node_modules/execa": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4153:            "resolved": "https://registry.npmjs.org/execa/-/execa-5.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4155:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4163:                "npm-run-path": "^4.0.1",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4169:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4175:        "node_modules/extract-zip": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4177:            "resolved": "https://registry.npmjs.org/extract-zip/-/extract-zip-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4179:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4190:                "node": ">= 10.17.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4196:        "node_modules/extract-zip/node_modules/get-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4198:            "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4200:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4206:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4212:        "node_modules/fast-deep-equal": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4214:            "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4216:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4219:        "node_modules/fast-fifo": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4221:            "resolved": "https://registry.npmjs.org/fast-fifo/-/fast-fifo-1.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4223:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4226:        "node_modules/fast-glob": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4228:            "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4230:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4233:                "@nodelib/fs.stat": "^2.0.2",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4234:                "@nodelib/fs.walk": "^1.2.3",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4240:                "node": ">=8.6.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4243:        "node_modules/fast-glob/node_modules/glob-parent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4245:            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4247:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4253:                "node": ">= 6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4256:        "node_modules/fast-json-stable-stringify": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4258:            "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4260:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4263:        "node_modules/fast-levenshtein": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4265:            "resolved": "https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4267:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4270:        "node_modules/fastq": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4272:            "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4274:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4280:        "node_modules/fd-slicer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4282:            "resolved": "https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4284:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4290:        "node_modules/file-entry-cache": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4292:            "resolved": "https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-6.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4294:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4300:                "node": "^10.12.0 || >=12.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4303:        "node_modules/fill-range": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4305:            "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4307:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4313:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4316:        "node_modules/find-replace": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4318:            "resolved": "https://registry.npmjs.org/find-replace/-/find-replace-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4320:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4326:                "node": ">=4.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4329:        "node_modules/find-up": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4331:            "resolved": "https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4333:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4340:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4346:        "node_modules/flat-cache": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4348:            "resolved": "https://registry.npmjs.org/flat-cache/-/flat-cache-3.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4350:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4358:                "node": "^10.12.0 || >=12.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4361:        "node_modules/flatted": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4363:            "resolved": "https://registry.npmjs.org/flatted/-/flatted-3.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4365:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4368:        "node_modules/fresh": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4370:            "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4372:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4375:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4378:        "node_modules/fs-extra": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4380:            "resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-10.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4382:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4390:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4393:        "node_modules/fs.realpath": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4395:            "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4397:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4400:        "node_modules/fsevents": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4402:            "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4404:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4412:                "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4415:        "node_modules/function-bind": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4417:            "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4419:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4425:        "node_modules/generator-function": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4427:            "resolved": "https://registry.npmjs.org/generator-function/-/generator-function-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4429:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4432:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4435:        "node_modules/get-caller-file": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4437:            "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4439:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4442:                "node": "6.* || 8.* || >= 10.*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4445:        "node_modules/get-intrinsic": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4447:            "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4449:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4464:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4470:        "node_modules/get-proto": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4472:            "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4474:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4481:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4484:        "node_modules/get-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4486:            "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-6.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4488:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4491:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4497:        "node_modules/get-uri": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4499:            "resolved": "https://registry.npmjs.org/get-uri/-/get-uri-6.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4501:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4509:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4512:        "node_modules/glob": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4514:            "resolved": "https://registry.npmjs.org/glob/-/glob-7.2.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4517:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4528:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4534:        "node_modules/glob-parent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4536:            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4538:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4544:                "node": ">=10.13.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4547:        "node_modules/glob/node_modules/brace-expansion": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4549:            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4551:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4558:        "node_modules/glob/node_modules/minimatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4560:            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4562:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4568:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4571:        "node_modules/globals": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4573:            "resolved": "https://registry.npmjs.org/globals/-/globals-13.24.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4575:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4581:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4587:        "node_modules/globby": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4589:            "resolved": "https://registry.npmjs.org/globby/-/globby-11.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4591:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4602:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4608:        "node_modules/gopd": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4610:            "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4612:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4615:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4621:        "node_modules/graceful-fs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4623:            "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4625:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4628:        "node_modules/graphemer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4630:            "resolved": "https://registry.npmjs.org/graphemer/-/graphemer-1.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4632:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4635:        "node_modules/has-flag": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4637:            "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4639:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4642:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4645:        "node_modules/has-symbols": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4647:            "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4649:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4652:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4658:        "node_modules/has-tostringtag": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4660:            "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4662:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4668:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4674:        "node_modules/hasown": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4676:            "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4678:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4684:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4687:        "node_modules/html-escaper": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4689:            "resolved": "https://registry.npmjs.org/html-escaper/-/html-escaper-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4691:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4694:        "node_modules/html-minifier-terser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4696:            "resolved": "https://registry.npmjs.org/html-minifier-terser/-/html-minifier-terser-7.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4698:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4713:                "node": "^14.13.1 || >=16.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4716:        "node_modules/htmlparser2": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4718:            "resolved": "https://registry.npmjs.org/htmlparser2/-/htmlparser2-6.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4720:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4736:        "node_modules/htmlparser2/node_modules/entities": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4738:            "resolved": "https://registry.npmjs.org/entities/-/entities-2.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4740:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4746:        "node_modules/http-assert": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4748:            "resolved": "https://registry.npmjs.org/http-assert/-/http-assert-1.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4750:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4757:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4760:        "node_modules/http-errors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4762:            "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.8.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4764:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4774:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4777:        "node_modules/http-errors/node_modules/depd": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4779:            "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4781:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4784:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4787:        "node_modules/http-proxy-agent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4789:            "resolved": "https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-7.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4791:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4798:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4801:        "node_modules/https-proxy-agent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4803:            "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4805:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4812:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4815:        "node_modules/human-signals": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4817:            "resolved": "https://registry.npmjs.org/human-signals/-/human-signals-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4819:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4822:                "node": ">=10.17.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4825:        "node_modules/iconv-lite": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4827:            "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4829:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4835:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4838:        "node_modules/ignore": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4840:            "resolved": "https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4842:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4845:                "node": ">= 4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4848:        "node_modules/import-fresh": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4850:            "resolved": "https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4852:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4859:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4865:        "node_modules/imurmurhash": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4867:            "resolved": "https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4869:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4872:                "node": ">=0.8.19"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4875:        "node_modules/inflation": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4877:            "resolved": "https://registry.npmjs.org/inflation/-/inflation-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4879:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4882:                "node": ">= 0.8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4885:        "node_modules/inflight": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4887:            "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4889:            "deprecated": "This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4890:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4897:        "node_modules/inherits": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4899:            "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4901:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4904:        "node_modules/internal-ip": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4906:            "resolved": "https://registry.npmjs.org/internal-ip/-/internal-ip-6.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4908:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4917:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4923:        "node_modules/ip-address": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4925:            "resolved": "https://registry.npmjs.org/ip-address/-/ip-address-10.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4927:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4930:                "node": ">= 12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4933:        "node_modules/ip-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4935:            "resolved": "https://registry.npmjs.org/ip-regex/-/ip-regex-4.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4937:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4940:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4943:        "node_modules/ipaddr.js": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4945:            "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4947:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4950:                "node": ">= 0.10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4953:        "node_modules/is-binary-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4955:            "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4957:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4963:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4966:        "node_modules/is-core-module": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4968:            "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4970:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4976:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4982:        "node_modules/is-docker": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4984:            "resolved": "https://registry.npmjs.org/is-docker/-/is-docker-2.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4986:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4992:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:4998:        "node_modules/is-extglob": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5000:            "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5002:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5005:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5008:        "node_modules/is-fullwidth-code-point": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5010:            "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5012:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5015:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5018:        "node_modules/is-generator-function": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5020:            "resolved": "https://registry.npmjs.org/is-generator-function/-/is-generator-function-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5022:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5029:                "safe-regex-test": "^1.1.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5032:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5038:        "node_modules/is-glob": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5040:            "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5042:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5048:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5051:        "node_modules/is-ip": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5053:            "resolved": "https://registry.npmjs.org/is-ip/-/is-ip-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5055:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5061:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5064:        "node_modules/is-module": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5066:            "resolved": "https://registry.npmjs.org/is-module/-/is-module-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5068:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5071:        "node_modules/is-number": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5073:            "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5075:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5078:                "node": ">=0.12.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5081:        "node_modules/is-path-inside": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5083:            "resolved": "https://registry.npmjs.org/is-path-inside/-/is-path-inside-3.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5085:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5088:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5091:        "node_modules/is-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5093:            "resolved": "https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5095:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5104:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5110:        "node_modules/is-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5112:            "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5114:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5117:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5123:        "node_modules/is-wsl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5125:            "resolved": "https://registry.npmjs.org/is-wsl/-/is-wsl-2.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5127:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5133:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5136:        "node_modules/isbinaryfile": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5138:            "resolved": "https://registry.npmjs.org/isbinaryfile/-/isbinaryfile-5.0.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5140:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5143:                "node": ">= 18.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5149:        "node_modules/isexe": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5151:            "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5153:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5156:        "node_modules/istanbul-lib-coverage": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5158:            "resolved": "https://registry.npmjs.org/istanbul-lib-coverage/-/istanbul-lib-coverage-3.2.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5160:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5163:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5166:        "node_modules/istanbul-lib-report": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5168:            "resolved": "https://registry.npmjs.org/istanbul-lib-report/-/istanbul-lib-report-3.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5170:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5178:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5181:        "node_modules/istanbul-reports": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5183:            "resolved": "https://registry.npmjs.org/istanbul-reports/-/istanbul-reports-3.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5185:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5192:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5195:        "node_modules/js-tokens": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5197:            "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5199:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5202:        "node_modules/js-yaml": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5204:            "resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5206:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5215:        "node_modules/json-buffer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5217:            "resolved": "https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5219:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5222:        "node_modules/json-schema-traverse": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5224:            "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5226:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5229:        "node_modules/json-stable-stringify-without-jsonify": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5231:            "resolved": "https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5233:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5236:        "node_modules/jsonc-parser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5238:            "resolved": "https://registry.npmjs.org/jsonc-parser/-/jsonc-parser-1.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5240:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5243:        "node_modules/jsonfile": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5245:            "resolved": "https://registry.npmjs.org/jsonfile/-/jsonfile-6.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5247:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5256:        "node_modules/keygrip": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5258:            "resolved": "https://registry.npmjs.org/keygrip/-/keygrip-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5260:            "deprecated": "Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5261:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5267:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5270:        "node_modules/keyv": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5272:            "resolved": "https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5274:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5280:        "node_modules/koa": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5282:            "resolved": "https://registry.npmjs.org/koa/-/koa-2.16.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5284:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5312:                "node": "^4.8.4 || ^6.10.1 || ^7.10.1 || >= 8.1.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5315:        "node_modules/koa-compose": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5317:            "resolved": "https://registry.npmjs.org/koa-compose/-/koa-compose-4.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5319:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5322:        "node_modules/koa-convert": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5324:            "resolved": "https://registry.npmjs.org/koa-convert/-/koa-convert-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5326:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5333:                "node": ">= 10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5336:        "node_modules/koa-etag": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5338:            "resolved": "https://registry.npmjs.org/koa-etag/-/koa-etag-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5340:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5346:        "node_modules/koa-send": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5348:            "resolved": "https://registry.npmjs.org/koa-send/-/koa-send-5.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5350:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5358:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5361:        "node_modules/koa-static": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5363:            "resolved": "https://registry.npmjs.org/koa-static/-/koa-static-5.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5365:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5372:                "node": ">= 7.6.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5375:        "node_modules/koa-static/node_modules/debug": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5377:            "resolved": "https://registry.npmjs.org/debug/-/debug-3.2.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5379:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5385:        "node_modules/levn": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5387:            "resolved": "https://registry.npmjs.org/levn/-/levn-0.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5389:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5396:                "node": ">= 0.8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5399:        "node_modules/lighthouse-logger": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5401:            "resolved": "https://registry.npmjs.org/lighthouse-logger/-/lighthouse-logger-1.4.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5403:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5410:        "node_modules/lighthouse-logger/node_modules/debug": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5412:            "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5414:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5420:        "node_modules/lighthouse-logger/node_modules/ms": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5422:            "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5424:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5427:        "node_modules/locate-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5429:            "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5431:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5437:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5443:        "node_modules/lodash.camelcase": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5445:            "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5447:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5450:        "node_modules/lodash.merge": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5452:            "resolved": "https://registry.npmjs.org/lodash.merge/-/lodash.merge-4.6.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5454:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5457:        "node_modules/log-update": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5459:            "resolved": "https://registry.npmjs.org/log-update/-/log-update-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5461:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5470:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5476:        "node_modules/lower-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5478:            "resolved": "https://registry.npmjs.org/lower-case/-/lower-case-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5480:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5486:        "node_modules/lru-cache": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5488:            "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-8.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5490:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5493:                "node": ">=16.14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5496:        "node_modules/make-dir": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5498:            "resolved": "https://registry.npmjs.org/make-dir/-/make-dir-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5500:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5506:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5512:        "node_modules/marky": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5514:            "resolved": "https://registry.npmjs.org/marky/-/marky-1.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5516:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5519:        "node_modules/math-intrinsics": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5521:            "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5523:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5526:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5529:        "node_modules/media-typer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5531:            "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5533:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5536:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5539:        "node_modules/merge-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5541:            "resolved": "https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5543:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5546:        "node_modules/merge2": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5548:            "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5550:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5553:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5556:        "node_modules/micromatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5558:            "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5560:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5567:                "node": ">=8.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5570:        "node_modules/mime-db": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5572:            "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5574:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5577:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5580:        "node_modules/mime-types": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5582:            "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5584:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5590:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5593:        "node_modules/mimic-fn": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5595:            "resolved": "https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5597:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5600:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5603:        "node_modules/minimatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5605:            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-9.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5607:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5613:                "node": ">=16 || 14 >=14.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5619:        "node_modules/mitt": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5621:            "resolved": "https://registry.npmjs.org/mitt/-/mitt-3.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5623:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5626:        "node_modules/mkdirp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5628:            "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5630:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5636:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5639:        "node_modules/ms": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5641:            "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5643:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5646:        "node_modules/nanocolors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5648:            "resolved": "https://registry.npmjs.org/nanocolors/-/nanocolors-0.2.13.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5650:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5653:        "node_modules/nanoid": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5655:            "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5657:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5669:                "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5672:        "node_modules/natural-compare": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5674:            "resolved": "https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5676:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5679:        "node_modules/negotiator": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5681:            "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5683:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5686:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5689:        "node_modules/netmask": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5691:            "resolved": "https://registry.npmjs.org/netmask/-/netmask-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5693:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5696:                "node": ">= 0.4.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5699:        "node_modules/no-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5701:            "resolved": "https://registry.npmjs.org/no-case/-/no-case-3.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5703:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5710:        "node_modules/normalize-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5712:            "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5714:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5717:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5720:        "node_modules/npm-run-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5722:            "resolved": "https://registry.npmjs.org/npm-run-path/-/npm-run-path-4.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5724:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5730:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5733:        "node_modules/nth-check": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5735:            "resolved": "https://registry.npmjs.org/nth-check/-/nth-check-2.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5737:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5746:        "node_modules/object-inspect": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5748:            "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5750:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5753:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5759:        "node_modules/on-finished": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5761:            "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5763:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5769:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5772:        "node_modules/once": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5774:            "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5776:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5782:        "node_modules/onetime": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5784:            "resolved": "https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5786:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5792:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5798:        "node_modules/only": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5800:            "resolved": "https://registry.npmjs.org/only/-/only-0.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5802:            "dev": true
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5804:        "node_modules/open": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5806:            "resolved": "https://registry.npmjs.org/open/-/open-8.4.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5808:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5816:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5822:        "node_modules/optionator": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5824:            "resolved": "https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5826:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5837:                "node": ">= 0.8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5840:        "node_modules/p-event": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5842:            "resolved": "https://registry.npmjs.org/p-event/-/p-event-4.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5844:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5850:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5856:        "node_modules/p-finally": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5858:            "resolved": "https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5860:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5863:                "node": ">=4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5866:        "node_modules/p-limit": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5868:            "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5869:            "integrity": "sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5870:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5876:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5882:        "node_modules/p-locate": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5884:            "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5886:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5892:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5898:        "node_modules/p-timeout": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5900:            "resolved": "https://registry.npmjs.org/p-timeout/-/p-timeout-3.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5902:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5908:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5911:        "node_modules/pac-proxy-agent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5913:            "resolved": "https://registry.npmjs.org/pac-proxy-agent/-/pac-proxy-agent-7.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5915:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5928:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5931:        "node_modules/pac-resolver": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5933:            "resolved": "https://registry.npmjs.org/pac-resolver/-/pac-resolver-7.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5935:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5942:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5945:        "node_modules/param-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5947:            "resolved": "https://registry.npmjs.org/param-case/-/param-case-3.0.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5949:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5956:        "node_modules/parent-module": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5958:            "resolved": "https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5960:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5966:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5969:        "node_modules/parse5": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5971:            "resolved": "https://registry.npmjs.org/parse5/-/parse5-6.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5973:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5976:        "node_modules/parse5-htmlparser2-tree-adapter": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5978:            "resolved": "https://registry.npmjs.org/parse5-htmlparser2-tree-adapter/-/parse5-htmlparser2-tree-adapter-6.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5980:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5986:        "node_modules/parseurl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5988:            "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5990:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5993:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5996:        "node_modules/pascal-case": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:5998:            "resolved": "https://registry.npmjs.org/pascal-case/-/pascal-case-3.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6000:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6007:        "node_modules/path-exists": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6009:            "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6011:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6014:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6017:        "node_modules/path-is-absolute": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6019:            "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6021:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6024:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6027:        "node_modules/path-key": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6029:            "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6031:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6034:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6037:        "node_modules/path-parse": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6039:            "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6041:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6044:        "node_modules/path-type": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6046:            "resolved": "https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6048:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6051:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6054:        "node_modules/pend": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6056:            "resolved": "https://registry.npmjs.org/pend/-/pend-1.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6058:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6061:        "node_modules/picocolors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6063:            "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6065:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6068:        "node_modules/picomatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6070:            "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6072:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6075:                "node": ">=8.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6081:        "node_modules/portfinder": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6083:            "resolved": "https://registry.npmjs.org/portfinder/-/portfinder-1.0.38.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6085:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6092:                "node": ">= 10.12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6095:        "node_modules/prelude-ls": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6097:            "resolved": "https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6099:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6102:                "node": ">= 0.8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6105:        "node_modules/prettier": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6107:            "resolved": "https://registry.npmjs.org/prettier/-/prettier-3.7.4.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6109:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6115:                "node": ">=14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6121:        "node_modules/progress": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6123:            "resolved": "https://registry.npmjs.org/progress/-/progress-2.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6125:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6128:                "node": ">=0.4.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6131:        "node_modules/proxy-agent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6133:            "resolved": "https://registry.npmjs.org/proxy-agent/-/proxy-agent-6.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6135:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6148:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6151:        "node_modules/proxy-agent/node_modules/lru-cache": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6153:            "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-7.18.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6155:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6158:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6161:        "node_modules/proxy-from-env": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6163:            "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6165:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6168:        "node_modules/pump": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6170:            "resolved": "https://registry.npmjs.org/pump/-/pump-3.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6172:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6179:        "node_modules/punycode": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6181:            "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6183:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6186:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6189:        "node_modules/puppeteer-core": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6191:            "resolved": "https://registry.npmjs.org/puppeteer-core/-/puppeteer-core-24.32.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6193:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6196:                "@puppeteer/browsers": "2.11.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6199:                "devtools-protocol": "0.0.1534754",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6205:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6208:        "node_modules/puppeteer-core/node_modules/ws": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6210:            "resolved": "https://registry.npmjs.org/ws/-/ws-8.18.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6212:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6215:                "node": ">=10.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6230:        "node_modules/qs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6232:            "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6234:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6240:                "node": ">=0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6246:        "node_modules/queue-microtask": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6248:            "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6250:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6267:        "node_modules/rambda": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6269:            "resolved": "https://registry.npmjs.org/rambda/-/rambda-7.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6271:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6274:        "node_modules/raw-body": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6276:            "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.5.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6278:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6287:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6290:        "node_modules/raw-body/node_modules/http-errors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6292:            "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6294:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6304:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6311:        "node_modules/raw-body/node_modules/statuses": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6313:            "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6315:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6318:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6321:        "node_modules/readdirp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6323:            "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-4.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6325:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6328:                "node": ">= 14.18.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6335:        "node_modules/relateurl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6337:            "resolved": "https://registry.npmjs.org/relateurl/-/relateurl-0.2.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6339:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6342:                "node": ">= 0.10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6345:        "node_modules/require-directory": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6347:            "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6349:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6352:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6355:        "node_modules/resolve": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6357:            "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.11.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6359:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6364:                "supports-preserve-symlinks-flag": "^1.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6370:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6376:        "node_modules/resolve-from": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6378:            "resolved": "https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6380:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6383:                "node": ">=4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6386:        "node_modules/resolve-path": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6388:            "resolved": "https://registry.npmjs.org/resolve-path/-/resolve-path-1.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6390:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6397:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6400:        "node_modules/resolve-path/node_modules/depd": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6402:            "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6404:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6407:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6410:        "node_modules/resolve-path/node_modules/http-errors": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6412:            "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.6.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6414:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6423:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6426:        "node_modules/resolve-path/node_modules/inherits": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6428:            "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6430:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6433:        "node_modules/resolve-path/node_modules/setprototypeof": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6435:            "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6437:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6440:        "node_modules/restore-cursor": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6442:            "resolved": "https://registry.npmjs.org/restore-cursor/-/restore-cursor-3.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6444:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6451:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6454:        "node_modules/reusify": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6456:            "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6458:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6462:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6465:        "node_modules/rimraf": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6467:            "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6470:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6482:        "node_modules/rollup": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6484:            "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.53.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6486:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6492:                "rollup": "dist/bin/rollup"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6495:                "node": ">=18.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6496:                "npm": ">=8.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6524:        "node_modules/run-parallel": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6526:            "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6528:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6548:        "node_modules/safe-buffer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6550:            "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6552:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6569:        "node_modules/safe-regex-test": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6571:            "resolved": "https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6573:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6581:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6587:        "node_modules/safer-buffer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6589:            "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6591:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6594:        "node_modules/semver": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6596:            "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6598:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6604:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6607:        "node_modules/setprototypeof": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6609:            "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6611:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6614:        "node_modules/shebang-command": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6616:            "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6618:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6624:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6627:        "node_modules/shebang-regex": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6629:            "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6631:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6634:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6637:        "node_modules/side-channel": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6639:            "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6641:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6651:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6657:        "node_modules/side-channel-list": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6659:            "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6661:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6668:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6674:        "node_modules/side-channel-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6676:            "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6678:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6687:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6693:        "node_modules/side-channel-weakmap": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6695:            "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6697:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6707:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6713:        "node_modules/signal-exit": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6715:            "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6717:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6720:        "node_modules/slash": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6722:            "resolved": "https://registry.npmjs.org/slash/-/slash-3.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6724:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6727:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6730:        "node_modules/slice-ansi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6732:            "resolved": "https://registry.npmjs.org/slice-ansi/-/slice-ansi-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6734:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6742:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6748:        "node_modules/smart-buffer": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6750:            "resolved": "https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6752:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6755:                "node": ">= 6.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6756:                "npm": ">= 3.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6759:        "node_modules/socks": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6761:            "resolved": "https://registry.npmjs.org/socks/-/socks-2.8.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6763:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6770:                "node": ">= 10.0.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6771:                "npm": ">= 3.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6774:        "node_modules/socks-proxy-agent": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6776:            "resolved": "https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-8.0.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6778:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6786:                "node": ">= 14"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6789:        "node_modules/source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6791:            "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.7.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6793:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6796:                "node": ">= 12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6799:        "node_modules/source-map-support": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6801:            "resolved": "https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.21.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6803:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6810:        "node_modules/source-map-support/node_modules/source-map": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6812:            "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6814:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6817:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6820:        "node_modules/statuses": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6822:            "resolved": "https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6824:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6827:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6830:        "node_modules/streamx": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6832:            "resolved": "https://registry.npmjs.org/streamx/-/streamx-2.23.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6834:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6842:        "node_modules/string-width": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6844:            "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6846:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6854:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6857:        "node_modules/strip-ansi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6859:            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6861:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6867:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6870:        "node_modules/strip-final-newline": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6872:            "resolved": "https://registry.npmjs.org/strip-final-newline/-/strip-final-newline-2.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6874:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6877:                "node": ">=6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6880:        "node_modules/strip-json-comments": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6882:            "resolved": "https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-3.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6884:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6887:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6893:        "node_modules/supports-color": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6895:            "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6897:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6903:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6906:        "node_modules/supports-preserve-symlinks-flag": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6908:            "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6910:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6913:                "node": ">= 0.4"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6919:        "node_modules/svgstore": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6921:            "resolved": "https://registry.npmjs.org/svgstore/-/svgstore-3.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6923:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6929:                "node": ">= 12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6932:        "node_modules/table-layout": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6934:            "resolved": "https://registry.npmjs.org/table-layout/-/table-layout-4.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6936:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6943:                "node": ">=12.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6946:        "node_modules/table-layout/node_modules/array-back": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6948:            "resolved": "https://registry.npmjs.org/array-back/-/array-back-6.2.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6950:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6953:                "node": ">=12.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6956:        "node_modules/tar-fs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6958:            "resolved": "https://registry.npmjs.org/tar-fs/-/tar-fs-3.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6960:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6971:        "node_modules/tar-stream": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6973:            "resolved": "https://registry.npmjs.org/tar-stream/-/tar-stream-3.1.7.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6975:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6983:        "node_modules/terser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6985:            "resolved": "https://registry.npmjs.org/terser/-/terser-5.44.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6987:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:6999:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7002:        "node_modules/terser/node_modules/commander": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7004:            "resolved": "https://registry.npmjs.org/commander/-/commander-2.20.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7006:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7009:        "node_modules/text-decoder": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7011:            "resolved": "https://registry.npmjs.org/text-decoder/-/text-decoder-1.2.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7013:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7019:        "node_modules/text-table": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7021:            "resolved": "https://registry.npmjs.org/text-table/-/text-table-0.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7023:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7026:        "node_modules/tinyglobby": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7028:            "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.15.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7030:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7037:                "node": ">=12.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7043:        "node_modules/tinyglobby/node_modules/fdir": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7045:            "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7047:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7050:                "node": ">=12.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7061:        "node_modules/tinyglobby/node_modules/picomatch": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7063:            "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7065:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7068:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7074:        "node_modules/to-regex-range": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7076:            "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7078:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7084:                "node": ">=8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7087:        "node_modules/toidentifier": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7089:            "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7091:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7094:                "node": ">=0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7097:        "node_modules/tr46": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7099:            "resolved": "https://registry.npmjs.org/tr46/-/tr46-5.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7101:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7107:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7110:        "node_modules/ts-api-utils": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7112:            "resolved": "https://registry.npmjs.org/ts-api-utils/-/ts-api-utils-2.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7114:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7117:                "node": ">=18.12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7123:        "node_modules/tslib": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7125:            "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7126:            "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7127:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7130:        "node_modules/tsscmp": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7132:            "resolved": "https://registry.npmjs.org/tsscmp/-/tsscmp-1.0.6.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7134:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7137:                "node": ">=0.6.x"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7140:        "node_modules/type-check": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7142:            "resolved": "https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7144:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7150:                "node": ">= 0.8.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7153:        "node_modules/type-fest": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7155:            "resolved": "https://registry.npmjs.org/type-fest/-/type-fest-0.20.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7157:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7160:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7166:        "node_modules/type-is": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7168:            "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7170:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7177:                "node": ">= 0.6"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7180:        "node_modules/typed-query-selector": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7182:            "resolved": "https://registry.npmjs.org/typed-query-selector/-/typed-query-selector-2.12.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7184:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7187:        "node_modules/typescript": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7189:            "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7191:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7195:                "tsserver": "bin/tsserver"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7198:                "node": ">=14.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7201:        "node_modules/typescript-lit-html-plugin": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7203:            "resolved": "https://registry.npmjs.org/typescript-lit-html-plugin/-/typescript-lit-html-plugin-0.9.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7205:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7211:                "vscode-languageserver-types": "^3.13.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7214:        "node_modules/typescript-styled-plugin": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7216:            "resolved": "https://registry.npmjs.org/typescript-styled-plugin/-/typescript-styled-plugin-0.13.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7219:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7225:                "vscode-languageserver-types": "^3.13.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7228:        "node_modules/typescript-template-language-service-decorator": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7230:            "resolved": "https://registry.npmjs.org/typescript-template-language-service-decorator/-/typescript-template-language-service-decorator-2.3.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7232:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7235:        "node_modules/typical": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7237:            "resolved": "https://registry.npmjs.org/typical/-/typical-4.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7239:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7242:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7245:        "node_modules/ua-parser-js": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7247:            "resolved": "https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-1.0.41.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7249:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7269:                "node": "*"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7272:        "node_modules/undici-types": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7274:            "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.16.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7276:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7279:        "node_modules/universalify": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7281:            "resolved": "https://registry.npmjs.org/universalify/-/universalify-2.0.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7283:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7286:                "node": ">= 10.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7289:        "node_modules/unpipe": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7291:            "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7293:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7296:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7299:        "node_modules/uri-js": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7301:            "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7303:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7309:        "node_modules/v8-to-istanbul": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7311:            "resolved": "https://registry.npmjs.org/v8-to-istanbul/-/v8-to-istanbul-9.3.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7313:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7321:                "node": ">=10.12.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7324:        "node_modules/vary": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7326:            "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7328:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7331:                "node": ">= 0.8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7334:        "node_modules/vscode-css-languageservice": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7336:            "resolved": "https://registry.npmjs.org/vscode-css-languageservice/-/vscode-css-languageservice-3.0.13.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7338:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7341:                "vscode-languageserver-types": "^3.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7345:        "node_modules/vscode-emmet-helper": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7347:            "resolved": "https://registry.npmjs.org/vscode-emmet-helper/-/vscode-emmet-helper-1.2.11.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7349:            "deprecated": "This package has been renamed to @vscode/emmet-helper, please update to the new name",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7350:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7355:                "vscode-languageserver-types": "^3.6.0-next.1"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7358:        "node_modules/vscode-html-languageservice": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7360:            "resolved": "https://registry.npmjs.org/vscode-html-languageservice/-/vscode-html-languageservice-2.1.12.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7362:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7365:                "vscode-languageserver-types": "^3.13.0",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7370:        "node_modules/vscode-languageserver-types": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7372:            "resolved": "https://registry.npmjs.org/vscode-languageserver-types/-/vscode-languageserver-types-3.17.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7374:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7377:        "node_modules/vscode-nls": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7379:            "resolved": "https://registry.npmjs.org/vscode-nls/-/vscode-nls-4.1.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7381:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7384:        "node_modules/vscode-uri": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7386:            "resolved": "https://registry.npmjs.org/vscode-uri/-/vscode-uri-1.0.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7388:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7391:        "node_modules/webdriver-bidi-protocol": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7393:            "resolved": "https://registry.npmjs.org/webdriver-bidi-protocol/-/webdriver-bidi-protocol-0.3.9.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7395:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7398:        "node_modules/webidl-conversions": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7400:            "resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-7.0.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7402:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7405:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7408:        "node_modules/whatwg-url": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7410:            "resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-14.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7412:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7419:                "node": ">=18"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7422:        "node_modules/which": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7424:            "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7426:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7432:                "node-which": "bin/node-which"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7435:                "node": ">= 8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7438:        "node_modules/word-wrap": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7440:            "resolved": "https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7442:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7445:                "node": ">=0.10.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7448:        "node_modules/wordwrapjs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7450:            "resolved": "https://registry.npmjs.org/wordwrapjs/-/wordwrapjs-5.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7452:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7455:                "node": ">=12.17"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7458:        "node_modules/wrap-ansi": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7460:            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-6.2.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7462:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7470:                "node": ">=8"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7473:        "node_modules/wrappy": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7475:            "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7477:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7480:        "node_modules/ws": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7482:            "resolved": "https://registry.npmjs.org/ws/-/ws-7.5.10.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7484:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7487:                "node": ">=8.3.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7502:        "node_modules/y18n": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7504:            "resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7506:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7509:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7512:        "node_modules/yargs": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7514:            "resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7516:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7528:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7531:        "node_modules/yargs-parser": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7533:            "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7535:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7538:                "node": ">=12"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7541:        "node_modules/yauzl": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7543:            "resolved": "https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7545:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7552:        "node_modules/ylru": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7554:            "resolved": "https://registry.npmjs.org/ylru/-/ylru-1.4.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7556:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7559:                "node": ">= 4.0.0"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7562:        "node_modules/yocto-queue": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7564:            "resolved": "https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7566:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7569:                "node": ">=10"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7575:        "node_modules/zod": {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7577:            "resolved": "https://registry.npmjs.org/zod/-/zod-3.25.76.tgz",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package-lock.json:7579:            "dev": true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:3:[KiCanvas] is an **interactive**, **browser-based** viewer for [KiCad] schematics and boards. You can try it out for yourself at https://kicanvas.org.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:9:You can also use KiCanvas on your own websites using the [embedding API]. It's written in modern vanilla [TypeScript] and uses the [Canvas] element and [WebGL] for rendering. You can learn more on the [development page][development documentation].
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:11:KiCanvas is developed by [Thea Flowers](https://thea.codes) with financial support from her [sponsors].
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:13:[KiCanvas]: https://kicanvas.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:14:[KiCad]: https://kicad.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:15:[file an issue]: https://github.com/theacodes/kicanvas/issues/new/choose
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:16:[embedding API]: https://kicanvas.org/embedding
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:17:[TypeScript]: https://typescript.dev
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:18:[Canvas]: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:19:[WebGL]: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:25:KiCanvas is very early in its development and there's a ton of stuff that hasn't been done, there's a [roadmap] that you can use to get an idea of the overall status of the project.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:27:[roadmap]: https://kicanvas.org/roadmap
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:33:- Any KiCad 5 files, KiCanvas can only parse files from KiCad 6 and later.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:34:- Some KiCad 7 features might not be fully implemented, such as custom fonts in schematics.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:35:- Browsers other than desktop Chrome, Firefox, and Safari may run into issues, as we aren't currently running automated tests against other browsers. We welcome issues related to browser compatibility, just make sure it hasn't already been reported.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:37:[GitHub issues]: https://github.com/theacodes/kicanvas/issues
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:43:[FAQ]: https://kicanvas.org/home/#faq
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:49:Contributions are welcome! However, since KiCanvas is in a super early stage please file an issue before you start working on something so we can coordinate. It's also recommended to take a moment and read over the [development documentation].
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\README.md:51:[development documentation]: https://kicanvas.org/development
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\CNAME:1:kicanvas.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\style.css:46:kicanvas-embed {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\style.css:56:kc-kicanvas-shell {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\tsconfig.json:19:        // "outDir": "./build", /* Specify an output folder for all emitted files. */
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\tsconfig.json:23:        // "preserveSymlinks": true,                         /* Disable resolving symlinks to their realpath. This correlates to the same flag in node. */
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\tsconfig.json:46:    "include": ["./src/**/*", "./test/**/*"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\tsconfig.json:47:    "exclude": ["./node_modules", "./**/node_modules/*", "./scripts/"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\mkdocs.yml:2:site_url: https://docs.kicanvas.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\mkdocs.yml:4:repo_url: "https://github.com/theacodes/kicanvas"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\mkdocs.yml:34:    - "Development": development.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\utilities.test.ts:10:suite("test.utilities", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\utilities.test.ts:11:    test(".assert_deep_partial()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\viewer.ts:18:import type { ProjectPage } from "../../kicanvas/project";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\styles\standalone.css:34:kc-kicanvas-shell {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:3:[KiCanvas] is an **interactive**, **browser-based** viewer for [KiCad] schematics and boards. You can try it out for yourself at [kicanvas.org](https://kicanvas.org).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:11:You can also use KiCanvas on your own websites using the [embedding API](embedding.md). It's written in modern vanilla [TypeScript] and uses the [Canvas] element and [WebGL] for rendering. You can learn more on the [development page](development.md).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:13:KiCanvas is developed by [Thea Flowers](https://thea.codes) with financial support from her [sponsors].
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:15:[KiCanvas]: http://kicanvas.org/home/
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:16:[KiCad]: https://kicad.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:17:[file an issue]: https://github.com/theacodes/kicanvas/issues/new/choose
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:18:[TypeScript]: https://typescript.dev
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:19:[Canvas]: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:20:[WebGL]: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:28:- Any KiCad 5 files, KiCanvas can only parse files from KiCad 6 and later.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:29:- Some KiCad 7 features might not be fully implemented, such as custom fonts in schematics.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:30:- Browsers other than desktop Chrome, Firefox, and Safari may run into issues, as we aren't currently running automated tests against other browsers. We welcome issues related to browser compatibility, just make sure it hasn't already been reported.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:32:[GitHub issues]: https://github.com/theacodes/kicanvas/issues
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:46:Nope, not at all. KiCanvas reads KiCad files directly.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:48:> Are you going to support KiCad 7 features? Custom fonts?
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:50:Yes. I'm actively working on bringing KiCanvas up to parity with KiCad 7, including custom fonts. For the time being, KiCad 7 files should parse and load in KiCanvas, however, KiCanvas may not render some KiCad 7 features correctly.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:54:Yes, KiCanvas will eventually let you view PCBs in "Assembly guide" mode. This won't require any extra KiCad plugins or anything.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:60:Because KiCanvas's developer-facing APIs for embedding and parsing are not yet ready. I don't want to publish it only to immediately break users as I rapidly iterate and change things. These developer APIs are my next priority after getting rendering to a good state. Stay tuned.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:62:> Why don't you support KiCad 5 files?
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:64:KiCad 5 files are a completely different format from V6 and onwards. Implementing parsers for that format would take a lot of time and I'm not interested in doing it.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:70:> Lol are you going to port all of KiCad to the browser?
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:72:No, KiCanvas is explicitly read-only and due to that assumption being baked in it wouldn't serve as a good base for a browser-based editor.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:77:- **Contribute code**: Since KiCanvas is still pretty early in its development, code contributions are harder to coordinate. Please file an issue or reach out before trying to contribute code, since I don't want you to waste your time.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:82:Contributions are welcome! However, since KiCanvas is in a super early stage please file an issue before you start working on something so we can coordinate. It's also recommended to take a moment and read over the [development documentation](development.md).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:92:- [KiSite](https://github.com/hmcty/kisite): A static site generator for KiCad projects
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:98:- [KiCAD-PRISM](https://github.com/krishna-swaroop/KiCAD-Prism): Cloud-based KiCad workspace, built on `ecad-viewer`
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\home.md:99:- [InteractiveHtmlBom](https://github.com/openscopeproject/interactivehtmlbom): Plugin to visualize KiCad BOM and assembly instructions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md:5:KiCanvas is free and open source source distributed under the terms specified below.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md:13:to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md:28:This notice must be included in any distributions of this project or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md:37:- Newstroke by Vladimir Uryvaev, Lingdong Huang, Adobe, and KiCad contributors. Originally licensed under Creative Commons CC0 1.0, amended with an MIT-like license, and utilizes glyphs that are licensed under the SIL Open Font License Version 1.1.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\license.md:47:You may copy, redistribute, and create derivative works from the material in
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\kicanvas:1:../../build
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\LICENSE:6:You may copy, redistribute, and create derivative works from the material in
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:3:KiCanvas is very early in its development and there's a ton of stuff that hasn't been done. The current top priority is parsing and rendering, while the next focus will be the embedding API.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:12:    - [x] Rendering KiCad 6 schematics
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:13:    - [x] Rendering KiCad 6 boards
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:14:    - [x] Rendering KiCad 6 text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:17:    - [x] Rendering KiCad 7 schematics
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:18:    - [x] Rendering KiCad 7 boards
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:19:    - [x] Rendering KiCad 7 text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:39:    - [ ] Copy selected item for pasting into KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:42:- [x] Standalone web application (kicanvas.org)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:48:    - [ ] Symbol library browser
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:49:    - [ ] Footprint library browser
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\roadmap.md:83:[Web Components]: https://developer.mozilla.org/en-US/docs/Web/API/Web_components
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\connections.kicad_sch:14:    (comment 3 "jellyfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\analogins.kicad_sch:14:    (comment 3 "gemini.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build.js:7:import fs from "node:fs";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build.js:11:    outfile: "build/kicanvas.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build.js:17:let result = await context.rebuild();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build.js:29:console.log("Saving metafile to build/esbuild-meta.json");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build.js:30:fs.writeFileSync("build/esbuild-meta.json", JSON.stringify(result.metafile));
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-font.js:8: * Transforms KiCad's newstroke font into a format KiCanvas can use.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-font.js:10: * Newstroke is distributed as a .cpp file and a old-format KiCad library,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-font.js:23:import * as fs from "node:fs/promises";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:7:import esbuild from "esbuild";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:8:import { resolve } from "node:path";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:9:import { readFile } from "node:fs/promises";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:31:        plugins: [CSSMinifyPlugin, ESbuildProblemMatcherPlugin],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:34:    return { options: options, context: await esbuild.context(options) };
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:40:    setup(build) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:41:        build.onLoad({ filter: /\.css$/ }, async (args) => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:43:            const css = await esbuild.transform(f, {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:52:// Enables VSCode to detect when the build starts/finishes
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:53:const ESbuildProblemMatcherPlugin = {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:54:    name: "esbuild-problem-matcher",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:56:    setup(build) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:57:        build.onStart(() => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:58:            console.log("[watch] build started");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:60:        build.onEnd((result) => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\bundle.js:61:            console.log("[watch] build finished");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-sprites.js:7:import * as fs from "node:fs/promises";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-sprites.js:8:import { resolve, basename } from "node:path";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-sprites.js:11:const ICON_SRC_DIR = resolve("src/kicanvas/icons");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\build-sprites.js:12:const OUT_FILE = resolve("src/kicanvas/icons/sprites.svg");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\serve.js:10:    outfile: "debug/kicanvas/kicanvas.js",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\serve.js:19:let { hosts, port } = await context.serve({
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\serve.js:20:    servedir: "./debug",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\serve.js:24:console.log(`[serve] listening at http://${hosts[0]}:${port}`);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\index.ts:8:import "./kicanvas/elements/kicanvas-shell";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\index.ts:9:import "./kicanvas/elements/kicanvas-embed";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\helium.kicad_sch:14:    (comment 3 "helium.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:1:import { defaultReporter, summaryReporter } from "@web/test-runner";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:2://import { chromeLauncher } from "@web/test-runner-chrome";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:3:import { esbuildPlugin } from "@web/dev-server-esbuild";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:5:// https://modern-web.dev/docs/test-runner/cli-and-configuration/
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:8:    files: "test/**/*.test.ts",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:9:    nodeResolve: true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:11:    // browsers: [
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:15:    //             devtools: true,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:20:        esbuildPlugin({
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\scripts\web-test-runner.config.mjs:37:    testFramework: {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:13:    test("no interpolated values", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:24:    test("content interpolation with primitives", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:40:    test("content interpolation with primitive arrays", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:47:    test("content interpolation with elements", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:58:    test("content interpolation with multiple elements", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:75:    test("content interpolation with dangerous text", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:82:    test("attribute interpolation with primitives", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:99:    test("mixed attribute interpolation", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:109:    test("interpolation with literal", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\dom\templates.test.ts:125:    test("top-level interpolation with multiple children", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:17:    test(".apply_symbol_transformations() - position only", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:34:    test(".apply_symbol_transformations() - rotations only", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:68:    test(".apply_symbol_transformations() - mirroring", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:97:    test(".stem()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:98:        // Reference data from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:132:    // Reference data from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:139:    test(".place_above()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:199:    test(".place_below()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\pin.test.ts:259:    test(".place_inside()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:12:import witch_hazel from "../../../src/kicanvas/themes/witch-hazel";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:33:    test(".get_text_offset()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:34:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:42:    test(".get_box_expansion()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:43:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:51:    test(".get_schematic_text_offset()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:54:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:75:    test(".get_schematic_text_offset() no tail", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:86:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:110:    test(".get_schematic_text_offset() with tail", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:121:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:138:    test(".get_schematic_text_offset()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\sch\painters\label.test.ts:148:        // Reference values from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\eda-text.test.ts:23:    test(".get_text_box() simple case", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\eda-text.test.ts:24:        // Known reference values taken from KiCad debugging.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\eda-text.test.ts:48:    test(".get_text_box() multiline case", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\eda-text.test.ts:49:        // Known reference values taken from KiCad debugging.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\font.test.ts:12:// Note: using StrokeFont as a concrete class to test base class methods.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\font.test.ts:16:    test(".wordbreak_markup()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\font.test.ts:23:        // TODO: Validate sizes with KiCad data.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\font.test.ts:37:        // Note: width reference values pulled from KiCad debugging
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\font.test.ts:53:    test(".break_lines()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\LICENSE:5:Permission to use, copy, modify, and/or distribute this software for any purpose
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:1:/* eslint-disable @typescript-eslint/ban-ts-comment */
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:94:    // interlink polygon nodes in z-order
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:152:// check whether a polygon node forms a valid ear with adjacent nodes
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:282:// go through all polygon nodes and cure small local self-intersections
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:299:            // remove two nodes involved
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:459:// interlink polygon nodes in z-order
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:552:// find the leftmost node of a polygon ring
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:574:// check if a diagonal between two polygon nodes is valid (lies in polygon interior)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:698:// create a node and optionally link it with previous one (in a circular doubly linked list)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:730:    // previous and next vertex nodes in a polygon ring
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:737:    // previous and next nodes in z-order
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\earcut\earcut.js:747:earcut.deviation = function (data, holeIndices, dim, triangles) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\mcu.kicad_sch:14:    (comment 3 "jellyfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\mcu.kicad_sch:31:      (property "ki_keywords" "test point tp" (id 4) (at 0 0 0)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\mcu.kicad_sch:34:      (property "ki_description" "test point" (id 5) (at 0 0 0)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\symbol.ts:159: * This is based on SCH_PAINTER::orientSymbol, where KiCad does some fun logic
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\symbol.ts:165:    // Note: KiCad uses a 2x2 transformation matrix for symbol orientation. It's
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\symbol.ts:167:    // with carefully crafted Matrix3s. KiCad's symbol matrix is defined as
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:21: * Implements KiCad rendering logic for symbol pins.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:24: * designed to recreate KiCad's behavior as closely as possible.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:81:     * KiCad doesn't directly set the transformation for symbol items, instead,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:83:     * See KiCad's sch_painter.cpp::orientSymbol.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:300: * KiCad saves pin orientation as a rotation, but presents it to the UI and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:322: * Note: only exported for the benefit of tests!
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\pin.ts:483: * Note: only exported for the benefit of tests!
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:16: * Implements KiCad rendering logic for net, global, and hierarchical labels.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:19: * It's designed to recreate KiCad's behavior as closely as possible.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:109:     * This takes into account orientation and any additional distance to make
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:119:        const dist = Math.round(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:125:            return new Vec2(-dist, 0);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:127:            return new Vec2(0, -dist);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:260:        const dist = Math.round(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:266:                return new Vec2(dist, 0);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:268:                return new Vec2(0, -dist);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:270:                return new Vec2(-dist, 0);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:272:                return new Vec2(0, dist);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painters\label.ts:437:            // Convert points to KiCad coordinate system
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\schematic\painter.ts:443:        // Position is tricky. KiCad's parser calls into SCH_FIELD::SetPosition
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\symbol-property-torture-test.kicad_sch:14:    (comment 3 "jellyfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\themes\kicad-default.ts:12:    friendly_name: "KiCad",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:15:    (comment 3 "starfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:13042:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:15375:    (descr "Abracon Miniature Ceramic Smd Crystal ABM8G http://www.abracon.com/Resonators/ABM8G.pdf, 3.2x2.5mm^2 package")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:16145:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:42713:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:42714:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:42741:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:42742:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44498:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44499:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44532:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44533:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44560:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\starfish.kicad_pcb:44561:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\examples\simple.kicad_sch:14:    (comment 3 "gemini.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:1:# <kicanvas-embed\>: The KiCanvas embedded viewer element
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:3:<!-- load kicanvas -->
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:5:<script type="module" src="/kicanvas/kicanvas.js"></script>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:11:The `<kicanvas-embed>` HTML element embeds one or more KiCad documents onto the page:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:14:<kicanvas-embed src="my-schematic.kicad_sch"></kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:17:<kicanvas-embed src="/examples/simple.kicad_sch"></kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:19:The above example shows the most basic usage of the `<kicanvas-embed>` element. It's usage is intentionally similar to the [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) and [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) elements. Through the use of additional [attributes](#attributes) you can control how the document is displayed, control interactivity, and load multiple files.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:23:    This page's format is modeled after MDN's [HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). It's intended to be familiar to web developers.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:27:During alpha, the best way to install KiCanvas is to [download the bundled kicanvas.js](/kicanvas/kicanvas.js), copy it into your project, and include it with a script tag:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:30:<script type="module" src="/kicanvas.js"></script>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:40:<kicanvas-embed src="my-schematic.kicad_sch" controls="basic"> </kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:43:<kicanvas-embed src="/examples/simple.kicad_sch" controls="basic"></kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:48:<kicanvas-embed src="my-schematic.kicad_sch" controls="full"> </kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:51:<kicanvas-embed src="/examples/simple.kicad_sch" controls="full"></kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:56:<kicanvas-embed
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:60:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:63:<kicanvas-embed src="/examples/simple.kicad_sch" controls="basic" controlslist="nodownload"></kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:71:This example shows that if you give the `<kicanvas-embed>` element an `id`, you can deep link into it using `#[id]:[reference]`:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:74:<kicanvas-embed id="my-schematic" src="my-schematic.kicad_sch" controls="basic">
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:75:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:82:This example shows how to use `<kicanvas-source>` to load multiple files.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:85:<kicanvas-embed controls="full">
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:86:    <kicanvas-source src="project.kicad_prj"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:87:    <kicanvas-source src="schematic1.kicad_sch"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:88:    <kicanvas-source src="schematic2.kicad_sch"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:89:    <kicanvas-source src="board.kicad_pcb"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:90:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:93:<kicanvas-embed controls="full">
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:94:    <kicanvas-source src="/examples/simple.kicad_sch"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:95:    <kicanvas-source src="/examples/starfish.kicad_pcb"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:96:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:102:This example shows how to use `<kicanvas-source>` along with inline KiCad data. In this case, it's a symbol copied from a schematic and pasted into the HTML source:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:105:<kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:107:    <kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:114:    </kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:117:    <kicanvas-source src="/examples/simple.kicad_sch"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:118:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:121:<kicanvas-embed controls="full">
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:122:    <kicanvas-source src="/examples/simple.kicad_sch"></kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:123:    <kicanvas-source name="inline.kicad_sch">
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:130:    </kicanvas-source>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:131:</kicanvas-embed>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:157:- `src` - the URL of the document to embed. If you want to show multiple documents within a single viewer, you can use multiple child `<kicanvas-source>` elements.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:159:- `name` - when providing the file source inline, this explicitly sets the file name. This is typically only necessary when there are multiple files within a project, as KiCad uses the file name to link schematic sheets, drawing sheets, and PCBs together. If unspecified, KiCanvas will generate a file name like `inline_0.kicad_sch`.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:175:| ??`kicanvas:click`          | The user clicks or taps within the embedded document                                              |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:176:| ??`kicanvas:documentchange` | The currently displayed document is changed, either through user interaction or programmatically. |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:177:| ??`kicanvas:error`          | An error occurs while loading source files                                                        |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:178:| ??`kicanvas:load`           | All sources files have been successfully loaded                                                   |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:179:| ??`kicanvas:loadstart`      | KiCanvas begins loading source files                                                              |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\embedding.md:180:| ??`kicanvas:select`         | The user selects (or deselects) an object within the document                                     |
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:20:- `kicad` contains the KiCad data layer and text layout implementation. This is where parsers for KiCad files and associated models live.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:22:- `viewers` contains classes that implement viewers for different KiCad documents. Viewers handle creating geometry using "Painters" and managing "Layers" for the renderer to draw. Viewers do not provide a user interface on their own, they're designed with high-level APIs that let various user interface elements control the viewer.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:23:- `kc-ui` contains generic, low-level web components used to build KiCanvas's user interface. Elements in here are generic enough to be re-used in other projects, but may be slightly tailored to KiCanvas's needs. For example, `<kc-ui-button>` and `<kc-ui-icon>`.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:24:- `kicanvas` contains the KiCanvas application and its elements. Elements here implement KiCanvas functionality, such as `<kc-project-panel>` and `<kc-symbols-panel>`.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:26:[KiCanvas]: https://kicanvas.org
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:27:[TypeScript]: https://typescript.dev
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:28:[Canvas]: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:29:[WebGL]: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:30:[Web Components]: https://developer.mozilla.org/en-US/docs/Web/API/Web_components
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\docs\docs\development.md:31:[Code of Conduct]: https://github.com/theacodes/kicanvas/blob/main/CODE_OF_CONDUCT.md
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\graphics\canvas2d.ts:67:        const dpr = window.devicePixelRatio;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\graphics\canvas2d.ts:82:        this.ctx2d!.scale(window.devicePixelRatio, window.devicePixelRatio);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:135:        // use the same order as KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:136:        // https://gitlab.com/kicad/code/develop/-/blob/master/common/eda_shape.cpp#L1616
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:387:        // TODO: Port KiCad's logic over.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:597:                    // KiCad approximates rounded rectangles using four line segments
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:870:        // Looks like the rotation angle for KiCad's symbol attribute rendering
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:1088:            const xbar_distance = extension
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:1092:            xbar_start = d.start.add(xbar_distance);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:1093:            xbar_end = d.end.add(xbar_distance);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\board\painter.ts:1113:        // TODO: KiCad checks to see if the text overlaps the crossbar and
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\font:17:EquName1=devcms
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\font:119:LibName2=device
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:15:    (comment 3 "starfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:12960:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:15298:    (descr "Abracon Miniature Ceramic Smd Crystal ABM8G http://www.abracon.com/Resonators/ABM8G.pdf, 3.2x2.5mm^2 package")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:15969:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:42557:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:42558:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:42585:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:42586:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44342:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44343:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44376:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44377:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44404:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\simple.kicad_pcb:44405:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:21:import shell_styles from "./kicanvas-shell.css";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:30: * <kc-kicanvas-shell> is the main entrypoint for the standalone KiCanvas
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:31: * application: It's the thing you see when you go to kicanvas.org.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:39: * <kc-kicanvas-shell>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:175:                        <img src="images/kicanvas.png" />
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:182:                        <strong>browser-based</strong>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:183:                        viewer for KiCad schematics and boards. You can learn
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:185:                        <a href="https://kicanvas.org/home" target="_blank"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:191:                            href="https://github.com/theacodes/kicanvas/issues/new/choose"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:202:                        or drag & drop your KiCad files, or<button
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:211:                            href="https://github.com/theacodes/kicanvas"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:217:                            href="https://github.com/theacodes/kicanvas#special-thanks"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:232:                        >. KiCanvas runs entirely within your browser, so your
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:237:                            href="https://github.com/theacodes/kicanvas"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-shell.ts:250:window.customElements.define("kc-kicanvas-shell", KiCanvasShellElement);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:28:const log = new Logger("kicanvas:embedtag");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:31: * kicanvas-embed tag
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:120:            "kicanvas-source",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:212:window.customElements.define("kicanvas-embed", KiCanvasEmbedElement);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:241:            if (child.nodeType === Node.TEXT_NODE) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:243:                content += child.nodeValue ?? "";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:246:                    `kicanvas-source children ${child.nodeType} are invaild.`,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:274:            log.warn(`kicanvas-source content ${file_name} is empty.`);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kicanvas-embed.ts:324:window.customElements.define("kicanvas-source", KiCanvasSourceElement);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:22:    test(".get_glyph()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:23:        // Expected values here are pulled from KiCad's memory after loading Newstroke.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:54:        // Note: only testing two glyphs here, but it's unlikely that these two would pass if others
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:58:    test(".get_interline()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:59:        // Expected values here are pulled from KiCad via debugging calls to respective StrokeFont methods.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:65:    test(".compute_overbar_vertical_position()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:74:    test(".get_text_as_glyphs()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:75:        // Expected values pulled from KiCad via debugging to StrokeFont::GetTextAsGlyphs
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:139:    test(".get_text_as_glyphs() with rotated, italic", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:140:        // Expected values pulled from KiCad via debugging to StrokeFont::GetTextAsGlyphs
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:201:    test(".get_line_extents()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:225:    test(".get_line_extents() with markup", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:271:    test(".draw() simple", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:281:        renderer.start_layer("test");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:288:        // Reference data from KiCad debugging.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:344:    test(".draw() multiline", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:354:        renderer.start_layer("test");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\stroke-font.test.ts:361:        // Reference data from KiCad debugging.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\sch-text.test.ts:13:    test(".set_spin_style_from_angle()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\graphics\webgl\glsl.d.ts:8: * Esbuild bundles glsl modules using the "text" content type. This tells typescript about it.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\sch-field.test.ts:17:    test(".shown_text", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\sch-field.test.ts:27:    test(".draw_rotation", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\sch-field.test.ts:50:    test(".position", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\sch-field.test.ts:80:    test(".bounding_box", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:23:    test(".bounding_box", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:38:        // Same test, but rotated.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:49:    test(".normalize_justification()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:66:    test(".rotate()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:100:    test(".mirror_horizontally()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\text\lib-text.test.ts:119:    test(".mirror_vertically()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:40:    test("with bare values", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:50:    test("with atoms", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:81:    test("with numbers", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:94:    test("with strings", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:114:    test("with base64", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:127:    test("with embedded data containing pipes", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:142:    test("with pipe character in middle of atom", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:143:        const tokens = tokenizer.tokenize("(test |middle|end)");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:146:            [ATOM, "test"],
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:154:    test("with simple lists", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\tokenizer.test.ts:169:    test("with nested lists", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:22:    test("with empty schematic file", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:23:        const sch = new schematic.KicadSch("test.kicad_sch", empty_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:37:    test("with paper settings & title block", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:38:        const sch = new schematic.KicadSch("test.kicad_sch", paper_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:62:    test("with wires, buses, no connects, and junctions", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:63:        const sch = new schematic.KicadSch("test.kicad_sch", wires_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:67:        // note: KiCad saves stuff out of order, so the numbers here
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:168:    test("with labels", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:169:        const sch = new schematic.KicadSch("test.kicad_sch", labels_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:252:    test("with drawings", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:253:        const sch = new schematic.KicadSch("test.kicad_sch", drawings_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:319:    test("with kicad9 drawings", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:321:            "test.kicad_sch",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:338:    test("with library symbols", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:339:        const sch = new schematic.KicadSch("test.kicad_sch", symbols_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:527:    test("with library symbols (KiCad 8)", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:529:            "test.kicad8_sch",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:578:    test("with library symbols (KiCad 10)", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:580:            "test.kicad_sch",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:773:    test("with symbols", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\schematic.test.ts:774:        const sch = new schematic.KicadSch("test.kicad_sch", symbols_sch_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\project.test.ts:20:    test("basic", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:14:    test(".start()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:23:    test(".positional()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:48:    test(".pair()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:59:    test(".list()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:75:    test(".collection()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:92:    test(".dict()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:107:    test(".atom()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:151:    test(".expr()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:170:    test(".object()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:186:    test(".item()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:201:    test(".vec2()", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\parser.test.ts:214:    test("with complex data", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:372:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:393:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:414:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:435:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:456:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:477:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:498:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:519:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:543:    (descr "X2SON 5 pin 1x1mm package (Reference Datasheet: http://www.ti.com/lit/ds/sbvs193d/sbvs193d.pdf Reference part: TPS383x) [StepUp generated footprint]")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:769:    (descr "X2SON 5 pin 1x1mm package (Reference Datasheet: http://www.ti.com/lit/ds/sbvs193d/sbvs193d.pdf Reference part: TPS383x) [StepUp generated footprint]")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:1670:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:1800:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:2149:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:2216:  (footprint "tomu-fpga:testpoint" (layer "B.Cu")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\tomu-fpga.kicad_pcb:2430:    (descr "X2SON 5 pin 1x1mm package (Reference Datasheet: http://www.ti.com/lit/ds/sbvs193d/sbvs193d.pdf Reference part: TPS383x) [StepUp generated footprint]")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:15:    (comment 3 "starfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:13042:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:15375:    (descr "Abracon Miniature Ceramic Smd Crystal ABM8G http://www.abracon.com/Resonators/ABM8G.pdf, 3.2x2.5mm^2 package")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:16145:    (descr "SOIC, 8 Pin (JEDEC MS-012AA, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_8.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:42713:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:42714:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:42741:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:42742:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44498:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44499:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44532:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44533:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44560:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\debug\examples\starfish.kicad_pcb:44561:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\async.ts:32: * Schedules a callback to be executed when the browser is idle or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\viewport.ts:9:import { SizeObserver } from "../../base/dom/size-observer";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\viewport.ts:18:    #observer: SizeObserver;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\viewport.ts:41:        this.#observer = new SizeObserver(this.renderer.canvas, () => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\viewport.ts:50:        this.#observer.dispose();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\painter.ts:14:const log = new Logger("kicanvas:project");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\painter.ts:146:        // https://gitlab.com/kicad/code/develop/-/blob/master/pcbnew/pcb_painter.cpp#L2236
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\events.ts:14:    static readonly type = "kicanvas:load";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\events.ts:27:    static readonly type = "kicanvas:select";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\events.ts:40:    static readonly type = "kicanvas:mousemove";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\viewers\base\document-viewer.ts:21:const log = new Logger("kicanvas:viewer");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\app.ts:8: * Common building blocks for KiCanvas's UI.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\activity-side-bar.ts:151:        const observer = new MutationObserver(async (mutations) => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\activity-side-bar.ts:163:        observer.observe(this, {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\activity-side-bar.ts:168:    static get observedAttributes() {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\button.ts:181:    static get observedAttributes() {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\css.d.ts:8: * Esbuild bundles css files in this package using the "text" content type.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:8:import type { Project } from "../kicanvas/project";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:945:        // https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#_footprint_text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:959:        // KiCad correctly parses both definitions
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:961:        // https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#_symbol_properties
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1073:    // https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#_properties
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1077:    // https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#_symbol_properties
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1096:            // parsed as 'symbol_property' node
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1113:            // parsed as 'property' node
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1155:        // is the default values from KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1433:        // The `arc` node in pts is undocumented in the following link:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\board.ts:1434:        // https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html#_footprint_polygon
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\common.ts:192:            (comment 3 "starfish.wntr.dev")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\common.ts:290:            // Note: KiCad saves height as the first number and width as the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\help-panel.ts:36:                        <a href="https://kicanvas.org/home">KiCanvas</a>, an
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\help-panel.ts:37:                        interactive, browser-based viewer for KiCad schematics
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\help-panel.ts:44:                            href="https://github.com/theacodes/kicanvas/issues/new/choose"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\help-panel.ts:51:                        KiCanvas is developed by
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\fontconv.awk:3:# awk script to convert KiCad font.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\fontconv.awk:123:function dist(glyph1, glyph2, subst,   sx, cn, ml, mr) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\fontconv.awk:298:	comx = comx + dist(gp, $2)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\fontconv.awk:304:	comx = comx + dist(gp, $2)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\disposable.ts:13: * * https://github.dev/microsoft/vscode/blob/main/src/vs/base/common/lifecycle.ts
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\color.ts:122:        // From KiCad's COLOR4D::Desaturate
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\graphics\webgl\vector.ts:662:     * @param depth - used for depth testing
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\graphics\webgl\renderer.ts:76:        const dpr = window.devicePixelRatio;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kc-schematic\info-panel.ts:58:                        ${entry("KiCad version", schematic.version)}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\project.ts:21:const log = new Logger("kicanvas:project");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\project.ts:195:        // from shortest to longest and walking through the paths to see if
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\project.ts:217:        // If we found a root page, we can build out the list of pages by
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\preferences.ts:20:    public alignControlsWithKiCad: boolean = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\preferences.ts:24:        this.storage.set("alignControlsWithKiCad", this.alignControlsWithKiCad);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\preferences.ts:32:        this.alignControlsWithKiCad = this.storage.get(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\preferences.ts:33:            "alignControlsWithKiCad",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\preferences.ts:46:    static readonly type = "kicanvas:preferences:change";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\any.d.kicad_pro.ts:8: * Esbuild bundles these using the "text" content type. This tells typescript about it.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\any.d.kicad_pcb.ts:8: * Esbuild bundles these using the "text" content type. This tells typescript about it.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\drawing_sheet.test.ts:12:    test("with default sheet", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:29:    test("with empty pcb file", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:30:        const pcb = new board.KicadPCB("test.kicad_pcb", empty_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:96:    test("with title block and properties", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:97:        const pcb = new board.KicadPCB("test.kicad_pcb", properties_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:132:    test("with paper settings & title block", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:133:        const pcb = new board.KicadPCB("test.kicad_pcb", paper_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:157:    test("with graphics", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:158:        const pcb = new board.KicadPCB("test.kicad_pcb", shapes_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:228:    test("with text", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:229:        const pcb = new board.KicadPCB("test.kicad_pcb", text_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:322:    test("with locked gr_text", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:341:    test("with locked fp_text", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:366:    test("with traces", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:367:        const pcb = new board.KicadPCB("test.kicad_pcb", traces_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:434:    test("with dimensions", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:435:        const pcb = new board.KicadPCB("test.kicad_pcb", dimensions_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:511:    test("with zones", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:512:        const pcb = new board.KicadPCB("test.kicad_pcb", zones_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:583:    test("with vias", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:584:        const pcb = new board.KicadPCB("test.kicad_pcb", vias_pcb_src);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:632:    test("with polygon", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:634:            "test.kicad_pcb",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:660:    test("with graphics", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:662:            "test.kicad_pcb",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:865:    test("with pads", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:867:            "test.kicad_pcb",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:1077:    test("with footprint symbol properties", function () {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\board.test.ts:1079:            "test.kicad_pcb",
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\any.d.kicad_sch.ts:8: * Esbuild bundles these using the "text" content type. This tells typescript about it.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\drawings.kicad_sch:127:      8aFFhnpmI84220WSJI6fryC/SPzdmqbx9g+7mBhZ64cfHZjX/2+2GrFlmPWFJl5oGgz3ztJ5fSQi
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\drawings.kicad_sch:133:      TGEFKCzJpKgsWxe8+Zklhnpmo75ew1M1+v8X5twM9czqQrcagxy5/mna7qbx37oyzOykMF9lWaKq
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\drawings.kicad_sch:230:      7YqsKCr3b6xN9zpxvkJ/rWBA4eo7/bz1w841Zo3RJHPm8So9BSIYVBnpm91WWepGmMwGTj22kmPl
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\download.ts:10:    Basic helper to initiate a download of a given File using the browser.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kc-board\info-panel.ts:51:                        ${entry("KiCad version", board.version)}
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\default_drawing_sheet.kicad_wks:17:  (tbtext "${KICAD_VERSION}" (name "") (pos 109 4.1) (comment "KiCad version"))
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\preferences-panel.ts:72:                prefs.alignControlsWithKiCad = target.checked;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\preferences-panel.ts:104:                                checked="${prefs.alignControlsWithKiCad}" />
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\common\preferences-panel.ts:105:                            Align controls with KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kc-board\layers-panel.ts:354:    static select_event = "kicanvas:layer-control:select";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\elements\kc-board\layers-panel.ts:355:    static visibility_event = "kicanvas:layer-control:visibility";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\drawing-sheet.ts:124:                // KiCad Version
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\drag-drop.ts:10:} from "../../kicanvas/services/vfs";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\services\vfs.ts:19: * This is the interface used by <kc-kicanvas-shell> to find and load files.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\file-picker.ts:7:import { LocalFileSystem } from "../../kicanvas/services/vfs";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\livereload.js:8:// @ts-expect-error: defined by esbuild
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\livereload.js:10:    new EventSource("/esbuild").addEventListener("change", () =>
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicanvas\icons\svg.d.ts:8: * Esbuild bundles svg files in this package using the "text" content type.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\kicad_wks.d.ts:8: * Esbuild bundles css files in this package using the "text" content type.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\pan-and-zoom.ts:8:import { Preferences } from "../../kicanvas/preferences";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\pan-and-zoom.ts:117:        // Prevent the browser's default context menu.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\pan-and-zoom.ts:139:        if (!prefs.alignControlsWithKiCad) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\pan-and-zoom.ts:158:        // work around browsers setting a huge scroll distance
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\pan-and-zoom.ts:162:        if (!prefs.alignControlsWithKiCad) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\parser.ts:14:export const log = new Logger("kicanvas:parser");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:113:    (descr "SMD pad as test Point, diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:114:    (tags "test point SMD pad")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:136:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:137:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:166:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:167:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:195:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:196:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:232:    (descr "Plated Hole as test Point, diameter 2.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:233:    (tags "test point plated hole")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:255:    (descr "Plated Hole as test Point, diameter 2.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:256:    (tags "test point plated hole")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:278:    (descr "THT rectangular pad as test Point, square 2.0mm_Drill1.0mm  side length, hole diameter 1.0mm")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:279:    (tags "test point THT pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:307:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:308:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:336:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:337:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:366:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:367:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:395:    (descr "SMD rectangular pad as test Point, square 1.0mm side length")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\test\kicad\files\footprint-pads.kicad_pcb:396:    (tags "test point SMD pad rectangle square")
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:9:type ResizeObserverCallback = (target: HTMLElement) => void;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:12: * Wrapper over ResizeObserver that implements IDisposable
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:14:export class SizeObserver implements IDisposable {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:15:    #observer: ResizeObserver;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:19:        private callback: ResizeObserverCallback,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:21:        this.#observer = new ResizeObserver(() => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:24:        this.#observer.observe(target);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:28:        this.#observer?.disconnect();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\dom\size-observer.ts:29:        this.#observer = undefined!;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\log.ts:53:const default_logger = new Logger("kicanvas");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\project-settings.ts:12: * See KiCad's PROJECT_FILE class
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\angle.ts:35:     * instead of radians to match KiCad's behavior and to avoid floating point
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\focus-overlay.ts:79:    #intersection_observer: IntersectionObserver;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\focus-overlay.ts:95:        this.#intersection_observer = new IntersectionObserver((entries) => {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\focus-overlay.ts:103:        this.#intersection_observer.observe(this);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\focus-overlay.ts:107:                this.#intersection_observer.disconnect();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:10:import type { Project } from "../kicanvas/project";
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:505:        /* TODO: this was added in KiCad 7 */
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:688:        /* TODO: This was added in KiCad 7 */
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1015:        // KiCad encodes the symbol unit into the name, for example,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1028:        // KiCad "De Morgan" body styles are indicated with a number greater
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1092:        // KiCad 10 (ver 20260306)
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1096:        // KiCad 9 and 8
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1319:            //    (project "kit-dev-coldfire-xilinx_5213"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\schematic.ts:1662:            //   (project "kit-dev-coldfire-xilinx_5213"
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\arc.ts:63:        // although KiCad always creates clockwise arcs, the file may contain
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\arc.ts:162:        // TODO: Pull KiCad's logic for this, since it adds more segments the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\arc.ts:242: * Ported from KiCad's KiMATH trigo
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\arc.ts:304:    // to the standard deviation.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\types.ts:42:// eslint-disable-next-line @typescript-eslint/no-wrapper-object-types
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\eda-text.ts:14: * KiCad uses EDA_TEXT as a sort of grab-bag of various things needed to render
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\eda-text.ts:19: * carefully matching KiCad's behavior, but it's still a lot to wrap your
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\eda-text.ts:33:     * KiCad uses Effects to encapsulate all of the various text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\eda-text.ts:51:     * KiCad uses At to encapsulate both position and rotation. How this is
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\eda-text.ts:295: * As per KiCad's Clamp_Text_PenSize, this limits normal text to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.h:7: * Copyright (C) 1992-2010 KiCad Developers, see change_log.txt for contributors.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.h:9: * This program is free software; you can redistribute it and/or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.h:14: * This program is distributed in the hope that it will be useful,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:4:Newstroke is a stroke (plotter) font originally designed for KiCad.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:10:font.lib         - main glyph library in KiCad library format
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:13:font.pro         - KiCad project
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:15:fontconv.awk     - AWK script for 'compiling' project to c-source used by KiCad
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:20:KiCad (http://kicad.sourceforge.net/) - for glyph editing
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\README.txt:25:* Edit glyphs with KiCad EESchema library editor.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\tokenizer.ts:9:    - https://dev-docs.kicad.org/en/file-formats/sexpr-intro/
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\tokenizer.ts:10:    - https://gitlab.com/edea-dev/edea/-/tree/main/edea
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:4: * This program source code file is part of KiCad, a free EDA CAD application.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:7: * Copyright (C) 1992-2019 KiCad Developers, see change_log.txt for contributors.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:9: * This program is free software; you can redistribute it and/or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:14: * This program is distributed in the hope that it will be useful,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:34: * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:50: * Source Han Sans is Copyright 2014-2019 Adobe (http://www.adobe.com/), with Reserved Font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:66: * development of collaborative font projects, to support the font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:72: * redistributed freely as long as they are not sold by themselves. The
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:74: * redistributed and/or sold with any software provided that any reserved
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:83: * include source files, build scripts and documentation.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:85: * "Reserved Font Name" refers to any names specified as such after the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:89: * components as distributed by the Copyright Holder(s).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:102: * modify, redistribute, and sell modified and unmodified copies of the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:109: * redistributed and/or sold with any software, provided that each copy
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:115: * 3) No Modified Version of the Font Software may use the Reserved Font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:127: * must be distributed entirely under this license, and must not be
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\newstroke_font.cpp:128: * distributed under any other license. The requirement for fonts to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:17: * Note: KiCad always passes any coordinates or sizes in scaled internal units
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:19: * represented as 12700 IU for EESchema and 1270000 IU for PCBNew. See KiCad's
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:23: * This is largely adapted from KiCad's KIFONT::FONT base class and beaten
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:57:     * Corresponds to KiCad's FONT::StringBoundaryLimits
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:97:     * Note: this behaves like KiCad's FONT::LinebreakText in that it only
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:194:     * Corresponds to KiCad's Font::DrawSingleLineText
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:244:     * Corresponds to KiCad's FONT::boundingBoxSingleLine
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:364:     * Corresponds to KiCad's FONT::drawMarkup, which doesn't actually draw,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:380:        return this.get_markup_node_as_glyphs(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:392:    protected get_markup_node_as_glyphs(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:393:        node: MarkupNode,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:405:        let node_style = style.copy();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:407:        if (!node.is_root) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:408:            if (node.subscript) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:409:                node_style = new TextStyle();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:410:                node_style.subscript = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:412:            if (node.superscript) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:413:                node_style = new TextStyle();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:414:                node_style.superscript = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:416:            node_style.overbar ||= node.overbar;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:418:            if (node.text) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:420:                    glyphs: node_glyphs,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:424:                    node.text,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:430:                    node_style,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:433:                glyphs = node_glyphs;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:439:        for (const child of node.children) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:444:            } = this.get_markup_node_as_glyphs(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:451:                node_style,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:468:     * Corresponds to KiCad's FONT::wordbreakMarkup
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:470:     * As per KiCad, a word can represent an actual word or a run of text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:481:        return this.wordbreak_markup_node(markup.root, size, style);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:485:    protected wordbreak_markup_node(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:486:        node: MarkupNode,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:490:        const node_style = style.copy();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:494:        if (!node.is_root) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:497:            if (node.subscript) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:499:                node_style.subscript = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:501:            if (node.superscript) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:503:                node_style.superscript = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:505:            if (node.overbar) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:507:                node_style.overbar = true;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:514:                if (node.text) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:516:                        node.text,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:522:                        node_style,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:525:                    word += node.text;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:529:                for (const child of node.children) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:530:                    const child_words = this.wordbreak_markup_node(
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:533:                        node_style,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:548:                const words = node.text.trim().split(" ");
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:551:                if (node.text.endsWith(" ")) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:563:                        node_style,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:570:        for (const child of node.children) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\font.ts:572:                this.wordbreak_markup_node(child, size, style),
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\glyph.ts:49:        // Note: our bbox calculation differs from KiCad's, however,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\custom-element.ts:33:     * https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/exportparts
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:15: * mirror_vertical are all implemented in order to match KiCad's behavior, see
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:55:     * This contains the positioning logic KiCad performs in
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:96:     * symbol text, since KiCad does not directly use a symbol's transformation
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:97:     * to orient text. Instead, KiCad deep copies the library symbol then calls
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:101:     * KiCad's sch_painter.cpp::orientSymbol.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\lib-text.ts:170:     * KiCad's rotation of LIB_TEXT objects is somewhat convoluted, but
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kc-ui\range.ts:131:    static get observedAttributes() {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\THIRD_PARTY_README.md:3:The Newstroke font is a Hershey font and is the primary font used in KiCad. It is licensed under [Creative Commons' CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\third_party\newstroke\THIRD_PARTY_README.md:5:This source distribution was retrieved from https://vovanium.ru/sledy/newstroke/en on Friday, January 20th, 2023.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:8: * KiCad text markup parser
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:10: * KiCad uses basic text markup to express subscript, superscript, and overbar
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:82:    const node = new MarkupNode();
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:88:            node.children.push(c);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:104:            node.children.push(c);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:108:            return node;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\markup.ts:112:    return node;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\math\vec2.ts:99:     * KiCad has to be weird about this, ofc.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:7: * This program source code file is part of KiCad, a free EDA CAD application.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:10: * Copyright (C) 1992-2019 KiCad Developers, see change_log.txt for contributors.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:12: * This program is free software; you can redistribute it and/or
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:17: * This program is distributed in the hope that it will be useful,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:37: * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:53: * Source Han Sans is Copyright 2014-2019 Adobe (http://www.adobe.com/), with Reserved Font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:69: * development of collaborative font projects, to support the font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:75: * redistributed freely as long as they are not sold by themselves. The
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:77: * redistributed and/or sold with any software provided that any reserved
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:86: * include source files, build scripts and documentation.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:88: * "Reserved Font Name" refers to any names specified as such after the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:92: * components as distributed by the Copyright Holder(s).
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:105: * modify, redistribute, and sell modified and unmodified copies of the
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:112: * redistributed and/or sold with any software, provided that each copy
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:118: * 3) No Modified Version of the Font Software may use the Reserved Font
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:130: * must be distributed entirely under this license, and must not be
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\newstroke-glyphs.ts:131: * distributed under any other license. The requirement for fonts to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:71: * placeholders will later be used to modify the constructed DOM node's
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:105:    let node;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:107:    while ((node = walker.nextNode()) !== null) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:108:        if (node.nodeType == Node.TEXT_NODE) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:109:            apply_content_value(node.parentNode, node as Text, values);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:110:        } else if (node.nodeType == Node.ELEMENT_NODE) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:111:            const elm = node as HTMLElement;
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:121: * Apply template values to a node's text content.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:123:function apply_content_value(node: Node | null, text: Text, values: unknown[]) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:124:    if (!node) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:134:    if (is_HTMLElement(node) && ["script", "style"].includes(node.localName)) {
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:146:        // Even numbered parts are text nodes.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:148:            node.insertBefore(new Text(part), text);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:156:                node.insertBefore(value, text);
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\base\web-components\html.ts:161:    // Clear the text data instead of removing the node, since removing it will
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\sch-field.ts:20: * This corresponds to and is roughly based on KiCad's SCH_FIELD class.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\sch-field.ts:45:        // KiCad represents transforms with a simple 2x2 matrix which
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\sch-field.ts:49:        // KiCad sets the transform of a symbol instance in
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:17: * This class is adapted from KiCad's STROKE_FONT.
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:103:        // KiCad grows the bounding box a little for stroke fonts to
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:120:        // KiCad doesn't include glyph thickness for interline spacing in
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:209:        // KiCad shortens the overbar slightly
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:223:        // but technically KiCad can show both at the same time. I wasn't able
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:290: * Newstroke is distributed as a .cpp file and a old-format KiCad library,
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\src\kicad\text\stroke-font.ts:293: * The code here is based on KiCad's STROKE_FONT::LoadNewStrokeFont

```

## KiCanvas local Node npm versions

```powershell
node --version; npm --version
```
Exit code: 0
Output:
```text
v22.15.0
10.9.2

```

## KiCanvas package.json scripts and dependencies

```powershell
Get-Content 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas\package.json' -Raw | ConvertFrom-Json | Select-Object scripts, dependencies, devDependencies
```
Exit code: 0
Output:
```text


scripts         : @{test:watch=web-test-runner --config scripts/web-test-runner.config.mjs --watch; 
                  test:coverage=web-test-runner --config scripts/web-test-runner.config.mjs --coverage; 
                  test=web-test-runner --config scripts/web-test-runner.config.mjs; lint:eslint=eslint --config 
                  .eslintrc.cjs src/ --ext .js,.ts; lint:types=tsc -p tsconfig.json; lint:prettier=prettier . --check; 
                  lint=npm run lint:eslint && npm run lint:types && npm run lint:prettier; format=prettier . --write; 
                  serve=node scripts/serve.js; build:no-check=node scripts/build.js; build:font=node 
                  scripts/build-font.js; build:sprites=node scripts/build-sprites.js; build=tsc -p tsconfig.json && 
                  node scripts/build.js; clean=rm -rf build && rm -rf debug/kicanvas}
dependencies    : 
devDependencies : @{@open-wc/semantic-dom-diff=^0.20.1; @types/mocha=^10.0.10; 
                  @typescript-eslint/eslint-plugin=^8.49.0; @typescript-eslint/parser=^8.49.0; 
                  @web/dev-server-esbuild=^1.0.4; @web/test-runner=^0.20.2; chai=^6.2.1; esbuild=^0.27.1; 
                  esbuild-plugin-copy=^2.1.1; eslint=^8.53.0; eslint-config-prettier=^9.0.0; 
                  eslint-plugin-mocha=^10.2.0; html-minifier-terser=^7.2.0; prettier=^3.7.4; svgstore=^3.0.1; 
                  typescript=^5.9.3; typescript-lit-html-plugin=^0.9.0}




```

## KiCanvas package manager lock files

```powershell
Get-ChildItem 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' -Force -Include package-lock.json,pnpm-lock.yaml,yarn.lock
```
Exit code: 0
Output:
```text

Name              Length
----              ------
package-lock.json 319214



```

## KiCanvas create isolated npm workspace copy

```powershell
New-Item -ItemType Directory -Force 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903'; robocopy 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903' /E /XD .git node_modules build debug .cache /XF .DS_Store
```
Exit code: 0
Output:
```text

Robocopy exit code: 1

```

## KiCanvas isolated workspace path

```powershell
Write-Output 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903'
```
Exit code: 0
Output:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903

```

## KiCanvas npm ci in isolated workspace

```powershell
npm --prefix 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903' ci --ignore-scripts
```
Exit code: 0
Output:
```text

added 497 packages, and audited 498 packages in 15s

99 packages are looking for funding
  run `npm fund` for details

10 vulnerabilities (1 low, 3 moderate, 5 high, 1 critical)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.

```
Errors:
```text
node.exe : npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check 
out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more 
comprehensive and powerful.
At C:\Program Files\nodejs\npm.ps1:29 char:3
+   & $NODE_EXE $NPM_CLI_JS $args
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (npm warn deprec...e and powerful.:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
npm warn deprecated @humanwhocodes/config-array@0.13.0: Use @eslint/config-array instead
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead
npm warn deprecated keygrip@1.1.0: Package no longer supported. Contact Support at https://www.npmjs.com/support for 
more info.
npm warn deprecated typescript-styled-plugin@0.13.0: Deprecated in favor of 
https://github.com/styled-components/typescript-styled-plugin
npm warn deprecated vscode-emmet-helper@1.2.11: This package has been renamed to @vscode/emmet-helper, please update 
to the new name
npm warn deprecated eslint@8.57.1: This version is no longer supported. Please see https://eslint.org/version-support 
for other options.

```

## KiCanvas npm run lint types in isolated workspace

```powershell
npm --prefix 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903' run lint:types
```
Exit code: 0
Output:
```text

> kicanvas@0.0.0 lint:types
> tsc -p tsconfig.json


```

## KiCanvas npm run build no check in isolated workspace

```powershell
npm --prefix 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903' run build:no-check
```
Exit code: 0
Output:
```text

> kicanvas@0.0.0 build:no-check
> node scripts/build.js

Building to build/kicanvas.js
[watch] build started
[watch] build finished
Build complete!
0 warnings
0 errors
Saving metafile to build/esbuild-meta.json

```

## KiCanvas isolated workspace build inventory

```powershell
Get-ChildItem 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903\build' -Recurse -File -ErrorAction SilentlyContinue | Select-Object FullName,Length | Select-Object -First 30
```
Exit code: 0
Output:
```text

FullName                                                                                               Length
--------                                                                                               ------
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903\build\esbuild-meta.json  67447
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\node_envs\kicanvas\workspace_20260430_161903\build\kicanvas.js       477759



```

## KiCanvas source repo status after isolated tests

```powershell
git -C 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicanvas' status --short
```
Exit code: 0
Output:
```text
```

## PcbDraw plot subcommand help with KiCad and Inkscape paths

```powershell
$env:PATH = 'C:\Program Files\Inkscape\bin;C:\Program Files\KiCad\9.0\bin;' + $env:PATH
$env:PYTHONPATH = 'C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe' plot --help
```
Exit code: 0
Output:
```text
Usage: pcbdraw plot [OPTIONS] INPUT OUTPUT

  Create a stylized drawing of the PCB.

Options:
  -s, --style TEXT                A name of built-in style or a path to style
                                  file
  -l, --libs COMMA SEPARATED LIST
                                  Comma separated list of libraries to use
  -p, --placeholders              Render placeholders to show the components
                                  origins
  -m, --remap FILE                JSON file with map from part reference to
                                  <lib>:<model> to remap packages
  --drill-holes / --no-drill-holes
                                  Make drill holes transparent
  --side [front|back]             Specify which side of the PCB to render
  --mirror                        Mirror the board
  --highlight COMMA SEPARATED LIST
                                  Comma separated list of components to
                                  highlight
  -f, --filter COMMA SEPARATED LIST
                                  Comma separated list of components to show,
                                  if not specified, show all
  -v, --vcuts KICAD LAYER         If layer specified, renders V-cuts from it
  --dpi INTEGER                   DPI for bitmap output
  --margin INTEGER                Specify margin of the final image in
                                  millimeters
  --silent                        Do not output any warnings
  --werror                        Treat warnings as errors
  --resistor-values COMMA SEPARATED LIST
                                  Comma separated list of resistor value
                                  remapping. For example, "R1:10k,R2:470"
  --resistor-flip COMMA SEPARATED LIST
                                  Comma separated list of resistor bands to
                                  flip
  --paste                         Add paste layer
  --components / --no-components  Render components
  --copper / --no-copper          Render copper
  --outline-width FLOAT           Outline width in mm
  --show-lib-paths                Show library paths and quit
  --help                          Show this message and exit.

```

## InteractiveHtmlBom command text correction

The earlier `InteractiveHtmlBom safe help command` section recorded the executed output correctly, but the displayed command text was malformed by PowerShell string interpolation. The command that was intended and successfully executed was:

```powershell
$env:PATH = 'C:\Program Files\KiCad\9.0\bin;' + $env:PATH
$env:PYTHONPATH = 'C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'
$env:INTERACTIVE_HTML_BOM_NO_DISPLAY = '1'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\generate_interactive_bom.exe' --help
```

Exit code: 0 in the original logged command.

## Documentation updates

Updated files:

```text
03_TOOLS\tool_logs\VISUAL_REVIEW_TOOLS_USAGE.md
00_CODEX_START\TOOL_INDEX.md
02_HISTORY\sessions\VISUAL_TOOLS_INSTALL_SESSION.md
```

## Visual tools final file presence check

```powershell
Test-Path required output files
```
Exit code: 0
Output:
```text

Path                                                     Exists
----                                                     ------
03_TOOLS\tool_logs\VISUAL_REVIEW_TOOLS_USAGE.md            True
00_CODEX_START\TOOL_INDEX.md                               True
02_HISTORY\command_logs\VISUAL_TOOLS_INSTALL_COMMANDS.md   True
02_HISTORY\sessions\VISUAL_TOOLS_INSTALL_SESSION.md        True



```

## Visual tools source repo final status checks

```powershell
git -C InteractiveHtmlBom/PcbDraw/kicanvas status --short
```
Exit code: 0
Output:
```text
[InteractiveHtmlBom]
[PcbDraw]
[kicanvas]

```

## Visual tools final status lines from TOOL_INDEX

```powershell
Select-String TOOL_INDEX for visual tool statuses
```
Exit code: 0
Output:
```text

LineNumber Line                                                                         
---------- ----                                                                         
        20 - Status: INSTALLED_NOT_ON_PATH                                              
        27 - Status: INSTALLED_NOT_ON_PATH                                              
        34 - Status: INSTALLED                                                          
        50 - Status: CREATED_SYNTAX_CHECKED_NOT_PROJECT_TESTED.                         
        72 - Status: INSTALLED_PROJECT_SCOPED_CODEX_CONFIGURED_ANALYSIS_ONLY            
        74 - Environment: `03_TOOLS\python_envs\kicad-mcp-pro`                          
        99 - Status: INSTALLED_ANALYSIS_ONLY                                            
       101 - Environment: `03_TOOLS\python_envs\kicad-happy`                            
       118 - Status: CLONED_NOT_INSTALLED                                               
       131 - Status: INSTALLED_OUTPUT_AUTOMATION_NOT_PROJECT_TESTED                     
       133 - Environment: `03_TOOLS\python_envs\kibot`                                  
       152 ### InteractiveHtmlBom                                                       
       153 - Status: INSTALLED_HELP_TESTED_NOT_PROJECT_TESTED                           
       155 - Environment: `03_TOOLS\python_envs\InteractiveHtmlBom`                     
       167 ### PcbDraw                                                                  
       168 - Status: INSTALLED_HELP_TESTED_NOT_PROJECT_TESTED                           
       170 - Environment: `03_TOOLS\python_envs\PcbDraw`                                
       182 ### KiCanvas                                                                 
       183 - Status: ISOLATED_NPM_BUILD_TESTED_NOT_PROJECT_TESTED                       
       185 - Isolated workspace: `03_TOOLS\node_envs\kicanvas\workspace_20260430_161903`



```
