# Auto-Open Project Dry Run Report

Date: `2026-05-06`

Target project:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro`

Target schematic:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

Mode: `DRY_RUN_ONLY`

No KiCad live launch, annotation, save, PCB edit, routing, or manufacturing output was performed.

## Validation Commands

```powershell
python -m py_compile 33_KICAD_GUI_AUTOMATION\scripts\windows\open_kicad_project.py 33_KICAD_GUI_AUTOMATION\scripts\windows\open_schematic_editor_gui.py 33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py 33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py 33_KICAD_GUI_AUTOMATION\scripts\windows\annotate_schematic_gui.py 33_KICAD_GUI_AUTOMATION\scripts\windows\save_schematic_gui.py 33_KICAD_GUI_AUTOMATION\scripts\windows\run_erc_gui.py
```

Result: `PASS`

```powershell
[System.Management.Automation.Language.Parser]::ParseFile(... open_kicad_project.ps1 ...)
```

Result: `PASS`

## Dry-Run Results

| Script | Result | Notes |
|---|---|---|
| `open_kicad_project.py` | `DRY_RUN_TARGET_EESCHEMA_ALREADY_OPEN` | Found target project/schematic paths and KiCad executable. Existing Eeschema was already open for the target schematic, clean title, so a duplicate launch would not be needed. |
| `ensure_eeschema_open.py` | `EESCHEMA_READY_FOR_TARGET` | Existing Eeschema matched the target schematic path and had no unsaved `*` title. |
| `run_native_annotation_workflow.py` | `DRY_RUN_READY_NATIVE_ANNOTATION_FROM_CLOSED_STATE` | Would ensure Eeschema, create backup, require `--allow-annotation`, require `--allow-save`, and optionally run GUI ERC when `--allow-gui-erc` is present. |

## Current Eeschema Observation During Dry Run

- Process ID: `5408`
- Title: `ESP32_CSI_WIFI_NODE - Schematic Editor` as reported through the detector, with encoding artifacts in PowerShell JSON display.
- Command line target: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
- Path match: `true`
- Unsaved GUI state: `false`

## Live Testing Status

- Live open-from-closed-state: `NOT_RUN`
- Live open schematic editor from KiCad project manager: `NOT_RUN`
- Live annotation from closed state: `NOT_RUN`
- GUI save in this task: `NOT_RUN`
- GUI ERC in this task: `NOT_RUN`

Live use requires a future explicit prompt with:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```
