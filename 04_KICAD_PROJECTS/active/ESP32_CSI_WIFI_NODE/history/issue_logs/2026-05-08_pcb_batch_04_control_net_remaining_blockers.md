# Remaining Blockers

Session: `PCB_BATCH_04_CONTROL_NET_ROUTING`

Date: `2026-05-08`

Status: `ACTIVE_BLOCKER`

## Blockers

- `/BOOT0` still has `4` unconnected items and no copied-board `0`-violation route candidate from this pass.
- `/ESP_EN` still has `5` unconnected items and no copied-board `0`-violation route candidate from this pass.
- USB data nets `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` remain deferred until the remaining control nets are clean.
- The board is still `DRC FAIL` by connectivity because `20` unconnected items remain.
