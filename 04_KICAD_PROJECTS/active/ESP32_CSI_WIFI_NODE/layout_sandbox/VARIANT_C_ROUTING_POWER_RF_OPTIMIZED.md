# Variant C - Routing / Power / RF Optimized

Status: `NEEDS_HUMAN_REVIEW`

Scope note: planning only. No real `.kicad_pcb` edits are approved by this file.

Important project-specific note: `U2` is planned as `ESP32-S3-WROOM-1U-N16R8`. In this variant, RF optimization means preserving a quiet upper RF connector and pigtail corridor rather than optimizing for a PCB antenna edge.

## 1. Board shape and dimensions assumption

- Shape: slightly stepped or asymmetrical rounded rectangle with an RF service bias near the top-right.
- Envelope assumption for comparison only: `84 mm x 34 mm`.
- Mechanical logic: still compact, but shaped to preserve a cleaner RF zone and cleaner routing corridors than Variant A.

## 2. ESP32 module placement

- `U2` in the upper-right quadrant, but pulled inward enough to leave a deliberate RF connector and pigtail service zone.
- USB-facing pins remain closer to the center-right so the USB path can stay short.

## 3. ESP32 antenna keepout

- Reserve a top-right quiet zone around the `-1U` RF connector and the first pigtail bend.
- No inductor, fuse, mounting hole, LED row, or test-pad breakout in that zone.
- This is the cleanest RF concept of the three.

## 4. USB-C placement and facing direction

- `J2` at the bottom-center to bottom-right transition.
- Receptacle mouth faces down/off-board.
- This gives the most direct path from `J2` to `U3` to `R6/R7` to `U2`.

## 5. Barrel jack placement and facing direction

- `J1` on the bottom-left edge.
- Barrel opening faces down/off-board.
- Separation from USB keeps the high-current entry and USB data cluster from competing for the same corridor.

## 6. Power path placement order

- `J1` -> `F1` -> `Q1` -> `D1`/`C1` -> `U1`/`L1`/`C2-C5` -> local `3V3` spine upward into `U2`.
- Cluster location: lower-left to center-left.
- Intent: shortest credible power chain with a direct `3V3` feed toward `U2`, while keeping switching activity away from the RF corner.

## 7. USB path placement

- `J2` -> `U3` -> `R6`/`R7` -> `U2`.
- Path stays in a tight bottom-center/right to center-right corridor with the least turning of the three concepts.
- `TP8`/`TP9` should remain DNI or be omitted unless a later short-stub proof exists.

## 8. Reset/boot buttons

- `SW1` and `SW2` on the right edge, below the RF corner and above the USB connector height.
- This keeps them reachable and avoids the bottom connector crowding of Variant A.

## 9. LEDs

- `D2`/`R8` and `D3`/`R9` near the lower-right top side, above the USB plug envelope.
- Keeps visibility good without intruding on the RF corner.

## 10. Test pads

- `TP1-TP7` split into two back-side groups:
  - power/control pads near the left-center
  - UART/control pads near the lower-right center
- `TP8`/`TP9` remain optional only because of USB stub risk.

## 11. Mounting holes

- Four holes retained, but the top-right hole is pulled away from the RF service zone.
- Better compromise than A, smaller than B.

## 12. Projected major trace paths

- 5 V entry stays on the left side into the buck cluster.
- `3V3` runs up a short left-center spine into `U2`.
- USB path stays compact from bottom-center/right into `U2`.
- Low-speed button/LED/test connections use short local escapes toward the right and back side.

## 13. Expected via strategy

- Critical power and USB paths should stay mostly on one layer in their local corridors.
- Use a controlled small number of vias for slow nets and test-pad escape only.
- This is the least via-hungry concept of the three.

## 14. Routing risks

- The stepped or asymmetrical shape needs careful enclosure confirmation.
- The RF corner and top-right hole spacing must be checked against real screw hardware.
- Tight control of USB test-pad policy is still required.

## 15. Mechanical/orientation risks

- Less mechanically obvious than Variant B because the outline is more purpose-shaped.
- Requires LJ approval that the asymmetry is justified and acceptable for enclosure use.

## 16. Human review items

- Confirm whether the asymmetrical shape is acceptable for the enclosure.
- Confirm exact `J1` and `J2` mechanical parts and board-edge relationship.
- Confirm `U2` RF connector and pigtail bend envelope in the top-right zone.
- Confirm top-right mounting-hole clearance against the pigtail path.
- Confirm final policy on `TP8`/`TP9`.

## 17. Scorecard

| Category | Max | Score | Notes |
| --- | ---: | ---: | --- |
| Mechanical correctness | 20 | 16 | Good, but shape is less conventional than Variant B. |
| Connector orientation correctness | 20 | 17 | Strong edge logic with clean J1/J2 separation. |
| Antenna/RF keepout correctness | 15 | 14 | Best RF service-zone preservation of the three. |
| Power path quality | 15 | 14 | Cleanest source-to-regulator-to-3V3 flow. |
| USB/data routing quality | 10 | 9 | Shortest and straightest projected USB corridor. |
| Component grouping quality | 10 | 9 | Best functional clustering balance. |
| Routing feasibility | 10 | 9 | Best overall routing structure. |

- Category subtotal: `88`
- Human-review risk level: `LOW`
- Human-review penalty: `2`
- Total score: `86`
- Variant status: `NEEDS_HUMAN_REVIEW`

## Machine Score Input

```json
{
  "project": "ESP32_CSI_WIFI_NODE",
  "variant_id": "VARIANT_C",
  "mechanical_correctness": 16,
  "connector_orientation_correctness": 17,
  "antenna_rf_keepout_correctness": 14,
  "power_path_quality": 14,
  "usb_data_routing_quality": 9,
  "component_grouping_quality": 9,
  "routing_feasibility": 9,
  "human_review_risk_level": "LOW",
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
  "notes": "Electrical-first concept using reviewed USB4105-class USB-C geometry, reviewed right-angle barrel-jack reference geometry, and a protected WROOM-1U pigtail service zone.",
  "human_review_notes": "Board dimensions remain assumed, exact package lock remains blocked elsewhere, and the asymmetrical outline needs LJ approval before placement."
}
```
