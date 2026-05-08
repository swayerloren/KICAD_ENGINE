# REAL_PCB_REPAIR_PASS_1_DRC_REPORT

Date: `2026-05-08`

Board hash after repair: `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC`

DRC command source: `reports/REAL_PCB_REPAIR_PASS_1_DRC.json`

## Summary

| Item | Before | After |
| --- | --- | --- |
| DRC result | `FAIL` | `FAIL` |
| Violations | `12` | `0` |
| Unconnected items | `65` | `65` |
| Schematic parity issues | `0` | `0` |

## Before

- `12 x drill_out_of_range`
- all violations pointed to `U2 pad 41`
- rule mismatch: board minimum through-hole diameter `0.30 mm`, actual thermal-via drill `0.20 mm`

## After

- live DRC violations: `0`
- live unconnected items: `65`
- remaining DRC failure mode: `unconnected_items`

## Repair Effect

The `U2 pad 41` drill-rule blocker is resolved. The board is still not routing-ready because DRC continues to fail on connectivity completeness, not on geometry-rule violations.
