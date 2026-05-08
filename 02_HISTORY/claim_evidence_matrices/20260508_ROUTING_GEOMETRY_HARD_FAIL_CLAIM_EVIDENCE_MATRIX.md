# Claim / Evidence Matrix - Routing Geometry Hard Fail

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| Routing geometry now has dedicated hard-fail rules. | `14_LAYOUT_AUTOMATION/ROUTING_GEOMETRY_HARD_FAIL_RULES.md` |
| Aggregate and focused detector scripts were added. | `14_LAYOUT_AUTOMATION/scripts/route_quality_common.py`, `routing_geometry_quality.py`, `detect_right_angle_traces.py`, `detect_acute_jogs.py`, `detect_bad_pad_entry.py`, `detect_unnecessary_zigzags.py` |
| Trace audit now records detailed geometry failures. | `14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py` |
| Scorecard now blocks pass status when geometry hard fails exist. | `14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py` |
| Good geometry passes and bad fixtures fail. | `14_LAYOUT_AUTOMATION/reports/ROUTING_GEOMETRY_HARD_FAIL_TEST_REPORT.md` and generated fixture outputs |
| Bad geometry now blocks an integrated routing pass. | Integration results in `ROUTING_GEOMETRY_HARD_FAIL_TEST_REPORT.md` for `good_45_degree_route` and `bad_90_degree_route` |
