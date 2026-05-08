# Quality Gate Failure: Prior False Annotation Pass Confirmed

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

Severity: `HIGH`

Status: `REPAIRED_FOR_ANNOTATION_ONLY`

## Failure

Prior reports treated annotation as passing, but LJ reported that KiCad GUI/ERC still showed unresolved or duplicate annotation references such as `J?`, `R?`, `C?`, `D?`, `U?`, `SW?`, `TP?`, `MH?`, `#PWR?`, and `#FLG?`, plus `Schematic is not fully annotated`.

This meant prior annotation PASS evidence was not strong enough. A direct regex scan or narrow placed-property check was insufficient because KiCad annotation also depends on actual placed-symbol and instance reference state.

## Corrective Action

An annotation-only repair was performed on:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Corrective action included:

- parsing actual placed-symbol S-expressions
- updating actual `Reference` properties
- adding matching KiCad-style `instances` reference blocks
- assigning unique `#PWR0101` through `#PWR0133`
- assigning unique `#FLG0101` through `#FLG0103`
- rerunning KiCad CLI ERC
- exporting a final reference table

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_FINAL.json`

## Current Result

Local saved-file validation now shows:

- KiCad CLI ERC: `PASS`, 0 errors, 0 warnings
- `Schematic is not fully annotated`: not present in local ERC output
- unresolved question references: `0`
- duplicate physical references: `0`
- duplicate `#PWR` references: `0`
- duplicate `#FLG` references: `0`
- missing instance references: `0`

## Remaining Gate Status

PCB update remains blocked. This quality-gate failure is repaired only for annotation/ERC. It does not approve visual readability, footprints, connector orientation, PMOS pin mapping, USB policy, or PCB transition.

## Required Future Rule

Do not mark annotation as pass unless:

1. actual placed-symbol `Reference` properties are exported and checked,
2. KiCad instance references are present and match,
3. duplicate checks include physical refs, `#PWR`, and `#FLG`,
4. direct unresolved `?` scans pass, and
5. KiCad ERC does not report `Schematic is not fully annotated`.
