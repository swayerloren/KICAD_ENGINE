# PCB Batch 04 Trace Change Summary

Status: `LIVE_TRACE_DELTA_CAPTURED`

Generated: `2026-05-08T12:06:57-04:00`

## Change Table

| Net | Layer | Segments Added | Vias Added | Before | After | Reason | DRC After |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `/U0RXD` | `F.Cu` | `5` | `0` | `unrouted` | `U2 pad 36 -> TP7` | copied-board rehearsal proved this corridor clears `/U0TXD` and the LED routes while keeping `0` violations | `0` violations, `20` unconnected items |

## Per-Net Detail

### `/U0RXD`

- Timestamp: `2026-05-08T12:06:26-04:00`
- From/to:
  - `U2 pad 36` at `(38.750, 27.820)` to `TP7 pad 1` at `(57.000, 64.000)`
- Layer: `F.Cu`
- Vias used: `0`
- Segment list:
  - `(38.750, 27.820) -> (42.000, 27.820)` width `0.20 mm`
  - `(42.000, 27.820) -> (42.000, 61.000)` width `0.20 mm`
  - `(42.000, 61.000) -> (55.000, 61.000)` width `0.20 mm`
  - `(55.000, 61.000) -> (55.000, 64.000)` width `0.20 mm`
  - `(55.000, 64.000) -> (57.000, 64.000)` width `0.20 mm`
- Reason:
  - this was the first current-board candidate that climbed left of the `/U0TXD` riser, crossed to the right only above `y=60`, and stayed clear of the existing `STATUS_LED` / `SLED` routes

## Deferred Control Nets

- `/BOOT0`
  - deferred because the current front-side search window still forces `U0TXD` crossings or left-cluster shorts/mask bridges
- `/ESP_EN`
  - deferred because the current front-side search window still forces `GND`, `+3V3`, and solder-mask conflicts around `R1`, `C1`, and `SW2`

## Result

- PCB hash before: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- PCB hash after: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- Tracks added live: `5`
- Vias added live: `0`
- DRC result after: `0` violations, `20` unconnected items
