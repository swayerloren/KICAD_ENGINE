# Staged Routing Runner Audit

Date: `2026-05-08`
Branch: `hardening/execution-contract`
Scope: `repo hardening only`

## Objective

Add a stage-gated routing runner plus a no-progress detector so routing work
cannot drift into out-of-order passes or report-only retry loops.

## Files Reviewed

- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`
- `14_LAYOUT_AUTOMATION/ROUTING_SCORECARD_RULES.md`
- `03_TOOLS/scripts/execution_contract/enforce_edit_required.py`
- `14_LAYOUT_AUTOMATION/scripts/routing_geometry_quality.py`

## Files Added

- `14_LAYOUT_AUTOMATION/STAGED_ROUTING_RUNNER.md`
- `14_LAYOUT_AUTOMATION/NO_PROGRESS_DETECTOR.md`
- `14_LAYOUT_AUTOMATION/scripts/routing_stage_contracts.py`
- `14_LAYOUT_AUTOMATION/scripts/staged_routing_runner.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_no_progress.py`
- `14_LAYOUT_AUTOMATION/scripts/routing_kpi_dashboard.py`

## Hardening Result

- Ten routing stages are now declared explicitly in code.
- Each stage now carries required inputs, allowed nets, forbidden nets, DRC
  requirement, geometry requirement, hash-delta requirement, copied-board
  rehearsal requirement, pass/fail outputs, and next allowed stage.
- Broad routing now has an explicit `BLOCKED_REPAIR_MODE`.
- The detector now uses final verified report metrics instead of generic
  rehearsal text.
- The initial ESP32 replay now flags the real stalled handoff between
  `PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md` and
  `PCB_BATCH_05_USB_DATA_ROUTING_REPORT.md`.

## Validation Result

- Python syntax check: `PASS`
- No-progress detector replay: `BLOCKED_REPAIR_MODE`
- KPI dashboard generation: `PASS`
- KiCad design files edited: `NO`

## Residual Risk

- The detector still depends on consistent report labels. Future routing reports
  that drift from the established label set may require parser updates or a
  machine-readable report schema.
