# REAL PCB Critical Trace Audit

Status: `TRACE_AUDIT_COMPLETE_FOR_LIVE_PASS_1`

Generated: `2026-05-08T08:14:38-04:00`

## Net-By-Net Audit

| Net | Live action | Result | Notes |
| --- | --- | --- | --- |
| `+3V3` | Routed on `B.Cu` with new trunk, decoupler branch, pull-up branch, LED branch, and `TP3` connection | `PASS_FOR_THIS_PASS` | Live DRC now shows `0` unconnected items on `+3V3`. |
| `GND` | Added `15` vias to stitch selected GND pads and open copper into the existing zone system | `PARTIAL_IMPROVEMENT` | Live DRC GND unconnected count reduced from `26` to `17`. |
| `/+5V_PROTECTED` | No live branch added in final accepted pass | `DEFERRED` | Only `TP1` remains unconnected. Copied-board branch candidates crossed the new `+3V3` route. |
| `/BOOT0` | No live route added in final accepted pass | `DEFERRED_STOP_CONDITION` | Copied-board rehearsals created real DRC crossings/shorts against `+3V3`. |
| `/ESP_EN` | No live route added in final accepted pass | `DEFERRED_STOP_CONDITION` | Copied-board rehearsals created real DRC crossings/shorts against `+3V3`. |
| USB D+/D- | Not touched | `NOT_IN_SCOPE` | This pass stayed power-focused. |

## `+3V3` Trace-By-Trace Detail

The accepted live `+3V3` work added these functional connections:

1. existing upper power branch into the right-side service/test area
2. `R3` branch tie-in
3. `U2 pad 2` to `C3`
4. `C3` to `C4`
5. `C3` down into the `R1` and `R2` pull-up cluster
6. `R1` to `R2`
7. right-side continuation into `TP3`

Widths used in the accepted live pass:

- `0.45 mm` on the main `TP3` service branch
- `0.35 mm` on the local `U2` and resistor/capacitor branches

## `GND` Via Audit

Accepted GND via intent:

- top-side module side-pads and decouplers
- left reset/boot button GND pads
- selected open-field stitching points that did not create DRC violations

Notable effect:

- GND still is not fully closed around the power-input and USB-side clusters
- the accepted GND work is improvement, not completion

## Rejected Rehearsal Branches

These candidates were tested on copied boards and rejected before live application:

- `/ESP_EN` broad live-routing rehearsal
- `/BOOT0` broad live-routing rehearsal
- `/+5V_PROTECTED` `TP1` spur rehearsal

Reason for rejection:

- they created copied-board DRC crossings, shorts, or ugly geometry on the actual current placement

## Audit Conclusion

The live board now has a completed `+3V3` rail and a better `GND` stitch state with `0` DRC violations.

The board is not ready for broad remaining-net routing. The next routing pass must solve `/BOOT0` and `/ESP_EN` with a copied-board control-net study first.
