# KiCad Auto-Open Project Workflow Audit

Date: `2026-05-06`

## Purpose

Audit the new dry-run-first workflow that lets future agents open the exact KiCad project and schematic editor when Eeschema is not already open.

## Scope

Target project:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro`

Target schematic:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Files Created

- `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/open_kicad_project.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/open_kicad_project.ps1`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/open_schematic_editor_gui.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/ensure_eeschema_open.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/run_native_annotation_workflow.py`
- `33_KICAD_GUI_AUTOMATION/reports/AUTO_OPEN_PROJECT_DRY_RUN_REPORT.md`

## Existing Scripts Upgraded

- `33_KICAD_GUI_AUTOMATION/scripts/windows/annotate_schematic_gui.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/save_schematic_gui.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/run_erc_gui.py`

These still default to dry-run and require explicit live/action flags.

## Documentation Updated

- `33_KICAD_GUI_AUTOMATION/README.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_ACTION_MATRIX.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/README.md`
- `03_TOOLS/kicad/KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Validation

| Check | Result |
|---|---|
| Python syntax check | `PASS` |
| PowerShell parser check | `PASS` |
| Dry-run `open_kicad_project.py` | `PASS` |
| Dry-run `ensure_eeschema_open.py` | `PASS` |
| Dry-run `run_native_annotation_workflow.py` | `PASS` |
| KiCad live launch | `NOT_RUN` |
| Live annotation | `NOT_RUN` |
| KiCad design files edited | `NO` |
| PCB files edited | `NO` |
| Manufacturing outputs generated | `NO` |

## Behavior Added

Future agents can now use a staged workflow:

1. Detect whether Eeschema is open.
2. If Eeschema is open for the exact target and clean, proceed.
3. If Eeschema is open for a different target, stop.
4. If Eeschema title starts with `*`, stop unless explicit approval handles unsaved state.
5. If no Eeschema window is open, live mode can launch the exact `.kicad_pro` with `--live`.
6. The schematic editor can be opened only through detectable GUI controls.
7. Native annotation requires `--allow-annotation`.
8. Save requires `--allow-save`.
9. GUI ERC requires `--allow-gui-erc`.

## Remaining Risk

Live open-from-closed-state has not been tested in this task. It must be tested later with explicit approval while KiCad is closed or in a controlled state. The scripts are designed to stop on ambiguous windows, dirty `*` titles, different projects, or missing controls.

## Classification

`DRY_RUN_READY_LIVE_TEST_REQUIRED`

