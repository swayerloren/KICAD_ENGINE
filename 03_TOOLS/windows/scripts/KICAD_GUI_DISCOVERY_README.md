# KiCad GUI Discovery Workflow

This workflow is for read-only discovery of running KiCad desktop windows.

## Before Running

- Run KiCad manually first.
- Open no production project unless LJ explicitly intends that project to be visible during discovery.
- Do not use these scripts to open projects.
- Do not use these scripts to save KiCad files.
- Do not click, type, send hotkeys, close windows, or move windows.

## What Discovery Does

- Detects visible windows and classifies each one.
- Records window titles, process names, process IDs, handles, bounds, sizes, confidence, and eligibility.
- Treats only `kicad.exe`, `eeschema.exe`, and `pcbnew.exe` as high-confidence KiCad processes.
- Marks title-only matches as `LOW_CONFIDENCE_TITLE_ONLY`.
- Attempts UI Automation inspection through `pywinauto` UIA backend only for high-confidence KiCad process windows.
- Attempts Win32 inspection through `pywinauto` Win32 backend only for high-confidence KiCad process windows.
- Captures screenshots only for high-confidence KiCad process windows when the screenshot script is explicitly run.
- Saves markdown reports under `03_TOOLS\windows\logs`.
- Saves screenshots under `03_TOOLS\windows\logs\screenshots`.

## Candidate Confidence Model

Every candidate report includes:

- `process_name`
- `pid`
- `window_title`
- `confidence`
- `reason`
- `eligible_for_inspection`
- `eligible_for_screenshot`
- `eligible_for_control`

High-confidence KiCad windows require process name:

- `kicad.exe`
- `eeschema.exe`
- `pcbnew.exe`

Title-only matches, including VS Code windows with titles such as `KICAD_ENGINE`, `KiCad Engine`, `README_GPT`, `.kicad`, or `kicad`, are low confidence only. They are never eligible for UIA inspection, Win32 inspection, screenshots, or control.

Default `eligible_for_control` is always `false`.

## What Discovery Must Not Do

- It must not click inside KiCad.
- It must not type into KiCad.
- It must not send hotkeys.
- It must not open or modify KiCad projects.
- It must not save KiCad files.
- It must not close, move, resize, or focus KiCad windows.

## Scripts

Use the `windows_gui` venv:

`C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui`

### Discover KiCad windows

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py"
```

Optional passive parameters:

```powershell
--allow-title-only-review
--target-pid <PID>
--output-dir "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs"
```

`--allow-title-only-review` may include low-confidence candidates in reports, but they remain ineligible for control.

`--target-pid` still rejects the target if its process name is not `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.

### Inspect KiCad UIA tree

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py"
```

### Inspect KiCad Win32 tree

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py"
```

### Capture visible KiCad window screenshots

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py"
```

## Expected Limits

KiCad canvas internals may not expose schematic or PCB objects through UI Automation or Win32 control trees. If the UI tree is weak, use screenshots and visual analysis as a fallback, or prefer safer non-GUI tooling such as `kicad-cli`, KiBot, `pcbnew`, MCP analysis mode, and static KiCad file inspection.

The first passive discovery run matched VS Code because its title contained `KICAD_ENGINE`. The scripts now classify that case as `LOW_CONFIDENCE_TITLE_ONLY` and exclude it from inspection, screenshot capture, and control eligibility.

## Use Before Automation

Run this discovery workflow before any future GUI automation attempt. Any future control action requires explicit approval, active project confirmation, backups, verification plan, rollback plan, screenshot/window-size verification, and a stated expected result.
