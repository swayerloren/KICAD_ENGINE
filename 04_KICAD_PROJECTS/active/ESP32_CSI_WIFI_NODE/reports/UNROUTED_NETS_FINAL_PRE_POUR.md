# Unrouted Nets Final Pre-Pour

Status: `NOT_MEASURED_BLOCKED`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Final Pre-Pour Unrouted Status

No final pre-pour unrouted-net count exists because routing repair was blocked and no routing repair occurred.

Final classification:

`ROUTING_BLOCKED_BY_FOOTPRINT_OR_MECHANICAL_ISSUE`

## Latest Available Unrouted Context

The latest reviewed pre-routing/post-orientation DRC reported:

- Unconnected pads: `78`
- DRC violations: `12 x U2 pad 41 drill_out_of_range`
- Footprint errors: `0`

This is not a final pre-pour measurement.

## Exact Blockers Preventing Final Unrouted Resolution

| Blocker | Evidence |
|---|---|
| Routing phase gate blocks routing | `check_phase_allowed.py --phase 8` returned `PHASE_GATE_RESULT: BLOCKED` |
| Placement repair not applied / placement not ready | `pcb_intelligence\ROUTING_RISK_REGISTER.md`; `PLACEMENT_DEPENDENCY_MAP.md` |
| J1 barrel jack mechanical strategy unresolved | `ROUTING_RISK_REGISTER.md` |
| U2 footprint/keepout width risk unresolved | `ROUTING_RISK_REGISTER.md`; `PLACEMENT_DEPENDENCY_MAP.md` |
| Four-hole compact mounting unresolved | `ROUTING_RISK_REGISTER.md` |
| U2 pad 41 drill-size violation remains open | latest available DRC context |
| USB D+/D- test pads remain stub risk | `ROUTING_RISK_REGISTER.md`; `TEST_PAD_ACCESS_PLAN.md` |
| Silkscreen/courtyard/clearance blockers remain | `ROUTING_RISK_REGISTER.md` |

Copper pour may begin: `NO`

