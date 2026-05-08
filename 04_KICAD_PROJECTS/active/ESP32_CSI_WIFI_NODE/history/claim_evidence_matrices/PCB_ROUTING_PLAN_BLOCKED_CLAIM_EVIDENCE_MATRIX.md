# PCB Routing Plan Claim/Evidence Matrix

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

| Claim | Status | Evidence | Human review required | Notes |
|---|---|---|---|---|
| Routing plan was created. | `VERIFIED_BY_FILE` | `reports/PCB_ROUTING_PLAN.md` | No | Planning artifact only. |
| Routing is blocked. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | Yes | Gate result is `FAIL`. |
| No `.kicad_pcb` exists. | `VERIFIED_BY_COMMAND` | Active project `kicad/` directory listing. | No | Only `.kicad_pro` and `.kicad_sch` were listed. |
| Placement pass 2 did not pass. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md` | Yes | Final result `PLACEMENT_ORIENTATION_FAIL`. |
| Copper-zone strategy did not pass. | `VERIFIED_BY_FILE` | `reports/COPPER_ZONE_STRATEGY_REPORT.md` | Yes | Final result `ZONE_SETUP_FAIL`. |
| Via strategy did not pass. | `VERIFIED_BY_FILE` | `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md` | Yes | Final result `HOLE_PAD_VIA_FAIL`. |
| Exact trace widths, clearances, and via sizes are not approved. | `PARTIALLY_VERIFIED` | Routing plan plus missing PCB/fab/stackup evidence. | Yes | Values intentionally blocked. |
| USB/RF/power route guidance requires post-placement source-backed review. | `PARTIALLY_VERIFIED` | Local USB, RF, and power layout rule files. | Yes | General rules only, not final constraints. |
| No traces were routed. | `VERIFIED_BY_FILE` | No `.kicad_pcb` exists; `reports/PCB_ROUTING_PLAN.md` states planning-only. | No | No PCB file exists to route. |

