# Maintenance Supervisor

This folder contains the live-state-aware maintenance supervisor for KiCad Engine.

## Purpose

The maintenance cycle exists to stop stale project status from blocking real work when live KiCad evidence says otherwise.

It does not edit KiCad design files.

## Canonical Command

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

This command is the required every-5-prompts maintenance action.

## What The Cycle Runs

1. build live project state from `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`
2. detect stale operational reports
3. reconcile gates against live file evidence
4. rebuild memory index
5. rebuild history index
6. rebuild AI-quality index
7. rebuild `CURRENT_KNOWN_PROBLEMS.md`
8. update project `memory/CURRENT_PROJECT_STATE.md`
9. update project `memory/CURRENT_BLOCKERS.md`
10. write `reports/MAINTENANCE_CYCLE_REPORT.md`

## Prompt Counter

The prompt counter remains project-local:

- `04_KICAD_PROJECTS/active/<PROJECT>/memory/PROMPT_COUNTER.md`

Threshold:

- `5` meaningful repo tasks

After a successful maintenance cycle, the counter is reset to `0`.

## Compatibility

Older `03_TOOLS/scripts/memory_maintenance/*` entrypoints may continue to exist, but the maintenance supervisor in this folder is the canonical path going forward.
