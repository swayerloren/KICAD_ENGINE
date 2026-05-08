# PCB Pill-Style Placement Repair Audit

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Audit type: `STRICT_VISUAL_MECHANICAL_AUDIT`

PCB edited during audit: `NO`

Routing allowed: `NO`

## Evidence Reviewed

| Evidence | Status |
|---|---:|
| `PCB_PILL_STYLE_PLACEMENT_REPAIR_REPORT.md` | `READ` |
| `PCB_PILL_STYLE_MECHANICAL_CONFLICTS.md` | `READ` |
| `PCB_PILL_STYLE_DRC_AFTER_PLACEMENT_REPAIR.md` | `READ` |
| `_verification/pcb_visual/PILL_STYLE_PLACEMENT_REPAIR_REVIEW.md` | `READ` |
| `_verification/pcb_visual/pill_style_placement_top.png` | `VISUALLY_REVIEWED_AS_LATEST_AVAILABLE_UNREPAIRED_IMAGE` |
| `_verification/pcb_visual/pill_style_placement_bottom.png` | `VISUALLY_REVIEWED_AS_LATEST_AVAILABLE_UNREPAIRED_IMAGE` |
| `_verification/pcb_visual/pill_style_placement_3d_top.png` | `VISUALLY_REVIEWED_AS_LATEST_AVAILABLE_UNREPAIRED_IMAGE` |

## Key Finding

The repaired placement does not exist.

`PCB_PILL_STYLE_PLACEMENT_REPAIR_REPORT.md` states:

- PCB edited: `NO`
- repair status: blocked by phase gate
- no new top/bottom/3D repair images were exported

Therefore this audit is a review of the latest available unrepaired pill-style placement, not a repaired placement.

## Strict Check Results

| Check | Result | Finding |
|---|---:|---|
| Board is still pill/dev-board style, not oversized | `PASS` | Latest visual evidence shows a compact narrow board, not the previous oversized layout. |
| `U2` is at the top with antenna/keepout facing top edge | `PASS_WITH_RISK` | `U2` is visually at the top and the RF/keepout region faces the top edge. The footprint/keepout is reported wider than the 38 mm board. |
| Antenna keepout is free and not in board middle | `PASS_WITH_RISK` | No routed copper or zones exist, and no visible components are placed inside the top RF area. Width/footprint validity remains unresolved. |
| `J2` USB-C is on bottom edge with mouth facing downward/off-board | `PARTIAL_PASS_REQUIRES_REPAIR` | `J2` is at the bottom, but prior repair report and DRC still flag edge alignment/overhang review. It was not repaired. |
| `J1` bottom/lower-left side/outward or clearly flagged | `FAIL_REQUIRES_LJ_DECISION` | `J1` is side-mounted lower-left and flagged as large/not pill-board-friendly. It is not a clean bottom-edge connector solution. |
| No components/courtyards overlap | `FAIL` | DRC still reports `18` courtyard overlaps. |
| Test pads are not crowded behind USB-C | `FAIL` | Latest visual evidence shows `TP1-TP9` as a bottom row directly above/near USB-C and mixed with nearby USB/LED/support parts. |
| Test pads are in a clean accessible row | `PARTIAL_FAIL` | The pads form a row, but the row is crowded and too close to the USB support/connector area. |
| `R6/R7/R8/R9` are not mixed into test pads | `FAIL` | Latest visual evidence shows `R6/R7` near or between the lower test pad row; USB support parts remain mixed into the service area. |
| `D1/D2/R3/R4` have readable placement | `PARTIAL_FAIL` | LEDs are visible, but `R3/R4` and labels are crowded near the test pad row and require silkscreen cleanup. |
| `SW1/SW2` are accessible | `PARTIAL_PASS_WITH_MECHANICAL_RISK` | Switches are visible/side-accessible, but surrounding placement remains crowded. |
| Mounting holes have clearance | `FAIL_REQUIRES_LJ_DECISION` | Four-hole strategy is unresolved; `MH3/MH4` are moved mid-board and not true corner holes. |
| No silkscreen text over pads/holes | `FAIL` | DRC reports `19` silkscreen overlap and `17` silkscreen clipped-by-mask violations. |
| `U1/C6/L1/C2/C5/C7/C8` form tight buck cluster | `PASS_WITH_DENSITY_RISK` | The buck cluster is compact, but the current density contributes to courtyard/clearance/silkscreen violations. |
| USB cluster compact near `J2` | `PASS_WITH_LAYOUT_RISK` | The USB cluster is compact, but it conflicts with test pad/service-area spacing and needs repair before routing. |
| No obvious wasted dead zone | `PASS` | Board is dense, not wasteful. The issue is mechanical crowding, not dead space. |

## DRC Classification

| DRC category | Count | Classification |
|---|---:|---|
| `unconnected_items` | 78 | `EXPECTED_UNROUTED` |
| `silk_overlap` | 19 | `SILKSCREEN_CLEANUP_ISSUE` |
| `courtyards_overlap` | 18 | `REAL_PLACEMENT_ISSUE` |
| `silk_over_copper` | 17 | `SILKSCREEN_CLEANUP_ISSUE` |
| `drill_out_of_range` | 12 | `DRILL_FOOTPRINT_LIBRARY_ISSUE` |
| `copper_edge_clearance` | 4 | `REQUIRES_LJ_DECISION` for USB-C board-edge/overhang and footprint edge-line acceptance |
| `clearance` | 3 | `REAL_PLACEMENT_ISSUE` |
| schematic parity issues | 0 | `PASS` |

## Audit Judgment

This placement is not ready for LJ visual approval as a repaired layout.

Primary reasons:

- No repair was applied after the previous placement audit.
- Test pads remain crowded near USB-C and USB support parts.
- `J1` remains a major mechanical compromise for the compact pill board.
- Four mounting holes remain unresolved on the compact outline.
- DRC still contains real placement issues: courtyard overlaps, clearance violations, USB-C edge clearance, and silkscreen/pad conflicts.
- `U2` footprint/keepout width and drill-size issues remain unresolved.

## Required Next Step

Resolve the phase-gate inconsistency, then perform a real placement repair pass before routing.

Routing may not begin.

## Final Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`
