# PCB ESP Routing And Via Repair Report

Date: `2026-05-09`

Project: `ESP32_CSI_WIFI_NODE`

Active PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Scope

User-requested scope was `U2`, `TP1-TP9`, `D1`, `D2`, `R3`, `R4`, `SW1`, `SW2`, `C7`, and `C8`.

The copied-board trials showed that a full live reroute of `BOOT0`, `ESP_EN`, `DP_E`, and `TP1` introduced new routing-rule errors against the current live `+3V3`, `STATUS_LED`, `U0RXD`, and `U0TXD` geometry. The accepted live delta was narrowed to the subset that was copied-board-proven to improve connectivity without adding new DRC rule violations.

`PCB_BAD_ROUTE_REMOVAL_REPORT.md` was requested as input but was not present in the repo at the time of this task.

## Backup

- Project backup: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups/ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb`
- Repo backup: `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb`
- Pre-edit live PCB SHA1: `a6876ff219831d5261d5acbbea7fa95d05c10f85`
- Post-edit live PCB SHA1: `7b8cd99113ba86a921178c161cabfa7f01fa1999`

## Applied Live Changes

### U2 / USB data side

- Routed `/DM_E` from `U2 pad 13` to `R8 pad 2` and `TP9`.
- New `/DM_E` geometry:
  - `F.Cu`: `(21.25, 37.98) -> (18.0, 37.98)`
  - `B.Cu`: `(18.0, 37.98) -> (18.0, 41.0) -> (11.0, 41.0) -> (11.0, 74.0) -> (34.825, 74.0)`
  - `F.Cu`: `(34.825, 74.0) -> (33.825, 75.0)`
  - `B.Cu`: `(34.825, 74.0) -> (55.0, 74.0) -> (55.0, 72.0)`
  - `F.Cu`: `(55.0, 72.0) -> (57.0, 72.0)`
- Added `/DM_E` vias at `(18.0, 37.98)`, `(34.825, 74.0)`, and `(55.0, 72.0)`.

### Button local cleanup

- Added the missing local `SW1` same-net bridge on `/BOOT0`:
  - `F.Cu`: `(5.15, 66.625) -> (5.15, 61.375)`
- Added the missing local `SW2` same-net bridge on `/ESP_EN`:
  - `F.Cu`: `(5.15, 56.625) -> (5.15, 51.375)`

### Ground stitching

- Added `GND` via at `(31.5, 44.775)` with `0.65 mm` diameter and `0.30 mm` drill.
- Added `GND` via at `(36.5, 44.775)` with `0.65 mm` diameter and `0.30 mm` drill.
- Both vias are below the ESP antenna keepout band and were accepted by live DRC.

### Zones

- Existing zones were refilled after the accepted live delta.

## Not Changed In The Accepted Live Pass

- `/DP_E` remained unchanged because combined `DM_E + DP_E` repair candidates introduced new DRC rule errors.
- `TP1` remained open because every copied-board branch candidate created conflicts against the current buck / `+3V3` / UART geometry.
- `U2 -> /ESP_EN` and `U2 -> /BOOT0` long control trunks remained unchanged because copied-board candidates introduced new DRC conflicts against the current routed corridors.
- `TP2` and `TP4` remained open for the same reason.
- `U0RXD`, `U0TXD`, and the existing `STATUS_LED` route were left in place during the accepted pass.
- No components were moved.
- No footprints were changed.
- No schematic files were edited.

## Validation

### Live DRC

Command:

`kicad-cli pcb drc --format json --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_ESP_ROUTING_AND_VIA_REPAIR_DRC.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Result:

- Violations: `0`
- Unconnected items: `13`

### Remaining Unconnected Nets

- `/+5V_PROTECTED`
- `/BOOT0`
- `/DM_C`
- `/DP_C`
- `/DP_E`
- `/ESP_EN`

Detailed remaining opens:

- `TP1` to `/+5V_PROTECTED`
- `U2 pad 27` to `/BOOT0` local network
- `TP4` to `/BOOT0`
- `/DM_C` chain between `J2`, `U3`, and `R8`
- `/DP_C` chain between `J2`, `U3`, and `R9`
- `U2 pad 14` to `R9 / TP8` on `/DP_E`
- `U2 pad 3` to local `/ESP_EN` network
- `TP2` to `/ESP_EN`

### Board-edge / keepout / schematic checks

- Board-edge clearance issues detected by live DRC: `NO`
- ESP antenna keepout respected: `YES`
- `.kicad_sch` changed: `NO`

## Outcome

This pass accepted only the copied-board-proven subset that improved the board without adding new DRC rule errors. The live board now has `0` DRC violations and `13` remaining unconnected items, down from the prior live baseline of `17` unconnected items.
