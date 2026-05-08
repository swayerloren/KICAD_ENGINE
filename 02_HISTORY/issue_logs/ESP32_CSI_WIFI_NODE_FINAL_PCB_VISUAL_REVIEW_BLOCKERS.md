# ESP32_CSI_WIFI_NODE Final PCB Visual Review Blockers

Date: `2026-05-08`

Status: `OPEN`

Project: `ESP32_CSI_WIFI_NODE`

## Current Live Blockers

- DRC violations: `0`
- Unconnected items: `17`
- Explicitly unrouted nets:
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`

## Remaining Must-Route Work

- `/+5V_PROTECTED`
  - `TP1` to the protected-rail copper near `U1/C2`
- `/BOOT0`
  - left cluster to `U2 pad 27`
  - `TP4` to `U2 pad 27`
- `/ESP_EN`
  - left cluster to `U2 pad 3`
  - `TP2` to `U2 pad 3`
- USB data path
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`

## Expected Non-Blocker Opens

- `SW1 pad 1` duplicate tactile-switch pad pair
- `SW2 pad 1` duplicate tactile-switch pad pair

## Next Action

Use the final LJ visual packet to approve or reject the current geometry. After that, continue only the remaining copied-board-proven routing repair work.
