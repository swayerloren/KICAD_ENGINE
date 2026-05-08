# PCB Full Routing Claim/Evidence Matrix

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

| Claim | Status | Evidence | Confidence | Human review required | Notes |
|---|---|---|---|---|---|
| Full routing was not performed. | `VERIFIED_BY_FILE` | `reports/PCB_FULL_ROUTING_REPORT.md` | `HIGH` | No | Report documents blocked workflow. |
| Critical routing is not pass/acceptable. | `VERIFIED_BY_FILE` | `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` | `HIGH` | Yes | Final result `CRITICAL_ROUTING_FAIL`. |
| Routing plan is blocked. | `VERIFIED_BY_FILE` | `reports/PCB_ROUTING_PLAN.md` | `HIGH` | Yes | Final result `ROUTING_PLAN_BLOCKED`. |
| No `.kicad_pcb` exists. | `VERIFIED_BY_COMMAND` | Active project `kicad/` file listing. | `HIGH` | No | Listing showed no PCB file. |
| DRC was not run. | `VERIFIED_BY_FILE` | `reports/PCB_FULL_ROUTING_REPORT.md` | `HIGH` | No | No PCB exists. |
| Trace-by-trace audit was not run. | `VERIFIED_BY_FILE` | `reports/TRACE_BY_TRACE_AUDIT.md` | `HIGH` | No | No traces exist. |
| Full-routing correctness remains unverified. | `PARTIALLY_VERIFIED` | Missing PCB and failed upstream routing gates. | `HIGH` | Yes | Do not infer pass. |

