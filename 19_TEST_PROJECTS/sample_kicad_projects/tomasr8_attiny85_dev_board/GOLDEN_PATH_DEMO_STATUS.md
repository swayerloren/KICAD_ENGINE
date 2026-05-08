# Golden Path Demo Status - ATtiny85 Development Board

Status: `GOLDEN_PATH_PARTIAL_BLOCKED_UNTIL_HUMAN_REVIEW`

## Source

- Project: ATtiny85 Development Board
- Source URL: https://github.com/tomasr8/attiny85-dev-board
- Source owner: `tomasr8`
- Imported commit: `488b99063b6bdbafa0f367ecc25901b55c4c7144`
- Source intake record: `32_OPEN_KICAD_SAMPLE_INTAKE/attribution/tomasr8_attiny85_dev_board_ATTRIBUTION.md`

## License

- License: MIT License
- License evidence: `LICENSE` and `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/tomasr8_attiny85_dev_board/LICENSE`
- License confidence: `HIGH_SOURCE_FILE_PRESENT`
- Public bundle status: `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`

## Original Project Status

- Imported original preserved under `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/tomasr8_attiny85_dev_board/`
- Normalized sample preserved under `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/tomasr8_attiny85_dev_board/`
- Controlled test copy created under `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`
- Original imported copy must remain unchanged.
- Gate-run backup: `99_BACKUPS/pre_codex_edits/20260503_145319_tomasr8_attiny85_dev_board_pre_golden_path_gate`

## KiCad Engine Audit Result

- Source audit report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md`
- Gate status report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_GATE_STATUS.md`
- Classification from read-only audit: `BROKEN_TEST_PROJECT`
- Latest controlled gate report: `reports/GOLDEN_PATH_GATE_REPORT.md`
- Latest final audit: `reports/GOLDEN_PATH_FINAL_AUDIT.md`
- Controlled demo classification: `GOLDEN_PATH_PARTIAL`

## ERC Result

- Result: `FAIL`
- Signal: `ERC_MESSAGES_6_ERRORS_1_WARNINGS_5`
- Evidence: `_verification/kicad_cli/erc_after_repair.rpt`
- Blocking item: `J1` USB-A shield pin is not connected. Shield policy requires human review.

## DRC Result

- Result: `FAIL`
- Signal: `DRC_VIOLATIONS_15; SCHEMATIC_PARITY_ISSUES_13; UNCONNECTED_PADS_0`
- Evidence: `_verification/kicad_cli/drc_after_repair.rpt`
- Improvement: custom footprint library mapping is now resolved by the project-local `fp-lib-table`.

## Schematic Visual Result

- Full-page schematic SVG/PDF/PNG export: `PASS`
- Close-up crop review: `PASS_WITH_HUMAN_REVIEW_REQUIRED`
- Visible unannotated reference text scan: `NONE_DETECTED_BY_TEXT_SCAN`
- Evidence: `reports/CLOSE_UP_REVIEW.md`

## PCB Visual Result

- PCB top SVG export: `PASS`
- PCB bottom SVG export: `PASS`
- PCB close-up crop review: `PASS_WITH_WARNINGS_NEEDS_HUMAN_REVIEW`
- Evidence: `reports/PCB_CLOSE_UP_REVIEW.md`

## Footprint Audit Status

- Static footprint status: `PARTIAL`
- Previously unresolved item `My footprints:MOLEX_48037-0001` is now mapped by project-local `fp-lib-table`.
- Controlled copy includes `custom_footprints/MOLEX_48037-0001.kicad_mod`.
- Exact connector package/orientation verification: `NEEDS_HUMAN_REVIEW`
- Evidence: `reports/FOOTPRINT_PACKAGE_AUDIT.md`

## Known Issues

1. ERC does not pass because `J1` shield policy is unresolved.
2. DRC does not pass because warnings and schematic parity issues remain.
3. `J1`, `J2`, and `U2` are blocked for human footprint/orientation/package review.
4. Schematic and PCB close-up crops exist, but human visual review remains required.
5. Upstream generated Gerbers/drill files are excluded from this controlled copy.
6. Public payload inclusion remains pending final human license/release review.

## What The Demo Proves

- KiCad Engine can promote a real imported sample into a controlled test project area.
- KiCad Engine can preserve attribution and license evidence.
- KiCad Engine can keep upstream generated outputs out of a controlled demo fixture.
- KiCad Engine can apply low-risk project-local repair without touching imported originals.
- KiCad Engine can maintain honest ERC/DRC/gate status rather than claiming a false pass.
- The fixture can be used to demonstrate detection of ERC, DRC, footprint, orientation, BOM, and human-review gates.

## What The Demo Does Not Prove

- It does not prove ERC passes.
- It does not prove DRC passes.
- It does not prove the board is electrically correct.
- It does not prove footprint correctness, connector orientation, or package drawing match.
- It does not prove manufacturing readiness.
- It does not prove public-release readiness.

## Required Before Calling This A Passing Golden Path

The sample must be repaired or explicitly accepted by human review, then rechecked:

- ERC pass or documented accepted warnings
- DRC pass or documented accepted warnings
- close-up visual review complete
- footprint/package audit complete
- connector orientation reviewed
- generated outputs remain `NOT_FINAL`
- public payload license review complete
