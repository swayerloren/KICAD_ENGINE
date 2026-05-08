# Linux Automation README

This folder is for Linux and headless KiCad automation planning.

No Linux tools are installed by these notes or scripts. Do not assume WSL, Docker, X11, Wayland, or a Linux KiCad install exists until a Linux environment check confirms it.

## Purpose

The Linux side is for:

- Headless/CI KiCad validation.
- Repeatable command-line checks.
- Linux KiCad CLI workflows.
- X11 GUI discovery and control experiments.
- Virtual display workflows using Xvfb.
- Container or CI automation when explicitly approved.

## Tool Placement

Common OS-neutral KiCad tools remain in `03_TOOLS\common` or existing legacy paths until migration is approved.

Existing important paths remain valid:

- `03_TOOLS\repos`
- `03_TOOLS\scripts`
- `03_TOOLS\python_envs`
- `03_TOOLS\node_envs`
- `03_TOOLS\tool_logs`

Linux-specific tools and scripts belong under `03_TOOLS\linux`.

## Linux-Specific Tool Families

- `xdotool`: X11 keyboard/mouse/window inspection and automation.
- `wmctrl`: X11 window listing and desktop/window metadata.
- `ydotool`: Lower-level input automation, often relevant to Wayland or non-X11 cases.
- `dogtail`: Linux accessibility-tree automation.
- `Xvfb`: Virtual X server for headless GUI workflows.
- `x11vnc`: Remote view/control of an X session for diagnostics.
- `Docker`: Containerized CI/headless flows.
- Linux KiCad CLI: Native Linux `kicad-cli` checks and exports.

## Safety Rules

- Do not run Linux GUI automation on production files first.
- Prefer `kicad-cli`, KiBot, static file inspection, and read-only validation before GUI automation.
- Do not install packages from Windows unless a future prompt explicitly sets up WSL/Linux.
- Do not run GUI automation against real projects until active project, backups, verification plan, and rollback plan are confirmed.
- Do not treat Linux-generated outputs as final unless the full KiCad Engine fabrication gate passes.

## Starter Scripts

- `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`: read-only Linux/KiCad environment check.
- `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh`: read-only Xvfb/headless readiness check.
- `03_TOOLS\linux\scripts\xdotool\list_windows.sh`: read-only X11 window listing with `xdotool`.
- `03_TOOLS\linux\scripts\wmctrl\list_windows.sh`: read-only X11 window listing with `wmctrl`.

These scripts do not include `sudo`, install commands, delete commands, or project modification commands.
