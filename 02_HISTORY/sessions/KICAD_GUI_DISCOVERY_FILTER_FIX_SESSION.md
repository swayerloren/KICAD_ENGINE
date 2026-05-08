# KiCad GUI Discovery Filter Fix Session

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Goal

Fix the Windows KiCad GUI discovery scripts so they only treat real KiCad processes as high-confidence KiCad windows.

## Context

The first passive discovery run matched a false positive:

- Title: `README_GPT.md - KICAD_ENGINE - Visual Studio Code`
- Process: `Code.exe`

The old filter used title text containing `kicad`, which made the workspace name `KICAD_ENGINE` appear as a KiCad candidate.

## Changes Made

- Added shared classifier: `03_TOOLS\windows\scripts\kicad_window_filter.py`.
- Updated `discover_kicad_windows.py` to classify visible windows and report high-confidence, low-confidence, and excluded windows.
- Updated `inspect_kicad_uia.py` to inspect only high-confidence KiCad process windows.
- Updated `inspect_kicad_win32.py` to inspect only high-confidence KiCad process windows.
- Updated `capture_kicad_window.py` to capture screenshots only for high-confidence KiCad process windows.
- Updated `KICAD_GUI_DISCOVERY_README.md`, `KICAD_GUI_CONTROL_LIMITS.md`, and `WINDOWS_GUI_AUTOMATION_README.md`.
- Updated `00_CODEX_START\TOOL_INDEX.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`.
- Created `03_TOOLS\windows\logs\KICAD_GUI_DISCOVERY_FILTER_FIX_REPORT.md`.

## New Rules

- High confidence requires process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Title-only matches are `LOW_CONFIDENCE_TITLE_ONLY`.
- Low-confidence title-only matches are not eligible for UIA inspection, Win32 inspection, screenshots, or control.
- `eligible_for_control` defaults to `false`.
- `--target-pid` still rejects the PID if the process name is not an allowed KiCad process.
- `--output-dir` controls report output location.

## Checks Run

Python compile check:

`PY_COMPILE_PASS`

Passive discovery:

- Report: `03_TOOLS\windows\logs\kicad_window_discovery_20260430_192204.md`
- High-confidence KiCad windows: 0
- Low-confidence title-only candidates: 2
- Excluded non-KiCad windows: 8

Passive UIA inspection:

- Report: `03_TOOLS\windows\logs\kicad_uia_inspection_20260430_192216.md`
- Inspected windows: 0

Passive Win32 inspection:

- Report: `03_TOOLS\windows\logs\kicad_win32_inspection_20260430_192216.md`
- Inspected windows: 0

Direct process check:

- `NO_KICAD_PROCESSES_FOUND`

Screenshot script:

- Not run because no high-confidence KiCad process window was found.

## Safety Notes

- No clicks were performed.
- No typing was performed.
- No hotkeys were sent.
- No windows were closed.
- KiCad was not opened.
- No files were saved.
- No KiCad projects were modified.
- ERC/DRC were not run.
- No fabrication outputs were generated.
- MCP permissions were not changed.

## Result

Filter fix result: PASS

No real KiCad window was found in the passive test environment.

The previous VS Code false-positive pattern is now low-confidence only and cannot be inspected, screenshotted, or controlled.
