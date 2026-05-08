# Control Planes

This file defines how Codex chooses tools inside `C:\Users\LJ\GitHub\KICAD_ENGINE`.

Codex must read this file during startup before selecting GUI control, Linux/headless workflows, MCP actions, or manufacturing-style outputs.

## 1. Common / Project Intelligence

Root: `03_TOOLS\common`

Purpose: OS-neutral KiCad project intelligence and deterministic automation.

Use first whenever possible:

- `kicad-cli`
- KiBot
- `pcbnew` scripts
- MCP analysis tools
- BOM/Gerber/PNP parsers
- File validators
- InteractiveHtmlBom
- PcbDraw
- KiCanvas

Common tools are preferred for static inspection, ERC, DRC, deterministic exports, project inventory, BOM/Gerber/PNP review, and repeatable reports.

Current legacy paths remain valid for common tools until migration is explicitly approved:

- `03_TOOLS\repos`
- `03_TOOLS\scripts`
- `03_TOOLS\python_envs`
- `03_TOOLS\node_envs`
- `03_TOOLS\tool_logs`

Do not move current repos, scripts, Python environments, Node environments, or logs unless a migration prompt explicitly approves it.

## 2. Windows GUI Hands/Eyes

Root: `03_TOOLS\windows`

Purpose: Windows desktop GUI discovery, visual inspection, and carefully gated KiCad GUI control when CLI/API/MCP tools are insufficient.

Use for:

- pywinauto
- PyAutoGUI
- OpenCV image matching
- Screenshots
- Window discovery
- UIA/Win32 inspection
- FlaUI/FlaUInspect
- AutoHotkey
- SikuliX

Start with discovery only:

1. List windows.
2. Confirm process name and window title.
3. Capture screenshot.
4. Inspect UIA/Win32 trees if useful.
5. Decide whether GUI control is still needed.

Never use GUI automation to randomly click, type, save, close windows, or modify projects.

Known warning: the first KiCad GUI discovery run on 2026-04-30 matched VS Code as a false positive because the title contained `KICAD_ENGINE`. Future discovery must prefer confirmed KiCad process names such as `kicad.exe`, `eeschema.exe`, and `pcbnew.exe` over title-only matching.

## 3. Linux / Headless / CI

Root: `03_TOOLS\linux`

Purpose: Linux/headless/CI automation and repeatable validation.

Use for:

- Linux `kicad-cli`
- KiBot
- Xvfb
- xdotool
- wmctrl
- ydotool
- dogtail
- Docker/headless validation

Linux/headless scripts must be read-only by default, avoid `sudo` inside scripts, avoid deleting project files, write logs, and fail safely when tools are missing.

Do not assume WSL, Linux KiCad, Docker, or Linux GUI automation is configured unless the current environment check says so.

## Tool Selection Order

For any KiCad task, Codex must choose the safest workable control plane in this order:

1. Read-only file/project inspection.
2. Common project-intelligence tools:
   - `kicad-cli`
   - KiBot
   - `pcbnew`
   - MCP analysis tools
   - validators/parsers
3. Windows GUI discovery:
   - window listing
   - UI tree inspection
   - screenshots
4. Windows GUI control:
   - pywinauto
   - AutoHotkey
   - PyAutoGUI
   - SikuliX
5. Linux/headless validation:
   - Linux `kicad-cli`
   - KiBot
   - Xvfb
   - Docker
6. Design edits only after:
   - active project confirmed
   - backup completed
   - edit scope stated
   - rollback plan stated
   - verification plan stated

## Safety Rules

- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.
- Do not use GUI control on the original finished PCB folders.
- Do not use coordinate automation without screenshot and window-size verification.
- Do not save through GUI automation unless explicitly approved.
- Do not enable MCP write, destructive, parallel shared-state, or manufacturing/export authority without explicit approval.
- Do not generate final fabrication outputs from GUI automation.
- Do not migrate repos, scripts, or environments unless a migration task explicitly approves it.

## Logs And Outputs

- Windows GUI logs: `03_TOOLS\windows\logs`
- Windows GUI screenshots: `03_TOOLS\windows\logs\screenshots`
- Linux/headless logs: `03_TOOLS\linux\logs`
- Tool logs and reports: `03_TOOLS\tool_logs`
- Command logs: `02_HISTORY\command_logs`
- Session logs: `02_HISTORY\sessions`
- Design reviews: `02_HISTORY\design_reviews`
- ERC/DRC reports: `02_HISTORY\erc_drc_reports`
- Generated manufacturing-style outputs: `05_OUTPUTS` or approved project output folders, marked `NOT_FINAL` unless the verification gate passes

## Documentation Maintenance

Update `README_GPT.md` and `FOR CHAT GPT.MD` whenever any of these change:

- tool structure
- control-plane model
- legacy path compatibility
- installed tool status
- Windows GUI automation status
- Linux/headless automation status
- MCP configuration or authority
- verification scripts
- health status
- known blockers
- readiness score

If only a project changes and the engine workflow does not change, update project memory/history and update `FOR CHAT GPT.MD` only when the project change affects future ChatGPT/Codex context.

