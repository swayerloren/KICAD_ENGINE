# ESP32_CSI_WIFI_NODE_REAL_PCB_ROUTING_PLAN_DIRECT_REPORT_PATH_MISMATCH

Date: `2026-05-07`

## Failure

The first attempt expected `generate_routing_plan.py`, `route_critical_nets_plan.py`, `detect_unrouted_nets.py`, `detect_trace_keepout_violations.py`, `trace_by_trace_audit.py`, and `score_routing_plan.py` outputs at direct project-report paths.

## Cause

The live-board audit flow had already written the authoritative JSON/Markdown artifacts under:

- `reports/real_board_routing_audit/`

The direct top-level report paths did not exist yet, so dependent commands failed with `FileNotFoundError`.

## Fix

Used the successful live audit output directory as the evidence source and wrote the requested project-facing summary reports from those artifacts.

## Status

Resolved.
