# REAL_PROJECT_ROUTING_WORKFLOW_AUDIT

Date: `2026-05-07`

Classification: `ROUTING_GATE_AND_WORKFLOW_DEFINED`

## Summary

This patch defines the next-stage plan for using the routing engine on a real KiCad PCB without touching `ESP32_CSI_WIFI_NODE`.

The new files do three things:

1. define exact real-project routing preconditions
2. define pass-by-pass routing workflow
3. define exact stop conditions and trace-by-trace review requirements

## Files Created

- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_PRECONDITIONS.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_TRACE_BY_TRACE_REVIEW.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`

## What Changed

- real routing now has a specific evidence gate rather than an implicit “if it seems ready” rule
- routing order is locked to critical-net-first passes
- trace-by-trace review is now explicitly mandatory on real boards
- stop conditions are now explicit for RF, USB, power, DRC, geometry, and placement-caused failure

## Readiness Position

This patch does not make the routing engine ready for a real board by itself.

It only defines the exact gate and workflow that must be satisfied before real routing may start.

## Remaining Blockers Before Real Project Routing

1. real `.kicad_pcb` to routing-schema extraction still does not exist
2. copied-board routing-state export still does not exist
3. DRC-coupled score ingestion for real boards still does not exist
4. real-board live routing-engine evidence still does not exist
5. blocked projects such as `ESP32_CSI_WIFI_NODE` remain ineligible regardless of the new workflow docs
