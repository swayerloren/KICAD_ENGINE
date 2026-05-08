# ESP32_CSI_WIFI_NODE Actual KiCad Annotation Repair Session

Date: `2026-05-06`

Active project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

Target schematic: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

## User Correction

LJ reported that KiCad ERC remained the source of truth and still showed annotation failures, including duplicate/unannotated `J?`, `R?`, `C?`, `D?`, `U?`, `SW?`, `TP?`, `MH?`, `#PWR?`, and `#FLG?` references. Prior annotation PASS reports were not trusted.

## Scope

Annotation/ERC only.

Not performed:

- visual layout cleanup
- symbol movement
- value changes
- footprint assignment or changes
- PCB edits
- PCB update from schematic
- routing
- manufacturing output generation

## Backup

Backup folder:

`99_BACKUPS/pre_codex_edits/20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair`

Pre-repair schematic SHA256:

`E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7`

Backup schematic SHA256:

`E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7`

Post-repair schematic SHA256:

`D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`

## Method

KiCad-native annotation via CLI was checked first. Local `kicad-cli sch --help` provides ERC/export commands but no annotation subcommand.

Repair method used: `STRUCTURED_S_EXPRESSION`

The saved schematic was parsed as placed-symbol S-expressions. The repair updated actual placed-symbol `Reference` properties and added KiCad-style instance reference blocks matching each placed symbol UUID.

## Results

| Item | Result |
| --- | --- |
| Placed symbols | `79` |
| Physical symbols | `43` |
| Power symbols | `33` |
| PWR_FLAG symbols | `3` |
| Missing instance refs after repair | `0` |
| Instance/ref mismatches after repair | `0` |
| Unresolved question references after repair | `0` |
| Duplicate physical refs after repair | `0` |
| Duplicate `#PWR` refs after repair | `0` |
| Duplicate `#FLG` refs after repair | `0` |
| KiCad CLI ERC | `PASS`, 0 errors, 0 warnings |
| `Schematic is not fully annotated` in local ERC | `NO` |

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ROLLBACK_AND_FIX_PLAN.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_FINAL.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_CHANGES.json`

## Remaining Blockers

PCB update remains blocked. This session fixed annotation evidence only. Visual readability, exact footprint/package verification, connector orientation, PMOS pin mapping, USB VBUS/shield policy, and LJ review remain unresolved.

## GUI Reload Note

If KiCad GUI had this schematic open while the file was repaired, LJ should close and reopen/reload the schematic before checking GUI/ERC state.
