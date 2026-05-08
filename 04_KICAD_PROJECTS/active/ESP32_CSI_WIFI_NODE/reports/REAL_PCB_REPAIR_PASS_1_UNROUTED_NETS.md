# REAL_PCB_REPAIR_PASS_1_UNROUTED_NETS

Date: `2026-05-08`

Board hash after repair: `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC`

Source: `reports/LIVE_PROJECT_STATE.json`

## Summary

- Detectable unrouted nets before repair: `16`
- Detectable unrouted nets after repair: `15`
- Net removed by the new GND zone strategy: `GND`

## Remaining Unrouted Nets

1. `/BOOT0`
2. `/CC1`
3. `/CC2`
4. `/DM_C`
5. `/DM_E`
6. `/DP_C`
7. `/DP_E`
8. `/ESP_EN`
9. `/PLED`
10. `/SHIELD`
11. `/SLED`
12. `/STATUS_LED`
13. `/U0RXD`
14. `/U0TXD`
15. `unconnected-(J2-VBUS-PadA4)`

## Notes

- `GND` is no longer counted as unrouted because the board now contains actual `GND` pours on `F.Cu` and `B.Cu`.
- This list is still a live routing blocker for phase 8 continuation.
