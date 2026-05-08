# PCB Full Routing Uncertainty Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Status

`UNVERIFIED_FULL_ROUTING_BLOCKED`

## Uncertainties

| Item | Severity | Confidence | Human review required | Notes |
|---|---|---|---|---|
| Remaining signal routing | `HIGH` | `LOW` | Yes | No PCB exists and critical routing failed. |
| LED/button/test-pad/misc routing | `MEDIUM` | `LOW` | Yes | No PCB exists and low-risk nets cannot be routed before critical nets. |
| Trace widths and clearances | `HIGH` | `LOW` | Yes | No routed board or DRC output exists. |
| Vias and stubs | `HIGH` | `LOW` | Yes | No routed board exists. |
| Antenna keepout crossings | `HIGH` | `LOW` | Yes | No PCB keepout or routes exist. |
| Courtyard/silkscreen/label readability | `MEDIUM` | `LOW` | Yes | No placed/routed PCB exists. |
| GND islands | `HIGH` | `LOW` | Yes | No zones exist. |

## Resolution

Keep full routing blocked until critical routing is pass/acceptable and all upstream PCB prerequisites are satisfied.

