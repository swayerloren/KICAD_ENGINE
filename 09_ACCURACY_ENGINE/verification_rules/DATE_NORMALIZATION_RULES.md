# Date Normalization Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/memory_maintenance/normalize_relative_dates.py`.

Current relevance: required for memory/history cleanup and current-state summaries.

## Vague Terms To Avoid

- yesterday
- today
- tomorrow
- recently
- current
- latest
- last run
- previous run
- now

## Rule

Use absolute dates and, when useful, local timestamps. If a vague date cannot be resolved from file metadata or report headers, flag:

`DATE_UNRESOLVED_NEEDS_HUMAN_REVIEW`

Do not silently rewrite historical statements if the intended date is ambiguous.
