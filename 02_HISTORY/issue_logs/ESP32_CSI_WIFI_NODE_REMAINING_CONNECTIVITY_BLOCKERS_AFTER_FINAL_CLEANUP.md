# ESP32_CSI_WIFI_NODE Remaining Connectivity Blockers After Final Cleanup

Generated: `2026-05-08T12:34:25-04:00`

Status: `OPEN`

## Live State

- PCB hash: `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D`
- DRC: `0` violations
- Unconnected items: `17`

## Open Blockers

- `/+5V_PROTECTED` test-point branch to `TP1` remains unrouted.
- `/BOOT0` still needs the `U2 pad 27` spine and `TP4` branch.
- `/ESP_EN` still needs the `U2 pad 3` spine and `TP2` branch.
- `/DM_C` still needs `U3 -> J2` plus the `A7/B7` Type-C duplicate tie.
- `/DP_C` still needs `R9 -> U3`, `U3 -> J2`, and the `A6/B6` Type-C duplicate tie.
- `/DM_E` still needs `U2 -> R8` and `R8 -> TP9`.
- `/DP_E` still needs `U2 -> R9` and `R9 -> TP8`.

## Rule Constraint

- The copied-board USB-local candidate already proved that local D+/D- cleanup can still introduce real shorts on the present geometry.
- Further cleanup must stay copied-board-first and preserve the current `0`-violation live baseline.
