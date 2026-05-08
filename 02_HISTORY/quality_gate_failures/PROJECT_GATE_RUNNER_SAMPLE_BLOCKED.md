# Quality Gate Failure - ATtiny85 Gate Runner Sample

Date: `2026-05-06`

Scope: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board`

Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Evidence

- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`
- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.json`

## Blocking Areas

- ERC error on `J1` USB-A shield policy.
- DRC violations and schematic parity issues.
- `J1` Molex USB-A footprint/orientation requires exact drawing review.
- `J2` programming header orientation/pinout requires human review.
- `U2` AMS1117 footprint/package/pin mapping requires source review.
- Schematic and PCB visual crop sections remain human-review-required.
- Fabrication readiness is blocked.

## Required Resolution

Resolve or explicitly human-accept upstream blockers, regenerate evidence reports, then rerun the project gate runner.
