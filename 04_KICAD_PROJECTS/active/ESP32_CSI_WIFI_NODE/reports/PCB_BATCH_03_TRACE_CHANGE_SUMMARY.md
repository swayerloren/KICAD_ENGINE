# PCB Batch 03 Trace Change Summary

Status: `LIVE_TRACE_DELTA_CAPTURED`

Generated: `2026-05-08T11:26:44-04:00`

## Change Table

| Net | Layer | Segments Added | Vias Added | Before | After | Reason | DRC After |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `/CC1` | `F.Cu` | `2` | `0` | `unrouted` | `J2 A5 -> R6 pad 2` | copied-board proof kept the board at `0` violations | `0` violations, `21` unconnected items |
| `/CC2` | `F.Cu` | `3` | `0` | `unrouted` | `J2 B5 -> R7 pad 2` | shifted path avoids `R7 pad 1 GND` clearance failure from the tighter rehearsal | `0` violations, `21` unconnected items |
| `/SHIELD` | `B.Cu` | `4` | `3` | `unrouted` | `J2 shell pads -> R5 pad 2` | bottom-side shield ring and tie was the only current-board candidate that held clean DRC | `0` violations, `21` unconnected items |

## Per-Net Detail

### `/CC1`

- Timestamp: `2026-05-08T11:25:47-04:00`
- From/to:
  - `J2 A5` at `(37.750, 87.645)` to `R6 pad 2` at `(32.325, 81.500)`
- Layer: `F.Cu`
- Vias used: `0`
- Segment list:
  - `(37.750, 87.645) -> (37.750, 84.800)` width `0.20 mm`
  - `(37.750, 84.800) -> (32.325, 81.500)` width `0.20 mm`
- Reason:
  - shortest clean branch from USB-C CC1 into the pull-down resistor on the current placement without disturbing other routed copper

### `/CC2`

- Timestamp: `2026-05-08T11:25:47-04:00`
- From/to:
  - `J2 B5` at `(40.750, 87.645)` to `R7 pad 2` at `(46.825, 81.500)`
- Layer: `F.Cu`
- Vias used: `0`
- Segment list:
  - `(40.750, 87.645) -> (40.750, 84.000)` width `0.20 mm`
  - `(40.750, 84.000) -> (46.825, 84.000)` width `0.20 mm`
  - `(46.825, 84.000) -> (46.825, 81.500)` width `0.20 mm`
- Reason:
  - the rehearsal proved the earlier tighter diagonal was too close to `R7 pad 1 GND`; the accepted offset path clears that issue

### `/SHIELD`

- Timestamp: `2026-05-08T11:25:47-04:00`
- From/to:
  - `J2 S1` shell pads at `(34.680, 88.220)`, `(34.680, 92.400)`, `(43.320, 88.220)`, `(43.320, 92.400)` to `R5 pad 2` at `(51.825, 78.000)`
- Layer: `B.Cu`
- Vias used: `3`
- Via list:
  - `(34.680, 88.220)`
  - `(43.320, 88.220)`
  - `(51.825, 78.000)`
- Segment list:
  - `(34.680, 88.220) -> (34.680, 92.400)` width `0.20 mm`
  - `(34.680, 92.400) -> (43.320, 92.400)` width `0.20 mm`
  - `(43.320, 92.400) -> (43.320, 88.220)` width `0.20 mm`
  - `(43.320, 88.220) -> (51.825, 78.000)` width `0.20 mm`
- Reason:
  - this is the proven shield return structure that ties the connector shell to the existing shield network without crossing the current front-side routing field

## Result

- PCB hash before: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- PCB hash after: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- Tracks added live: `9`
- Vias added live: `3`
- DRC result after: `0` violations, `21` unconnected items
