# Golden Path Repair Log - ATtiny85 Sample

Status: `LOW_RISK_REPAIRS_APPLIED`

Generated: `2026-05-03`

## Scope

Target copy:

`19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board`

Protected original:

`32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/tomasr8_attiny85_dev_board`

The imported original was not modified.

## Backup

Backup path:

`99_BACKUPS/pre_codex_edits/20260503_145319_tomasr8_attiny85_dev_board_pre_golden_path_gate`

## Repairs Applied

| Repair | Files changed | Reason | Risk |
| --- | --- | --- | --- |
| Added project-local footprint library table for upstream custom footprint nickname. | `fp-lib-table` | KiCad project used `My footprints:MOLEX_48037-0001` and the custom footprint file was already present in `custom_footprints`. | Low; project-local mapping only. |
| Added hidden review-status metadata to high-risk parts. | `attiny85.kicad_sch` | `J1`, `J2`, and `U2` lacked explicit verification/review status. | Low-to-medium; schematic metadata only, no circuit connectivity changed. |
| Replaced default schematic visual block config with ATtiny85-specific crop windows. | `_verification/schematic_visual/visual_blocks.json` | Default ESP32-oriented crop names were not meaningful for this sample. | Low; generated review config only. |
| Added PCB visual block config for top-side close-up review. | `_verification/pcb_visual/visual_blocks.json` | The sample needed repeatable PCB close-up review evidence. | Low; generated review config only. |
| Fixed project validator library-table parsing for quoted library names containing spaces. | `03_TOOLS/scripts/project_validation/validate_kicad_project.py` | The validator falsely treated `My footprints` as unresolved even though KiCad resolved it. | Low; parser bug fix, syntax-checked. |

## Repairs Not Applied

| Issue | Reason not repaired |
| --- | --- |
| USB-A shield pin unconnected ERC error | Shield/chassis policy is a design decision. No source or user instruction proved the intended connection. |
| DRC schematic parity net conflicts | Repairing these would require PCB/netlist synchronization or net-name edits beyond low-risk demo repair. |
| Silkscreen edge clearance warnings on J1 | Could require footprint geometry or placement change; exact connector drawing and mechanical intent are not verified. |
| Connector/regulator/diode/LED exact package verification | Requires source drawing and human orientation review. |

## Result

`GOLDEN_PATH_PARTIAL`

The sample is more useful as a public demo fixture because missing footprint mapping and visual review setup were repaired. It remains blocked from clean pass or fabrication-readiness claims.
