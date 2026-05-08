# Claim Evidence Matrix - Full Routing

Date: 2026-05-06

| Claim | Evidence | Status |
|---|---|---|
| Full routing is blocked | `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` final classification is `BLOCKED` | `VERIFIED_FROM_REPORT` |
| No PCB file exists | `Test-Path ...ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `VERIFIED_BY_COMMAND` |
| No remaining nets were routed | No PCB file exists and no KiCad design-file edit was performed | `VERIFIED_BY_WORKFLOW` |
| DRC was not run | No PCB exists | `VERIFIED_BY_WORKFLOW` |
| Unrouted count is unknown | No PCB exists to inspect | `VERIFIED_BY_WORKFLOW` |
