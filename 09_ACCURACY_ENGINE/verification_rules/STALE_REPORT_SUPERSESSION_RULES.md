# Stale Report Supersession Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/memory_maintenance/mark_superseded_reports.py`.

Current relevance: defines how old reports remain historical without controlling current truth.

## Rules

- Never delete stale reports automatically.
- Mark superseded reports through `SUPERSEDED_REPORTS.md` or equivalent maintenance index.
- If a report predates a later design artifact that changes the truth, classify it `STALE` or `SUPERSEDED`.
- If a report documents a real past failure, preserve it as `HISTORICAL_ONLY` unless the failure is still active.
- Current-state files must name the active evidence that supersedes old reports.
