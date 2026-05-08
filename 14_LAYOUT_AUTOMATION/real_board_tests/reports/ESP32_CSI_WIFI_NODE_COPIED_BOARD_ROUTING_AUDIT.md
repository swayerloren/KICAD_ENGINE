# Real Board Routing Audit

- source_pcb: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- copied_pcb: `14_LAYOUT_AUTOMATION/real_board_tests/sample_inputs/ESP32_CSI_WIFI_NODE_20260507_210220/ESP32_CSI_WIFI_NODE.kicad_pcb`
- source_sha256: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`
- copied_sha256: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

- project: `ESP32_CSI_WIFI_NODE`
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
| detect_unrouted_nets.py | 1 |
| detect_trace_keepout_violations.py | 0 |
| trace_by_trace_audit.py | 1 |
| score_routing_plan.py | 1 |

## DRC

| risk | violations | errors | warnings | unconnected |
| --- | --- | --- | --- | --- |
| HIGH | 12 | 12 | 0 | 65 |

## Not Extracted

- per-net ratsnest extraction not implemented; only total unconnected count is extracted
- zone polygon outlines not extracted

## Blockers

- 16 unrouted nets remain
- 3 trace audit entries flagged
- GND strategy missing
- critical power net missing
- routing plan did not pass
- unrouted critical net
