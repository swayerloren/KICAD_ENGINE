# Projects Index

## Active Projects

### ESP32_CSI_WIFI_NODE

- Path: [04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE)
- Active project path: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- KiCad files: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/`
- Reports: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/`
- Visual review: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual/`
- Memory: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/`
- History: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/`

Current active-project status:

- PCB exists: `YES`
- Placement exists: `YES`
- Partial routing exists: `YES`
- Board outline: `60.0 mm x 95.0 mm`
- Footprints: `43`
- Tracks: `74`
- Vias: `32`
- Zones: `2`
- DRC: `0` violations, `17` unconnected items
- Detectable unrouted nets: `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`
- Fabrication-ready: `NO`

Latest known blockers:

- USB data nets remain unresolved
- `/+5V_PROTECTED`, `/BOOT0`, and `/ESP_EN` still need review or closure per live reports
- Human visual review is still required before any fabrication-style claim

Primary status files:

- [CURRENT_PROJECT_STATE.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md)
- [CURRENT_BLOCKERS.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md)
- [FINAL_PCB_VISUAL_REVIEW_PACKET.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_PCB_VISUAL_REVIEW_PACKET.md)
- [LJ_FINAL_PCB_REVIEW_CHECKLIST.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LJ_FINAL_PCB_REVIEW_CHECKLIST.md)
- [PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md)

Current next action:

- Continue human-reviewed connectivity closure planning for `/+5V_PROTECTED`, `/BOOT0`, `/ESP_EN`, `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E` only after the current live blockers are rechecked against the latest reports.

## Archived Projects

### CLEAN_KICAD_PASSING_SAMPLE

- Path: `04_KICAD_PROJECTS/archive/CLEAN_KICAD_PASSING_SAMPLE`
- Status: archived reference/sample workspace

### SAMPLE_KICAD_TEST_PROJECT

- Path: `04_KICAD_PROJECTS/archive/SAMPLE_KICAD_TEST_PROJECT`
- Status: archived demo/test project with historical reports and NOT_FINAL artifacts

## Templates

- Path: `04_KICAD_PROJECTS/templates/`
- Purpose: standard project scaffolds, requirements templates, README/AGENTS templates, and KiBot defaults

## Notes

- The active project is the only current production-style engineering target in this repo.
- Archive folders are useful for demos, tests, and historical workflow evidence, not current production claims.
