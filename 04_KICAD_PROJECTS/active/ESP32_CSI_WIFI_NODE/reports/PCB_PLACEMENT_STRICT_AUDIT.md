# ESP32_CSI_WIFI_NODE PCB Placement Strict Audit

Date: 2026-05-07

Audit type: `STRICT_PLACEMENT_AUDIT_ONLY`

PCB edited during this audit: `NO`

Target PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Input Evidence

| Evidence | Status | Notes |
|---|---:|---|
| `PCB_PLACEMENT_REAL_LAYOUT_REPORT.md` | `MISSING` | Prior placement-report write was interrupted before this Markdown report was created. Audit used PCB file evidence instead. |
| `PCB_PLACEMENT_DRC_REPORT.md` | `MISSING` | Prior placement-report write was interrupted before this Markdown report was created. Audit used `PCB_PLACEMENT_DRC_REPORT.rpt` instead. |
| `PCB_PLACEMENT_DRC_REPORT.rpt` | `READ` | KiCad DRC report created 2026-05-07T10:51:26-0400. |
| `PCB_PLACEMENT_ORIENTATION_RISK_REPORT.md` | `READ` | Existing report is stale and marked `NOT_RUN_NO_ACTUAL_PLACEMENT`; risks remain valid as human-review flags. |
| `placement_real_layout_top.png` | `VISUALLY_REVIEWED` | Created from the existing KiCad SVG review export for audit viewing. |
| `placement_real_layout_bottom.png` | `VISUALLY_REVIEWED` | Created from the existing KiCad SVG review export for audit viewing. |

## File-Based Placement Findings

| Check | Result | Evidence |
|---|---:|---|
| Board outline is 100 x 65 mm | `PASS` | Edge.Cuts bbox is `(0.0, 0.0)` to `(100.0, 65.0)`, with 4 Edge.Cuts segments. |
| No footprint pile/grid remains | `PASS` | All 43 footprints have intentional coordinate placement; no arbitrary pile/grid remains. |
| No footprint is far outside board | `PASS` | File audit found `outside_or_not_near = NONE`; intentional edge-mounted connector bodies are near board edges. |
| Four mounting holes near corners | `PASS` | `MH1 (5,5)`, `MH2 (95,5)`, `MH3 (5,60)`, `MH4 (95,60)`. |
| J1 barrel jack faces left edge | `PASS_FOR_REVIEW` | `J1` at `(7.00, 22.50)`, rotation `180`; body bbox reaches left edge area. Human connector review still required. |
| J2 USB-C faces right edge | `PASS_FOR_REVIEW` | `J2` at `(94.65, 18.00)`, rotation `0`; bbox right edge is `100.00 mm`. Human connector review still required. |
| U2 ESP32 module keepout area | `PASS_FOR_REVIEW` | `U2` at `(72.00, 50.50)`, top/right half; visual/file review shows module placed with open upper board region. Footprint/package review still required. |
| U1/L1/C6/C2/C5/C7/C8 regulator cluster | `PASS_FOR_REVIEW` | Power regulator cluster is compact around x `38.5-46 mm`, y `12.5-34 mm`. Routing thermal/current review still required. |
| U3/R6/R7/R8/R9 USB support cluster | `PASS_FOR_REVIEW` | USB support cluster is compact behind J2 around x `81-86 mm`, y `11-21 mm`. USB pin/route review still required. |
| Reset/boot switches accessible | `PASS` | `SW1 (30,12)` and `SW2 (45,12)` are near lower board area and not hidden under module/connectors. |
| LEDs visible | `PASS` | `D1 (59,12)` and `D2 (65,12)` are near lower visible board area. |
| Test pads accessible | `PASS` | `TP1-TP9` are in a bottom-edge row at y `6.50 mm`, x `25-73 mm`. |
| Reference/value text readable | `NEEDS_MINOR_REPAIR_OR_REVIEW` | Values are hidden/reduced, but DRC reports 9 silk-over-copper and 5 silk-overlap warnings. |
| No courtyard overlaps | `PASS` | Current DRC category count has `0` courtyard overlaps. |
| No high-risk orientation silently accepted | `PASS` | High-risk connector, polarity, USB, PMOS, ESD, regulator, and ESP32 risks remain explicitly flagged for LJ review. |

