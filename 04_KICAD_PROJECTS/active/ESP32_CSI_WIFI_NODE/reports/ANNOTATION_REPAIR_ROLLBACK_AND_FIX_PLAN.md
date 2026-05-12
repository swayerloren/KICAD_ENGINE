# Annotation Repair Rollback And Fix Plan

Project: `ESP32_CSI_WIFI_NODE`

Generated: `2026-05-06 18:31:27 -04:00`

Target schematic: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Backup path:

`99_BACKUPS/pre_codex_edits/20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair`

## Stop Condition From LJ

The visual cleanup pass is stopped. No visual layout cleanup, symbol movement, footprint assignment, PCB update, routing, or manufacturing output is allowed in this task.

## Historical Status Warning

This plan is preserved as historical evidence only.

It documents a saved-file structured-text recovery path that is no longer
accepted as authoritative annotation proof under the current repo rules.

## Current Evidence Before This Repair

Two local KiCad CLI ERC checks on the saved target schematic reported 0 violations:

- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_PRECHECK.rpt`
- `reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_PRECHECK_FROM_PROJECT_DIR.rpt`

However, LJ reports that KiCad ERC in the GUI still shows duplicate/unannotated references and `Schematic is not fully annotated`. This repair treats KiCad annotation metadata as suspect and will rebuild both placed-symbol `Reference` properties and KiCad-style per-symbol `instances` reference entries.

## Primary Method Decision

KiCad 9.0.7 `kicad-cli sch` exposes `erc` and `export`; it does not expose a command-line annotation subcommand in this environment.

Method used:

`STRUCTURED_S_EXPRESSION_REPAIR_HISTORICAL_ONLY`

The repair will:

1. Parse top-level placed schematic symbols as balanced S-expressions.
2. Update actual placed-symbol `Reference` properties to the required unique references.
3. Add or update each placed symbol's KiCad-style `instances` block:

   ```text
   (instances
     (project "ESP32_CSI_WIFI_NODE"
       (path "/<symbol_uuid>"
         (reference "<REF>")
         (unit 1)
       )
     )
   )
   ```

4. Keep power and PWR_FLAG references unique and hidden.
5. Leave values, footprints, wires, positions, PCB files, and circuit intent unchanged.

## Required Reference Map

- `J1`: barrel jack
- `J2`: USB-C connector
- `F1`: fuse/PTC
- `Q1`: PMOS
- `D1`: TVS diode
- `D2`: power LED
- `D3`: status LED
- `U1`: buck regulator
- `U2`: ESP32 module
- `U3`: USB ESD
- `L1`: inductor
- `SW1`: reset switch
- `SW2`: boot switch
- `C1` through `C8`: capacitors
- `R1` through `R9`: resistors
- `TP1` through `TP9`: test pads
- `MH1` through `MH4`: mounting holes
- `#PWR0101` and up: power symbols
- `#FLG0101` and up: PWR_FLAG symbols

## Verification Plan

After the annotation repair:

1. Run `kicad-cli sch erc` on the saved target schematic.
2. Confirm ERC has 0 annotation errors.
3. Confirm ERC does not say `Schematic is not fully annotated`.
4. Scan the saved file for unresolved references ending in `?`.
5. Export `ANNOTATION_REFERENCE_TABLE_FINAL.md`.
6. Check duplicate physical references.
7. Check duplicate `#PWR` references.
8. Check duplicate `#FLG` references.
9. Export fresh schematic SVG/PDF/PNG.
10. Keep `SCHEMATIC_TO_PCB_GATE_STATUS.md` blocked.

Rollback plan: restore `ESP32_CSI_WIFI_NODE.kicad_sch` from the backup folder above.
