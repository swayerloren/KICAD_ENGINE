# Claim Evidence Matrix: ESP32_CSI_WIFI_NODE Schematic Audit Only

Date: 2026-05-06

| Claim | Status | Evidence |
| --- | --- | --- |
| The target schematic exists. | `VERIFIED_BY_FILE` | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch` was located and parsed. |
| The project file exists. | `VERIFIED_BY_FILE` | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro` was located. |
| ERC passes with 0 errors and 0 warnings. | `VERIFIED_BY_COMMAND` | `reports/SCHEMATIC_AUDIT_ONLY_ERC.rpt`; `kicad-cli` output reported 0 violations. |
| Actual symbol instances have no duplicate references. | `VERIFIED_BY_COMMAND` | Shared schematic parser reported no duplicate actual references. |
| Actual symbol instances have no placeholder references ending in `?`. | `VERIFIED_BY_COMMAND` | Shared schematic parser reported an empty placeholder-reference list. |
| All 43 physical symbols have blank footprint fields. | `VERIFIED_BY_COMMAND` | `reports/SCHEMATIC_AUDIT_ONLY_ANNOTATION_CHECK.md/json`; parser summary found 43 blank physical footprints. |
| Physical symbols are missing datasheet fields. | `VERIFIED_BY_COMMAND` | Annotation report found 43 `MISSING_DATASHEET_FIELD` warnings. |
| BOM alignment fails because BOM lock was not provided. | `VERIFIED_BY_COMMAND` | `reports/SCHEMATIC_AUDIT_ONLY_BOM_LOCK_ALIGNMENT_CHECK.md/json`. |
| Close-up visual review fails. | `VERIFIED_BY_COMMAND` | `reports/SCHEMATIC_AUDIT_ONLY_CLOSE_UP_REVIEW.md`. |
| PCB update is blocked. | `VERIFIED_BY_FILE` | Project gate rules plus audit findings: missing footprints, unresolved `NEEDS_REVIEW`, incomplete visual review, missing BOM lock. |
| Text overlap findings require human review. | `PARTIALLY_VERIFIED` | SVG text heuristic found near-coordinate collisions, but visual judgment is not fully automated. |
