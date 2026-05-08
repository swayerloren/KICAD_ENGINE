# ESP32_CSI_WIFI_NODE PCB Batch 03 USB Control Routing Session

Date: `2026-05-08`

Status: `COMPLETED`

## Scope

- Resume the interrupted `PCB_BATCH_03_USB_CONTROL_ROUTING` pass without restarting unrelated audits.
- Repair the batch-03 routing script if needed.
- Apply only the copied-board-proven `/CC1`, `/CC2`, `/SHIELD` USB-support candidate to the live PCB.

## Outcome

- Live PCB hash before: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- Live PCB hash after: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- PCB changed: `YES`
- Nets routed live:
  - `/CC1`
  - `/CC2`
  - `/SHIELD`
- Vias added: `3`
- DRC after: `0` violations, `21` unconnected items
- Detectable unrouted nets after: `7`

## Key Notes

- The interrupted prior run had already proven the USB-support subset on copied boards; this session resumed from that proof instead of redoing the entire routing search.
- `esp32_csi_usb_control_batch_03.py` required a via-summary safety repair before live use.
- The remaining nets `/BOOT0`, `/ESP_EN`, `/U0RXD`, `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` are still deferred pending clean copied-board rehearsal.
