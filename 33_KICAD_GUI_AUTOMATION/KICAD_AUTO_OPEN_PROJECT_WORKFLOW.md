# KiCad Auto-Open Project Workflow

Status: `DRY_RUN_IMPLEMENTED_LIVE_NOT_TESTED`

## Purpose

Allow future Codex/Claude sessions to recover from `NO_EESCHEMA_WINDOW` by safely opening the exact target KiCad project and schematic editor before running native GUI actions.

This workflow was created after native annotation succeeded on `ESP32_CSI_WIFI_NODE`, but an earlier attempt failed only because Eeschema was not open.

## Scope

Allowed under this workflow:

- detect KiCad/Eeschema windows
- launch the exact target `.kicad_pro` when no Eeschema window is open
- open or focus the schematic editor
- confirm the active schematic path
- capture screenshots
- hand off to native annotation/save/ERC workflow

Not allowed:

- opening a different project
- controlling PCB editor
- updating PCB from schematic
- placement, routing, zones, or manufacturing outputs
- saving a dirty `*` GUI state without explicit approval and backup
- blind clicking

## Required Inputs

- Target project path: `.kicad_pro`
- Target schematic path: `.kicad_sch`
- Active project confirmation
- Backup plan before any annotation/save-capable action

## Workflow

1. Detect Eeschema with `detect_eeschema_window.ps1`.
2. If Eeschema is open for the exact target and title is clean, continue.
3. If Eeschema is open for the exact target but title starts with `*`, stop unless LJ explicitly approves preserving/saving the GUI state.
4. If Eeschema is open for a different project, stop.
5. If no Eeschema window is open, run `open_kicad_project.py` in dry-run or live mode.
6. After KiCad project manager opens, run `open_schematic_editor_gui.py` in dry-run or live mode.
7. Verify Eeschema command line points to the exact target `.kicad_sch`.
8. Capture screenshot.
9. Only then continue to native annotation, save, and ERC gates.

## Commands

Dry-run:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
```

Live open only:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live
```

Future native annotation from closed state:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

## Current Validation

- Python syntax validation: required before use.
- PowerShell parser validation: required before use.
- Dry-run validation: required and safe.
- Live launch from closed state: not tested in this documentation task.
- Live annotation from closed state: not tested in this documentation task.

