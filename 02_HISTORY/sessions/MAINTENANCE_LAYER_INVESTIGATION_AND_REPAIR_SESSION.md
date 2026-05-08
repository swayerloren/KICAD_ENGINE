# MAINTENANCE_LAYER_INVESTIGATION_AND_REPAIR_SESSION

Date: `2026-05-07`

## Summary

Investigated the KiCad Engine maintenance and state-management layer for `ESP32_CSI_WIFI_NODE`, identified why stale `NO_PCB` and stale gate reports survived, and repaired the live-state wiring so maintenance and phase checks now reconcile against actual KiCad files before blocking work.

## Result

- every-5-prompts layer existed: `PARTIAL_ONLY`
- prompt counter existed: `YES`
- prompt counter location: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md`
- automatic maintenance supervisor existed: `NO`
- live KiCad truth rebuild existed: `NO`
- stale-report detection existed: `NO`
- live-aware gate reconciliation existed: `NO`
- `check_phase_allowed.py` used live state before repair: `NO`
- KiCad design files edited: `NO`

## Root Cause

The repo had prompt-counter rules and a legacy memory-maintenance path, but it did not have a robust maintenance supervisor that rebuilt live project state from `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`. The gate checker relied on stale markdown reports, and the reports themselves often had no source hashes or file-timestamp linkage. That allowed old `NO_PCB`, `0 footprints`, and pre-routing blocker narratives to survive after the real PCB already existed.

## Repair Performed

- created `03_TOOLS/scripts/maintenance/` as the canonical maintenance supervisor
- created `03_TOOLS/scripts/project_state/` live-state builders and stale-report detection
- updated `03_TOOLS/scripts/project_gate/check_phase_allowed.py` to rebuild/read live state first
- updated startup and closeout docs so the every-5-prompts rule points to the new maintenance command
- regenerated live project state, stale-report audit, gate reconciliation, and maintenance cycle outputs for `ESP32_CSI_WIFI_NODE`

## Validation

- Python syntax check: `PASS`
- maintenance cycle run: `PASS`
- phase 2 after reconciliation: `ALLOWED`
- phase 3 after reconciliation: `ALLOWED`
- phase 8 after reconciliation: `BLOCKED_FOR_REAL_LIVE_BOARD_REASONS`

## Safety

No `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol library, footprint library, or manufacturing output files were modified in this task.
