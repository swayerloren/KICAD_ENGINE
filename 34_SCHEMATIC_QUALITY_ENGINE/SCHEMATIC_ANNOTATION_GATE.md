# Schematic Annotation Gate

## Hard Rule

Raw `.kicad_sch` text edits are not accepted as annotation proof.

## Required Annotation Evidence

- KiCad native `Annotate Schematic` was applied through the approved GUI gate,
  or LJ explicitly confirms the manual native KiCad action
- schematic saved from KiCad GUI
- GUI ERC shows no annotation violations when safely automatable
- `kicad-cli sch erc` passes after save
- saved schematic scan shows no unresolved `?` references
- duplicate-reference scan passes

## Visible Placeholder Fail List

No visible or stored unresolved:

- `R?`
- `C?`
- `D?`
- `U?`
- `J?`
- `TP?`
- `SW?`
- `MH?`
- `#PWR?`
- `#FLG?`

## Gate Result

If native annotation proof is unresolved, schematic-to-PCB progression remains
blocked even when the saved file looks annotated.

## Exact Workflow Command

Future live native annotation from a closed or open-safe state must use:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

Closed-state recovery must go through the auto-open workflow first. Raw text
annotation remains non-authoritative.
