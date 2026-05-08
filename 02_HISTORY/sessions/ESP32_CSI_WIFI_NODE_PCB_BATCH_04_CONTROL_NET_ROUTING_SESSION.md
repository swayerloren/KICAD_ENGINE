# ESP32_CSI_WIFI_NODE PCB Batch 04 Control Net Routing Session

Date: `2026-05-08`

Status: `COMPLETED`

## Scope

- Run `PCB_BATCH_04_CONTROL_NET_ROUTING` on the live board.
- Rehearse `/BOOT0`, `/ESP_EN`, and `/U0RXD` on copied boards first.
- Apply only the control-net subset that preserved `0` DRC violations.

## Outcome

- Live PCB hash before: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- Live PCB hash after: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- PCB changed: `YES`
- Nets routed live:
  - `/U0RXD`
- Vias added: `0`
- DRC after: `0` violations, `20` unconnected items
- Detectable unrouted nets after: `6`

## Key Notes

- The copied-board search found a clean front-side `/U0RXD` corridor that clears the existing `/U0TXD` and LED routes.
- The focused `/BOOT0` and `/ESP_EN` searches did not produce a `0`-violation candidate on the current geometry.
- USB data nets remain deferred because the control-net set is still incomplete.
