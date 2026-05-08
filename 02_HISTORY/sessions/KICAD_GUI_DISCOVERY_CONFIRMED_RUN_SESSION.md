# KiCad GUI Discovery Confirmed Run Session

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Goal

Run read-only KiCad GUI discovery using the fixed high-confidence process filter while KiCad was manually open and visible.

## Safety Rules Followed

- No clicks were performed.
- No typing was performed.
- No hotkeys were sent.
- No windows were closed.
- No files were saved.
- No KiCad project files were modified.
- ERC/DRC were not run.
- No fabrication or project outputs were generated.
- MCP permissions were not changed.
- GUI control remained disabled; `eligible_for_control=false`.

## Commands Run

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' `
  'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py' `
  --allow-title-only-review `
  --output-dir 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs'

& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' `
  'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py' `
  --allow-title-only-review `
  --output-dir 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs'

& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' `
  'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py' `
  --allow-title-only-review `
  --output-dir 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs'

& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe' `
  'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py' `
  --allow-title-only-review `
  --output-dir 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\logs'
```

The screenshot script was run only after discovery found a high-confidence KiCad process window.

## Discovery Result

Report:

`03_TOOLS\windows\logs\kicad_window_discovery_20260430_192803.md`

Result:

- Total visible windows scanned: 11
- High-confidence KiCad windows: 1
- Low-confidence title-only candidates: 2
- Excluded non-KiCad windows: 8

High-confidence KiCad window:

- Process name: `kicad.exe`
- PID: `19576`
- Window title: `COMMAND LINK DRAFT — KiCad 9.0`
- Confidence: `HIGH_CONFIDENCE_KICAD_PROCESS`
- `eligible_for_inspection=true`
- `eligible_for_screenshot=true`
- `eligible_for_control=false`
- Bounds: `2403,191,3357,842`
- Size: `954x651`

Low-confidence title-only candidates:

- `Code.exe`, PID `33864`, title `FOR CHAT GPT.MD - KICAD_ENGINE - Visual Studio Code`
- `chrome.exe`, PID `20048`, title `Open Source KiCad Integration - Google Chrome - Lj_stuntz`

Both low-confidence candidates had inspection, screenshot, and control eligibility disabled.

## UIA Inspection Result

Report:

`03_TOOLS\windows\logs\kicad_uia_inspection_20260430_192817.md`

Result:

- Inspected KiCad windows: 1
- Inspected process: `kicad.exe`
- Inspected PID: `19576`
- Controls recorded: 65
- Low-confidence title-only candidates were not inspected.

## Win32 Inspection Result

Report:

`03_TOOLS\windows\logs\kicad_win32_inspection_20260430_192816.md`

Result:

- Inspected KiCad windows: 1
- Inspected process: `kicad.exe`
- Inspected PID: `19576`
- Controls recorded: 241
- Low-confidence title-only candidates were not inspected.

## Screenshot Result

Report:

`03_TOOLS\windows\logs\kicad_window_screenshot_20260430_192827.md`

Screenshot:

`03_TOOLS\windows\logs\screenshots\kicad_window_20260430_192827_COMMAND_LINK_DRAFT_KiCad_9_0_19576.png`

Result:

- Screenshot count: 1
- Captured only the high-confidence `kicad.exe` window.
- Low-confidence title-only candidates were not captured.

## Assessment

The fixed filter is reliable for process-level KiCad GUI discovery:

- Real KiCad process detection worked.
- VS Code and Chrome title-only false positives were not inspected or captured.
- Control remained disabled for every candidate.

GUI automation should remain discovery-only for now. The next step can be a gated control-readiness test, but not actual GUI control, and only if LJ explicitly approves a non-destructive readiness prompt.

## Documentation Updated

- `00_CODEX_START\TOOL_INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

Backups were created in `99_BACKUPS\pre_codex_edits` before those documentation edits.
