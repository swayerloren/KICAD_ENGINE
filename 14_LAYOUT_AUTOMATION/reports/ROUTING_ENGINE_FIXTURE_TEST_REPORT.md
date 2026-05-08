# ROUTING_ENGINE_FIXTURE_TEST_REPORT

Date: `2026-05-07`

## Scope

Ran the upgraded routing engine against four JSON fixtures under `14_LAYOUT_AUTOMATION/test_fixtures/`.

Each fixture was processed through:

1. `generate_routing_plan.py`
2. `route_critical_nets_plan.py`
3. `detect_unrouted_nets.py`
4. `detect_trace_keepout_violations.py`
5. `trace_by_trace_audit.py`
6. `score_routing_plan.py`

Each step produced JSON and Markdown outputs under `14_LAYOUT_AUTOMATION/reports/fixture_runs/`.

## Results

| fixture | status | total score | hard fails | unrouted nets | keepout violations | audit flags | ready for real KiCad test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `esp32_usb_power_fixture` | `PASS` | `90` | `0` | `0` | `0` | `0` | `YES` |
| `can_node_fixture` | `PASS` | `94` | `0` | `0` | `0` | `0` | `YES` |
| `regulator_power_fixture` | `PASS` | `92` | `0` | `0` | `0` | `0` | `YES` |
| `bad_keepout_violation_fixture` | `AUTO_BLOCKED_BAD_LAYOUT` | `42` | `7` | `1` | `2` | `2` | `NO` |

## What The Tests Proved

- The engine can parse a concrete routing fixture schema.
- The engine can produce routing-plan JSON and Markdown outputs.
- The engine can identify critical nets, power nets, and USB nets.
- The engine can detect RF and antenna keepout crossings.
- The engine can detect unrouted critical nets.
- The engine can enforce trace-by-trace audit coverage.
- The engine can hard-fail on missing GND strategy, incomplete USB pair planning, keepout violations, and vias without reason on critical nets.

## What Still Does Not Exist

- real `.kicad_pcb` extraction into the routing schema
- copied-board routing-state export from KiCad/pcbnew
- DRC-coupled route scoring from a real board
- real differential-pair tuning metrics from KiCad geometry
- production proof that the engine can drive or verify a real board without human review

## Conclusion

The routing engine is now useful as a strict planning and audit layer for fixture-driven development.

It is not yet ready to touch a real active-project KiCad board.
