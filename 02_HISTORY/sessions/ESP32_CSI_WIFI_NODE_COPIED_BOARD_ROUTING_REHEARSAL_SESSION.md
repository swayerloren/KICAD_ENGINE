# ESP32_CSI_WIFI_NODE Copied Board Routing Rehearsal Session

Status: `UNVERIFIED`
Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

Performed copied-board routing rehearsal only after confirming the copied-board
placement-readiness status was `PLACEMENT_READY_FOR_ROUTING`. The real project
PCB was not edited. Four copied candidates were evaluated and all failed the
enforceable PCB quality gate.

## Outputs

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/20260510_143529/`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/COPIED_BOARD_ROUTING_REHEARSAL_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/COPIED_BOARD_ROUTING_CANDIDATE_COMPARISON.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/COPIED_BOARD_PCB_QUALITY_GATE_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual/COPIED_BOARD_ROUTING_REHEARSAL_REVIEW.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/20260510_143529/candidate_C_targeted_local_repair/reports/TRACE_CHANGE_LOG.md`

## Candidate Result

- Safest untouched control: `candidate_A_baseline`
- Best routed attempt: `candidate_C_targeted_local_repair`
- Final classification: `COPIED_ROUTING_BLOCKED`

## Validation

- Real PCB hash unchanged:
  `ACA326C7B7C96AA67FED119E8DF54BDEBF80148C6B5F34F998780137C2BA1DD1`
- Real schematic hash unchanged in this task:
  `A82DD63FBD226227F777677D6EF5491BC9EAF27411A369C13A24C014F82F24E6`
- Real project file copies existed under the rehearsal root before routing
  attempts were applied.
- `run_real_board_routing_audit.py` and `run_pcb_quality_gate.py` were run on
  each candidate.

## Key Findings

- `candidate_C_targeted_local_repair` cleared the detectable-unrouted-net
  heuristic to `0`, but still ended with `49` DRC violations and `4`
  unconnected items.
- Remaining open nets on the best routed attempt are `/BOOT0` and `/ESP_EN`.
- All routed candidates still fail geometry, power-width, USB, and connector
  proof gates.
- Real-board routing remains blocked.
