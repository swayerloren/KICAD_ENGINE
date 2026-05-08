# ESP32_CSI_WIFI_NODE Real PCB Full Routing Pass Session

Date: `2026-05-08`

## Goal

Route remaining non-critical nets only if the live board could be improved without breaking the `0`-violation critical-pass DRC state.

## What Happened

- Confirmed the critical-pass precondition was satisfied.
- Created backup `99_BACKUPS\pre_codex_edits\20260508_082440_ESP32_CSI_WIFI_NODE_real_pcb_full_routing_pass`.
- Built a scenario-driven routing helper and rehearsed multiple candidate subsets on copied boards.
- Rejected broad non-critical routing attempts that produced crossings, shorts, or clearance failures.
- Applied only the accepted copied-board subset to the live PCB:
  - `/PLED`
  - `/SLED`
  - `/STATUS_LED`
  - `/U0TXD`
  - `unconnected-(J2-VBUS-PadA4)`
- Saved the real PCB, reran DRC, and exported fresh SVG board views.

## Outcome

- PCB hash before: `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`
- PCB hash after: `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6`
- DRC after save: `0` violations, `44` unconnected items
- Result: `PARTIAL_SUCCESS_SAFE_NON_CRITICAL_SUBSET`

## Next Action

Run a copied-board reroute study for `/BOOT0`, `/ESP_EN`, `/U0RXD`, `TP1 /+5V_PROTECTED`, `CC1/CC2`, and `SHIELD`, then only bring the accepted geometry onto the live board.
