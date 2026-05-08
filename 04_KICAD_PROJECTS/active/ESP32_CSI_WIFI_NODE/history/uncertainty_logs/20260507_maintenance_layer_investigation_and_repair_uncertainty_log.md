# Maintenance Layer Investigation And Repair Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-07T22:39:00-04:00`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `MEDIUM`
Confidence: `MEDIUM`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Uncertainties

- the live placement-inside-outline test is geometric and bounding-box based; it is not a substitute for full human placement review
- several operational reports still lack both schematic and PCB hashes, so they are weak even when not formally stale
- historical project history entries still describe earlier blocked states and may confuse future agents if they are read as live status instead of history

## Controlled By

- `LIVE_PROJECT_STATE.json`
- `STALE_REPORTS_AUDIT.md`
- `GATE_RECONCILIATION_REPORT.md`
- `MAINTENANCE_CYCLE_REPORT.md`

## Required Follow-Up

- expand source-hash coverage across remaining operational reports
- keep human review in the routing continuation gate
