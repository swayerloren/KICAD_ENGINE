# Start Router Upgrade Claim / Evidence Matrix

Date: `2026-05-10`

| Claim | Evidence |
| --- | --- |
| `START_HERE_FOR_AI_AGENTS.md` now points to `TASK_ROUTER.md` | `rg -n "TASK_ROUTER\.md" START_HERE_FOR_AI_AGENTS.md` |
| All main routes have required docs, allowed actions, blockers, and outputs | PowerShell validation loop across the four `TASK_TYPE_TO_*` files |
| The router supports schematic, PCB, fab, memory/history, and open-source-tool work | content of `TASK_ROUTER.md` plus the companion route tables |
| No KiCad design files changed | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned no paths |
| Maintenance ran when due | `run_maintenance_cycle.py` output and reset `memory/PROMPT_COUNTER.md` |
