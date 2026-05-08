# PCB_PLACEMENT_PASS_1_BLOCKED_UNCERTAINTY_LOG

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Uncertainties

| Item | Status | Required evidence |
| --- | --- | --- |
| Board outline | `MISSING` | Created/synced `.kicad_pcb` with verified outline. |
| Fixed mechanical part placement | `UNKNOWN` | Board size, mounting-hole geometry, connector drawings, and enclosure constraints. |
| ESP32 module placement | `UNKNOWN` | Verified footprint, antenna/U.FL keepout, pigtail/SMA mechanical path. |
| Power path placement | `UNKNOWN` | Verified footprints and board constraints. |
| USB path placement | `UNKNOWN` | Exact USB-C/ESD footprints, connector orientation, and board-edge relation. |
| DRC status after placement | `NOT_RUN` | Placement must occur before DRC can verify placement-related issues. |

These uncertainties block placement.

