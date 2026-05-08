# Routing Geometry Hard Fail Audit

Date: `2026-05-08`
Branch: `hardening/execution-contract`

## Purpose

Harden the routing audit and scorecard so visible bad geometry is a blocking
condition, not a soft note.

## Changes

- Added dedicated geometry rules at
  `14_LAYOUT_AUTOMATION/ROUTING_GEOMETRY_HARD_FAIL_RULES.md`.
- Added shared geometry analysis in
  `14_LAYOUT_AUTOMATION/scripts/route_quality_common.py`.
- Added aggregate and focused detector scripts:
  - `routing_geometry_quality.py`
  - `detect_right_angle_traces.py`
  - `detect_acute_jogs.py`
  - `detect_bad_pad_entry.py`
  - `detect_unnecessary_zigzags.py`
- Updated `trace_by_trace_audit.py` so each geometry failure includes net,
  segment coordinates, layer, reason, and recommended fix.
- Updated `score_routing_plan.py` so hard-fail geometry blocks pass status.
- Updated routing workflow and stop-condition docs to treat ugly geometry as a
  real stop condition.
- Added dedicated routing-geometry fixtures and generated test outputs.

## Hard Fail Statuses Implemented

- `RIGHT_ANGLE_FOUND`
- `ACUTE_JOG_FOUND`
- `PAD_ENTRY_GEOMETRY_POOR`
- `UNNECESSARY_ZIGZAG_FOUND`
- `CRITICAL_LOOP_DETOUR_FOUND`
- `KEEP_OUT_CROSSING_FOUND`
- `UNJUSTIFIED_VIA_FOUND`
- `TRACE_WIDTH_MISMATCH_FOUND`

## Validation Result

- Syntax checks passed.
- Good 45-degree fixture passed.
- Bad right-angle, acute-jog, pad-entry, and zigzag fixtures all failed.
- Trace audit plus scorecard integration confirmed that bad geometry now blocks
  routing pass status.

## Residual Limitation

Pad-entry quality is inferred from segment runout length because the fixture
schema does not carry full pad-shape entry geometry. That is acceptable for the
current planning/audit layer, but real-board extraction can refine it later.
