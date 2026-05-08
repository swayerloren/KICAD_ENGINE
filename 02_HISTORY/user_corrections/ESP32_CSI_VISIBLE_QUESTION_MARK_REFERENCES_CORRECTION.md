# User Correction: ESP32_CSI_VISIBLE_QUESTION_MARK_REFERENCES_CORRECTION

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

Status: `USER_CORRECTION_CONFIRMED`

## Correction

LJ reported that prior Codex reports falsely claimed schematic annotation had passed while KiCad GUI/ERC still showed unannotated references such as `J?`, `#PWR?`, `#FLG?`, and visible `D?`, `R?`, `SW?`, `C?`, `J?`.

## Required Future Behavior

- Do not accept weak regex-only annotation checks.
- Parse actual placed schematic symbols and their `Reference` properties.
- Run KiCad ERC after annotation repair.
- Scan both saved source and generated visual exports for unresolved question-mark references.
- Do not claim KiCad GUI status from stale prior reports.
- If the live GUI is not inspected, say so explicitly.

## Evidence From Repair Session

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/EMERGENCY_ANNOTATION_REPAIR_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ERC_AFTER_ANNOTATION_REPAIR.md`

## Durable Lesson

Annotation PASS requires current saved-file placed-symbol evidence plus KiCad ERC evidence. It must not be inferred from old reports or superficial token scans.
