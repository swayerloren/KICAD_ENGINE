# KiCad GUI Automation Index

## Core Docs

- `README.md` - purpose and current status.
- `KICAD_GUI_AUTOMATION_RULES.md` - mandatory rules for agents.
- `KICAD_WINDOW_STATE_RULES.md` - how to interpret GUI title/path state.
- `KICAD_NATIVE_ANNOTATION_WORKFLOW.md` - native annotation workflow and fallback.
- `KICAD_GUI_SAFETY_GATES.md` - required gates before GUI actions.
- `KICAD_GUI_ACTION_MATRIX.md` - allowed, gated, and prohibited actions.
- `KICAD_GUI_FAILURE_MODES.md` - expected failure modes and responses.

## Windows Scripts

- `scripts/windows/detect_kicad_windows.ps1`
- `scripts/windows/detect_eeschema_window.ps1`
- `scripts/windows/detect_unsaved_kicad_state.ps1`
- `scripts/windows/screenshot_kicad_window.py`
- `scripts/windows/annotate_schematic_gui.py`
- `scripts/windows/run_erc_gui.py`
- `scripts/windows/save_schematic_gui.py`

## Reports

Generated GUI automation reports belong under `reports/`.

## Examples

Safe usage examples belong under `examples/`.
