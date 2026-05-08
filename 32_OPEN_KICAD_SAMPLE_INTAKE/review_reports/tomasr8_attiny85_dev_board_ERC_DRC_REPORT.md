# ERC/DRC Report - tomasr8_attiny85_dev_board

Generated: `2026-05-03T18:36:21Z`

Status: `READ_ONLY_KICAD_CLI_CHECK`

## ERC

Command: `kicad-cli sch erc --format report --severity-all --exit-code-violations --output C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\tomasr8_attiny85_dev_board\tomasr8_attiny85_dev_board_erc.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\tomasr8_attiny85_dev_board\attiny85.kicad_sch`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\tomasr8_attiny85_dev_board`

Exit code: `5`

Report path: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts/tomasr8_attiny85_dev_board/tomasr8_attiny85_dev_board_erc.rpt`

Report signal: `ERC_MESSAGES_7_ERRORS_1_WARNINGS_6`

### STDOUT Excerpt

```text
Found 7 violations
Saved ERC Report to C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\tomasr8_attiny85_dev_board\tomasr8_attiny85_dev_board_erc.rpt

```

## DRC

Command: `kicad-cli pcb drc --format report --severity-all --schematic-parity --exit-code-violations --output C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\tomasr8_attiny85_dev_board\tomasr8_attiny85_dev_board_drc.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\tomasr8_attiny85_dev_board\attiny85.kicad_pcb`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\tomasr8_attiny85_dev_board`

Exit code: `5`

Report path: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts/tomasr8_attiny85_dev_board/tomasr8_attiny85_dev_board_drc.rpt`

Report signal: `DRC_VIOLATIONS_16; FOOTPRINT_ERRORS_13; UNCONNECTED_0`

### STDOUT Excerpt

```text
Found 16 violations
Found 0 unconnected items
Found 13 schematic parity issues
Saved DRC Report to C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\tomasr8_attiny85_dev_board\tomasr8_attiny85_dev_board_drc.rpt

```

## Interpretation

A nonzero exit means KiCad reported violations or the command failed. This audit does not repair projects and does not override KiCad results.
