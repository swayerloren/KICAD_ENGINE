# KiCad GUI Discovery Workflow Created

Date: 2026-04-30

## Scope

Created a safe Windows KiCad GUI discovery workflow for passive window discovery, UIA inspection, Win32 inspection, screenshot capture, and process/window metadata collection.

## Safety Notes

- Did not click inside KiCad.
- Did not type into KiCad.
- Did not send hotkeys.
- Did not open or modify KiCad projects.
- Did not save KiCad files.
- Did not run discovery against KiCad during creation.
- Did not control KiCad windows.
- Did not modify MCP permissions.

## Files Created

- `03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py`
- `03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py`
- `03_TOOLS\windows\scripts\KICAD_GUI_DISCOVERY_README.md`

## Files Updated

- `00_CODEX_START\TOOL_INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Backups Created

- `99_BACKUPS\pre_codex_edits\TOOL_INDEX_BACKUP_20260430_183246.md`
- `99_BACKUPS\pre_codex_edits\README_GPT_BACKUP_20260430_183246.md`
- `99_BACKUPS\pre_codex_edits\FOR CHAT GPT_BACKUP_20260430_183246.MD`

## Checks Run

Syntax checks:

- `discover_kicad_windows.py`: passed
- `inspect_kicad_uia.py`: passed
- `inspect_kicad_win32.py`: passed
- `capture_kicad_window.py`: passed

Dependency import checks:

- `pywinauto`: passed
- `pygetwindow`: passed
- `psutil`: passed
- `PIL`: passed
- `PIL.ImageGrab`: passed

## How To Run Discovery

Run KiCad manually first. Open no production project unless LJ intends that project to be visible during discovery.

Use:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py"
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py"
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py"
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py"
```

Reports are written under `03_TOOLS\windows\logs`. Screenshots are written under `03_TOOLS\windows\logs\screenshots`.

## Next Recommended Prompt

Run the KiCad GUI discovery workflow with KiCad manually opened to a non-production blank/session state, then create a no-control GUI readiness report from the generated logs.
