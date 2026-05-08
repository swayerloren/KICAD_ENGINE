# KiCad GUI Automation Rules

Status: `MANDATORY`

## Core Rule

GUI automation is opt-in, safety-gated, and evidence-producing. It is not a general permission to click around KiCad.

## Mandatory Rules

1. Detect the KiCad/Eeschema window before any GUI action.
2. Confirm the open GUI path matches the active project schematic.
3. Treat a title beginning with `*` as `UNSAVED_GUI_STATE`.
4. Capture a screenshot before and after any approved GUI action.
5. Create or confirm a backup before any action that could save or modify a KiCad file.
6. Never save an unsaved GUI state unless the user explicitly approves overwriting the disk file.
7. Stop if more than one Eeschema window is open unless the correct window is unambiguously identified.
8. Stop if the GUI path and expected schematic path disagree.
9. Stop if pywinauto/pyautogui are unavailable and the requested action requires GUI control.
10. Never touch PCB layout, routing, copper zones, board setup, or manufacturing outputs from this GUI layer.

## Annotation Rule

For annotation tasks, raw `.kicad_sch` text edits are not enough. The accepted paths are:

- verified KiCad-native annotation through GUI automation on the exact active schematic, or
- manual LJ action in KiCad followed by saved-file and GUI verification.

If neither is possible, classify as `BLOCKED_PENDING_KICAD_NATIVE_ANNOTATION`.

The first verified live automation success is `ESP32_CSI_WIFI_NODE` on `2026-05-06`: native dialog opened, annotation applied, schematic saved from GUI, GUI ERC showed `Violations (0)`, `kicad-cli` ERC passed, the saved schematic had 0 unresolved `?` references, and duplicate-reference checks passed. Use `KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md` as the model.

## Required Evidence

For any GUI-assisted annotation session, capture:

- before screenshot
- process command line
- window title
- unsaved state
- expected-vs-open path comparison
- backup path
- annotation action log
- after screenshot
- GUI ERC result or manual ERC confirmation
- saved-file reference table after save

## Annotation Gate Evidence

The authoritative annotation gate is:

1. Native KiCad annotation applied.
2. Schematic saved from KiCad GUI.
3. GUI ERC 0 violations when safely automatable.
4. `kicad-cli` ERC pass after GUI save.
5. Saved schematic scan 0 unresolved `?` references.
6. Duplicate-reference scan pass.

Visual cleanup may resume after this gate, but only as a separate task. PCB update remains blocked until the full schematic-to-PCB gate passes.

## Prohibited

- coordinate clicks without screenshot and window-size verification
- blind hotkeys
- saving a dirty GUI state without user approval
- relying on file regex scans as GUI proof
- continuing visual cleanup when the GUI still shows question-mark references
