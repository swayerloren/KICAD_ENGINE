# Variant A - Compact Dev Board Style

Status: `NEEDS_HUMAN_REVIEW`

Scope note: planning only. No real `.kicad_pcb` edits are approved by this file.

Important project-specific note: `U2` is currently planned as `ESP32-S3-WROOM-1U-N16R8`, which is the external-antenna `-1U` module. In this variant, the "antenna keepout" means reserved RF connector and coax/pigtail clearance, not a WROOM PCB-antenna no-copper zone.

## 1. Board shape and dimensions assumption

- Shape: compact rounded rectangle / pill-style dev board.
- Envelope assumption for comparison only: `78 mm x 30 mm`.
- Mechanical logic: smallest board that still fits J1, J2, U2, four planning holes, buttons, and test access.
- Constraint: dimensions are not locked by enclosure evidence yet.

## 2. ESP32 module placement

- `U2` in the upper third of the board, centered slightly right of midline.
- RF connector side of the `-1U` module faces the upper-right area so the pigtail can leave without crossing USB or the buck cluster.

## 3. ESP32 antenna keepout

- Reserve a no-crowding RF service zone around the `U2` RF connector and the immediate pigtail bend radius area.
- No power inductor, barrel jack body, mounting hole, LED cluster, or test-pad row in that zone.

## 4. USB-C placement and facing direction

- `J2` on the bottom edge, slightly right of center.
- Receptacle mouth faces down/off-board.
- Mechanical tabs and body overhang are assumed from the reviewed `USB4105`-class candidate geometry.

## 5. Barrel jack placement and facing direction

- `J1` on the bottom edge, left side.
- Barrel opening faces down/off-board.
- Rear solder-leg side faces inward toward the protection chain.
- Mechanical envelope is based on the reviewed right-angle barrel-jack reference geometry.

## 6. Power path placement order

- `J1` -> `F1` -> `Q1` -> `D1`/`C1` input protection and bulk -> `U1`/`L1`/`C2-C5` buck cluster -> local `3V3` distribution toward `U2`.
- Cluster location: lower-left quadrant.
- Intent: keep the wide 5 V path short and keep the buck cluster away from the RF service zone.

## 7. USB path placement

- `J2` -> `U3` ESD -> `R6`/`R7` series resistors -> `U2` USB pins.
- Keep the whole USB chain in the lower-right to center-right corridor.
- `TP8`/`TP9` stay optional only; omit or move to very short stubs later.

## 8. Reset/boot buttons

- `SW1` and `SW2` on the right edge, vertically stacked near mid-height.
- Reason: thumb access remains practical even when cables are plugged into the bottom edge.

## 9. LEDs

- `D2`/`R8` power LED and `D3`/`R9` status LED near the lower-right top side.
- Must stay visible above the inserted USB plug body.

## 10. Test pads

- `TP1-TP7` in two short back-side rows under the center section.
- `TP8`/`TP9` marked as optional due USB stub risk.
- Power and control pads grouped away from the RF side.

## 11. Mounting holes

- Keep all four planned holes `MH1-MH4`, but use very tight corner placement.
- This is the main mechanical compromise of the compact variant.

## 12. Projected major trace paths

- 5 V path runs up the left side from `J1` into the buck input cluster.
- `3V3` leaves the lower-left buck cluster and climbs toward `U2` along the left/center spine.
- USB path stays on the lower-right to center-right corridor.
- Low-speed debug/test nets escape inward and then to back-side pads.

## 13. Expected via strategy

- Prefer top-layer clustering for `J1` power chain and the buck loop.
- Use a few bottom escapes for test pads and slow control nets.
- USB pair should stay on one layer if possible; zero vias preferred.

## 14. Routing risks

- Bottom-edge crowding between `J1` and `J2`.
- Four mounting holes on a narrow board compress routing channels.
- Limited space between USB chain, button stack, and LED visibility area.

## 15. Mechanical/orientation risks

- Compact width makes connector body clearance and screw-head clearance sensitive.
- Needs careful confirmation that the barrel plug and USB plug do not mechanically fight each other.

## 16. Human review items

- Confirm exact board-width target from enclosure or panel constraint.
- Confirm exact `J1` and `J2` footprints, tabs, overhang, and keepouts.
- Confirm `U2` `-1U` RF connector orientation and pigtail bend space.
- Confirm whether four holes are really required on this narrow outline.
- Confirm whether `TP8`/`TP9` should be omitted entirely.

## 17. Scorecard

| Category | Max | Score | Notes |
| --- | ---: | ---: | --- |
| Mechanical correctness | 20 | 13 | Usable, but edge and hole crowding are significant. |
| Connector orientation correctness | 20 | 15 | Edge logic is clean, but exact footprints are still candidate-based. |
| Antenna/RF keepout correctness | 15 | 12 | RF service zone is protected, but compact height reduces margin. |
| Power path quality | 15 | 11 | Power chain is credible, but compressed. |
| USB/data routing quality | 10 | 7 | Direct enough, but crowded by compact bottom-edge packaging. |
| Component grouping quality | 10 | 7 | Functional grouping works, but density is high. |
| Routing feasibility | 10 | 6 | Likely workable, but routing channels are tight. |

- Category subtotal: `71`
- Human-review risk level: `MEDIUM`
- Human-review penalty: `5`
- Total score: `66`
- Variant status: `NEEDS_HUMAN_REVIEW`

## Machine Score Input

```json
{
  "project": "ESP32_CSI_WIFI_NODE",
  "variant_id": "VARIANT_A",
  "mechanical_correctness": 13,
  "connector_orientation_correctness": 15,
  "antenna_rf_keepout_correctness": 12,
  "power_path_quality": 11,
  "usb_data_routing_quality": 7,
  "component_grouping_quality": 7,
  "routing_feasibility": 6,
  "human_review_risk_level": "MEDIUM",
  "board_dimensions_known": false,
  "board_dimensions_guessed_anyway": false,
  "mounting_holes_required": true,
  "mounting_holes_present": true,
  "usb_c_required": true,
  "usb_c_on_intended_edge": true,
  "usb_c_facing_correctly": true,
  "barrel_jack_required": true,
  "barrel_jack_placed": true,
  "barrel_jack_facing_correctly": true,
  "esp32_antenna_keepout_blocked": false,
  "high_risk_connector_orientation_reviewed": true,
  "all_footprints_assigned": true,
  "high_risk_connector_footprints_tied_to_exact_package": true,
  "routing_projection_crosses_antenna_keepout": false,
  "power_path_sensible": true,
  "notes": "Compact concept using USB4105-class USB-C geometry and right-angle barrel-jack reference geometry as sandbox mechanical proxies only.",
  "human_review_notes": "Board dimensions are not locked, exact connector footprints remain blocked by project gate evidence, and four-hole density may be unacceptable."
}
```
