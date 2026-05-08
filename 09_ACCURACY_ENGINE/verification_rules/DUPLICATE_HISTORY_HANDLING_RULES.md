# Duplicate History Handling Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/memory_maintenance/detect_duplicate_history.py`.

Current relevance: prevents repeated blocker/history records from confusing future agents.

## Rules

- Duplicate history records must not be deleted.
- Group duplicate blocker topics by subject and evidence path.
- Preserve the earliest occurrence as historical evidence.
- Use current project-state files to identify which blocker is still active.
- Mark old duplicates as `HISTORICAL_ONLY`, `STALE`, or `SUPERSEDED` through maintenance indexes.

## Required Duplicate Topics

At minimum, detect repeated records about:

- missing PCB
- PCB sync
- Q1 pin mapping
- placement blockers
- routing blockers
- JLCPCB/export/signoff blockers
- automated visual pass overclaims
