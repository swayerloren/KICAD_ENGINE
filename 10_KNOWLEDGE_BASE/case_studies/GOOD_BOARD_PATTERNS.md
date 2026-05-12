# Good Board Patterns

Status: `STYLE_SCORECARD_INPUT`

## Repeated Good Patterns

- connectors placed so their real openings face off-board
- USB connector, ESD, CC resistors, and data resistors kept compact
- buck input, switch node, inductor, and output caps kept as a tight cluster
- RF module keepout left clear and facing the board edge
- local schematic wiring used inside blocks instead of label-only clutter
- test pads grouped into a service cluster instead of being scattered

## Promotion Rule

Good-board examples may influence style scorecards only when the pattern is:

1. repeated across multiple examples, or
2. supported by official KiCad or vendor guidance already stored elsewhere.

## Registry Anchors

| Registry ID | Domain | Confidence | Use |
| --- | --- | --- | --- |
| `url_000043` | `docs.espressif.com` | `MEDIUM_TO_HIGH` | ESP32 checklist comparison |
| `url_010086` | `ti.com` | `HIGH` | official app-note-backed USB or power layout guidance |
| `url_010093` | `ti.com` | `HIGH` | official layout pattern evidence |
| `url_010234` | `pcbway.com` | `MEDIUM` | fab package workflow comparison only |

