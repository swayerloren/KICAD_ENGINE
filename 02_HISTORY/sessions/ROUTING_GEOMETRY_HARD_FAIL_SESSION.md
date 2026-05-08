# Routing Geometry Hard Fail Session

Date: `2026-05-08`
Branch: `hardening/execution-contract`
Task type: `DOCS_ONLY`
Task contract: `02_HISTORY/sessions/ROUTING_GEOMETRY_HARD_FAIL_TASK_CONTRACT.json`

## Summary

Implemented hard-fail routing geometry checks so routing work cannot pass with
right angles, acute jogs, poor critical-net pad entry, unnecessary zigzags,
critical detours, keepout crossings, unjustified vias, or trace-width
mismatches.

## Validation Summary

- Python syntax checks: `PASS`
- Aggregate geometry fixtures:
  - `good_45_degree_route`: `PASS`
  - `bad_90_degree_route`: `RIGHT_ANGLE_FOUND`
  - `bad_acute_jog_route`: `ACUTE_JOG_FOUND`
  - `bad_pad_entry_route`: `PAD_ENTRY_GEOMETRY_POOR`
  - `bad_zigzag_route`: `UNNECESSARY_ZIGZAG_FOUND`
- Integration:
  - good route fixture passes routing plan + trace audit + scorecard
  - bad 90-degree fixture fails trace audit + scorecard on geometry

## KiCad Design Files

- No `.kicad_sch` files edited
- No `.kicad_pcb` files edited
- No routing performed
