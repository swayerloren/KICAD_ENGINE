# 02_HISTORY Index

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:41:21`

Project: `KICAD_ENGINE`

Supersedes: older hand-maintained history index wording.

Superseded by: `None`

Evidence files: `02_HISTORY/MASTER_HISTORY_INDEX.md`, `03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py`.

Current relevance: human-facing history routing index; detailed generated inventory is in `MASTER_HISTORY_INDEX.md`.

## PURPOSE
AI-readable routing index for history and evidence records.

## CURRENT MAINTENANCE ENTRYPOINTS

- Global generated index: `02_HISTORY/MASTER_HISTORY_INDEX.md`
- ESP32 maintenance last run: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/MEMORY_MAINTENANCE_LAST_RUN.md`
- ESP32 superseded reports: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/SUPERSEDED_REPORTS.md`
- ESP32 false-pass incidents: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/FALSE_PASS_INCIDENTS.md`
- Cleanup validation output: `05_OUTPUTS/release_readiness/memory_history_cleanup_apply_result.json`

## WHAT_BELONGS_HERE
- `MASTER_HISTORY_INDEX.md`
- `sessions/`
- `command_logs/`
- `design_reviews/`
- `failed_attempts/`
- `issue_logs/`
- AI quality history folders.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Project source files.
- Durable design defaults without evidence review.

## AI_AGENT_RULES
- Write history after meaningful work.
- Use project `history/` for project-specific evidence.
- Before trusting repeated blocker records, run or review duplicate-history maintenance output.
- Current-state summaries belong in project `memory/`; raw command/session evidence stays in `02_HISTORY` or project `history/`.

## SAFE_EDIT_RULES
- Preserve prior records.
- Keep unresolved problems in issue logs.
- Never delete old history automatically. Mark supersession externally.

## PUBLIC_RELEASE_NOTES
- Public history should not expose private credentials or misleading final-fabrication claims.
