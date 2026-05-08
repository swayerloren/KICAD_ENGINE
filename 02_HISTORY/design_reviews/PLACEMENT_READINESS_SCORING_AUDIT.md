# Placement Readiness Scoring Audit

Status: `COMPLETED`

Date: `2026-05-08`

Branch: `hardening/execution-contract`

## Purpose

Add a placement-readiness scorecard so routing preconditions no longer rely on
generic placement reports alone.

## Scope

- no `.kicad_sch` edits
- no `.kicad_pcb` edits
- no routing
- no manufacturing outputs

## Files Added

- `14_LAYOUT_AUTOMATION/PLACEMENT_READINESS_SCORECARD.md`
- `14_LAYOUT_AUTOMATION/scripts/score_placement_readiness.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_connector_orientation_risks.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_power_path_placement_risks.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_usb_cluster_placement_risks.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_antenna_keepout_placement_risks.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_testpad_accessibility_risks.py`

## Files Updated

- `14_LAYOUT_AUTOMATION/scripts/_placement_common.py`
- `14_LAYOUT_AUTOMATION/scripts/README.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_PRECONDITIONS.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`
- `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`

## Validation Run

Copied-board source:

- `C:\Users\LJ\AppData\Local\Temp\kicad_engine_placement_readiness\ESP32_CSI_WIFI_NODE_copy.kicad_pcb`

Copied-board hash:

- `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`

Placement result on copied board:

- status: `PLACEMENT_READY_FOR_ROUTING`
- total score: `98 / 100`
- hard fails: `_none_`
- warning: `regulator -> output_cluster spacing is looser than preferred (13.60 mm).`

Category scores:

- connector orientation proof: `20 / 20`
- board outline / mechanical fit: `15 / 15`
- antenna keepout compliance: `15 / 15`
- power path adjacency: `13 / 15`
- USB cluster compactness: `10 / 10`
- test pad accessibility: `10 / 10`
- courtyard / body clearance: `10 / 10`
- routing feasibility: `5 / 5`

## Outcome

Routing workflow documentation now requires a fresh placement readiness scorecard
with exact result `PLACEMENT_READY_FOR_ROUTING` before routing may be treated as
eligible.

This hardening pass separates:

- placement readiness
- live routing/connectivity blockers
- stale-report history

The active `ESP32_CSI_WIFI_NODE` board remains blocked from more routing by live
connectivity state, not by placement readiness.
