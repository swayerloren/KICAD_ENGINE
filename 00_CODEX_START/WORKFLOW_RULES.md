# Workflow Rules

## Startup Workflow
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Identify the active project.
4. Review relevant memory and history.
5. State scope before touching KiCad files.
6. Read `CONTROL_PLANES.md` before choosing common, Windows GUI, or Linux/headless tooling.

## Work Boundaries
- Work only in the active project folder for project-specific work.
- Keep active KiCad projects in `04_KICAD_PROJECTS/active/`.
- Keep templates in `04_KICAD_PROJECTS/templates/`.
- Keep legacy KiCad/Codex repositories in `03_TOOLS/repos/`.
- Keep OS-neutral/common project intelligence in `03_TOOLS/common/` or established legacy paths.
- Keep Windows GUI hands/eyes tooling in `03_TOOLS/windows/`.
- Keep Linux/headless/CI automation tooling in `03_TOOLS/linux/`.
- Keep generated outputs in `05_OUTPUTS/` unless a project explicitly tracks them.
- Keep datasheets and reference files in `06_DATASHEETS/`.
- Keep pre-edit backups in `99_BACKUPS/pre_codex_edits/`.

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
Use only when common tools are insufficient:
- pywinauto
- FlaUI
- AutoHotkey
- PyAutoGUI
- Screenshot tools
- SikuliX

Rules:
- Start with discovery only.
- Do not use coordinate clicks without screenshots and window-size verification.
- Do not randomly type into KiCad.
- Do not run production project GUI automation until the project is identified and backed up.
- Record screenshots and logs.

### 3. Linux / Headless / CI
Use for repeatable validation:
- Linux `kicad-cli`
- KiBot
- Xvfb
- xdotool
- wmctrl
- dogtail
- Docker

Rules:
- Run headless checks first.
- Do not write to production projects unless working on an approved copied project.
- Scripts must be repeatable and logged.

## Tool Selection Rule
- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.

## Common-First Workflow
For KiCad review, verification, export, and documentation tasks:

1. Start with read-only file/project inspection.
2. Use common project-intelligence tools when possible:
   - `kicad-cli`
   - KiBot
   - `pcbnew`
   - MCP analysis tools
   - validators and parsers
3. Write reports and logs to the approved history/tool/output folders.
4. Escalate to GUI discovery only when CLI/API/MCP/common tools cannot answer the question safely.

## GUI-Discovery-Before-GUI-Control Workflow
Windows GUI automation must start as discovery-only:

1. Confirm active project and whether the open project is original, copied reference, or active design.
2. Run window discovery.
3. Capture screenshots.
4. Inspect UIA/Win32 trees if useful.
5. Confirm whether GUI control is still required.
6. Prefer UIA/Win32 element-based control over coordinates.
7. Do not click, type, send hotkeys, save, or close windows without explicit approval for that action.

## Linux/Headless Workflow
Linux/headless work must be planned and logged:

1. Confirm the Linux/WSL/VM/container environment.
2. Run read-only environment checks first.
3. Use Linux `kicad-cli`, KiBot, Xvfb, Docker, or X11 helpers only when appropriate for repeatable validation.
4. Do not write to production projects unless working on an approved copied project.
5. Keep scripts repeatable, logged, and safe when tools are missing.

## Path Migration Rule
- No path migration is allowed unless the user explicitly approves a migration task.
- Do not move existing repos, scripts, Python environments, Node environments, logs, or MCP config paths during ordinary tool work.
- If a migration is approved, move one repo/tool at a time and update `TOOL_INDEX.md`, `REPO_MAP.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and history logs.

## ChatGPT Handoff Rule
- Update `FOR CHAT GPT.MD` whenever tool structure, control planes, workflow rules, active project context, known blockers, or setup readiness changes.
- If the long-form context changes, update `README_GPT.md` and keep it synchronized with `FOR CHAT GPT.MD`.

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
- Project-specific history goes in `02_HISTORY/project_history/<project-id>/`.

## Tooling Limits
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP yet.
- If a requested check cannot run because tooling is missing, explain the limitation and record it in history when relevant.
