# Routing Geometry Hard Fail Commands

Date: `2026-05-08`
Branch: `hardening/execution-contract`

## Commands Run

```text
git status -sb
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python -m py_compile 14_LAYOUT_AUTOMATION/scripts/route_quality_common.py 14_LAYOUT_AUTOMATION/scripts/routing_geometry_quality.py 14_LAYOUT_AUTOMATION/scripts/detect_right_angle_traces.py 14_LAYOUT_AUTOMATION/scripts/detect_acute_jogs.py 14_LAYOUT_AUTOMATION/scripts/detect_bad_pad_entry.py 14_LAYOUT_AUTOMATION/scripts/detect_unnecessary_zigzags.py 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py
python 14_LAYOUT_AUTOMATION/scripts/routing_geometry_quality.py <fixture> <output.json> --markdown <output.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_right_angle_traces.py <fixture> <output.json> --markdown <output.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_acute_jogs.py <fixture> <output.json> --markdown <output.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_bad_pad_entry.py <fixture> <output.json> --markdown <output.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_unnecessary_zigzags.py <fixture> <output.json> --markdown <output.md>
python 14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py <fixture> <routing_plan.json> --markdown <routing_plan.md>
python 14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py <routing_plan.json> <critical_plan.json> --markdown <critical_plan.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py <fixture> <unrouted.json> --markdown <unrouted.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py <fixture> <keepouts.json> --markdown <keepouts.md>
python 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py <fixture> <trace_audit.json> --markdown <trace_audit.md>
python 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py <fixture> <routing_plan.json> <critical_plan.json> <unrouted.json> <keepouts.json> <trace_audit.json> <score.json> --markdown <score.md>
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 02_HISTORY/sessions/ROUTING_GEOMETRY_HARD_FAIL_TASK_CONTRACT.json
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "routing geometry hard-fail hardening session" --apply
```

## Key Results

- Geometry checker passed the good fixture and failed all bad fixtures.
- Focused detector wrappers returned the expected hard-fail status codes.
- Scorecard integration now blocks bad geometry instead of only logging it.
