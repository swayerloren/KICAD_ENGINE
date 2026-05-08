# Claim Evidence Matrix - Critical Routing

Date: 2026-05-06

| Claim | Evidence | Status |
|---|---|---|
| Critical routing is blocked | `reports/PCB_COPPER_ZONE_GROUND_PLANE_REPORT.md` and `reports/PCB_PLACEMENT_STRICT_AUDIT.md` | `VERIFIED_FROM_REPORTS` |
| No PCB file exists | `Test-Path ...ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `VERIFIED_BY_COMMAND` |
| Schematic-to-PCB gate is failed | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | `VERIFIED_FROM_REPORT` |
| No critical nets were routed | No PCB file exists; no KiCad design-file edit was performed | `VERIFIED_BY_WORKFLOW` |
| DRC was not run | No PCB exists | `VERIFIED_BY_WORKFLOW` |
