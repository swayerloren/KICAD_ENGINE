# COMMAND LINK Direct Edit Review

Date: 2026-04-30

Approved workspace:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK`

LJ explicitly approved direct Codex repair/review/re-export work in this finished PCB folder for this task. Original files were not deleted, and original Fiverr/fabrication outputs were preserved in place.

## Snapshot And Archive

- Full snapshot: `C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\project_snapshots\COMMAND_LINK_DIRECT_EDIT_APPROVED_20260430_203134`
- Working folder: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134`
- Original output archive: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\original_fiverr_outputs_snapshot`
- Archived items: original BOM CSV, PDF, STL, fabrication folder, fabrication zip, pick-and-place folder, pick-and-place zip.

## Source Files Located

- `COMMAND LINK DRAFT.kicad_pro`
- `COMMAND LINK DRAFT.kicad_sch`
- `COMMAND LINK DRAFT.kicad_pcb`
- `COMMAND LINK BOM.csv`
- `Fabrication files`
- `pick and place file`
- `COMMAND LINK DRAFT.pdf`
- `COMMAND LINK DRAFT.stl`

## Source Issues Fixed

1. Missing U2 footprint library reference

   The schematic and PCB referenced `ULN2803ADW:IC_ULN2803ADW`, but there was no project-local footprint table or library. The actual U2 footprint was embedded in the PCB, so this was a resolvable library-reference issue rather than missing board geometry.

   Fix:
   - Added `ULN2803ADW.pretty\IC_ULN2803ADW.kicad_mod`, exported from the embedded U2 footprint.
   - Added `fp-lib-table` pointing `ULN2803ADW` to `${KIPRJMOD}/ULN2803ADW.pretty`.

2. `CAN_P` ERC label warning

   The `CAN_P` label overlapped the horizontal wire enough for ERC to report `label_multiple_wires`. The net intent was clear from the adjacent wire/junction geometry.

   Fix:
   - Moved the label anchor to `(313.69, 91.44)`.
   - Changed label justification to `right bottom` so text is away from the connected wires.

3. Co-located GND via warning

   The PCB contained two GND vias at exactly `(82.675, 68.525)` with identical size, drill, layers, and net. Only the UUID differed.

   Fix:
   - Removed one duplicate via.
   - Kept the matching GND via in place.

## Issues Not Auto-Fixed

- Courtyard overlap between C3 and C9: requires human assembly/layout review; moving footprints or changing courtyards would alter layout intent.
- Starved thermal warnings at R2 pad 2, U3 pad 2, and U4 pad 2: requires human layout review; changing zone settings or pad thermal behavior could alter current/thermal behavior.
- 40 footprint-library mismatch warnings: these are standard-library comparison warnings against the installed KiCad 9 libraries. The board geometry is embedded and previously fabricated; updating footprints from library could change verified layout geometry, so these were not auto-corrected.

## NOT_FINAL Export Package

New package:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL`

Generated:

- Gerbers
- Excellon PTH/NPTH drill files plus drill maps
- KiCad CLI BOM CSV
- KiCad CLI position CSV
- Schematic PDF
- PCB layer PDF
- STEP

The export wrapper initially failed because the PowerShell helper parameter name collided with PowerShell argument handling and invoked `kicad-cli` without arguments. That failed log was preserved as `export_commands.log`. The successful rerun is logged in `export_commands_rerun.log`.

## Old Vs New Output Comparison

- BOM: old grouped semicolon CSV and new KiCad CLI comma CSV use different formats, but both expand to 46 references and quantity sum 46. No reference designators were added or removed.
- Pick-and-place: old top-side CSV and new position CSV are byte-identical; both contain 43 top-side placements and 0 bottom-side placements.
- Gerbers: old and new non-drill Gerber layer names match. Sizes differ slightly on copper layers after duplicate via cleanup; all matching Gerber hashes differ because files were regenerated.
- Drill: old package used `COMMAND LINK DRAFT-PTH-drl.gbr` and `COMMAND LINK DRAFT-NPTH-drl.gbr`; new package adds standalone Excellon `COMMAND LINK DRAFT-PTH.drl` and `COMMAND LINK DRAFT-NPTH.drl`.
- PDF/STL/STEP: original PDF and STL remain preserved. New schematic PDF, PCB layer PDF, and STEP were generated under `NOT_FINAL`. STEP export reported missing 3D models for J2, J3, J4, and L1.

## Readiness

- Ready for human review: yes.
- Ready for fabrication: no.

Fabrication readiness is blocked by remaining DRC violations, footprint mismatch review, mechanical/assembly review, and the normal fabrication gate.
