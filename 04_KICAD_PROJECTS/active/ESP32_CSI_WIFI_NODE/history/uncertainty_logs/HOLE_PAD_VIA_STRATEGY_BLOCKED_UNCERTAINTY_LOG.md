# HOLE_PAD_VIA_STRATEGY_BLOCKED_UNCERTAINTY_LOG

Date: 2026-05-03

## Uncertainties

| Item | Confidence | Blocking | Notes |
|---|---|---|---|
| Mounting-hole count and coordinates | `HIGH_UNCERTAINTY` | Yes | No board outline or mechanical requirements. |
| Mounting-hole diameter and plated status | `HIGH_UNCERTAINTY` | Yes | Requires hardware/enclosure/user decision. |
| Mounting-hole GND/isolation policy | `HIGH_UNCERTAINTY` | Yes | Requires EMC/mechanical/human decision. |
| Test-pad count and target nets | `HIGH_UNCERTAINTY` | Yes | Requires schematic/BOM lock and test strategy. |
| Test-pad size and spacing | `HIGH_UNCERTAINTY` | Yes | Requires fab limits and access method. |
| Signal/power/stitching/thermal via sizes | `HIGH_UNCERTAINTY` | Yes | Requires fab profile, stackup, current/thermal/layout context. |
| Ground stitching pattern | `HIGH_UNCERTAINTY` | Yes | Requires board outline, zones, antenna/USB/ESD placement, and return-path plan. |

## Required Future Evidence

- `.kicad_pcb` file.
- Board outline and stackup.
- Selected fab profile or user-confirmed fab limits.
- Placement pass reports.
- Test strategy and required probe nets.
- Mounting hardware and enclosure constraints.
- DRC and visual outputs after hole/pad/via placement.

