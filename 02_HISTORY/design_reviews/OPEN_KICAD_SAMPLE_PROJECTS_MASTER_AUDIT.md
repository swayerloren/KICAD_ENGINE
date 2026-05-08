# Open KiCad Sample Projects Master Audit

Date: `2026-05-03`

Status: `READ_ONLY_ENGINEERING_AUDIT_COMPLETE`

Source report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md`

## Scope

This audit covered the normalized imported KiCad sample projects under:

`32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/`

The audit was read-only with respect to KiCad design sources. No `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, library files, Gerbers, drill files, or manufacturing outputs were edited or generated.

## Samples Audited

| sample | classification | ERC | DRC | annotation | visual export | gate result |
| --- | --- | --- | --- | --- | --- | --- |
| `esp_rs_esp_rust_board` | `BROKEN_TEST_PROJECT` | `FAIL`, 73 messages, 6 errors, 67 warnings | `FAIL`, 81 DRC violations, 95 footprint/parity errors, 0 unconnected | 0 unannotated references found | schematic/top/bottom SVG export passed | blocked |
| `m4a1x_tps5430` | `BROKEN_TEST_PROJECT` | `FAIL`, 36 messages, 0 errors, 36 warnings | `FAIL`, 87 DRC violations, 30 footprint/parity errors, 0 unconnected | 0 unannotated references found | schematic/top/bottom SVG export passed | blocked |
| `tomasr8_attiny85_dev_board` | `BROKEN_TEST_PROJECT` | `FAIL`, 7 messages, 1 error, 6 warnings | `FAIL`, 16 DRC violations, 13 footprint/parity errors, 0 unconnected | 0 unannotated references found | schematic/top/bottom SVG export passed | blocked |

## Engineering Interpretation

All three samples are useful as failure/regression fixtures. None should be promoted to:

- `GOLDEN_PATH_CANDIDATE`
- clean benchmark baseline
- reference-grade design evidence
- public payload sample
- manufacturing-ready example

The most useful next role for these samples is automated regression testing of import, inventory, ERC/DRC parsing, missing library detection, schematic/PCB visual export, and gate reporting.

## Evidence Created

Per-sample reports:

- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ENGINEERING_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ERC_DRC_REPORT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_VISUAL_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_GATE_STATUS.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ENGINEERING_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ERC_DRC_REPORT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_VISUAL_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_GATE_STATUS.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ERC_DRC_REPORT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_VISUAL_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_GATE_STATUS.md`

Generated evidence artifacts:

- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/sample_engineering_audit_command_summary.json`

## Limitations

- Close-up schematic crops were not generated because the imported samples do not include KiCad Engine visual block definitions under `_verification/schematic_visual/visual_blocks.json`.
- The audit did not repair projects, add missing libraries, migrate library references, modify footprints, or update schematics/PCBs.
- The audit did not verify license suitability beyond previously recorded import status.
- The audit did not validate actual electrical design intent against datasheets.

## Required Follow-Up

1. Keep all three samples blocked from golden-path/reference promotion.
2. Add a benchmark class for broken imported samples so they can test failure detection without being scored as valid designs.
3. Create optional normalized-sample visual block configs in a future explicitly approved repair/enrichment pass.
4. If any sample is intended for a clean benchmark, repair it in a normalized copy only, preserve the original import, and rerun ERC, DRC, visual audit, library checks, and gate review.

## Final Classification

`BROKEN_TEST_PROJECT`

