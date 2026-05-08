# Tool Platform Strategy

This document defines the platform-aware tool structure for `KICAD_ENGINE`.

The current legacy paths remain valid:

- `03_TOOLS\repos`
- `03_TOOLS\scripts`
- `03_TOOLS\python_envs`
- `03_TOOLS\node_envs`
- `03_TOOLS\tool_logs`

Do not move existing repos, scripts, or environments until LJ explicitly approves a migration task. Existing scripts, logs, installed virtual environments, and MCP configuration may contain hardcoded legacy paths.

## Platform Roots

### `03_TOOLS\common`

Purpose: OS-neutral KiCad project intelligence and project-file automation.

Use for tools that can reasonably support Windows and Linux, or that operate on KiCad project files rather than desktop GUI state.

Examples:

- KiBot
- `kicad-cli` wrappers
- InteractiveHtmlBom
- KiCanvas
- PcbDraw
- `pcbnew` scripts
- MCP servers
- Validators and static analyzers
- Cross-platform KiCad file parsers

Subfolders:

- `03_TOOLS\common\repos`: future OS-neutral repos.
- `03_TOOLS\common\scripts`: future OS-neutral scripts.
- `03_TOOLS\common\docs`: strategy notes and common tool docs.

### `03_TOOLS\windows`

Purpose: Windows desktop GUI control and visual automation.

Use for tools that control or inspect native Windows desktop applications, KiCad GUI windows, accessibility trees, screenshots, or mouse/keyboard workflows.

Examples:

- pywinauto
- FlaUI
- FlaUInspect
- AutoHotkey
- PyAutoGUI
- SikuliX
- Inspect.exe notes
- Accessibility Insights notes
- Window discovery scripts
- Screenshot comparison scripts

Subfolders:

- `03_TOOLS\windows\repos`: future Windows-specific tool repos.
- `03_TOOLS\windows\scripts`: future Windows GUI automation scripts.
- `03_TOOLS\windows\scripts\pywinauto`: pywinauto scripts.
- `03_TOOLS\windows\scripts\pyautogui`: PyAutoGUI scripts for Windows.
- `03_TOOLS\windows\scripts\ahk`: AutoHotkey scripts.
- `03_TOOLS\windows\scripts\screenshots`: screenshot capture/review helpers.
- `03_TOOLS\windows\scripts\window_discovery`: window/control discovery helpers.
- `03_TOOLS\windows\docs`: Windows GUI automation notes.
- `03_TOOLS\windows\logs`: Windows automation logs.

### `03_TOOLS\linux`

Purpose: Linux GUI, headless, CI, and container automation.

Use for tools that run KiCad or visual automation on Linux desktops, virtual displays, containers, or CI systems.

Examples:

- xdotool
- wmctrl
- ydotool
- dogtail
- Xvfb
- x11vnc
- PyAutoGUI on X11
- SikuliX Linux
- Docker
- Linux KiCad CLI
- AppImage control scripts

Subfolders:

- `03_TOOLS\linux\repos`: future Linux-specific tool repos.
- `03_TOOLS\linux\scripts`: future Linux automation scripts.
- `03_TOOLS\linux\scripts\xdotool`: xdotool helpers.
- `03_TOOLS\linux\scripts\wmctrl`: wmctrl helpers.
- `03_TOOLS\linux\scripts\ydotool`: ydotool helpers.
- `03_TOOLS\linux\scripts\dogtail`: dogtail accessibility automation.
- `03_TOOLS\linux\scripts\xvfb`: virtual display helpers.
- `03_TOOLS\linux\scripts\screenshots`: screenshot capture/review helpers.
- `03_TOOLS\linux\scripts\appimage_control`: KiCad AppImage helpers.
- `03_TOOLS\linux\docs`: Linux automation notes.
- `03_TOOLS\linux\logs`: Linux automation logs.

## Placement Rules

- Put OS-neutral KiCad intelligence in `common`.
- Put native Windows GUI automation in `windows`.
- Put Linux/headless/CI automation in `linux`.
- Keep installed Python virtual environments in `03_TOOLS\python_envs` unless a future migration explicitly changes that rule.
- Keep installed Node workspaces in `03_TOOLS\node_envs` unless a future migration explicitly changes that rule.
- Keep existing legacy paths valid until every reference has been audited and updated.
- Do not give GUI automation tools or MCP servers destructive/write/manufacturing authority by default.

## Migration Rule

Repo migration is deferred. Before moving any existing repo:

1. Inventory all references to its current path.
2. Identify scripts, docs, config files, logs, and venv metadata that mention it.
3. Create backups.
4. Move one repo at a time.
5. Update `00_CODEX_START\TOOL_INDEX.md`, `00_CODEX_START\REPO_MAP.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`.
6. Re-run safe help/version checks.
7. Write command and session logs.
