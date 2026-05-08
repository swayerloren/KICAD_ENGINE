# PCB_UPDATE_FROM_SCHEMATIC_BLOCKED_UNCERTAINTY_LOG

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Uncertainties Blocking PCB Update

| Item | Status | Required evidence |
| --- | --- | --- |
| All footprints | `UNVERIFIED` | Assigned KiCad footprint for every physical schematic symbol and exact package drawing match. |
| USB-C connector | `UNVERIFIED` | Exact MPN, drawing, footprint, pin numbering, board-edge orientation, and human review. |
| AO3401A-class PMOS | `UNVERIFIED` | Exact device, pin mapping, body diode orientation, and footprint pad mapping. |
| Regulator/passives | `UNVERIFIED` | Exact MPNs, package drawings, derating, layout evidence, and footprint verification. |
| ESP32-S3 module | `UNVERIFIED` | Exact Espressif module variant land pattern and footprint match. |
| PCB board state | `NOT_CREATED_OR_NOT_FOUND` | Gate must pass before board creation/update can occur. |

