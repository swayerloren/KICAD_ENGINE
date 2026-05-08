# Trace By Trace Verification Rules

## Purpose

Define the minimum audit standard for route verification.

## Rules

- Every trace must appear in the trace-by-trace audit.
- Every audited trace must include net name, segment count, via count, width set, and issue list.
- Critical nets must include an explicit critical-review note.
- Angle or geometry problems must be called out, not hidden behind DRC pass.
- Autorouted traces remain `REVIEW_ONLY` until they pass full audit.
- Routing geometry hard-fail statuses must be recorded explicitly when present:
  `RIGHT_ANGLE_FOUND`, `ACUTE_JOG_FOUND`, `PAD_ENTRY_GEOMETRY_POOR`,
  `UNNECESSARY_ZIGZAG_FOUND`, `CRITICAL_LOOP_DETOUR_FOUND`,
  `KEEP_OUT_CROSSING_FOUND`, `UNJUSTIFIED_VIA_FOUND`, and
  `TRACE_WIDTH_MISMATCH_FOUND`.
- Every geometry failure entry must include net name, segment coordinates,
  layer, reason, and recommended fix.
- A trace audit cannot be treated as passable if any hard-fail geometry status
  exists.

## Required Outputs

- one audit entry per trace
- summary counts for critical traces, vias, and flagged issues
- explicit list of traces needing reroute or manual review
- explicit list of geometry hard-fail findings with reroute guidance
