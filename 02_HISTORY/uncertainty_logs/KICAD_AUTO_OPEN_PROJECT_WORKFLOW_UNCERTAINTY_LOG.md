# Uncertainty Log: KiCad Auto-Open Project Workflow

Date: `2026-05-06`

## Unverified Items

- Live launch of `kicad.exe <target.kicad_pro>` from a closed state was not tested.
- Live UI Automation selection of the project-manager schematic editor control was not tested.
- Live native annotation from a fully closed state was not tested.

## Reason

The task explicitly required dry-run validation only and said not to launch KiCad live unless explicitly safe and approved.

## Follow-Up

Run a future controlled live test with KiCad closed:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py --project "<target.kicad_pro>" --schematic "<target.kicad_sch>" --live --allow-annotation --allow-save --allow-gui-erc
```

