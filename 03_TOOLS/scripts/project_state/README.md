# Project State Scripts

These scripts build a live, file-derived project-state layer for KiCad Engine.

They are for operational truth, not for editing KiCad design files.

## Purpose

The project-state layer exists to stop stale markdown from overriding real KiCad evidence.

It inspects:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- file hashes
- file timestamps
- live PCB inventory and outline
- DRC JSON when available
- operational report freshness and contradictions

## Canonical Outputs

For an active project, the main outputs are:

- `reports/LIVE_PROJECT_STATE.json`
- `reports/LIVE_PROJECT_STATE.md`
- `reports/STALE_REPORTS_AUDIT.md`
- `reports/GATE_RECONCILIATION_REPORT.md`

Supporting files may also be written under:

- `reports/live_project_state/`

## Scripts

- `build_live_project_state.py`
  - Builds live project truth from the actual project files.
- `detect_stale_reports.py`
  - Marks contradictory or hashless stale-prone operational reports.
- `reconcile_project_gates.py`
  - Reconciles phase/gate decisions against the live project state.
- `update_phase_status_from_live_state.py`
  - Refreshes project `memory/CURRENT_PROJECT_STATE.md`, `CURRENT_BLOCKERS.md`, and `NEXT_ALLOWED_PHASE.md`.
- `project_state_common.py`
  - Shared helpers used by the scripts above.

## Stale Report Rules

A report is stale when any of these are true:

- it records an older PCB hash than the live `.kicad_pcb`
- it records an older schematic hash than the live `.kicad_sch`
- it has no relevant source hash and is older than the live source file
- it says `NO_PCB` while the live `.kicad_pcb` exists with footprints
- it says `0 footprints` while the live PCB has footprints
- it says routing is missing while the live PCB has tracks
- it says placement is missing while the live PCB shows placed footprints inside the outline bbox

## Example

```powershell
python 03_TOOLS\scripts\project_state\build_live_project_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\project_state\detect_stale_reports.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\project_state\reconcile_project_gates.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\project_state\update_phase_status_from_live_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
```
