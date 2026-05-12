# ESP32_CSI_WIFI_NODE Schematic-To-PCB Gate Status

Generated: `2026-05-06 18:45:00 -04:00`

Gate result: `FAIL`

PCB update allowed: `NO`

## Historical Annotation Warning

The annotation repair notes below are historical evidence only.

Raw structured-text repair of a saved `.kicad_sch` is not accepted as current
annotation proof under the active repo rules. Current authoritative annotation
proof must come from the KiCad-native GUI workflow plus saved-file and ERC
evidence, and live-state authority outranks older gate narratives when they
conflict.

## GUI Annotation Mismatch Addendum

Updated: `2026-05-06 18:55:00 -04:00`

LJ reports that the KiCad GUI still shows visible unannotated references such as `R?`, `D?`, `SW?`, `C?`, and `MH?`.

Windows process inspection confirms `eeschema.exe` is opened on the exact active schematic path, but its window title starts with `*`, indicating modified/unsaved GUI state:

`*ESP32_CSI_WIFI_NODE [ESP32_CSI_WIFI_NODE] - Schematic Editor`

Therefore, saved-disk parse and CLI ERC evidence must not be treated as GUI annotation approval.

Current annotation GUI gate: `FAIL_NOT_GUI_VERIFIED`

Required next step: LJ must manually run KiCad `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`, then Codex can re-check the saved file.

Visual cleanup may resume: `NO`

## Actual KiCad Annotation Repair Update

The latest annotation-only repair updated the saved schematic at:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Historical method attempt: `STRUCTURED_S_EXPRESSION`

Reason: local `kicad-cli` does not expose a schematic annotation command, so the repair parsed placed-symbol S-expressions and updated actual placed-symbol `Reference` properties plus matching KiCad-style `instances` reference blocks.

Evidence:

- `reports/ANNOTATION_REPAIR_ROLLBACK_AND_FIX_PLAN.md`
- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt`
- `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`
- `reports/ANNOTATION_REFERENCE_TABLE_FINAL.json`
- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_CHANGES.json`

Historical annotation-attempt result: `PASS_BY_KICAD_CLI_ERC_AND_STRUCTURED_REFERENCE_TABLE`

Current policy status: `NOT_ACCEPTED_AS_AUTHORITATIVE_ANNOTATION_PROOF`

KiCad ERC annotation message `Schematic is not fully annotated`: `NOT_PRESENT` in the current local `kicad-cli` ERC output.

This does not make the schematic ready for PCB update.

## Gate Summary

| Requirement | Status | Evidence |
| --- | --- | --- |
| All references annotated | `PASS_CONFIRMED_BY_KICAD_CLI_ERC_AND_REFERENCE_TABLE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`, `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md` |
| No duplicate physical references | `PASS_CONFIRMED_BY_REFERENCE_TABLE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md` |
| No duplicate `#PWR` references | `PASS_CONFIRMED_BY_REFERENCE_TABLE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md` |
| No duplicate `#FLG` references | `PASS_CONFIRMED_BY_REFERENCE_TABLE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.md` |
| No visible/stored unresolved `?` references | `PASS_FOR_QUESTION_REFS_ONLY` | direct scan and generated SVG/crop scan during annotation repair |
| Every physical symbol has a footprint candidate | `PASS_CANDIDATE_ONLY` | `reports/FOOTPRINT_ASSIGNMENT_PLAN.md` |
| ERC pass | `PASS` | `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt` |
| Full-page schematic export exists | `PASS` | `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png` |
| Close-up crops exist | `PASS_AUTOMATED_ARTIFACTS_ONLY` | `_verification/schematic_visual/crops/` |
| Human-readable visual review | `FAIL` | prior strict visual audits found readability defects; this task did not perform visual cleanup |
| BOM lock alignment | `WARN` | `PRE_SCHEMATIC_BOM_LOCK.md`, `reports/FOOTPRINT_ASSIGNMENT_PLAN.md` |
| No unresolved NEEDS_REVIEW markers | `FAIL` | `NEEDS_REVIEW_BEFORE_SCHEMATIC.md` |
| High-risk footprints verified to package drawings | `FAIL` | Candidate footprints only; no exact package drawing verification |
| Connector orientation review complete | `FAIL` | USB-C and barrel jack remain human-review required |
| PMOS pin mapping resolved | `FAIL` | AO3401A symbol/footprint pin mapping remains blocked |
| USB VBUS/shield policy resolved | `FAIL` | Still human-review required |

## Blocking Items

- Human-readable schematic visual quality is still not approved.
- High-risk package/footprint decisions are still candidate-only.
- `NEEDS_REVIEW`, `BLOCKED`, and `UNVERIFIED` markers remain.
- LJ has not completed the required visual/orientation review.
- Connector orientation, polarity-sensitive parts, PMOS pin mapping, USB VBUS policy, and USB shield policy remain blocked until human review or exact source evidence resolves them.

## Required Next Step

Do not update PCB.

LJ should close and reopen or reload the schematic in KiCad before checking GUI/ERC state, because a stale open GUI may still show the pre-repair annotation state. If LJ confirms the GUI/ERC annotation issue is gone, visual cleanup may resume as a separate visual-only task. PCB update remains forbidden unless this file is later changed to exact gate result `PASS`.
