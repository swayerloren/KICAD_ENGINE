# Memory Maintenance Scripts

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `01_MEMORY`, `02_HISTORY`, project `memory/`, project `history/`, and project `reports/`.

Current relevance: maintenance layer for compiling current truth without deleting history.

## Purpose

These scripts maintain the existing `01_MEMORY`, `02_HISTORY`, `09_ACCURACY_ENGINE`, and project memory/history folders. They do not create a replacement memory system.

## Safety Rules

- Default mode is dry-run.
- `--apply` is required before writing markdown/index/status files.
- KiCad design files are never edited.
- Old history is never deleted.
- Stale, superseded, false-pass, and duplicate records are indexed and marked by maintenance reports.

## Scripts

- `run_memory_maintenance.py`: main orchestrator.
- `compile_current_project_state.py`: writes or prints the current project-state summary.
- `normalize_relative_dates.py`: detects vague date wording and flags unresolved terms.
- `detect_duplicate_history.py`: groups repeated blocker/history topics.
- `mark_superseded_reports.py`: compiles superseded report index.
- `rebuild_memory_indexes.py`: dry-run/apply wrapper for existing memory index builder.
- `rebuild_history_indexes.py`: dry-run/apply wrapper for existing history index builder.
- `increment_prompt_counter.py`: increments project `memory/PROMPT_COUNTER.md`; dry-run by default.
- `check_maintenance_due.py`: checks whether the counter has reached the maintenance threshold.
- `reset_prompt_counter_after_maintenance.py`: resets the counter after successful maintenance; dry-run by default.

## Example

```powershell
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --repo-root .
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --repo-root . --apply
```
