# KiCad GUI Detection Report

Date: `2026-05-06`

Task scope: `READ_ONLY_GUI_DETECTION_ONLY`

Target schematic:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Safety Statement

- Clicked GUI controls: `NO`
- Saved schematic: `NO`
- Annotated schematic: `NO`
- Edited KiCad files: `NO`
- Updated PCB: `NO`
- Generated manufacturing outputs: `NO`

## Detection Commands

Detection used the read-only scripts under `33_KICAD_GUI_AUTOMATION/scripts/windows/`:

- `detect_kicad_windows.ps1 -Json`
- `detect_eeschema_window.ps1 -Json`
- `detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath <target> -Json`

## Running KiCad / Eeschema Window

| Field | Result |
|---|---|
| Process ID | `16892` |
| Process name | `eeschema.exe` |
| Executable path | `C:\Program Files\KiCad\9.0\bin\eeschema.exe` |
| Window title | `ESP32_CSI_WIFI_NODE — Schematic Editor` |
| Title starts with `*` | `NO` |
| Unsaved GUI state detected | `NO` |
| Command line | `"C:\Program Files\KiCad\9.0\bin\eeschema.exe" "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"` |
| Open schematic path | `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` |
| Expected schematic path match | `YES` |
| Overall read-only GUI state | `GUI_STATE_READ_ONLY_OK` |

## Window Geometry

Pywinauto read-only window enumeration found:

| Field | Result |
|---|---|
| Window handle | `2098178` |
| Class | `wxWindowNR` |
| Rectangle | `L1912, T-8, R3848, B1042` |
| Visible | `YES` |
| Enabled | `YES` |

## Screenshot Result

Valid KiCad window screenshot:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_printwindow_20260506_194923.bmp`

Screenshot method:

- First default-Python screenshot attempt failed because default Python does not have `pywinauto`.
- Second helper-script capture with the `windows_gui` Python environment produced a screenshot file, but visual inspection showed it captured the VS Code/Codex window, not KiCad. Treat that file as `INVALID_SCREENSHOT_EVIDENCE`.
- A non-interactive Windows `PrintWindow` capture by exact Eeschema window handle succeeded and produced the valid KiCad screenshot listed above.

Invalid screenshot artifacts, not to be used as KiCad evidence:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_20260506_194923.png`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_rect_20260506_194923.png`

## Conclusions

1. A running Eeschema window was detected.
2. The Eeschema window title is `ESP32_CSI_WIFI_NODE — Schematic Editor`.
3. The title does not start with `*`, so no unsaved GUI state was detected by title inspection.
4. The running process path is `C:\Program Files\KiCad\9.0\bin\eeschema.exe`.
5. The Eeschema command line points to the expected active schematic path.
6. Read-only path matching passed.
7. Screenshot evidence was captured successfully only through the final `PrintWindow` handle-based method.

## Status

`KICAD_GUI_DETECTION_PASS`

This report proves only window detection, title state, process path, open schematic path matching, and screenshot capture. It does not prove annotation correctness, ERC status, schematic visual readability, or PCB readiness.
