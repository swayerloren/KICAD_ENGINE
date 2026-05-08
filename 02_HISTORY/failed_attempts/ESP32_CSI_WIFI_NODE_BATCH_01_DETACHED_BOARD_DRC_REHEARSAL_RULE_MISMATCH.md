# ESP32_CSI_WIFI_NODE Batch 01 Detached Board DRC Rehearsal Rule Mismatch

Date: `2026-05-08`

Status: `RESOLVED`

## What Failed

- Early copied-board rehearsals were run against detached `.kicad_pcb` copies without the matching project `.kicad_pro`.
- `kicad-cli pcb drc` then fell back to a `0.30 mm` minimum drill rule and falsely revived the old `U2 pad 41` and `0.20 mm` via drill violations.

## Resolution

- Repeated the rehearsal with `ESP32_CSI_WIFI_NODE.kicad_pcb` and the matching `ESP32_CSI_WIFI_NODE.kicad_pro` in the same copied project folder.
- The corrected rehearsal showed the true result: `GND zone thermal -> full` improves unconnected items `44 -> 27` with `0` violations.
