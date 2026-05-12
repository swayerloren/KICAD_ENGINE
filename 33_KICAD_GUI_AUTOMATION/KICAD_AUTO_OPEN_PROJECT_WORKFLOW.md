# KiCad Auto-Open Project Workflow

Status: `DRY_RUN_IMPLEMENTED_LIVE_GATED`

## Purpose

Allow future Codex/Claude sessions to recover safely when Eeschema is closed by
opening the exact target `.kicad_pro`, then opening or focusing the exact
target schematic editor before native annotation.

## Hard Rules

1. If Eeschema is not open, attempt the open path in dry-run first.
2. Launch only the exact requested `.kicad_pro`.
3. If Eeschema is open for a different project, stop.
4. If the matching Eeschema title starts with `*`, stop unless explicitly
   allowed.
5. Opening the project/schematic does not grant permission to annotate, save,
   run ERC, update PCB, route, or generate outputs.

## Workflow

1. Detect Eeschema window state for the exact target `.kicad_sch`.
2. If the target schematic is already open and clean, continue without opening
   anything else.
3. If a different-project Eeschema window is open, stop.
4. If the matching target Eeschema window is dirty with `*`, stop unless
   explicitly allowed.
5. If no Eeschema window is open, dry-run or live-launch the exact
   `.kicad_pro`.
6. Open or focus the schematic editor from the KiCad project manager.
7. Re-check that `eeschema.exe` now points to the exact target `.kicad_sch`.

## Dry-Run Command

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
```

## Live Open Only

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live
```

If the matching target Eeschema window is already dirty and LJ explicitly wants
to preserve/save that GUI state, add:

```powershell
--allow-unsaved-existing
```

## Hand-Off To Native Annotation

After the exact target schematic is open, use the native annotation workflow:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

## Expected Dry-Run Result

When Eeschema is closed and the target paths are valid, the dry-run result from
`ensure_eeschema_open.py` should be:

`DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA`

That is the proof that Codex can safely attempt to open the schematic if it is
closed, without touching the design in dry-run mode.
