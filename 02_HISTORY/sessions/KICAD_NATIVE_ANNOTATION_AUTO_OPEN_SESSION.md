# KiCad Native Annotation Auto-Open Session

Date: `2026-05-10`
Task type: `AUDIT_ONLY`
Repo: `C:\Users\LJ\GitHub\KICAD_ENGINE`
Validation target: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Summary

Upgraded the native KiCad GUI annotation workflow so it is dry-run by default,
can safely recover from a closed Eeschema state, uses explicit live flags for
open/annotation/save/ERC actions, and bundles the full post-save proof chain
into the main workflow wrapper.

## Key Results

- Closed-state recovery is now an explicit auto-open workflow instead of an
  implied prerequisite.
- The main live workflow now requires:
  `--live --allow-annotation --allow-save --allow-gui-erc`
- The full workflow now records:
  - backup path
  - before screenshot
  - native annotation result
  - GUI save result
  - GUI ERC result
  - after screenshot
  - post-save `kicad-cli` ERC result
  - saved-schematic unresolved-`?` and duplicate-reference scans

## Dry-Run Evidence

- `run_native_annotation_workflow.py`:
  `DRY_RUN_READY_NATIVE_ANNOTATION_WORKFLOW`
- `ensure_eeschema_open.py`:
  `DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA`
- detected starting GUI state:
  `NO_EESCHEMA_WINDOW`

## Safety Outcome

- No live annotation was performed.
- No KiCad design files were edited.
- No PCB update, routing, zone work, or manufacturing outputs were run.
