# Trace Projection Rules

## Purpose

Force route thinking before real routing begins.

## Hard Rules

1. Every variant must include projected routes for required net groups.
2. Projections must prefer 45-degree geometry.
3. Acute projected geometry is a fail.
4. RF keepout crossings are a fail.
5. Missing required projected routes count as projected open nets.
6. Projected detour ratio above `2x` direct distance is a fail.
7. Projected rectangular or boxy perimeter routes are a fail.
8. Projected test-point stub longer than `5 mm` is a fail.
9. Projected board-edge crossing is a fail.
10. Projected reference-plane split risk is a fail.

## Required Net Groups

At minimum project:

- power input path
- regulator cluster path
- `+3V3` distribution path
- USB/data path when present
- boot/reset or equivalent control path when present

## Allowed Projection Result Codes

- `PROJECTED_OK`
- `PROJECTED_WARNING_LONG_PATH`
- `BLOCKED_CONNECTOR_DIRECTION`
- `BLOCKED_RF_KEEPOUT`
- `BLOCKED_BOARD_EDGE`
- `BLOCKED_PLANE_SPLIT_RISK`
- `BLOCKED_EXCESSIVE_DETOUR`
- `BLOCKED_TEST_POINT_STUB`
- `BLOCKED_NO_CHANNEL`
- `OPEN_REQUIRED`

## Important Boundary

Projected routing is not real routing.

It is a gate signal that answers:

- is the path plausible
- does placement create obvious open nets
- does the path already look mechanically or electrically wrong
- would the real geometry audit immediately fail the route if the projected shape were built literally

## Canonical Rule Links

- `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/GROUNDING_AND_RETURN_PATH_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/TEST_POINT_LAYOUT_RULES.md`
