# KiCad GUI Screenshot Evidence Audit

Date: `2026-05-06`

Mode: `READ_ONLY_GUI_EVIDENCE_AUDIT`

Active project:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

Target schematic:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Safety Statement

- Clicked GUI controls: `NO`
- Saved schematic: `NO`
- Annotated schematic: `NO`
- Edited schematic: `NO`
- Edited PCB: `NO`
- Generated manufacturing outputs: `NO`
- Files edited in this task: reports only

## Current GUI Detection Attempt

Fresh read-only detection at `2026-05-06T20:09:05` reported:

| Check | Result |
|---|---|
| Eeschema window detected | `NO` |
| Expected path confirmed in current window | `NO_CURRENT_WINDOW_TO_CHECK` |
| Unsaved `*` state | `NO_CURRENT_WINDOW_TO_CHECK` |
| Fresh screenshot captured | `NO` |

Because no Eeschema window was detected during the fresh check, no current live GUI screenshot could be captured safely.

## Latest Valid GUI Screenshot Used

Per task instruction, the latest valid handle-based `PrintWindow` screenshot from `_verification/gui_detection/` was used as image evidence:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_printwindow_20260506_194923.bmp`

Screenshot SHA256:

`CEF9251F3A7795A2F359B03284F7036D1298918BB0438A981FCF4E4E5C10191F`

Evidence timestamp from the prior detection report: `2026-05-06 19:49-19:51 local`

That screenshot showed:

| Field | Result |
|---|---|
| Window title | `ESP32_CSI_WIFI_NODE — Schematic Editor` |
| Title starts with `*` | `NO` |
| Open schematic path | matched target path in prior detection |
| Screenshot source | non-interactive handle-based Windows `PrintWindow` capture |

## Visible Question-Mark Reference Review

Inspection method: visual review of the latest valid full-window screenshot. No OCR was used, so the result is image-evidence level, not OCR-level certainty.

| Pattern | Schematic-body finding |
|---|---|
| `R?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `C?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `D?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `SW?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `J?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `U?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `Q?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `F?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `TP?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `MH?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `#PWR?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |
| `#FLG?` | `NOT_OBVIOUS_IN_SCHEMATIC_BODY` |

Important limitation: the screenshot is a full-window view with the schematic zoomed out. It is good enough to say no large, obvious question-mark references are visible in the schematic body, but it is not a substitute for KiCad-native ERC or close-up visual review.

Non-schematic UI note: the KiCad toolbar contains an icon/label that visually resembles `R??` / `R42`. That is not schematic content and is not counted as a schematic unresolved reference.

## Obvious Visual Defects

Result: `VISUAL_DEFECTS_FOUND`

The screenshot still shows a visually crowded schematic. At full-window scale, several functional blocks are not comfortably human-readable:

- Input power / protection area is dense and hard to inspect.
- Buck regulator area has crowded labels and symbols.
- ESP32 module block has dense pin labels and nearby labels.
- USB-C / USB ESD / CC / series resistor area is crowded.
- Reset / boot and LED sections are small and visually dense.
- Test pad and review-note areas are not presented as clean inspection-ready blocks.

This agrees with prior strict visual reports that classified the schematic as not ready for human visual approval.

## Saved-File / CLI Report Comparison

Saved-file and CLI evidence reviewed:

- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
- `reports/FINAL_SCHEMATIC_READINESS_AUDIT.md`
- `reports/STRICT_VISUAL_READABILITY_REAUDIT.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`

Comparison:

| Topic | Saved-file / CLI reports | GUI screenshot evidence | Agreement |
|---|---|---|---|
| Annotation question refs | Saved-file and CLI evidence say no unresolved `?` refs and ERC annotation message is absent. | Latest valid screenshot shows no obvious schematic-body unresolved `?` refs at full-window scale. | `AGREES_WITH_LIMITED_VISUAL_CERTAINTY` |
| Human-readable visual quality | Prior strict audits say visual readability fails. | Screenshot still shows crowded/unreadable blocks at full-page scale. | `AGREES` |
| PCB readiness | Gate file says `FAIL`, PCB update allowed `NO`. | Screenshot provides no evidence that PCB gate has passed. | `AGREES` |
| Current live GUI state | Prior valid screenshot had clean title; fresh detection now finds no Eeschema window. | No current live window to inspect. | `CURRENT_STATE_NOT_VERIFIED` |

## Final Findings

1. Detected current GUI window title: `NO_CURRENT_EESCHEMA_WINDOW_DETECTED`
2. Unsaved state: `NO_CURRENT_WINDOW_TO_CHECK`; latest valid screenshot title did not start with `*`.
3. Screenshot path used: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\kicad_gui_detection_printwindow_20260506_194923.bmp`
4. Visible `?` refs found: `NO_OBVIOUS_SCHEMATIC_BODY_QUESTION_REFS_IN_LATEST_VALID_SCREENSHOT`, with no OCR-level certainty.
5. Obvious visual defects found: `YES`
6. GUI evidence agrees with saved-file reports: `YES_FOR_NO_OBVIOUS_QUESTION_REFS_AND_VISUAL_FAIL`, with the limitation that no current live window was detected during the fresh check.
7. Manual KiCad annotation still required: `YES_FOR_FORMAL_NATIVE_GATE_CLOSURE_IF_LJ_HAS_NOT_ALREADY_RUN_AND_CONFIRMED_GUI_ERC`; this audit did not run annotation or GUI ERC.
8. Visual cleanup may resume: `NOT_FROM_THIS_AUDIT_ALONE`; first reopen/detect the schematic and confirm current GUI has no `*` title and no visible question refs, or have LJ confirm native annotation/GUI ERC is clean.
9. PCB update remains blocked: `YES`

## Status

`GUI_SCREENSHOT_EVIDENCE_AUDIT_PARTIAL`

Reason: latest valid GUI screenshot evidence is useful and agrees with saved-file reports on the main points, but a fresh current Eeschema window was not detected, so this audit cannot certify the current live GUI state.
