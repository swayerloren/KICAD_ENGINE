# KiCad Native Annotation Auto-Open Audit

Date: `2026-05-10`
Task type: `AUDIT_ONLY`
Scope: `Repo tooling, GUI workflow docs, startup-router updates, dry-run validation`

## Objective

Upgrade the native KiCad GUI annotation workflow so future Codex/Claude
sessions can safely recover from a closed Eeschema state, open the exact target
project/schematic, run native annotation only through explicit live flags, save
through KiCad GUI, run GUI ERC plus post-save `kicad-cli` ERC, and verify no
unresolved `?` or duplicate references remain.

## Script Changes

- Added shared helper:
  `33_KICAD_GUI_AUTOMATION/scripts/windows/gui_workflow_common.py`
- Updated:
  `ensure_eeschema_open.py`
  `open_kicad_project.py`
  `open_schematic_editor_gui.py`
  `run_native_annotation_workflow.py`
  `annotate_schematic_gui.py`
  `run_erc_gui.py`
  `save_schematic_gui.py`

## Workflow/Rule Changes

- `KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
- `KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
- `KICAD_ANNOTATION_DO_AND_DO_NOT.md`
- `KICAD_GUI_ACTION_MATRIX.md`
- `KICAD_GUI_SAFETY_GATES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_ANNOTATION_GATE.md`
- startup/router and prompt docs now point native-annotation work at the
  closed-state-safe workflow automatically

## Validation

- Python syntax check for `33_KICAD_GUI_AUTOMATION/scripts/windows/*.py`: `PASS`
- Dry-run workflow on `ESP32_CSI_WIFI_NODE`: `PASS`
  - `run_native_annotation_workflow.py` result:
    `DRY_RUN_READY_NATIVE_ANNOTATION_WORKFLOW`
  - `ensure_eeschema_open.py` result:
    `DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA`
  - observed starting state on this machine:
    `NO_EESCHEMA_WINDOW`
- Task contract validation: `PASS`
- Index rebuild: `PASS`
- No tracked or staged `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files
  changed: `PASS`

## Live Command Recorded For Future Use

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

## Notes

- This task did not run live annotation.
- This task did not edit `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files.
- The workflow now makes closed-state recovery explicit and dry-run-safe before
  any live GUI action is allowed.
