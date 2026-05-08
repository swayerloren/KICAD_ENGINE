# COMMAND LINK Direct Edit ERC/DRC Report

Date: 2026-04-30

Project path:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK`

## Baseline

Baseline scripts were run after snapshot and archive.

- Inventory: found 1 `.kicad_pro`, 1 `.kicad_sch`, and 1 `.kicad_pcb`.
- Baseline ERC: exit code 5, 0 errors, 2 warnings.
- Baseline DRC: exit code 5, 46 violations.

Baseline ERC warnings:

- Missing footprint library `ULN2803ADW`.
- `CAN_P` label connected more than one wire.

Baseline DRC categories:

- 40 footprint-library mismatch warnings.
- 3 starved thermal errors.
- 1 courtyard overlap error.
- 1 co-located hole warning.
- 1 missing footprint library warning.
- 0 unconnected pads.

## Fix Verification

After adding the project-local U2 footprint library:

- ERC reduced to 1 warning: `CAN_P` label.
- DRC reduced to 45 violations; the missing `ULN2803ADW` library warning was removed.

After adjusting the `CAN_P` label:

- ERC passed with exit code 0.
- ERC messages: 0 errors, 0 warnings.

After removing the duplicate GND via:

- DRC reduced to 44 violations.
- The co-located hole warning was removed.

## Final ERC

Final report folder:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\final_verification\erc_20260430_204227`

Result:

- Exit code: 0
- Errors: 0
- Warnings: 0
- Status: PASS

## Final DRC

Final report folder:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\final_verification\drc_20260430_204232`

Result:

- Exit code: 5
- Violations: 44
- Unconnected pads: 0
- Footprint errors: 0
- Status: FAIL

Remaining DRC classification:

- Courtyard overlap C3/C9: actual assembly/layout concern; needs human approval or layout revision.
- Starved thermal R2 pad 2: actual copper/thermal concern; needs human approval or layout revision.
- Starved thermal U3 pad 2: actual copper/thermal concern; needs human approval or layout revision.
- Starved thermal U4 pad 2: actual copper/thermal concern; needs human approval or layout revision.
- 40 footprint-library mismatches: library-environment/stale footprint comparison issue against installed KiCad standard libraries; not auto-fixed because updating from library could alter verified layout geometry.

## Removed Issues

- Missing footprint library `ULN2803ADW`: fixed by project-local library/table.
- `CAN_P` ERC label warning: fixed by label placement/justification.
- Co-located hole warning at `(82.675, 68.525)`: fixed by removing one duplicate identical GND via.

## Fabrication Status

Not fabrication-ready.

New exports are `NOT_FINAL` and require human review of remaining DRC items, footprint mismatch implications, BOM, PNP, drill, Gerber, STEP/mechanical output, and visual package comparison before release.
