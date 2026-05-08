# Maintenance Layer Investigation And Repair Response Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-07T22:39:00-04:00`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `92/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `19/20`
- Datasheet/component accuracy: `14/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `8/10`
- Uncertainty disclosure: `8/10`
- End-user usefulness: `9/10`

## Basis

The repair was validated with syntax checks, a live maintenance cycle run, and phase checks against the active project. The remaining score gap comes from stale-prone reports that still need source-hash adoption and from the fact that placement/routing continuation still requires human review.

## Evidence

- `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`
- `03_TOOLS/scripts/project_state/*`
- `03_TOOLS/scripts/project_gate/check_phase_allowed.py`
- `reports/LIVE_PROJECT_STATE.md`
- `reports/STALE_REPORTS_AUDIT.md`
- `reports/GATE_RECONCILIATION_REPORT.md`
