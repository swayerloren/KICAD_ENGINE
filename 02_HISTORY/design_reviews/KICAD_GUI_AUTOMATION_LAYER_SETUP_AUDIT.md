# KiCad GUI Automation Layer Setup Audit

Date: `2026-05-06`

Status: `GUI_DISCOVERY_AND_DRY_RUN_LAYER_READY`

Live GUI control status: `BLOCKED_UNTIL_SELECTOR_WORKFLOW_VERIFIED`

## Scope

This audit covers the setup of `33_KICAD_GUI_AUTOMATION/` and related repo rules for safe KiCad schematic GUI interaction. The work was created because saved-file and CLI annotation evidence did not reliably match what LJ saw in the live KiCad schematic editor for `ESP32_CSI_WIFI_NODE`.

## Files Created

- `33_KICAD_GUI_AUTOMATION/README.md`
- `33_KICAD_GUI_AUTOMATION/INDEX.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_AUTOMATION_RULES.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_WINDOW_STATE_RULES.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_SAFETY_GATES.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_ACTION_MATRIX.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_FAILURE_MODES.md`
- `33_KICAD_GUI_AUTOMATION/scripts/README.md`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/README.md`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/detect_kicad_windows.ps1`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/detect_eeschema_window.ps1`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/detect_unsaved_kicad_state.ps1`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/screenshot_kicad_window.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/annotate_schematic_gui.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/run_erc_gui.py`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/save_schematic_gui.py`
- `33_KICAD_GUI_AUTOMATION/examples/ESP32_CSI_WIFI_NODE_SAFE_DETECTION.md`
- `33_KICAD_GUI_AUTOMATION/reports/README.md`
- `03_TOOLS/kicad/KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md`

## Files Updated

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`

## Rules Added

- KiCad GUI automation is opt-in and safety-gated.
- Window/process/path detection must run before any GUI action.
- If the Eeschema title starts with `*`, classify the state as `UNSAVED_GUI_STATE`.
- The open GUI schematic path must match the intended active project schematic path.
- GUI screenshots must be captured before and after live GUI actions once live actions are enabled.
- Annotation tasks must use KiCad-native annotation by verified GUI automation or stop with manual instructions for LJ.
- Raw `.kicad_sch` text edits are not sufficient proof that KiCad annotation is correct.
- GUI automation must not touch PCB layout, routing, zones, or manufacturing outputs.

## Validation

| Check | Result | Evidence |
|---|---:|---|
| Python syntax validation | `PASS` | `python -m py_compile` returned success for all new Python scripts. |
| PowerShell parser validation | `PASS` | Parser validation returned `PASS` for all new `.ps1` scripts. |
| Read-only Eeschema detection | `PASS` | `detect_unsaved_kicad_state.ps1` found the active Eeschema window, exact schematic path match, and `unsaved_gui_state: false`. |
| Live GUI annotation | `NOT_RUN` | Live GUI selector workflow is not verified. |
| KiCad design files edited | `NO` | This task created tooling/docs only. |

## Tool Availability

Default Python environment:

- `pywinauto`: `MISSING`
- `pyautogui`: `MISSING`
- `PIL`: `AVAILABLE`
- `mss`: `MISSING`

Existing GUI Python environment:

- Path: `03_TOOLS/python_envs/windows_gui/Scripts/python.exe`
- `pywinauto`: `AVAILABLE`
- `pyautogui`: `AVAILABLE`
- `PIL`: `AVAILABLE`
- `mss`: `MISSING`

## Current ESP32_CSI_WIFI_NODE Status

Read-only detection found an Eeschema window for:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

The detected title was `ESP32_CSI_WIFI_NODE — Schematic Editor`, with no leading `*`, so the read-only detector reported no unsaved GUI state at the time of validation.

This does not prove the schematic is layout-ready. PCB update remains blocked until native annotation/manual GUI verification, ERC, visual readability, footprint/package, and high-risk schematic-to-PCB gates pass.

## Blockers

- Live annotation automation is not production-ready because KiCad 9 menu/dialog selectors have not been verified with screenshots and controlled test actions.
- GUI ERC automation is not production-ready for the same reason.
- Save automation is dry-run/manual-fallback only until conflict handling and selector maps are verified.

## Classification

`GUI_DISCOVERY_AND_DRY_RUN_LAYER_READY`

The repo now has a safe foundation for KiCad GUI state detection and manual fallback. It does not yet have approved live GUI action automation.
