# Claim Evidence Matrix - PCB Zone Setup

Date: 2026-05-06

| Claim | Evidence | Status |
|---|---|---|
| PCB file does not exist | `Test-Path ...ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `VERIFIED_BY_COMMAND` |
| Placement is not ready | `reports/PCB_PLACEMENT_STRICT_AUDIT.md` | `VERIFIED_FROM_REPORT` |
| Board outline is absent | `reports/PCB_PLACEMENT_STRICT_AUDIT.md` | `VERIFIED_FROM_REPORT` |
| Schematic-to-PCB gate is failed | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | `VERIFIED_FROM_REPORT` |
| No zones were added | No PCB exists; no KiCad design-file edit was performed | `VERIFIED_BY_WORKFLOW` |
| Critical routing may not begin | Zone setup report and placement strict audit | `VERIFIED_BY_GATE_LOGIC` |
