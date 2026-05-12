# Trace Angle Routing Rules

## Canonical Status

This file is the canonical angle-geometry rule surface for routed copper.

## Mandatory Rules

- 90-degree routed corners are rejected unless a waiver is explicitly recorded.
- Acute trace bends are rejected.
- Default normal routing uses 45-degree bends.
- USB, RF, and other sensitive nets should use smooth entry, exit, and turning geometry.
- Power traces may be wider than signal traces, but they still must avoid crude square corners.
- `BUCK_SW` and other switching-node copper must stay short, compact, and visually clean.
- If placement forces ugly geometry, fix the local placement instead of forcing bad routing.
- KiCad DRC pass does not override trace-geometry failure.

## Gate Behavior

- Run `python 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py --project <ACTIVE_PROJECT_PATH>` before claiming routing quality.
- A board fails this gate on any of:
  - `RIGHT_ANGLE_FOUND`
  - `ACUTE_JOG_FOUND`
- The PCB quality gate must treat any of the above as blocking.

## Review Flags

- `TRACE_ANGLE_REVIEW_REQUIRED`
- `NO_RIGHT_ANGLE_TRACE_CORNERS_REQUIRED`
- `NO_ACUTE_TRACE_BENDS_REQUIRED`
- `TRACE_GEOMETRY_AUDIT_REQUIRED`
- `DRC_PASS_NOT_ROUTING_QUALITY_APPROVAL`

## Source Registry References

- `url_000005` - Nexperia switching-behavior / EMC app note context
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
