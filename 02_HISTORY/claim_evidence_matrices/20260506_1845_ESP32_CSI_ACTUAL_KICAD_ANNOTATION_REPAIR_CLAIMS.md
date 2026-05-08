# Claim/Evidence Matrix: ESP32 CSI Actual KiCad Annotation Repair

Date: `2026-05-06`

| Claim | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Backup was created before editing. | `VERIFIED_BY_FILE` | `99_BACKUPS/pre_codex_edits/20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair` | Backup hash matches pre-repair schematic hash. |
| KiCad-native CLI annotation was not available. | `VERIFIED_BY_COMMAND` | `kicad-cli sch --help` | Local CLI exposes ERC/export, not annotation. |
| Repair method was structured S-expression editing. | `VERIFIED_BY_FILE` | `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_CHANGES.json`, changed `.kicad_sch` | Placed-symbol references and instances were edited. |
| All 79 placed symbols have matching instance references. | `VERIFIED_BY_FILE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.json` | `missing_instances: 0`, `instance_mismatches: 0`. |
| There are no unresolved stored question references for requested prefixes. | `VERIFIED_BY_COMMAND` | direct `rg` scan recorded in command log | No matches for requested unresolved reference patterns. |
| Duplicate physical, `#PWR`, and `#FLG` refs are absent. | `VERIFIED_BY_FILE` | `reports/ANNOTATION_REFERENCE_TABLE_FINAL.json` | Duplicate maps are empty. |
| KiCad ERC no longer reports annotation errors locally. | `VERIFIED_BY_COMMAND` | `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt` | ERC messages: 0 errors, 0 warnings. |
| The live KiCad GUI will show the same state without reload. | `UNVERIFIED` | none | User should close/reopen or reload schematic before GUI verification. |
| Visual cleanup may resume. | `PARTIALLY_VERIFIED` | annotation is now clear in saved-file evidence | Resume only after GUI reload confirms annotation clear; visual cleanup itself remains separate. |
| PCB update is still blocked. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | Gate result remains `FAIL`. |
