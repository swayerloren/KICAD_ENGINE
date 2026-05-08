# Power And Buck Routing Review

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Input Power Cluster Review

Cluster: `J1/F1/Q1/D3/C2/C5`

Result:

- `Q1` was re-oriented so the protected-input pad exits toward the local power network instead of forcing the earlier awkward detour.
- `C2` and `C5` were re-oriented so their power pads face the protected-input trunk.
- `J1 -> F1 -> Q1` now follows a short direct flow without harsh right-angle bends.
- `Q1 -> protected-input -> D3/U1` now reads like a deliberate local power path rather than a stitched autoroute.

Review judgment:

- clean enough for Stage 1 completion
- no local routing defect remains that should block USB routing

## Buck Cluster Review

Cluster: `U1/C6/L1/C7/C8`

Result:

- `C6` was moved into the `U1/L1` gap and rotated so `SW` and `BST` can be entered cleanly.
- the prior `SW/BST` crossing is removed
- `BUCK_SW` is short and direct
- `BUCK_BST` is short and local
- the `+3V3` output route remains compact, with the via pair kept intentionally for cleaner `L1/C7/C8` access

Review judgment:

- buck geometry now looks deliberate rather than script-generated
- no `SW/BST` repair remains open
- this cluster is suitable to leave as-is for the next routing phase

## Remaining Limits

- `TP1` on `/+5V_PROTECTED` remains intentionally deferred
- USB and other low-speed nets remain intentionally unrouted
- copper pours remain intentionally blocked
- unrelated `U2 pad 41` drill-rule violations remain open
