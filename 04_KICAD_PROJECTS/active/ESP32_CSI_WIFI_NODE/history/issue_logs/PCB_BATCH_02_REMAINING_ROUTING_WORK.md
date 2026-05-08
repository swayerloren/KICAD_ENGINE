# PCB Batch 02 Remaining Routing Work

Date: `2026-05-08`

Status: `OPEN`

## Current Open Issues

- `27` unconnected items remain after the batch-02 power routing repair.
- `10` detectable unrouted nets remain:
  - `/BOOT0`
  - `/CC1`
  - `/CC2`
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`
  - `/ESP_EN`
  - `/SHIELD`
  - `/U0RXD`
- The board is cleaner and still at `0` DRC violations, but it is not ready for final review or fabrication claims.

## Recommended Next Action

- Start a targeted USB/control routing pass for `/BOOT0`, `/ESP_EN`, `/U0RXD`, then `/CC1`, `/CC2`, and `/SHIELD`.
