# Claim Evidence Matrix - ESP32_CSI_WIFI_NODE Full Routing And Copper

Date: 2026-05-07

| claim | evidence | status |
|---|---|---|
| Schematic parity passes | `reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt` reports 0 schematic parity issues | PROVEN |
| Current partial route has no route shorts/crossings in DRC | `reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt` lists only U2 drill violations plus unconnected items | PROVEN |
| Routing is incomplete | `reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt` reports 67 unconnected items | PROVEN |
| Copper pours were not created | Board stats and `reports/COPPER_POUR_GND_ZONE_REPORT.md` | PROVEN |
| RF keepout not invaded by current route endpoints/vias | pcbnew inspection found zero track/via point hits in recorded RF keepout rectangle | PROVEN_LIMITED |
| NOT_FINAL export is blocked | DRC not clean and routing incomplete | PROVEN |

