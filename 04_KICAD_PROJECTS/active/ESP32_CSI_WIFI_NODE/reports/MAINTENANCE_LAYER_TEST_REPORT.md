# Maintenance Layer Test Report

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Scope

Tested the repaired maintenance/state layer only. No KiCad design files were edited.

## Commands Run

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 2
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 3
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 8
```

## Maintenance Run Result

- result: `PASS`
- prompt counter before: `1`
- prompt counter after maintenance reset: `0`
- live classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
- stale report count: `5`

## Live PCB Evidence Seen By The Repaired Layer

- PCB exists: `YES`
- footprints: `43`
- placement evidence: `43 / 43` inside board outline bbox
- routing evidence: `24` tracks, `2` vias
- live project state source: `REBUILT_FROM_LIVE_FILES`

## Phase Results

### Phase 2

- result: `ALLOWED`
- status: `ALREADY_DONE_BY_LIVE_FILE_EVIDENCE`
- key evidence: live PCB exists with `43` footprints

### Phase 3

- result: `ALLOWED`
- status: `ALREADY_DONE_OR_SUPERSEDED_BY_LIVE_PLACEMENT`
- key evidence: live PCB shows placed footprints inside outline bbox

### Phase 8

- result: `BLOCKED`
- status: `PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
- key evidence: live PCB contains routing with `24` tracks and `2` vias

## Stale Reports Ignored

- `CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md`
- `PCB_INTELLIGENCE_BASED_DRC_REPORT.md`
- `PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md`
- `PCB_SYNC_STATUS.md`
- `SCHEMATIC_TO_PCB_GATE_STATUS.md`

These stale reports did not override live PCB existence, live footprint count, placement evidence, or routing evidence.

## Verification Result

- stale `NO_PCB` style reports override live PCB file evidence: `NO`
- stale `0-footprint` style reports override live PCB file evidence: `NO`
- live PCB state visible in phase-check output: `YES`
- remaining routing blockers based on actual board state instead of stale markdown: `YES`

## True Live Blockers Remaining

- live DRC is `FAIL` with `12` violations and `65` unconnected items
- `16` detectable unrouted nets remain
- no zones or accepted GND strategy exist on the current live board
- existing routed geometry is not fully verified for continuation

## Conclusion

The repaired maintenance/state layer is working for this project. It honors live KiCad file evidence first, ignores stale blocker reports, and still blocks unsafe routing continuation for real board-state reasons.
