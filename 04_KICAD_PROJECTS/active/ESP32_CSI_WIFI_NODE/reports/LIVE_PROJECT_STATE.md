# Live Project State

Generated: `2026-05-08T14:49:56-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`

## Source Files

| File | Exists | SHA256 | Timestamp |
| --- | --- | --- | --- |
| `kicad_pro` | `True` | `CE1853F7614F591B5AF042ECBCF17ACC3BEB3D97091540B7B913D949900532D5` | `2026-05-08T07:04:57-04:00` |
| `kicad_sch` | `True` | `CBF1473DBCD18ED370B1E121B9BCE91F422C269A1FC9D6AF4B369E12476E52C5` | `2026-05-07T10:39:37-04:00` |
| `kicad_pcb` | `True` | `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697` | `2026-05-08T12:56:52-04:00` |

## Live PCB Truth

| Item | Result |
| --- | --- |
| PCB exists | `True` |
| Board outline exists | `True` |
| Board size | `60.0 mm x 95.0 mm` |
| Footprints | `43` |
| Mounting holes | `4` |
| Tracks | `74` |
| Vias | `32` |
| Zones | `2` |
| Placed inside outline bbox | `43 / 43` |
| Routing exists | `True` |
| Detectable unrouted nets | `4` |

## DRC

| Item | Result |
| --- | --- |
| Runnable | `True` |
| Result | `FAIL` |
| Violations | `0` |
| Unconnected items | `17` |

## Routed Nets

- `+3V3`
- `/+5V_FUSED`
- `/+5V_IN`
- `/+5V_PROTECTED`
- `/BOOT0`
- `/BUCK_BST`
- `/BUCK_SW`
- `/CC1`
- `/CC2`
- `/ESP_EN`
- `/PLED`
- `/SHIELD`
- `/SLED`
- `/STATUS_LED`
- `/U0RXD`
- `/U0TXD`
- `GND`
- `unconnected-(J2-VBUS-PadA4)`

## Unrouted Nets

- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`

## Next Action

Repair or explicitly accept the current routed geometry, approve live placement/orientation, and resolve GND strategy plus critical unrouted nets before new routing.
