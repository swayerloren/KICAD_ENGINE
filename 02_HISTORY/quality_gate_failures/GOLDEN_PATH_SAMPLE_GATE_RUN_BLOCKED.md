# Quality Gate Failure - Golden Path Sample Gate Run

Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

Created: `2026-05-03`

## Trigger

The promoted ATtiny85 sample was run through the gated workflow and did not achieve a clean pass.

## Evidence

- Gate report: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- ERC: `_verification/kicad_cli/erc_after_repair.rpt`
- DRC: `_verification/kicad_cli/drc_after_repair.rpt`
- Footprint audit: `reports/FOOTPRINT_PACKAGE_AUDIT.md`

## Blocking Conditions

- ERC has an unconnected USB shield error.
- DRC has violations and parity issues.
- Exact connector/regulator/header footprint verification is not complete.
- Human orientation/polarity review is not complete.
- No fabrication outputs were generated.

## Required Action

Keep the sample classified as `GOLDEN_PATH_PARTIAL` until the blockers are resolved or explicitly accepted by a human reviewer for demo-only use.
