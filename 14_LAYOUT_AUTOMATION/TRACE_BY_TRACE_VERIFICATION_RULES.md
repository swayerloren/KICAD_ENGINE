# Trace By Trace Verification Rules

## Purpose

Define the minimum audit standard for route verification.

## Rules

- Every trace must appear in the trace-by-trace audit.
- Every audited trace must include net name, segment count, via count, width set, and issue list.
- Critical nets must include an explicit critical-review note.
- Angle or geometry problems must be called out, not hidden behind DRC pass.
- Autorouted traces remain `REVIEW_ONLY` until they pass full audit.

## Required Outputs

- one audit entry per trace
- summary counts for critical traces, vias, and flagged issues
- explicit list of traces needing reroute or manual review
