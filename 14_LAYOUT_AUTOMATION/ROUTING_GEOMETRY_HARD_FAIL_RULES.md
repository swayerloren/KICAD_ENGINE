# Routing Geometry Hard Fail Rules

## Purpose

Prevent routing passes from being marked acceptable when the copper geometry is
visually crude or electrically careless even if a basic DRC snapshot is clean.

## Hard Fail Statuses

- `RIGHT_ANGLE_FOUND`
- `ACUTE_JOG_FOUND`
- `PAD_ENTRY_GEOMETRY_POOR`
- `UNNECESSARY_ZIGZAG_FOUND`
- `CRITICAL_LOOP_DETOUR_FOUND`
- `KEEP_OUT_CROSSING_FOUND`
- `UNJUSTIFIED_VIA_FOUND`
- `TRACE_WIDTH_MISMATCH_FOUND`

## Rules

1. A routing pass cannot be `PASS` when any hard-fail geometry status exists.
2. 45-degree or smoother geometry is required unless an explicit engineering
   justification exists.
3. 90-degree bends are fail by default.
4. Acute non-45 jogs are always fail.
5. Poor pad-entry runout is fail on critical nets.
6. Unnecessary long detours are fail on critical nets.
7. RF or antenna keepout crossings remain hard fail regardless of local
   geometry quality.
8. Critical-net vias without a recorded reason are hard fail.
9. Segment width below the assigned net target is hard fail.

## Required Finding Fields

Every geometry hard-fail output must include:

- net name
- segment coordinates
- layer
- reason
- recommended fix

## Boundary

These checks block routing acceptance and scorecard pass. They do not make a
board fabrication-ready.
