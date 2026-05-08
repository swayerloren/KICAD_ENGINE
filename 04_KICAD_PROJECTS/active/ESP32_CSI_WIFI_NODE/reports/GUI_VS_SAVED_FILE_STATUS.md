# GUI vs Saved-File Status

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

## Current Status Summary

| Evidence Source | Status |
|---|---|
| Fresh GUI detection | `NO_EESCHEMA_WINDOW` |
| Latest valid GUI screenshot | `AVAILABLE` |
| Saved-file structured reference table | `PASS` |
| Saved-file KiCad CLI ERC | `PASS` |
| Human-readable visual quality | `FAIL` |
| Schematic-to-PCB gate | `FAIL` |
| PCB update allowed | `NO` |

## Saved-File / CLI Evidence

Saved-file and CLI reports currently state:

- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`: local `kicad-cli sch erc` reported 0 violations and no `Schematic is not fully annotated` message.
- `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`: structured reference validation found no unresolved question-mark references and no duplicate physical, `#PWR`, or `#FLG` references.
- `reports/FINAL_SCHEMATIC_READINESS_AUDIT.md`: annotation and ERC passed, but human-readable visual quality failed.
- `reports/STRICT_VISUAL_READABILITY_REAUDIT.md`: visual status failed across most schematic blocks.
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`: gate result remains `FAIL`; PCB update allowed is `NO`.

## GUI Evidence

Latest valid screenshot:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_printwindow_20260506_194923.bmp`

That screenshot shows the schematic editor title as `ESP32_CSI_WIFI_NODE — Schematic Editor` with no leading `*` and displays the target schematic.

Visual inspection of that screenshot found:

- No obvious unresolved question-mark references in the schematic body.
- Obvious crowding/unreadability in several schematic blocks.
- No evidence that the schematic-to-PCB gate has passed.

## Agreement Matrix

| Question | GUI Evidence | Saved-File / CLI Evidence | Result |
|---|---|---|---|
| Are obvious `R?`, `C?`, `D?`, `SW?`, `J?`, `U?`, `Q?`, `F?`, `TP?`, `MH?`, `#PWR?`, or `#FLG?` refs visible? | `NO_OBVIOUS_IN_LATEST_SCREENSHOT` | `NO_UNRESOLVED_REFS` | `AGREE_WITH_LIMITED_VISUAL_CERTAINTY` |
| Does the schematic look human-readable enough for approval? | `NO` | `NO` | `AGREE` |
| Is PCB update allowed? | `NO_EVIDENCE_OF_PASS` | `NO` | `AGREE` |
| Is current live GUI state verified right now? | `NO_CURRENT_EESCHEMA_WINDOW` | saved file only | `NOT_VERIFIED` |

## Manual Annotation Requirement

Formal status: `STILL_REQUIRED_UNTIL_NATIVE_GUI_GATE_IS_CLOSED`

The latest valid screenshot does not show obvious question-mark references, and saved-file/CLI evidence is clean. However, this task did not run KiCad-native annotation or GUI ERC, and the fresh GUI detection no longer found an Eeschema window. If LJ has not already run KiCad `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC` and confirmed the GUI/ERC view is clean, that manual native step remains required before the GUI annotation mismatch can be considered closed.

## Visual Cleanup Status

Visual cleanup may resume only after the current GUI state is re-established:

1. LJ opens or reopens the target schematic.
2. Read-only GUI detection confirms exact path match.
3. The title does not start with `*`.
4. The GUI view shows no visible question-mark references, or LJ confirms native annotation/GUI ERC is clean.

Even then, PCB update remains blocked until visual readability and all high-risk schematic-to-PCB gates pass.

## Final Decision

GUI vs saved-file status: `PARTIAL_AGREEMENT_CURRENT_GUI_NOT_DETECTED`

PCB update remains blocked: `YES`
