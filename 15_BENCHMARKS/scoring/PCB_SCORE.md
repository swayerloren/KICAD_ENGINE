# PCB Score

Default PCB/layout allocation: 15 points.

## Criteria

| Area | Points | Checks |
| --- | ---: | --- |
| Footprint placement risk | 3 | Mechanical constraints, connector access, keepouts, height, edge constraints, and service access are reviewed |
| High-risk net handling | 3 | USB, CAN, RF, clocks, switching regulators, high-current, and analog nets are identified and routed/planned conservatively |
| Power and grounding | 3 | Return paths, pours, regulator loops, decoupling placement, thermal relief, and current paths are reviewed |
| Connector/polarity orientation | 2 | Pin 1, cable direction, mating parts, shell pads, polarity marks, and human review are explicit |
| DRC discipline | 2 | DRC report exists or absence is justified for a planning-only task |
| Review artifacts | 2 | Screenshots/renders/plots/reports are included where appropriate and marked `NOT_FINAL` |

## Automatic Penalties

- Connector orientation not reviewed: subtract up to 3.
- Exact footprint not verified for mechanical connector: subtract up to 4 or cap under master rubric.
- DRC errors ignored: subtract up to 3.
- Switching regulator layout not reviewed: subtract up to 3.
- RF or USB layout treated as generic routing: subtract up to 3.

## Notes

KiCad Engine should not claim complete AI placement or autorouting from this score. PCB score can measure planning, review, DRC interpretation, and explicit risk handling until actual layout automation is implemented and tested.
