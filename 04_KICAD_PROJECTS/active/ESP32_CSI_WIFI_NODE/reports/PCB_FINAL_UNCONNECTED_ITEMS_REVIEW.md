# PCB Final Unconnected Items Review

Status: `LIVE_CLASSIFICATION_COMPLETE`

Generated: `2026-05-08T12:34:25-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Post-cleanup DRC baseline: `0` violations, `17` unconnected items

## Classification Table

| # | Net | Item pair summary | Classification | Action |
| --- | --- | --- | --- | --- |
| 1 | `/+5V_PROTECTED` | `TP1` to protected-rail copper near `U1/C2` | `must route` | keep deferred until a clean right-edge or bottom-side branch is proven |
| 2 | `/BOOT0` | `SW1 pad 1` duplicate-to-duplicate | `expected duplicate pad/open shield/mechanical` | do not force bridge without footprint-review need |
| 3 | `/BOOT0` | left `R2/SW1` cluster to `U2 pad 27` | `must route` | copied-board planning still required |
| 4 | `/BOOT0` | `TP4` to `U2 pad 27` | `must route` | copied-board planning still required |
| 5 | `/DM_C` | `U3 pad 2` to `R8 pad 1` | `must route` | local USB cleanup candidate rejected in rehearsal due real shorts |
| 6 | `/DM_C` | `J2 A7/B7` duplicate connector pair | `must route` | this is a real USB-C orientation tie, not an intentional open |
| 7 | `/DM_C` | `J2` to `U3 pad 2` | `must route` | defer until a clean USB route exists |
| 8 | `/DM_E` | `U2 pad 13` to `R8 pad 2` | `must route` | defer until clean MCU-side USB route exists |
| 9 | `/DM_E` | `R8 pad 2` to `TP9` | `must route` | defer until clean right-side branch exists |
| 10 | `/DP_C` | `U3 pad 1` to `J2 A6` | `must route` | defer until a clean USB route exists |
| 11 | `/DP_C` | `J2 A6/B6` duplicate connector pair | `must route` | this is a real USB-C orientation tie, not an intentional open |
| 12 | `/DP_C` | `R9 pad 1` to `U3 pad 1` | `must route` | local USB cleanup candidate rejected in rehearsal due real shorts |
| 13 | `/DP_E` | `U2 pad 14` to `R9 pad 2` | `must route` | defer until clean MCU-side USB route exists |
| 14 | `/DP_E` | `R9 pad 2` to `TP8` | `must route` | defer until clean right-side branch exists |
| 15 | `/ESP_EN` | `SW2 pad 1` duplicate-to-duplicate | `expected duplicate pad/open shield/mechanical` | do not force bridge without footprint-review need |
| 16 | `/ESP_EN` | left `R1/C1/SW2` cluster to `U2 pad 3` | `must route` | copied-board planning still required |
| 17 | `/ESP_EN` | `TP2` to `U2 pad 3` | `must route` | copied-board planning still required |

## Summary

- `must route`: `15`
- `expected duplicate pad/open shield/mechanical`: `2`
- `intentionally unconnected`: `0`
- `needs schematic review`: `0`

## Notes

- No remaining item in this pass required a schematic edit.
- The two switch duplicate opens should not be used as a reason to force extra copper onto the live board.
- The remaining unresolved items are all genuine PCB routing blockers for final connectivity closure.
