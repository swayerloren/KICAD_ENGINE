# PCB Routing Quality Rules

## Scope

Use this file with `TRACE_ANGLE_ROUTING_RULES.md` for all routing prompts,
rehearsals, quality gates, and final reviews.

## Geometry Rules

- Follow `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`.
- Prefer short, direct routing over decorative or script-generated pathing.
- Zigzags, boxy perimeter routes, and rectangular loops are rejected.
- Routed length above `2x` the direct span is an excessive-detour failure unless a waiver is recorded.
- Test-point stubs longer than `5 mm` are rejected unless a measurement/programming need is documented.
- Traces must not cross the board edge, RF keepouts, or obvious return-path blockers.
- Plane-splitting routes that break GND return continuity are routing-quality failures.

## Power Rules

- Power-input, fused, protected, regulator, and `+3V3` routes must stay compact and local.
- `BUCK_SW` must stay short and away from USB, RF, and sensitive control nets.
- Avoid skinny neckdowns unless the footprint geometry forces them.

## Signal Rules

- USB and other paired signals must remain short, clean, and paired where practical.
- Avoid long USB stubs, long test-pad branches, and avoidable via count on critical nets.
- Keep routing out of RF keepouts, mounting-hole clearance zones, and connector mechanical escape areas.

## Review Gate

- DRC pass is required.
- Open-net pass is required.
- Visual routing review is required.
- The geometry audit is required:
  - `python 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py --project <ACTIVE_PROJECT_PATH>`
- Routing quality is `FAIL` on any of:
  - `RIGHT_ANGLE_FOUND`
  - `ACUTE_JOG_FOUND`
  - `UNNECESSARY_ZIGZAG_FOUND`
  - `RECTANGULAR_LOOP_FOUND`
  - `PERIMETER_BOX_ROUTE_FOUND`
  - `EXCESSIVE_DETOUR_RATIO`
  - `TEST_POINT_STUB_TOO_LONG`
  - `BOARD_EDGE_CROSSING`
  - `KEEP_OUT_CROSSING_FOUND`
  - `RETURN_PATH_SPLIT_RISK`

## Source Registry References

- `url_000005` - Nexperia switching / EMI application note
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
