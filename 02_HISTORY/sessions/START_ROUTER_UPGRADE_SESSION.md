# Start Router Upgrade Session

Date: `2026-05-10`
Task type: `DOCS_ONLY`
Status: `COMPLETED`

## Request

Upgrade the repo startup/router layer so future sessions can say `Read
START_HERE_FOR_AI_AGENTS.md and route yourself correctly` and automatically
load the right docs for schematic, GUI annotation, footprint/package, PCB,
routing, fab, memory/history, and open-source-tool tasks.

## Work Performed

- read the current startup, AGENTS, handoff, structure, memory/history, and
  prompt-pack entry docs
- created a new task-router layer under `00_CODEX_START/`
- rewired `START_HERE_FOR_AI_AGENTS.md`, `AGENTS.md`, `README_GPT.md`,
  `FOR CHAT GPT.MD`, and prompt-pack startup docs to point at the router
- added a durable startup-routing rule to `01_MEMORY/DESIGN_RULES_MEMORY.md`
- validated route coverage and verified no KiCad design files changed
- validated the `DOCS_ONLY` task contract successfully
- rebuilt the standard repo, memory, history, AI-quality, and known-problem
  indexes

## Maintenance Event

The active-project prompt counter reached the maintenance threshold during this
task. The required command was run:

`python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

The counter was reset to `0` before document edits continued.

## Validation Summary

- `START_HERE_FOR_AI_AGENTS.md` now points to `00_CODEX_START/TASK_ROUTER.md`
- all supported task routes are represented in required-doc, allowed-action,
  blocker, and output tables
- no `.kicad_sch` files changed
- no `.kicad_pcb` files changed

## Notes

- This was a documentation/router upgrade only.
- No KiCad design edits, routing, zones, or fabrication outputs were created.
