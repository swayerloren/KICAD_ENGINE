# KiCad GUI Discovery Run Session

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Goal

Run read-only Windows GUI discovery against the currently open KiCad application.

## Safety Rules Followed

- No clicks were performed.
- No typing was performed.
- No hotkeys were sent.
- KiCad was not closed.
- No KiCad files were saved.
- No KiCad project files were modified.
- No ERC, DRC, export, or fabrication commands were run.

## Environment

- Python venv: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui`
- Python executable: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe`
- Log root: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs`

## Commands Run

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py'
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py'
Get-Process -Name kicad,eeschema,pcbnew -ErrorAction SilentlyContinue
Get-Process | Where-Object { $_.ProcessName -match 'kicad|eeschema|pcbnew' -or $_.MainWindowTitle -match '\bKiCad\b|PCB Editor|Schematic Editor|Footprint Editor' }
```

## Outputs Created

- Window discovery report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_window_discovery_20260430_184630.md`
- UIA inspection report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_uia_inspection_20260430_184649.md`
- Win32 inspection report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_win32_inspection_20260430_184649.md`
- Screenshot report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_window_screenshot_20260430_184700.md`
- Screenshot file: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\screenshots\kicad_window_20260430_184700_README_GPT_md_-_KICAD_ENGINE_-_Visual_Studio_Code_33864.png`

## Discovery Result

The scripts detected one candidate window:

- Title: `README_GPT.md - KICAD_ENGINE - Visual Studio Code`
- Process ID: `33864`
- Process name: `Code.exe`
- Bounds: `1912,-8,3848,1042`
- Size: `1936x1050`

This was a false positive. The discovery scripts treat any visible window title containing `kicad` as a KiCad candidate, so the VS Code window was matched because the workspace title contains `KICAD_ENGINE`.

Direct process checks found no visible or running `kicad.exe`, `eeschema.exe`, or `pcbnew.exe` process during this run.

## UIA Inspection Result

- UIA report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_uia_inspection_20260430_184649.md`
- Candidate inspected: VS Code false positive
- Process name: `Code.exe`
- Controls recorded: `7`

UIA did not inspect a real KiCad window in this run.

## Win32 Inspection Result

- Win32 report: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\kicad_win32_inspection_20260430_184649.md`
- Candidate inspected: VS Code false positive
- Process name: `Code.exe`
- Controls recorded: `3`

Win32 did not inspect a real KiCad window in this run.

## Screenshot Result

The screenshot script captured the same false-positive VS Code window:

`C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs\screenshots\kicad_window_20260430_184700_README_GPT_md_-_KICAD_ENGINE_-_Visual_Studio_Code_33864.png`

No confirmed KiCad application screenshot was captured.

## Feasibility Assessment

GUI automation is not ready for control based on this run.

The passive scripts themselves ran without sending input, but the candidate filtering needs to be stricter before any control task. Future discovery should prefer process-name matching for `kicad.exe`, `eeschema.exe`, and `pcbnew.exe`, and should treat title-only matches as low-confidence candidates unless the process is also KiCad.

## What Should Stay CLI/API Controlled

Use CLI/API/MCP/KiBot for:

- ERC
- DRC
- BOM export and parsing
- Gerber/drill/STEP exports
- project file discovery
- backup workflows
- deterministic report generation
- BOM/Gerber/PNP validation

Use Windows GUI discovery only for read-only window/UI visibility checks until a real KiCad window is confirmed and a safer filter is in place.

## Recommended Next Step

Fix the Windows GUI discovery scripts to avoid matching VS Code or other non-KiCad windows whose titles contain `KICAD_ENGINE`. Then open KiCad visibly and rerun discovery-only checks.
