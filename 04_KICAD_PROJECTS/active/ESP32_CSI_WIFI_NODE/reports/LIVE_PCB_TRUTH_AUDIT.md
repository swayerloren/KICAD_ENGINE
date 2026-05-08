# LIVE PCB Truth Audit

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Final classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`

## PCB Identity

| Item | Result |
| --- | --- |
| PCB exists | `YES` |
| SHA256 | `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844` |
| Timestamp | `2026-05-07 16:28:37 -04:00` |
| File size | `170233 bytes` |

## Live Board State

| Item | Result |
| --- | --- |
| Board outline exists | `YES` |
| Board outline shape | `RECTANGULAR_EDGE_CUTS` |
| Board size | `60.0 mm x 95.0 mm` |
| Footprints present | `YES` |
| Footprint count | `43` |
| Mounting/mechanical holes present | `YES` |
| Mounting hole count | `4` mounting-hole footprints: `MH1-MH4` |
| Tracks present | `YES` |
| Track segment count | `24` |
| Grouped trace count | `6` |
| Vias present | `YES` |
| Via count | `2` |
| Zones present | `NO` |
| Zone count | `0` |
| Components placed inside board outline | `YES_BY_FOOTPRINT_ANCHOR_BBOX_CHECK (43/43 anchors inside)` |
| Edge-mounted parts | `J1` and `J2` visually sit on the bottom edge as expected edge parts |

## Routed / Unrouted State

Existing routed nets detected from the live board:

- `/+5V_IN`
- `/+5V_FUSED`
- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- `+3V3`

Detectable unrouted nets: `16`

- `unconnected-(J2-VBUS-PadA4)`
- `/BOOT0`
- `/ESP_EN`
- `/PLED`
- `/SLED`
- `/STATUS_LED`
- `/CC1`
- `/CC2`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`
- `/SHIELD`
- `/U0RXD`
- `/U0TXD`
- `GND`

## DRC Result

DRC runnable: `YES`

Current DRC result: `FAIL`

| Item | Result |
| --- | --- |
| DRC violations | `12` |
| Violation class | `12 x drill_out_of_range` |
| Affected item | `U2 pad 41` |
| Unconnected items | `65` |
| Schematic parity in this audit | `NOT_RUN_IN_THIS_SESSION` |

Evidence:

- `reports/live_pcb_truth_audit/LIVE_PCB_TRUTH_AUDIT_DRC.json`
- `reports/live_pcb_truth_audit/real_board_routing_audit_summary.md`

## Stale Reports Found

- `reports/PCB_PLACEMENT_PASS_1_REPORT.md`: claimed `NO_PCB` and `0` placements; contradicted by the live board.
- `reports/AUTO_PCB_START_REPORT.md`: claimed no `.kicad_pcb`, no outline, and no placement in the current state; contradicted by the live board.
- `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`: valid as a gate blocker, but stale as a factual project-state narrative because real PCB/placement/routing already exist.
- `reports/CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md`: still describes a rejected `100 mm x 65 mm` board; the live board is `60 mm x 95 mm`.
- `reports/PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md`: still says `Routing performed: NO`; the live board now contains routed copper.
- `reports/PCB_INTELLIGENCE_BASED_DRC_REPORT.md`: stale track count and stale unconnected count for the current board revision.
- `reports/PCB_PLACEMENT_ORIENTATION_REVIEW.md`: missing before this audit.
- `reports/REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`: missing before this audit.

## Reports Updated

- `reports/LIVE_PCB_TRUTH_AUDIT.md`
- `reports/PCB_FILE_CURRENT_STATE.md`
- `reports/STALE_GATE_REPORT_RECONCILIATION.md`
- `reports/REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
- `reports/PCB_PLACEMENT_CURRENT_STATE_REPORT.md`
- `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
- `reports/PCB_PLACEMENT_ORIENTATION_REVIEW.md`
- `reports/ROUTING_CURRENT_STATE_REPORT.md`
- `reports/REAL_PCB_ROUTING_PLAN.md`
- `reports/ROUTING_START_BLOCKERS.md`
- `reports/AUTO_PCB_START_REPORT.md`
- `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `_verification/pcb_visual/LIVE_PCB_TRUTH_AUDIT_REVIEW.md`

## Current Real Phase

| Item | Result |
| --- | --- |
| PCB created | `YES` |
| Placement exists | `YES` |
| Routing exists | `YES_PARTIAL` |
| Placement repair needed | `YES` |
| Routing plan may continue | `NO` |

## Why Routing May Not Continue

- Formal phase gate still blocks routing because `SCHEMATIC_TO_PCB_GATE_STATUS.md` is still exact `FAIL`.
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` remains `BLOCKED`.
- Placement exists but is not formally approved by a refreshed live-board orientation/mechanical review.
- `12` DRC violations remain on `U2 pad 41`.
- `65` unconnected items remain.
- `16` unrouted nets remain.
- No zones / no accepted GND strategy exist on the live board.

## Exact Next Action

Run a live placement/mechanical approval pass on the current `60 mm x 95 mm` board and either approve or repair the existing `J1` / `J2` / `U2` / test-pad / mounting-hole layout before any further routing.
