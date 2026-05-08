# PCB Critical Nets Routing Claim/Evidence Matrix

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

| Claim | Status | Evidence | Confidence | Human review required | Notes |
|---|---|---|---|---|---|
| Critical-net routing was not performed. | `VERIFIED_BY_FILE` | `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` | `HIGH` | No | Report documents no routing. |
| No `.kicad_pcb` exists. | `VERIFIED_BY_COMMAND` | Active project `kicad/` file listing. | `HIGH` | No | Listing showed `.kicad_pro`, `.kicad_sch`, and `fp-info-cache`; no PCB. |
| Schematic-to-PCB gate is `FAIL`. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | `HIGH` | Yes | Gate blocks routing. |
| Routing plan is blocked. | `VERIFIED_BY_FILE` | `reports/PCB_ROUTING_PLAN.md` | `HIGH` | Yes | Final result `ROUTING_PLAN_BLOCKED`. |
| Placement pass 2 is failed/not run. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md` | `HIGH` | Yes | Final result `PLACEMENT_ORIENTATION_FAIL`. |
| Copper-zone strategy is failed/not run. | `VERIFIED_BY_FILE` | `reports/COPPER_ZONE_STRATEGY_REPORT.md` | `HIGH` | Yes | Final result `ZONE_SETUP_FAIL`. |
| DRC was not run. | `VERIFIED_BY_FILE` | `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` | `HIGH` | No | No PCB exists. |
| Exact critical routing constraints remain unverified. | `PARTIALLY_VERIFIED` | Missing PCB, stackup, fab profile, verified footprints, placement, and source-backed layout evidence. | `HIGH` | Yes | Do not infer constraints. |

