# Claim Evidence Matrix: ESP32_CSI Emergency Annotation Repair

Date: `2026-05-06`

| Claim | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Backup was created before edit. | `VERIFIED_BY_FILE` | `99_BACKUPS/pre_codex_edits/20260506_180514_ESP32_CSI_WIFI_NODE_emergency_annotation_repair` | Includes `.kicad_sch` and `.kicad_pro`. |
| Original and backup schematic hashes matched. | `VERIFIED_BY_COMMAND` | SHA256 `344B550EBFB36DE43B9E7AA5D395C7463F7E1E5CDA19A3BD9DA8ED134FF4D6EB` | Recorded before edit. |
| Physical symbols were already uniquely annotated in saved source. | `VERIFIED_BY_FILE` | Placed-symbol parser output and `reports/ANNOTATION_REFERENCE_TABLE.md` | User-observed GUI state may have been stale or different; not used as proof. |
| Power symbols and PWR_FLAG symbols were normalized to unique references. | `VERIFIED_BY_FILE` | `reports/EMERGENCY_ANNOTATION_REPAIR_CHANGES.json`, `reports/ANNOTATION_REFERENCE_TABLE.md` | `#PWR0101`..`#PWR0133`, `#FLG0101`..`#FLG0103`. |
| No stored unresolved `?` references remain. | `VERIFIED_BY_COMMAND` | Direct schematic scan and parser table | Patterns included physical, `#PWR?`, and `#FLG?`. |
| No duplicate references remain. | `VERIFIED_BY_COMMAND` | `reports/ANNOTATION_REFERENCE_TABLE.md` | Physical, `#PWR`, and `#FLG` checked. |
| KiCad ERC no longer reports not fully annotated. | `VERIFIED_BY_COMMAND` | `reports/ERC_AFTER_ANNOTATION_REPAIR.rpt` | `kicad-cli sch erc` found 0 violations. |
| No visible `?` references remain in generated SVG/crops. | `VERIFIED_BY_COMMAND` | `reports/ANNOTATION_VISIBLE_QUESTION_REFERENCE_SCAN.md` | Generated visual evidence only. |
| Live KiCad GUI no longer shows stale `?` refs. | `UNVERIFIED` | Not directly controlled or inspected | LJ should reload saved schematic if an existing GUI window shows stale state. |
| PCB update remains blocked. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | Visual and high-risk part decisions remain unresolved. |
