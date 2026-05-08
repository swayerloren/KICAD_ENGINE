# PCB Mechanical Setup Claim Evidence Matrix

Date: `2026-05-06 22:15:29 -04:00`

| Claim | Evidence | Status |
| --- | --- | --- |
| Selected layout plan exists | `reports/PCB_SELECTED_LAYOUT_PLAN.md`; `Test-Path` returned `True` | `SUPPORTED` |
| PCB file exists | `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `REFUTED` |
| Board outline was created | No PCB exists; `reports/PCB_MECHANICAL_SETUP_REPORT.md` says not run | `REFUTED` |
| Mounting holes were placed | No PCB exists; `reports/PCB_BOARD_OUTLINE_AND_HOLES_REPORT.md` says not created | `REFUTED` |
| Constraints were created | No PCB exists; `reports/PCB_MECHANICAL_SETUP_REPORT.md` says not applied | `REFUTED` |
| Keepouts were created | No PCB exists; `reports/PCB_MECHANICAL_SETUP_REPORT.md` says not applied | `REFUTED` |
| DRC result exists | DRC not run because no PCB exists | `REFUTED` |
| Component placement may begin | `reports/PCB_SYNC_STATUS.md` says placement planning may begin `NO`; no PCB exists | `REFUTED` |
