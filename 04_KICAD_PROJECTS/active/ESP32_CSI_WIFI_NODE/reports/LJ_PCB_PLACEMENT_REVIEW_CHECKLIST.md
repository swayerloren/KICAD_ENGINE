# LJ PCB Placement Review Checklist

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Status: `AWAITING_LJ_PLACEMENT_REVIEW`

Routing allowed now: `NO`

## Placement Checks

| Check | LJ status |
|---|---|
| Board outline is 100 mm x 65 mm | `[ ] APPROVE / [ ] REJECT` |
| `MH1` at `(5,5)` has acceptable screw and edge clearance | `[ ] APPROVE / [ ] REJECT` |
| `MH2` at `(95,5)` has acceptable screw and edge clearance | `[ ] APPROVE / [ ] REJECT` |
| `MH3` at `(5,60)` has acceptable screw and edge clearance | `[ ] APPROVE / [ ] REJECT` |
| `MH4` at `(95,60)` has acceptable screw and edge clearance | `[ ] APPROVE / [ ] REJECT` |
| `J1` barrel jack is on left edge and faces off-board left | `[ ] APPROVE / [ ] REJECT` |
| `J2` USB-C is on right edge and faces off-board right | `[ ] APPROVE / [ ] REJECT` |
| `U2` ESP32 module position/orientation is acceptable | `[ ] APPROVE / [ ] REJECT` |
| `U2` antenna/U.FL/pigtail keepout is acceptable | `[ ] APPROVE / [ ] REJECT` |
| Power chain placement is acceptable: `J1 -> F1 -> Q1 -> D3/C2/C5 -> U1 -> L1 -> C7/C8 -> U2` | `[ ] APPROVE / [ ] REJECT` |
| USB support placement is acceptable: `J2 -> U3 -> R8/R9 -> U2`, with `R6/R7` near J2 | `[ ] APPROVE / [ ] REJECT` |
| `SW1` and `SW2` are accessible | `[ ] APPROVE / [ ] REJECT` |
| `D1` and `D2` LEDs are visible enough for prototype use | `[ ] APPROVE / [ ] REJECT` |
| `TP1-TP9` are accessible along the bottom edge | `[ ] APPROVE / [ ] REJECT` |
| Reference text is acceptable for prototype review, or minor cleanup is approved before routing | `[ ] APPROVE / [ ] REJECT` |

## Orientation And Footprint Risks

| Risk | LJ status |
|---|---|
| Confirm `J1` barrel jack footprint orientation and center-pin polarity | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `J2` USB-C footprint orientation, shell pad placement, and board-edge alignment | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `Q1` AO3401A physical SOT-23 orientation after pin-mapping repair | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `D3` TVS/protection diode polarity and footprint marking | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `U3` USB ESD array pin mapping/orientation | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `U1` AP63203 regulator package orientation and pin-1 location | `[ ] ACCEPT / [ ] REJECT` |
| Confirm `U2` ESP32-S3-WROOM-1U vs footprint/package suitability | `[ ] ACCEPT / [ ] REJECT` |
| Confirm U2 0.20 mm drill/rule issue disposition | `[ ] ACCEPT / [ ] REJECT` |

## Routing Gate

Routing may begin only after:

- `[ ]` LJ accepts or rejects the placement.
- `[ ]` All rejected placement/orientation items have a repair decision.
- `[ ]` The U2 drill/rule issue is resolved or explicitly accepted for prototype review.
- `[ ]` Routing phase is explicitly requested.

Current routing decision: `ROUTING_BLOCKED`
