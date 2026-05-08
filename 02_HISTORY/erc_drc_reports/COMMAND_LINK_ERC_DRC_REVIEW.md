# COMMAND LINK ERC/DRC Review

Date: 2026-04-30

Project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`

Review output root: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE\review_outputs\NOT_FINAL_read_only_review_20260430_180511`

## ERC

Command script: `03_TOOLS\scripts\run_erc.ps1`

Status: `FAILED_OR_VIOLATIONS_REPORTED`

KiCad CLI exit code: 5

Report path:

`C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE\review_outputs\NOT_FINAL_read_only_review_20260430_180511\erc_20260430_180611\erc_report.txt`

Summary:

- ERC messages: 2.
- Errors: 0.
- Warnings: 2.

Findings:

- Missing footprint library `ULN2803ADW` for symbol `U2 [ULN2803A]`.
- Label `CAN_P` connects more than one wire.

## DRC

Command script: `03_TOOLS\scripts\run_drc.ps1`

Status: `FAILED_OR_VIOLATIONS_REPORTED`

KiCad CLI exit code: 5

Report path:

`C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE\review_outputs\NOT_FINAL_read_only_review_20260430_180511\drc_20260430_180618\drc_report.txt`

Summary:

- Total DRC violations: 46.
- Unconnected pads/items: 0.
- Footprint errors: 0.

Violation categories:

| Category | Count |
| --- | ---: |
| `courtyards_overlap` | 1 |
| `starved_thermal` | 3 |
| `holes_co_located` | 1 |
| `lib_footprint_mismatch` | 40 |
| `lib_footprint_issues` | 1 |

## Interpretation

ERC and DRC both completed, but neither passed cleanly. Several findings are likely tied to local library/environment differences, especially the missing `ULN2803ADW` library and footprint-library mismatch warnings. The courtyard, thermal relief, and co-located-hole findings should be reviewed as possible design or intentional-override issues.

## Safety

No KiCad source files were edited. No final manufacturing outputs were generated. These reports are read-only review artifacts only.
