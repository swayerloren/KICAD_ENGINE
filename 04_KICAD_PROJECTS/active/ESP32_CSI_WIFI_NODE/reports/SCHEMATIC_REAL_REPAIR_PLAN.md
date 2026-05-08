# Schematic Real Repair Plan

Project: `ESP32_CSI_WIFI_NODE`
Date: `2026-05-06`
Task: repair the schematic for readability, annotation, footprint assignment, and LJ visual review.

## Active Files

- Target schematic: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- Project file: `kicad/ESP32_CSI_WIFI_NODE.kicad_pro`
- PCB file: none in scope; do not create or edit `.kicad_pcb`.

## Backup

Pre-edit backup:

`99_BACKUPS/pre_codex_edits/20260506_162153_ESP32_CSI_WIFI_NODE_schematic_real_repair`

Backed up:

- `ESP32_CSI_WIFI_NODE.kicad_sch`
- `ESP32_CSI_WIFI_NODE.kicad_pro`

Rollback plan: restore the backed-up `.kicad_sch` and `.kicad_pro` files to `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/`.

## Repair Boundaries

- Edit only the schematic source and report/verification files.
- Do not edit or create a PCB.
- Do not update PCB from schematic.
- Do not route, place, create zones, or generate manufacturing outputs.
- Use only footprint candidates listed in `reports/FOOTPRINT_ASSIGNMENT_PLAN.md`.
- Do not mark any footprint as verified exact package drawing.

## Planned Schematic Repairs

1. Keep all reference designators annotated and check that no stored or visible physical references end in `?`.
2. Assign candidate footprints from `reports/FOOTPRINT_ASSIGNMENT_PLAN.md`.
3. For rows with blocked exact part/package evidence, keep the visible value concise and add hidden review/status fields so LJ can see remaining risk in reports without crowding the schematic.
4. Hide footprint/library/path fields from normal schematic view.
5. Shorten long visible values that caused schematic crowding while preserving `NEEDS_REVIEW` or `BLOCKED` where it matters.
6. Hide or move long schematic note fields so normal schematic view is readable.
7. Space value/reference text away from wires, pins, power symbols, and other text using conservative local text offsets.
8. Preserve circuit connectivity and intent unless ERC exposes a clear issue.

## Planned Verification

After edits:

1. Run ERC with `kicad-cli`.
2. Run schematic annotation checker.
3. Run schematic completeness checker.
4. Run BOM lock alignment checker if its interface supports the current lock file.
5. Run NEEDS_REVIEW checker.
6. Export schematic SVG/PDF/PNG if supported by local tools.
7. Generate close-up crops and visual review.
8. Update:
   - `reports/SCHEMATIC_VERIFICATION_REPORT.md`
   - `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
   - `_verification/VISUAL_CHECK_REPORT.md`
   - `_verification/schematic_visual/CLOSE_UP_REVIEW.md`

## Expected Gate Result

Expected final status: `READY_FOR_LJ_VISUAL_REVIEW_WITH_NEEDS_REVIEW_ITEMS`.

PCB update is expected to remain blocked because several high-risk footprint/package decisions are still candidates rather than verified exact package drawings.
