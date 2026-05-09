# PCB ESP Routing And Via Repair Session

Date: `2026-05-09`

Project: `ESP32_CSI_WIFI_NODE`

Task type: `ROUTING_EDIT_REQUIRED`

## Summary

Started from the pre-task backup because the live board still contained a failed exploratory routing pass. Multiple copied-board trials were run against `U2 / TP / ESP` routing candidates. Most broad reroute variants introduced new DRC rule errors against the current `+3V3`, `STATUS_LED`, `U0RXD`, and `U0TXD` geometry.

Accepted the narrower copied-board-proven subset only:

- `/DM_E` repaired from `U2` to `R8` to `TP9`
- local `SW1` `/BOOT0` bridge added
- local `SW2` `/ESP_EN` bridge added
- two `GND` stitching vias added under the lower half of `U2`

## Result

- Live board restored from backup before applying the accepted subset
- Live DRC: `0` violations, `13` unconnected items
- Schematic edits: `NO`
- Component movement: `NO`
- Footprint changes: `NO`

## Remaining blocked items

- `TP1` on `/+5V_PROTECTED`
- `U2/TP4` on `/BOOT0`
- `J2/U3/R8` on `/DM_C`
- `J2/U3/R9` on `/DP_C`
- `U2/R9/TP8` on `/DP_E`
- `U2/TP2` on `/ESP_EN`

## Evidence

- Backup: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups/ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb`
- Backup: `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb`
- Live DRC JSON: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_ESP_ROUTING_AND_VIA_REPAIR_DRC.json`
- Repair report: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_ESP_ROUTING_AND_VIA_REPAIR_REPORT.md`
