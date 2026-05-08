# Remaining Before NOT_FINAL JLCPCB Export

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Final classification: `BLOCKED_BEFORE_NOT_FINAL_EXPORT`

## Export Decision

NOT_FINAL JLCPCB export is blocked.

Reason: the PCB is not routed, not copper-poured, not final-DRC-clean, and not approved for final PCB review.

## Remaining Required Work

| Area | Required action | Current status |
|---|---|---|
| Phase gate | Pass or formally approve logged exception | `BLOCKED` |
| Placement/mechanical | Repair and approve current placement | `ACTIVE_BLOCKER` |
| J1 barrel jack | Provide verified 3D model or choose different verified footprint/connector | `ACTIVE_BLOCKER` |
| U2 drill/rule issue | Resolve or document LJ/manufacturer acceptance | `ACTIVE_BLOCKER` |
| Routing | Complete routing and prove no unrouted nets | `NOT_DONE` |
| USB route | Route and review D+/D-, CC, ESD, shield policy | `NOT_DONE` |
| Buck route | Route and review BUCK_SW, BST, +3V3, GND loop | `NOT_DONE` |
| Power widths | Verify +5V and +3V3 width rules | `NOT_DONE` |
| Copper zones | Create/refill GND zones and stitching vias where allowed | `NOT_DONE` |
| RF keepout | Prove no copper/traces/vias/components violate keepout | `NOT_PROVEN` |
| Final DRC | Run `kicad-cli pcb drc --schematic-parity --severity-all` | `NOT_DONE` |
| Visual evidence | Export top/bottom/3D final review images | `NOT_DONE` |
| LJ review | Final human PCB visual review | `NOT_READY` |

## Do Not Export Yet

- Gerbers: `NO`
- Drill files: `NO`
- BOM: `NO`
- CPL / pick-and-place: `NO`
- STEP: `NO`
- JLCPCB package: `NO`

