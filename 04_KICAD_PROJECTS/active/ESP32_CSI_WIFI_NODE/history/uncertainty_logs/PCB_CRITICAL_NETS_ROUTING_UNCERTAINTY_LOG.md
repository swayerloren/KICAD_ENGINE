# PCB Critical Nets Routing Uncertainty Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Status

`UNVERIFIED_ROUTING_BLOCKED`

## Uncertainties

| Item | Severity | Confidence | Human review required | Notes |
|---|---|---|---|---|
| Critical power trace width and copper geometry | `HIGH` | `LOW` | Yes | No PCB, current budget, stackup, or fab profile exists. |
| Regulator critical-loop layout | `HIGH` | `LOW` | Yes | Requires exact component placement and datasheet layout guidance. |
| USB D+/D- geometry and routing quality | `HIGH` | `LOW` | Yes | Requires exact connector/ESD placement, stackup, and DRC constraints. |
| ESP32 EN/BOOT routing | `MEDIUM` | `LOW` | Yes | Source verification remains required before layout. |
| Decoupling loop routing | `HIGH` | `LOW` | Yes | No component placement exists. |
| ESD/protection routing | `HIGH` | `LOW` | Yes | Connector/entry-point placement and exact footprints unresolved. |
| Antenna keepout | `HIGH` | `LOW` | Yes | No PCB keepout geometry exists. |

## Resolution

Keep critical routing blocked until the schematic-to-PCB gate, PCB creation/update, placement, via strategy, and zone strategy pass.

