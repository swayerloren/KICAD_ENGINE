# Windows GUI Automation Install Session

Date: 2026-04-30

## Scope

Installed Windows GUI automation Python packages into an isolated workspace venv and created passive documentation/scripts for future KiCad desktop-control experiments.

## Safety Notes

- Did not control KiCad.
- Did not click, type, move, resize, focus, or close windows.
- Did not modify KiCad project files.
- Did not install Linux tools.
- Did not move existing repos.
- Did not modify MCP permissions.

## Environment

- Venv: `03_TOOLS\python_envs\windows_gui`
- Python: 3.12.10
- pip: 25.0.1 inside the venv

## Installed Packages

- `pywinauto 0.6.9`
- `PyAutoGUI 0.9.54`
- `PyGetWindow 0.0.9`
- `pyperclip 1.11.0`
- `pillow 12.2.0`
- `opencv-python 4.13.0.92`
- `psutil 7.2.2`

Dependency packages were also installed by pip: `comtypes`, `MouseInfo`, `numpy`, `PyMsgBox`, `PyRect`, `PyScreeze`, `pytweening`, `pywin32`, and `six`.

## Import Check

Import-only check passed for:

- `pywinauto`
- `pyautogui`
- `pygetwindow`
- `pyperclip`
- `PIL`
- `cv2`
- `psutil`

## Files Created

- `03_TOOLS\windows\docs\WINDOWS_GUI_AUTOMATION_README.md`
- `03_TOOLS\windows\docs\KICAD_GUI_CONTROL_LIMITS.md`
- `03_TOOLS\windows\scripts\window_discovery\discover_windows.py`
- `03_TOOLS\windows\scripts\screenshots\take_screenshot.py`
- `02_HISTORY\command_logs\WINDOWS_GUI_AUTOMATION_INSTALL_COMMANDS.md`
- `02_HISTORY\sessions\WINDOWS_GUI_AUTOMATION_INSTALL_SESSION.md`

## Files Updated

- `00_CODEX_START\TOOL_INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Backups Created

- `99_BACKUPS\pre_codex_edits\TOOL_INDEX_BACKUP_20260430_181958.md`
- `99_BACKUPS\pre_codex_edits\README_GPT_BACKUP_20260430_181958.md`
- `99_BACKUPS\pre_codex_edits\FOR CHAT GPT_BACKUP_20260430_181958.MD`

## Status

Status: INSTALLED_IMPORT_CHECKED_PASSIVE_ONLY

The environment is ready for passive window discovery and screenshot capture. It is not approved for KiCad control yet.

## Next Recommended Prompt

Run the passive Windows GUI discovery and screenshot scripts, then create a KiCad GUI control readiness report without clicking or typing.
