# Sample Projects Index

Status: `PUBLIC_SAMPLE_INDEX`

## Purpose

This index lists controlled sample projects that KiCad Engine users can inspect
or run through the one-command gate runner.

Samples are evidence fixtures, not approved reference designs. A sample can be
useful even when it fails because the failure demonstrates that KiCad Engine
reports blockers honestly.

## Samples

| Sample | Local Path | Source | License Evidence | Current Gate Status | Public Bundle Status |
| --- | --- | --- | --- | --- | --- |
| ATtiny85 Development Board | `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/` | `https://github.com/tomasr8/attiny85-dev-board` | MIT license preserved locally and in imported original | `BLOCKED_UNTIL_HUMAN_REVIEW` | `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW` |

## ATtiny85 Fixture Summary

The ATtiny85 sample is the current controlled golden-path demo fixture. It was
selected because it is small, has schematic and PCB files, includes an explicit
MIT license in the import evidence, and is useful for demonstrating the gate
system.

Current honest status:

- It is a controlled demo fixture.
- It is not a clean passing design.
- It is blocked until human review and remaining ERC/DRC/footprint issues are
  resolved.
- It must not be used as manufacturing evidence.

Key reports:

- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md`
- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`

## Import Boundary

Raw imports live under `32_OPEN_KICAD_SAMPLE_INTAKE/`. Do not edit
`32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`. Only controlled sample copies
under `19_TEST_PROJECTS/sample_kicad_projects/` may be used for demo repair or
workflow testing, and only after backup and explicit task scope.
