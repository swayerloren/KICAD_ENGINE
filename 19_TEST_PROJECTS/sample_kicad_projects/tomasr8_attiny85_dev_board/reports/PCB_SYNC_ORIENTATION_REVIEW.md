# PCB Sync And Orientation Review - ATtiny85 Golden Path Sample

Status: `NEEDS_HUMAN_REVIEW`

Generated: `2026-05-03`

## PCB Sync Evidence

- DRC command: `kicad-cli pcb drc --format report --severity-all --schematic-parity`
- Report: `_verification/kicad_cli/drc_after_repair.rpt`
- DRC violations: `15`
- Unconnected pads: `0`
- Schematic parity issues: `13`

## PCB Visual Evidence

- Top SVG: `_verification/pcb_visual/attiny85_top_NOT_FINAL.svg`
- Bottom SVG: `_verification/pcb_visual/attiny85_bottom_NOT_FINAL.svg`
- Top PNG: `_verification/pcb_visual/attiny85_top_NOT_FINAL.png`
- PCB close-up review: `reports/PCB_CLOSE_UP_REVIEW.md`
- PCB crop folder: `_verification/pcb_visual/crops`

## Orientation Review Items

| Item | Status | Notes |
| --- | --- | --- |
| `J1` USB-A connector | `BLOCKED_UNTIL_HUMAN_REVIEW` | Custom footprint exists and is mapped, but exact drawing/orientation is not verified. DRC reports silkscreen edge clearance warnings. |
| `J2` programming header | `BLOCKED_UNTIL_HUMAN_REVIEW` | Header orientation and pinout require human review. |
| `U2` AMS1117 regulator | `BLOCKED_UNTIL_HUMAN_REVIEW` | SOT-223 footprint candidate exists; exact package and pin mapping require source review. |
| `D1`, `D2` zener diodes | `NEEDS_HUMAN_REVIEW` | DRC parity reports net-name conflicts around diode pads; polarity review required. |
| `D3`, `D4` LEDs | `NEEDS_HUMAN_REVIEW` | DRC parity reports net-name conflicts around LED pads; polarity review required. |
| Board outline | `PARTIALLY_REVIEWED` | Visual exports succeeded. No manufacturing output generated. |
| Unrouted nets | `PASS_BY_DRC` | DRC reported `Found 0 unconnected pads`. |

## Result

`PCB_ORIENTATION_REVIEW_BLOCKED`

The PCB has no unrouted pads, but the gate cannot pass because ERC/DRC/parity and human-review blockers remain.
