# Failed Attempt: Schematic Gate Checker Option Mismatch

Date: 2026-05-06  
Project: `ESP32_CSI_WIFI_NODE`  
Severity: `LOW`

## What Failed

Initial invocations of the schematic checker scripts used unsupported option names:

- `--report-md`
- `--report-json`

The local scripts expect:

- `--output`
- `--json-output`

## Impact

No project files were modified by the failed commands. The commands exited with argument parser errors before running checks.

## Recovery

The checker commands were rerun with the correct local arguments and produced:

- `reports/SCHEMATIC_ELECTRICAL_GATE_ANNOTATION_CHECK.md`
- `reports/SCHEMATIC_ELECTRICAL_GATE_COMPLETENESS_CHECK.md`
- `reports/SCHEMATIC_ELECTRICAL_GATE_BOM_LOCK_ALIGNMENT_CHECK.md`
- `reports/SCHEMATIC_ELECTRICAL_GATE_NEEDS_REVIEW_MARKER_CHECK.md`

## Lesson

Check local script `--help` or existing report-generation usage before assuming option names.

## Additional Non-Blocking Command Failure

`git status --short` was attempted during final inspection and failed with:

`fatal: not a git repository (or any of the parent directories): .git`

Impact: no project files were modified by this command. This only prevented git-based change confirmation in the current shell context.
