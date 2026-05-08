# Gate Reconciliation Report

Generated: `2026-05-08T15:15:02-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Phase Results

| Phase | Name | Result | Phase Status | Next Required Phase |
| --- | --- | --- | --- | --- |
| `2` | PCB Creation / Update From Schematic | `ALLOWED` | `ALREADY_DONE_BY_LIVE_FILE_EVIDENCE` | `3` |
| `3` | Placement Planning | `ALLOWED` | `ALREADY_DONE_OR_SUPERSEDED_BY_LIVE_PLACEMENT` | `4` |
| `8` | Routing | `BLOCKED` | `PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT` | `8` |

## Evidence Decisions

### Phase `2`
- `LIVE_FILE_EVIDENCE`: Live PCB exists with 43 footprints.
Warnings:
- Live PCB existence proves Phase 2 already occurred even though upstream schematic gate remains FAIL.

### Phase `3`
- `STALE_REPORT_IGNORED`: SCHEMATIC_TO_PCB_GATE_STATUS.md is older than the live schematic and cannot overrule live-state reconciliation.
- `LIVE_FILE_EVIDENCE`: Live PCB shows placed footprints inside outline bbox (43 / 43).
Warnings:
- Placement planning is already superseded by live placement evidence on the current board.

### Phase `8`
- `LIVE_FILE_EVIDENCE`: Live PCB contains routing: tracks=74, vias=32.
- `STALE_REPORT_IGNORED`: REAL_PCB_UPDATE_FROM_SCHEMATIC report is stale and does not control routing gating.
- `STALE_REPORT_IGNORED`: SCHEMATIC_TO_PCB_GATE_STATUS.md is stale against the live schematic and is not used as a direct routing blocker.
- `STALE_REPORT_IGNORED`: PCB_LAYOUT_SANDBOX_GATE_STATUS.md is stale and cannot be used to claim NO_PCB or missing placement.
Warnings:
- Human review is required because historical schematic-gate evidence conflicts with the existence of a live PCB.
- Human review is required before routing continuation because the live board exists despite stale or conflicting formal gate history.
Blockers:
- Live DRC is FAIL with 0 violations and 17 unconnected items.
- 4 detectable unrouted nets remain.

## Stale Reports Ignored

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\AUTO_PCB_START_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\CURRENT_EXISTING_TRACE_AUDIT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PCB_TRUTH_AUDIT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FILE_CURRENT_STATE.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_INTELLIGENCE_BASED_DRC_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_CURRENT_STATE_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_ORIENTATION_REVIEW.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_PASS_1_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_SYNC_STATUS.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_ROUTING_PLAN.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_CURRENT_STATE_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_START_BLOCKERS.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`
