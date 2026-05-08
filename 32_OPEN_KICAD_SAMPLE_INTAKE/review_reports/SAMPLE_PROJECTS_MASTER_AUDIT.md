# Sample Projects Master Audit

Generated: `2026-05-03T18:36:21Z`

Status: `READ_ONLY_ENGINEERING_AUDIT_COMPLETE`

## Summary

| sample | classification | erc | erc_signal | drc | drc_signal | unannotated | missing_footprints | embedded_or_no_prefix_fp | missing_3d_models | visual_exports |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| esp_rs_esp_rust_board | BROKEN_TEST_PROJECT | FAIL | ERC_MESSAGES_73_ERRORS_6_WARNINGS_67 | FAIL | DRC_VIOLATIONS_81; FOOTPRINT_ERRORS_95; UNCONNECTED_0 | 0 | 1 | 7 | 4 | sch=PASS; top=PASS; bottom=PASS |
| m4a1x_tps5430 | BROKEN_TEST_PROJECT | FAIL | ERC_MESSAGES_36_ERRORS_0_WARNINGS_36 | FAIL | DRC_VIOLATIONS_87; FOOTPRINT_ERRORS_30; UNCONNECTED_0 | 0 | 0 | 0 | 1 | sch=PASS; top=PASS; bottom=PASS |
| tomasr8_attiny85_dev_board | BROKEN_TEST_PROJECT | FAIL | ERC_MESSAGES_7_ERRORS_1_WARNINGS_6 | FAIL | DRC_VIOLATIONS_16; FOOTPRINT_ERRORS_13; UNCONNECTED_0 | 0 | 1 | 0 | 0 | sch=PASS; top=PASS; bottom=PASS |


## Interpretation

- `GOLDEN_PATH_CANDIDATE` means the sample is a candidate for a clean demo after human review; it is not release approval.
- `BENCHMARK_CANDIDATE` means it is useful for benchmark work after technical review.
- `BROKEN_TEST_PROJECT` means it is valuable as a failure/regression fixture.
- No sample is fabrication-ready from this audit.
- No KiCad design files were edited and no new Gerbers were generated.
- Imported upstream Gerbers, drill files, BOMs, placement files, PDFs, and STEP/STL files are source artifacts only.

## Per-Sample Reports

### esp_rs_esp_rust_board

- Engineering audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ENGINEERING_AUDIT.md`
- ERC/DRC report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ERC_DRC_REPORT.md`
- Visual audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_VISUAL_AUDIT.md`
- Gate status: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_GATE_STATUS.md`

### m4a1x_tps5430

- Engineering audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ENGINEERING_AUDIT.md`
- ERC/DRC report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ERC_DRC_REPORT.md`
- Visual audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_VISUAL_AUDIT.md`
- Gate status: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_GATE_STATUS.md`

### tomasr8_attiny85_dev_board

- Engineering audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md`
- ERC/DRC report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ERC_DRC_REPORT.md`
- Visual audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_VISUAL_AUDIT.md`
- Gate status: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_GATE_STATUS.md`
