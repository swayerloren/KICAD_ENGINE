# 01_MEMORY Index

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:41:21`

Project: `KICAD_ENGINE`

Supersedes: older hand-maintained memory index wording.

Superseded by: `None`

Evidence files: `01_MEMORY/MASTER_MEMORY_INDEX.md`, `03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py`.

Current relevance: human-facing memory routing index; detailed generated inventory is in `MASTER_MEMORY_INDEX.md`.

## PURPOSE
AI-readable routing index for durable global memory.

## CURRENT MAINTENANCE ENTRYPOINTS

- Global generated index: `01_MEMORY/MASTER_MEMORY_INDEX.md`
- ESP32 current truth: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md`
- ESP32 active blockers: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md`
- ESP32 superseded reports: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/SUPERSEDED_REPORTS.md`
- ESP32 false-pass incidents: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/FALSE_PASS_INCIDENTS.md`
- Maintenance script: `03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py`

## WHAT_BELONGS_HERE
- `MASTER_MEMORY_INDEX.md`
- Global memory files.
- `projects/` legacy project memory summaries.

## WHAT_DOES_NOT_BELONG_HERE
- Command transcripts.
- Raw reports.
- Fabrication outputs.

## AI_AGENT_RULES
- Read memory before repeating workflows or touching project files.
- Promote facts from history to memory only when durable.
- For current truth, read project `memory/CURRENT_PROJECT_STATE.md`, `CURRENT_BLOCKERS.md`, `SUPERSEDED_REPORTS.md`, and `NEXT_ALLOWED_PHASE.md` when present.
- If memory conflicts with higher evidence, follow `09_ACCURACY_ENGINE/verification_rules/EVIDENCE_HIERARCHY_RULES.md`.

## SAFE_EDIT_RULES
- Preserve prior memory entries.
- Do not store secrets.
- Do not delete stale entries automatically; mark them `STALE`, `SUPERSEDED`, or `HISTORICAL_ONLY`.

## PUBLIC_RELEASE_NOTES
- Public payloads should include only reusable, non-private memory.
