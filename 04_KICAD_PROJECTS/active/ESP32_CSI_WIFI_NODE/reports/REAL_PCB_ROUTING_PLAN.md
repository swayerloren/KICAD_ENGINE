# ESP32_CSI_WIFI_NODE Real PCB Routing Plan

Date: `2026-05-07`

Final result: `ROUTING_BLOCKED`

Board hash: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

## Scope

This is a read-only routing plan derived from the current real PCB file:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

No PCB edits were made in this audit.

## Board-Derived Facts

| Item | Result |
| --- | --- |
| Nets extracted | `52` |
| Pads extracted | `167` |
| Track segments extracted | `24` |
| Grouped traces | `6` |
| Vias extracted | `2` |
| Zones extracted | `0` |
| Keepouts extracted | `0` |
| DRC risk | `HIGH` |
| DRC violations | `12` |
| DRC unconnected items | `65` |

## Partial Routing Already Present

Routed nets detected on the live board:

- `/+5V_FUSED`
- `/+5V_IN`
- `/+5V_PROTECTED`
- `/BUCK_BST`
- `/BUCK_SW`
- `+3V3`

## Current Unrouted Nets

Count: `16`

Critical unrouted nets:

- `unconnected-(J2-VBUS-PadA4)`
- `/BOOT0`
- `/ESP_EN`

Additional unrouted nets:

- `/PLED`
- `/SLED`
- `/STATUS_LED`
- `/CC1`
- `/CC2`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`
- `/SHIELD`
- `/U0RXD`
- `/U0TXD`
- `GND`

## Live Routing Audit Findings

- trace-audit flagged entries: `3`
- GND strategy: `MISSING`
- zones: `NONE`
- bottom-side routing: `present but minimal`

## Decision

Codex may not begin additional routing on this board.

Reasons:

- formal phase gate still blocks routing
- `SCHEMATIC_TO_PCB_GATE_STATUS.md` is still exact `FAIL`
- `16` unrouted nets remain
- `12` DRC violations remain
- `65` unconnected items remain
- no accepted GND strategy exists
