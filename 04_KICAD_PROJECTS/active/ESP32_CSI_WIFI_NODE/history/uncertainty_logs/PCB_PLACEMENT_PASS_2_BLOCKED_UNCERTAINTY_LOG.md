# PCB_PLACEMENT_PASS_2_BLOCKED_UNCERTAINTY_LOG

Date: 2026-05-03

## Uncertainties

| Item | Confidence | Blocking | Notes |
|---|---|---|---|
| Future board size and outline | `HIGH_UNCERTAINTY` | Yes | No mechanical requirements are available in current reports. |
| Connector orientation | `HIGH_UNCERTAINTY` | Yes | No exact connector drawings, footprints, or board edge exist. |
| PMOS orientation | `HIGH_UNCERTAINTY` | Yes | AO3401A symbol/footprint pin mapping remains blocked. |
| Polarity-sensitive part orientation | `HIGH_UNCERTAINTY` | Yes | No PCB footprint/silkscreen/fab evidence exists. |
| Courtyard clearance | `UNKNOWN` | Yes | No PCB footprint geometry exists. |

## Required Future Evidence

- `.kicad_pcb` file.
- Board outline.
- Assigned footprints.
- Exact package drawings.
- Connector drawings and human orientation review.
- DRC and visual outputs after placement.

