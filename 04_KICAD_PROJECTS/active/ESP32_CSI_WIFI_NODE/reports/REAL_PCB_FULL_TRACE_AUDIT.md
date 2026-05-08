# REAL PCB Full Trace Audit

Status: `TRACE_AUDIT_COMPLETE_FOR_ACCEPTED_SUBSET`

Generated: `2026-05-08T09:00:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Accepted Live Nets

### `/PLED`

- Status: `ROUTED_ACCEPTED`
- Geometry: direct local top-side connection between `R3 pad 1` and `D1 pad 2`
- DRC effect: cleared the former `/PLED` unconnected item

### `/SLED`

- Status: `ROUTED_ACCEPTED`
- Geometry: direct local top-side connection between `R4 pad 1` and `D2 pad 2`
- DRC effect: cleared the former `/SLED` unconnected item

### `/STATUS_LED`

- Status: `ROUTED_ACCEPTED`
- Geometry:
  - short top-side escape from `U2 pad 38`
  - via-assisted bottom-side trunk
  - short top-side re-entry into `R4 pad 2`
- DRC effect: cleared the former `/STATUS_LED` unconnected item without disturbing the LED resistor/diode cluster

### `/U0TXD`

- Status: `ROUTED_ACCEPTED`
- Geometry: top-side service run from `U2 pad 37` to `TP6`
- DRC effect: cleared the former `/U0TXD` unconnected item

### `unconnected-(J2-VBUS-PadA4)`

- Status: `ROUTED_ACCEPTED`
- Geometry: via-assisted tie joining the duplicated USB-C VBUS pad pair inside `J2`
- DRC effect: cleared the former internal `J2` VBUS pad-pair unconnected item

## Not Applied Live

### `/U0RXD`

- Status: `DEFERRED_AFTER_REHEARSAL`
- Reason:
  - copied-board candidates still collided with live `+3V3` geometry or nearby service-area clearances
  - no `0`-violation rehearsal geometry was reached during this pass

### `/BOOT0`

- Status: `DEFERRED_AFTER_REHEARSAL`
- Reason:
  - copied-board candidates crossed or shorted into existing service and power corridors

### `/ESP_EN`

- Status: `DEFERRED_AFTER_REHEARSAL`
- Reason:
  - copied-board candidates crossed or shorted into existing pull-up and service routing

### `/+5V_PROTECTED` at `TP1`

- Status: `DEFERRED_AFTER_REHEARSAL`
- Reason:
  - copied-board candidates still conflicted with live power geometry near the regulator area and service corridor

### `/CC1`, `/CC2`, `/SHIELD`

- Status: `DEFERRED_AFTER_REHEARSAL`
- Reason:
  - copied-board direct candidates were not yet clean enough around the USB-C pad field and shield geometry

## Remaining DRC Connectivity Buckets

- `GND`: `17`
- `/ESP_EN`: `5`
- `/BOOT0`: `4`
- `/SHIELD`: `4`
- `/DM_C`: `3`
- `/DP_C`: `3`
- `/DM_E`: `2`
- `/DP_E`: `2`
- `/+5V_PROTECTED`: `1`
- `/CC1`: `1`
- `/CC2`: `1`
- `/U0RXD`: `1`

## Audit Conclusion

The accepted live subset is real, saved, and DRC-clean. The board is improved but still incomplete.

Routing continuation is still blocked until the remaining service/control nets can be rehearsed cleanly on a copied board and then replayed onto the live board without breaking the current `0`-violation state.
