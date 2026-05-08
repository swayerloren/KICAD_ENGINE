# Emergency Annotation Repair Plan

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-06  
Target schematic: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

## Scope

Repair only actual placed-symbol `Reference` properties in the KiCad schematic source so KiCad GUI/ERC cannot see unannotated or duplicate references.

No visual layout cleanup, footprint assignment, value changes, PCB update, routing, or manufacturing outputs are in scope.

## Backup And Hashes

Backup folder:

`99_BACKUPS/pre_codex_edits/20260506_180514_ESP32_CSI_WIFI_NODE_emergency_annotation_repair`

Original schematic SHA256 before edit:

`344B550EBFB36DE43B9E7AA5D395C7463F7E1E5CDA19A3BD9DA8ED134FF4D6EB`

Backup schematic SHA256:

`344B550EBFB36DE43B9E7AA5D395C7463F7E1E5CDA19A3BD9DA8ED134FF4D6EB`

## Pre-Edit Evidence

Direct placed-symbol parse of the target schematic found:

- placed symbols: 79
- physical symbols: 43
- power symbols: 33
- PWR_FLAG symbols: 3
- placed references containing `?`: 0
- duplicate placed references: 0

Fresh KiCad CLI ERC before edit:

- command input: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- result: 0 errors, 0 warnings
- report: `reports/ERC_BEFORE_EMERGENCY_ANNOTATION_REPAIR.rpt`

This conflicts with the KiCad GUI/user-observed unannotated-reference state. The repair will still refresh placed-symbol references to remove ambiguity and normalize power/flag references.

## Repair Method

1. Parse balanced top-level placed `(symbol ...)` blocks from the schematic file.
2. Ignore `lib_symbols` template definitions.
3. Extract each placed symbol's:
   - `Reference`
   - `Value`
   - `lib_id`
   - `uuid`
4. Preserve already valid physical references unless an unresolved `?` or duplicate is found.
5. Assign deterministic unique references to any unresolved/duplicate physical references by prefix.
6. Normalize all power-symbol references to unique `#PWR0101`, `#PWR0102`, ... style references.
7. Normalize all `PWR_FLAG` references to unique `#FLG0101`, `#FLG0102`, ... style references.
8. Write only changed `Reference` property values.

## Validation Plan

After edit:

1. Run a direct file scan for unresolved reference patterns:
   - physical `J?`, `R?`, `C?`, `D?`, `SW?`, `Q?`, `U?`, `TP?`, `MH?`, `L?`, `Y?`, `F?`
   - `#PWR?`
   - `#FLG?`
2. Export a placed-symbol reference table:
   - `Ref | Symbol/Lib ID | Value | UUID`
3. Run duplicate checks for physical, `#PWR`, and `#FLG` references.
4. Run KiCad CLI ERC.
5. Export fresh schematic SVG/PDF/PNG.
6. Generate a small visible-question-reference crop report.
7. Update `SCHEMATIC_TO_PCB_GATE_STATUS.md` as still blocked for visual/footprint/high-risk decisions unless every gate passes.

## Success Criteria

Do not claim success unless:

- direct file scan finds no unresolved `?` reference patterns
- placed-symbol table has no unresolved references
- duplicate reference check passes
- KiCad ERC no longer reports "Schematic is not fully annotated"
- no visible `?` references are found in generated visual evidence

## Rollback Plan

Restore:

`99_BACKUPS/pre_codex_edits/20260506_180514_ESP32_CSI_WIFI_NODE_emergency_annotation_repair/ESP32_CSI_WIFI_NODE.kicad_sch`

to:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
