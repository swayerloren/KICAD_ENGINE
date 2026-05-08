# Variant B - Connector / Mechanical Optimized

Status: `NEEDS_HUMAN_REVIEW`

Scope note: planning only. No real `.kicad_pcb` edits are approved by this file.

Important project-specific note: `U2` is planned as `ESP32-S3-WROOM-1U-N16R8`. In this variant, RF planning focuses on reserved pigtail and connector clearance, not a PCB antenna edge zone.

## 1. Board shape and dimensions assumption

- Shape: straightforward rectangle biased for connector and hole clearance.
- Envelope assumption for comparison only: `88 mm x 38 mm`.
- Mechanical logic: favor edge connector usability, four-hole spacing, and cable insertion room over compactness.

## 2. ESP32 module placement

- `U2` in the upper-right quadrant.
- RF connector side aimed toward the top edge so the pigtail path leaves upward with minimal interaction with power entry.

## 3. ESP32 antenna keepout

- Reserve the full top-right corner band as RF connector and pigtail clearance.
- Keep mounting hardware, LEDs, and test pads out of that top-right service zone.

## 4. USB-C placement and facing direction

- `J2` on the bottom-right edge.
- Receptacle mouth faces down/off-board.
- Dedicated clearance lane left around the shell tabs and plug body.

## 5. Barrel jack placement and facing direction

- `J1` on the bottom-left edge.
- Barrel opening faces down/off-board.
- Large body clearance retained around the jack to protect insertion access.

## 6. Power path placement order

- `J1` -> `F1` -> `Q1` -> `D1`/`C1` -> `U1`/`L1`/`C2-C5` -> `3V3` rail toward the center and upper-right.
- Cluster location: left side from lower-left to mid-left.
- Intent: keep the power side mechanically isolated from USB and buttons.

## 7. USB path placement

- `J2` -> `U3` -> `R6`/`R7` -> `U2`.
- Route corridor: bottom-right upward into the right-center to meet `U2`.
- Mechanical benefit: USB chain gets dedicated space and easy plug access.

## 8. Reset/boot buttons

- `SW1` and `SW2` on the right edge, but above the USB connector height.
- This prevents the inserted USB cable from blocking button access.

## 9. LEDs

- `D2`/`R8` and `D3`/`R9` on the upper-left to upper-center visual band.
- Intent: visible from the top face and not hidden by bottom-edge connectors.

## 10. Test pads

- `TP1-TP7` on the back side in a long service row.
- `TP8`/`TP9` optional only, positioned only if later USB stub review allows them.

## 11. Mounting holes

- Four corner holes with wider edge margins than Variant A.
- Best screw-head and washer clearance of the three concepts.

## 12. Projected major trace paths

- 5 V path rises from the lower-left into the left-side power island.
- `3V3` runs from left-center toward `U2` across the upper-middle.
- USB path runs from lower-right upward into `U2` on the right side.
- Buttons and LED traces stay short to the upper and right control area.

## 13. Expected via strategy

- Fewer forced vias from mechanical crowding than Variant A.
- One or two vias likely for test-pad breakout and slow control cleanup.
- USB pair can likely stay on one layer.

## 14. Routing risks

- Longer cross-board `3V3` distribution path than Variant C.
- More total board area can tempt loose low-speed routing later.
- Right-side control cluster may still compete with USB escape near `U2`.

## 15. Mechanical/orientation risks

- Largest board of the three options.
- May be less desirable if enclosure space is tight.
- Needs confirmation that the pigtail bend and top-right service zone are actually compatible with the enclosure.

## 16. Human review items

- Confirm whether the enclosure really supports the larger rectangular footprint.
- Confirm that four-corner mounting is required instead of a simpler two-hole strategy.
- Confirm exact `J1`/`J2` footprints and body overhang.
- Confirm `U2` RF connector and pigtail exit orientation relative to the enclosure wall.

## 17. Scorecard

| Category | Max | Score | Notes |
| --- | ---: | ---: | --- |
| Mechanical correctness | 20 | 18 | Best connector and hole clearance of the three. |
| Connector orientation correctness | 20 | 18 | Very clean mechanical logic for J1 and J2. |
| Antenna/RF keepout correctness | 15 | 12 | Good reserved RF corner, though not as routing-clean as Variant C. |
| Power path quality | 15 | 11 | Sensible, but `3V3` spread is longer than ideal. |
| USB/data routing quality | 10 | 7 | Dedicated USB corridor, but right-side climb is not shortest. |
| Component grouping quality | 10 | 8 | Mechanical grouping is strong. |
| Routing feasibility | 10 | 7 | Better than A, but still not the cleanest electrical flow. |

- Category subtotal: `81`
- Human-review risk level: `LOW`
- Human-review penalty: `2`
- Total score: `79`
- Variant status: `NEEDS_HUMAN_REVIEW`

## Machine Score Input

```json
{
  "project": "ESP32_CSI_WIFI_NODE",
  "variant_id": "VARIANT_B",
  "mechanical_correctness": 18,
  "connector_orientation_correctness": 18,
  "antenna_rf_keepout_correctness": 12,
  "power_path_quality": 11,
  "usb_data_routing_quality": 7,
  "component_grouping_quality": 8,
  "routing_feasibility": 7,
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
  "notes": "Mechanical-first concept using reviewed USB4105-class USB-C geometry and reviewed right-angle barrel-jack reference geometry as sandbox proxies.",
  "human_review_notes": "Board dimensions are still an assumption, enclosure fit is not yet verified, and exact connector/package lock remains outside this planning task."
}
```
