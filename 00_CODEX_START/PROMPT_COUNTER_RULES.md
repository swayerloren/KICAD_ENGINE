# Prompt Counter Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/maintenance/prompt_counter.py`, `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`, `03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py`, `check_maintenance_due.py`, `reset_prompt_counter_after_maintenance.py`.

Current relevance: startup rule for triggering memory/history maintenance after repeated repo work.

## Purpose

The prompt counter is a project-specific maintenance trigger. It does not replace session logs, command logs, project memory, or project history.

## Rules

1. Every meaningful Codex/Claude repo task increments the active project prompt counter.
2. Casual chat does not count unless repo files are audited, classified, modified, or validated.
3. After `5` meaningful repo tasks, the live-state maintenance cycle is required.
4. If maintenance is due, block new engineering work until maintenance runs.
5. Maintenance command:

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project <active_project>
```

6. After successful maintenance, reset the counter to `0`.
7. The counter is project-specific and belongs in the active project's `memory/` folder.
8. The counter is a trigger only. It is not evidence that maintenance ran.

## Standard Files

For `ESP32_CSI_WIFI_NODE`:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md`

## Standard Commands

Increment:

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
```

Check:

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Reset after successful maintenance:

```powershell
python 03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
```

Direct maintenance run:

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

## Engineering Work Block

If `check_maintenance_due.py` reports `MAINTENANCE_DUE`, Codex/Claude must not start schematic edits, PCB edits, routing, zones, fabrication outputs, production reviews, or signoff tasks until `run_maintenance_cycle.py` completes.

Allowed work while maintenance is due:

- Run memory/history maintenance.
- Reset the counter after successful maintenance.
- Create maintenance/session/command reports.
- Answer non-engineering questions without modifying repo files.
