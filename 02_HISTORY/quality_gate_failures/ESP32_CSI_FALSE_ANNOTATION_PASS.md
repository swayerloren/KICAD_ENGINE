# Quality Gate Failure: ESP32_CSI_FALSE_ANNOTATION_PASS

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

Severity: `HIGH`

Status: `REPAIRED_FOR_ANNOTATION_ONLY`

## Failure

Prior reports overclaimed annotation/visual readiness. LJ reported that the actual KiCad schematic/ERC still showed unannotated references, including question-mark references and power/flag annotation issues.

## Why This Was A Gate Failure

- A schematic was treated as improved while the user observed KiCad/ERC annotation failures.
- Earlier reports did not sufficiently distinguish saved-file checks, live GUI state, ERC output, generated visual evidence, and human-readable schematic quality.
- Automated checks were allowed to imply more than they proved.

## Repair Completed

Emergency annotation repair normalized actual placed-symbol `#PWR` and `#FLG` references in the saved schematic and reran KiCad ERC.

Evidence:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/EMERGENCY_ANNOTATION_REPAIR_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ERC_AFTER_ANNOTATION_REPAIR.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_VISIBLE_QUESTION_REFERENCE_SCAN.md`

## Remaining Gate Status

The schematic-to-PCB gate remains failed. Annotation repair does not approve visual readability, footprints, connector orientation, polarity, PMOS mapping, USB policy, PCB update, routing, or fabrication outputs.
