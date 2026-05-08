# Claim Evidence Matrix - Golden Path Sample Gate Run

Date: `2026-05-03`

| Claim | Status | Evidence |
| --- | --- | --- |
| Promoted sample was backed up before edits. | `VERIFIED_BY_FILE` | `99_BACKUPS/pre_codex_edits/20260503_145319_tomasr8_attiny85_dev_board_pre_golden_path_gate` |
| Imported original was not edited. | `PARTIALLY_VERIFIED` | Work commands and edits targeted `19_TEST_PROJECTS/...`; no edits were intentionally made under `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals`. |
| Custom footprint library mapping was repaired. | `VERIFIED_BY_FILE` | `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/fp-lib-table` |
| Annotation now passes. | `VERIFIED_BY_COMMAND` | `reports/ANNOTATION_CHECK.md` |
| ERC still fails. | `VERIFIED_BY_COMMAND` | `_verification/kicad_cli/erc_after_repair.rpt` |
| DRC still fails but has zero unconnected pads. | `VERIFIED_BY_COMMAND` | `_verification/kicad_cli/drc_after_repair.rpt` |
| Schematic visual exports and crops were generated. | `VERIFIED_BY_FILE` | `_verification/schematic_visual` and `reports/CLOSE_UP_REVIEW.md` |
| PCB visual exports and crops were generated. | `VERIFIED_BY_FILE` | `_verification/pcb_visual` and `reports/PCB_CLOSE_UP_REVIEW.md` |
| BOM was exported as review-only. | `VERIFIED_BY_FILE` | `_verification/bom/attiny85_BOM_NOT_FINAL.csv` |
| Sample is not fabrication ready. | `VERIFIED_BY_COMMAND` | ERC/DRC failures plus no fab outputs generated. |
