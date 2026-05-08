# Claim Evidence Matrix - ESP32_CSI_WIFI_NODE Schematic Electrical Blockers

| Claim | Status | Evidence | Notes |
|---|---|---|---|
| Backup was created before schematic edits. | VERIFIED_BY_COMMAND | `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_20260503_073335` | Contains `.kicad_pro` and `.kicad_sch`. |
| Active schematic was edited. | VERIFIED_BY_FILE | `kicad/ESP32_CSI_WIFI_NODE.kicad_sch` | Edits were limited to schematic source. |
| PCB was not updated. | VERIFIED_BY_COMMAND | Search found no `.kicad_pcb` in active project. | No PCB update command was run. |
| Manufacturing outputs were not generated. | VERIFIED_BY_COMMAND | Search found no `.gbr`, `.drl`, `.pos`, `.step`, `.stp`, or `.zip` files in active project. | Schematic PDF/SVG visual exports are review artifacts, not manufacturing outputs. |
| ERC passed. | VERIFIED_BY_COMMAND | `reports/ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_ERC.txt` | 0 errors, 0 warnings. |
| Power rail naming was repaired. | VERIFIED_BY_FILE | Schematic source contains `+5V_IN`, `+5V_FUSED`, `+5V_PROTECTED`; old `5V_RAW` absent. | Embedded unused library cache may still include `power:+5V` symbol definition text. |
| C1 was updated to requested review value. | VERIFIED_BY_FILE | Schematic source contains `47uF_>=16V_BULK_NEEDS_REVIEW`; old `47uF_10V` absent. | Text-only value update; exact MPN remains unverified. |
| AO3401A pin mapping was resolved. | CONTRADICTED | Gate/audit mark AO3401A as blocked. | Not resolved; explicitly blocked. |
| USB VBUS policy was resolved. | CONTRADICTED | Gate/audit mark USB VBUS policy as blocked. | Not resolved; explicitly blocked. |
| USB shield strategy was resolved. | CONTRADICTED | Gate/audit mark USB shield as blocked. | Not resolved; explicitly blocked. |
| Schematic-to-PCB gate passed. | CONTRADICTED | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` says `FAIL`. | PCB update remains forbidden. |