## Current DRC Evidence

KiCad DRC command result from `PCB_PLACEMENT_DRC_REPORT.rpt`:

- DRC violations: `26`
- Unconnected items: `78`
- Schematic parity issues: `0`

DRC categories:

| Category | Count | Placement impact |
|---|---:|---|
| `drill_out_of_range` | 12 | U2 pad 41 holes are 0.20 mm while board setup minimum drill is 0.30 mm. This is a footprint/rule review item before fabrication. |
| `silk_over_copper` | 9 | Reference/silkscreen cleanup required before final PCB audit. |
| `silk_overlap` | 5 | Reference/silkscreen cleanup required before final PCB audit. |
| `unconnected_items` | 78 | Expected because routing has not started and is intentionally blocked. |

No current DRC shorts, courtyard overlaps, schematic parity errors, or copper edge clearance errors were found in the latest DRC report.

## Visual Audit Notes

Top visual review confirms:

- Board outline is present.
- Footprints are distributed into functional regions rather than a pile.
- J1 is on the left edge.
- J2 is on the right edge.
- U2 is in the upper/right half.
- Power components are clustered left/center.
- USB support components are clustered behind J2.
- Test pads are in a bottom-edge row.
- Mounting holes are at the four corners.

Bottom visual review shows no bottom-side component pile. Bottom view primarily shows through-hole/castellated features because no bottom routing/zones exist yet.

## Remaining Review Risks

| Item | Status | Required before routing/fab |
|---|---:|---|
| J1 barrel jack physical orientation and polarity | `HUMAN_REVIEW_REQUIRED` | Confirm mating opening, center-pin polarity, and enclosure clearance. |
| J2 USB-C connector orientation | `HUMAN_REVIEW_REQUIRED` | Confirm mouth direction, board-edge alignment, shell pads, and footprint pin numbering. |
| U2 ESP32-S3 module footprint and antenna/U.FL clearance | `HUMAN_REVIEW_REQUIRED` | Confirm WROOM-1U vs WROOM-1 footprint suitability and RF keepout/cable path. |
| Q1 AO3401A PMOS physical orientation | `HUMAN_REVIEW_REQUIRED` | Confirm source/gate/drain orientation after the pin-mapping repair. |
| D3 TVS/protection polarity | `HUMAN_REVIEW_REQUIRED` | Confirm package polarity/marking before routing. |
| U3 USB ESD pin mapping | `HUMAN_REVIEW_REQUIRED` | Confirm connector-side/device-side pins before routing D+/D-. |
| U1 buck regulator orientation and thermal layout | `HUMAN_REVIEW_REQUIRED` | Confirm pin-1/package orientation and regulator layout direction. |
| U2 drill/rule issue | `NEEDS_REVIEW` | Resolve 0.20 mm U2 drill rule conflict or document accepted manufacturer capability. |
| Silkscreen readability | `NEEDS_MINOR_REPAIR` | Clean reference fields before final audit. |

## Classification

Final classification: `PLACEMENT_READY_FOR_LJ_REVIEW`

Routing status: `BLOCKED_UNTIL_LJ_PLACEMENT_REVIEW_AND_RISK_ACCEPTANCE`

Rationale: The physical placement is no longer a pile/grid, no footprint is far outside the board, the outline and mounting holes match the approved specification, and current DRC has no shorts or courtyard overlaps. Routing must not begin until LJ reviews connector orientation, RF/antenna clearance, high-risk footprint orientation, the U2 drill/rule issue, and silkscreen cleanup risk.
