# ERC/DRC Report - m4a1x_tps5430

Generated: `2026-05-03T18:36:21Z`

Status: `READ_ONLY_KICAD_CLI_CHECK`

## ERC

Command: `kicad-cli sch erc --format report --severity-all --exit-code-violations --output C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\m4a1x_tps5430\m4a1x_tps5430_erc.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\m4a1x_tps5430\TPS5430.kicad_sch`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\m4a1x_tps5430`

Exit code: `5`

Report path: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts/m4a1x_tps5430/m4a1x_tps5430_erc.rpt`

Report signal: `ERC_MESSAGES_36_ERRORS_0_WARNINGS_36`

### STDOUT Excerpt

```text
Found 36 violations
Saved ERC Report to C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\m4a1x_tps5430\m4a1x_tps5430_erc.rpt

```

## DRC

Command: `kicad-cli pcb drc --format report --severity-all --schematic-parity --exit-code-violations --output C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\m4a1x_tps5430\m4a1x_tps5430_drc.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\m4a1x_tps5430\TPS5430.kicad_pcb`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\normalized_samples\m4a1x_tps5430`

Exit code: `5`

Report path: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts/m4a1x_tps5430/m4a1x_tps5430_drc.rpt`

Report signal: `DRC_VIOLATIONS_87; FOOTPRINT_ERRORS_30; UNCONNECTED_0`

### STDOUT Excerpt

```text
Found 87 violations
Found 0 unconnected items
Found 30 schematic parity issues
Saved DRC Report to C:\Users\LJ\GitHub\KICAD_ENGINE\32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\engineering_audit_artifacts\m4a1x_tps5430\m4a1x_tps5430_drc.rpt

```

## Interpretation

A nonzero exit means KiCad reported violations or the command failed. This audit does not repair projects and does not override KiCad results.
