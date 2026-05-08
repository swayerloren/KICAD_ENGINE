# Report Status Tagging Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/memory_maintenance`.

Current relevance: required header schema for new meaningful reports.

## Required Status Tags

Every meaningful report should use one of:

- `ACTIVE_EVIDENCE`
- `ACTIVE_BLOCKER`
- `RESOLVED_BLOCKER`
- `SUPERSEDED`
- `STALE`
- `FALSE_PASS`
- `HISTORICAL_ONLY`
- `NEEDS_HUMAN_REVIEW`

## Required Header Fields

Every meaningful report should include:

- Status
- Generated date/time
- Project
- Supersedes
- Superseded by
- Evidence files
- Current relevance

## Maintenance Rule

Do not delete old reports. Add supersession/status evidence through project memory/history maintenance records.
