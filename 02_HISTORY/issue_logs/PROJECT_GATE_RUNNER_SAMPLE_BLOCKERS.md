# Issue Log - ATtiny85 Sample Gate Blockers

Date: `2026-05-06`

Status: `OPEN`

## Issue

The promoted ATtiny85 sample does not pass the one-command KiCad Engine project gate runner.

## Evidence

- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md`

## Blockers

1. ERC fails on `J1` shield policy.
2. DRC fails with 15 DRC violations.
3. DRC reports 13 schematic parity/footprint issues.
4. Footprint audit requires human review for `J1`, `J2`, `U2`, and polarity-sensitive parts.
5. Schematic and PCB close-up review sections remain `NOT_REVIEWED`.
6. Fabrication readiness is blocked.

## Next Step

Use this sample as a blocked-gate demo fixture until a future repair pass resolves or explicitly human-accepts the blockers.
