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
- Generated manufacturing-style outputs must remain `NOT_FINAL` until the full verification gate passes.

## Tool Selection Safety
- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.
- Read `CONTROL_PLANES.md` before choosing Windows GUI control or Linux/headless workflows.

## KiCad Engine Control Planes

### 1. Common / Project Intelligence
Use first whenever possible:
- `kicad-cli`
- KiBot
- `pcbnew` Python
- MCP analysis tools
- File validators
- BOM, Gerber, and pick-and-place parsers

### 2. Windows GUI Hands/Eyes
Use only when common tools are insufficient.

Rules:
- Start with discovery only.
- Do not use coordinate clicks without screenshots and window-size verification.
- Do not randomly type into KiCad.
- Do not run production project GUI automation until the project is identified and backed up.
- Record screenshots and logs.

### 3. Linux / Headless / CI
Use for repeatable validation.

Rules:
- Run headless checks first.
- Do not write to production projects unless working on an approved copied project.
- Scripts must be repeatable and logged.

## Review Discipline
- Verify connector pinouts, polarity, voltage ratings, current ratings, thermal limits, and mechanical constraints against datasheets.
- Keep review findings separate from edits unless the user asks for implementation.
- Do not overwrite user work.
- Do not revert unrelated changes.

## GUI Automation Safety
- Do not randomly click in KiCad.
- Do not randomly type in KiCad.
- Do not send hotkeys unless explicitly approved for a specific action.
- Do not use coordinate automation without screenshot and window-size verification.
- Do not save through GUI automation without explicit approval.
- Do not use GUI automation on original finished PCB folders.
- Do not generate final fabrication outputs from GUI automation.
- Always run discovery and capture screenshots before any approved GUI control.
- Prefer UIA/Win32 element-based control over coordinates.
- Record GUI screenshots and action logs under `03_TOOLS\windows\logs`.

## Repository And Migration Safety
- Do not perform destructive repo migration.
- Do not move current repos, scripts, Python environments, Node environments, logs, or MCP config paths unless a migration prompt explicitly approves it.
- Do not modify third-party repos casually.
- Do not pull third-party repos unless explicitly requested.
- Keep legacy paths valid until a migration is approved and verified.

## Finished PCB Reference Safety
- Do not edit original finished PCB folders.
- Do not overwrite original finished PCB BOM, Gerbers, drill files, pick-and-place files, PDFs, STL files, ZIPs, backups, or KiCad files.
- If review edits or experiments are needed, create a copied reference/revision workspace first.

## Linux / Headless Safety
- Linux/headless scripts must be read-only by default.
- Do not use `sudo` inside Linux/headless scripts.
- Do not delete project files.
- Do not generate final manufacturing outputs unless verify-before-fab is explicitly approved.
- Write logs for Linux/headless checks.
- Fail safely if tools are missing.

## Secret Handling
Do not store passwords, API keys, license keys, private tokens, or credentials in:
- `01_MEMORY/`
- `02_HISTORY/`
- Project notes
- Generated reports
