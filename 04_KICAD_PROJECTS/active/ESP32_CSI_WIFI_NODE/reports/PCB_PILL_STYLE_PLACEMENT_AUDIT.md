# PCB Pill-Style Placement Audit

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Audit type: `STRICT_HUMAN_STYLE_PLACEMENT_REVIEW`

PCB edited during audit: `NO`

Routing allowed: `NO`

## Evidence Reviewed

| Evidence | Status |
|---|---:|
| `PCB_PILL_STYLE_PLACEMENT_REPORT.md` | `READ` |
| `PCB_PILL_STYLE_DRC_REPORT.md` | `READ` |
| `PCB_PILL_STYLE_MECHANICAL_CONFLICTS.md` | `READ` |
| `pill_style_placement_top.png` | `VISUALLY_REVIEWED` |
| `pill_style_placement_3d_top.png` | `VISUALLY_REVIEWED` |
| Latest DRC summary | `READ` |

## Human-Style Review

| Check | Result | Finding |
|---|---:|---|
| Practical ESP32/STM32 pill-style look | `PARTIAL_PASS` | It now looks like a narrow dev board, with ESP32 top and USB bottom. However it is too mechanically compromised to treat as a good placement. |
| Excessive dead space | `PASS` | The previous giant dead area is gone. The new board is dense rather than wasteful. |
| U2 at top with antenna/keepout toward top edge | `PASS_WITH_RISK` | Visual render shows U2 at top and RF/keepout toward the top edge. Risk: footprint/keepout is wider than the 38 mm board. |
| Antenna keepout free of copper/components/traces | `PASS_WITH_RISK` | No routing/zones exist and components are not placed in the top RF zone. Risk remains because footprint/keepout/courtyard extends beyond side edges. |
| USB-C at bottom edge and oriented | `PASS_FOR_REVIEW` | J2 is visually at the bottom edge with intentional overhang. DRC edge-clearance findings require footprint/edge review. |
| Barrel jack practical | `FAIL` | J1 is bulky for this pill board and consumes side area. It should be replaced with a smaller input connector or the board should move to wider Option C. |
| Four mounting holes practical | `FAIL` | Four M2.5 holes are not practical on this 38 mm layout with this ESP32 footprint and barrel jack. Use 2-hole strategy or wider board. |
| Buttons accessible | `PARTIAL_PASS` | SW1/SW2 are side/lower accessible, but placement is crowded and affected by surrounding mechanical density. |
| LEDs visible | `PASS_FOR_REVIEW` | D1/D2 are visible near the lower/right region. |
| Test pads accessible and in clean row | `PARTIAL_PASS` | TP1-TP9 are in a clean row, but the row is crowded near USB/support components and has courtyard/silkscreen pressure. |
| Power path compact | `PASS_WITH_RISK` | Power components are compact. J1 and D3/caps are mechanically tight, and DRC still reports related courtyard/clearance issues. |
| Buck regulator loop compact | `PASS_WITH_RISK` | U1/L1/C6/C7/C8 are compact, but the cluster is too tight for courtyard-clean placement. |
| USB path short and sensible | `PASS_WITH_RISK` | USB support is short and near J2, but test pads near USB remain stub-risk and DRC has dense-area conflicts. |
| Components too spread out | `PASS` | They are not too spread out. The problem is the opposite: too dense for the current footprint set. |
| References/values readable | `FAIL_FOR_ROUTING` | Values are hidden, but reference/silkscreen readability is not acceptable yet. DRC reports `silk_overlap` and `silk_over_copper`. |
| Courtyard conflicts | `FAIL` | Current DRC reports `18` courtyard overlaps. |
| DRC errors that matter before routing | `FAIL` | Mechanical/courtyard/clearance/drill/edge/silkscreen issues matter before routing. Unconnected items are expected, but the other categories block routing. |

## DRC Review

Latest DRC summary from the current placement:

| Category | Count | Audit disposition |
|---|---:|---|
| `unconnected_items` | 78 | Expected because no routing has been done. |
| `silk_overlap` | 19 | Must be cleaned before final layout. |
| `courtyards_overlap` | 18 | Placement/mechanical blocker. |
| `silk_over_copper` | 17 | Must be cleaned before final layout. |
| `drill_out_of_range` | 12 | U2 footprint/rule blocker. |
| `copper_edge_clearance` | 4 | USB-C board-edge/overhang review blocker. |
| `clearance` | 3 | Placement density blocker before routing. |
| `schematic parity` | 0 | Pass. |

## Human Review Judgment

The placement is a useful proof of the pill-board concept, but it is not ready to route.

Main reasons:

- `U2` footprint/keepout is wider than the 38 mm board.
- The barrel jack is not pill-board-friendly.
- Four M2.5 holes are not practical with this narrow board and current footprint set.
- Courtyard overlaps and tight clearances are still present.
- Silkscreen/readability is not acceptable yet.
- USB-C edge/overhang needs explicit footprint/edge review.

## Recommended Direction

Preferred next decision:

1. Switch to two mounting holes.
2. Replace or DNP the barrel jack in favor of a smaller input connector, or choose the wider `45 x 80 mm` option.
3. Confirm or replace the ESP32-S3-WROOM-1U footprint/keepout.
4. Only then perform a new placement pass.

## PCB Intelligence Layer Addendum

Updated: 2026-05-07

A project-specific read-only PCB intelligence layer now exists at:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/pcb_intelligence/`

This layer documents actual PCB pad-net topology, all 43 physical components, 52 pad-connected nets, placement dependencies, critical power/USB/GND routing rules, test pad access constraints, ESP32 RF keepout constraints, via/layer strategy, copper-zone strategy, and unresolved routing/mechanical risks.

Future placement repair must read this folder before moving parts. Routing remains blocked.

## Final Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing status: `ROUTING_BLOCKED`

This placement should go to LJ for decision review, but not as a placement-ready-to-route board.
