# Prompt Counter Rule Upgrade Audit

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:45:00-04:00`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `00_CODEX_START/PROMPT_COUNTER_RULES.md`, `03_TOOLS/scripts/memory_maintenance/*prompt_counter*.py`, `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md`.

Current relevance: audit record for adding project-specific prompt-count maintenance triggers.

## Result

Prompt-count maintenance rules were added to the existing memory/history system.

No parallel memory/history system was created.

## Files Created

- `00_CODEX_START/PROMPT_COUNTER_RULES.md`
- `03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py`
- `03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py`
- `03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md`

## Files Updated

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `01_MEMORY/MEMORY_UPDATE_RULES.md`
- `03_TOOLS/scripts/memory_maintenance/README.md`
- generated memory/history/known-problems indexes

`02_HISTORY/HISTORY_MAINTENANCE_RULES.md` was not present, so it was not updated.

## Counter Behavior

- Counter is project-specific.
- Meaningful repo tasks increment the counter.
- Casual chat does not count unless repo files are audited or modified.
- Counter threshold is `5`.
- Counter does not replace session logs or command logs.

## Maintenance Trigger Behavior

At count `5` or higher, `check_maintenance_due.py` reports:

`BLOCK_ENGINEERING_WORK_UNTIL_MAINTENANCE_RUNS`

Required maintenance command:

```powershell
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project <active_project> --apply
```

After successful maintenance:

```powershell
python 03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py --project <active_project> --apply
```

## Validation

- Python syntax check: `PASS`
- Increment counter dry-run: `PASS`
- Check maintenance due dry-run: `PASS`
- Reset counter dry-run: `PASS`
- KiCad design files changed: `NO`

## ESP32_CSI_WIFI_NODE Counter State

- Prompt count: `1`
- Maintenance threshold: `5`
- Maintenance due: `NO`

## Classification

`PROMPT_COUNTER_RULE_UPGRADE_COMPLETE`
