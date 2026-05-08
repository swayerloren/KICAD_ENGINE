# Real Board Routing Audit

- project: `esp-rust-board`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- ready_for_copied_board_live_test: `True`
- ready_for_active_project_routing: `False`

## Pipeline Steps

| step | returncode |
| --- | --- |
| extract_kicad_pcb_to_routing_schema.py | 0 |
| pcb | 0 |
| generate_routing_plan.py | 1 |
| route_critical_nets_plan.py | 0 |
| detect_unrouted_nets.py | 0 |
| detect_trace_keepout_violations.py | 0 |
| trace_by_trace_audit.py | 1 |
| score_routing_plan.py | 1 |

## DRC

| risk | violations | errors | warnings | unconnected |
| --- | --- | --- | --- | --- |
| HIGH | 81 | 3 | 78 | 0 |

## Not Extracted

- ZONE_0_/Buck_Coil exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_1_+BATT exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_2_+5V exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_3_GND exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_4_+3V3 exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_5_VBUS exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_6_GND exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_7_+3V3 exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- per-net ratsnest extraction not implemented; only total unconnected count is extracted

## Blockers

- 26 trace audit entries flagged
- regulator critical loop not planned
- routing plan did not pass
