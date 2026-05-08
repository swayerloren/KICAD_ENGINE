# Routing Stage 1/2 Professional DRC Report

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Final classification: `STAGE_1_2_PROFESSIONAL_ROUTING_READY_FOR_USB`

## Baseline

Pre-edit DRC evidence:

- `reports/ROUTING_STAGE_1_2_PROFESSIONAL_BASELINE_DRC.rpt`

Baseline result:

- Violations: `13`
- Unconnected items: `65`
- Schematic parity issues: `0`

Baseline blocker detail:

- `1 x tracks_crossing` in the buck `SW/BST` area
- `12 x drill_out_of_range` on `U2 pad 41`

## Post-Edit

Authoritative post-edit DRC evidence:

- `reports/ROUTING_STAGE_1_2_PROFESSIONAL_DRC_LIVE.rpt`

Post-edit result:

- Violations: `12`
- Unconnected items: `65`
- Schematic parity issues: `0`

## Delta

Resolved in this pass:

- `1 x tracks_crossing` in the buck cluster
- all Stage 1/2 local routing shorts/clearance issues created during intermediate trials

Still present after this pass:

- `12 x drill_out_of_range` on `U2 pad 41`

Not changed by scope:

- `65` unconnected items outside the completed Stage 1/2 local routing scope

## Interpretation

- Stage 1 / Stage 2 local routing is now DRC-clean.
- The remaining DRC errors are unrelated legacy drill-rule violations on `U2 pad 41`.
- Schematic parity remains `PASS`.
- USB routing may begin next.
- Copper pour is still `NO`.
