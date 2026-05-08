# ESP32_CSI_WIFI_NODE Schematic Repair Plan

Generated: 2026-05-06
Source audit: `reports/SCHEMATIC_AUDIT_ONLY_REPORT.md`
Mode: plan only, no schematic edits made

## Repair Status

Current status: `BLOCKED_BEFORE_PCB_UPDATE`

The schematic can be repaired incrementally, but footprint assignment and policy decisions require source-backed or human-reviewed inputs. PCB update remains blocked.

## Priority 0: Gate Blockers

1. Restore or create the missing project BOM/control files:
   - `PRE_SCHEMATIC_BOM_LOCK.md`
   - `SCHEMATIC_READY_PARTS_LIST.md`
   - `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`
   Required content: exact value/MPN/source/verification status for each physical part, or explicit `NEEDS_REVIEW`.

2. Resolve or formally block all symbol `NEEDS_REVIEW` values:
   - `J1` barrel jack MPN, center-positive pinout, mechanical drawing, and footprint.
   - `F1` PTC hold/trip current, voltage, package, derating, and footprint.
   - `Q1` AO3401A-class PMOS exact MPN, pin mapping, package, footprint, and orientation.
   - `D1` TVS MPN, working voltage/clamp direction, package, and footprint.
   - `C1` bulk capacitor exact MPN, voltage rating, capacitance, size, and footprint.
   - `L1` inductor MPN, saturation current, DCR, package, and footprint.
   - `J2` USB-C receptacle exact MPN, shell/CC/pin numbering, mechanical drawing, and footprint.
   - `R3` USB shield policy: direct, RC, 0R/DNI, chassis strategy, or blocked.
   - `U3` USB ESD exact MPN, package, pin mapping, and footprint.
   - `R6/R7` USB series resistor value, package, and placement policy.
   - `MH1-MH4` drill, plated status, keepout, mounting hardware, and board outline relationship.

3. Resolve policy blockers:
   - USB VBUS/backfeed policy.
   - USB shield/EMC policy.
   - ESP32-S3-WROOM-1U symbol and footprint equivalence.
   - Status LED GPIO selection.
   - Antenna/pigtail/SMA/enclosure mechanical policy.
   - Optional USB D+/D- test stub policy.

4. Assign footprints only after exact package drawings are verified:
   - Do not assign generic connector, PMOS, ESD, regulator, module, barrel jack, or mounting-hole footprints by package name alone.
   - Mark every unverified footprint as `NEEDS_REVIEW` until exact package drawing evidence exists.

## Priority 1: Schematic Field Cleanup

These are safe only after backup and explicit edit approval:

1. Add a `Verification_Status` property to high-risk symbols, especially `U1`.
2. Add `Datasheet` or source-link fields for physical parts where source links exist.
3. Hide `Footprint`, `Datasheet`, and library/path fields from normal schematic view where they clutter the drawing.
4. Keep unresolved status visible in values or notes until resolved; do not hide blockers.
5. Re-run annotation, BOM alignment, needs-review marker, and ERC checks.

## Priority 2: Visual Repair

1. Adjust `_verification/schematic_visual/visual_blocks.json` for blocks whose crops produced no visible text:
   - `cc_resistors`
   - `reset_boot`
   - `leds`
   - `test_pads`
2. Regenerate close-up crops.
3. Inspect each crop and record `PASS`, `FAIL`, or `NEEDS_REVIEW`.
4. Move overlapping or unreadable reference/value/net labels only after schematic backup.

## Priority 3: Re-Audit And Gate

After repairs:

1. Run `check_schematic_annotation.py`.
2. Run `check_schematic_completeness.py`.
3. Run `check_bom_lock_alignment.py` using the restored BOM lock path.
4. Run `check_needs_review_markers.py`.
5. Run ERC.
6. Export full-page schematic SVG/PDF.
7. Generate close-up crops and complete visual review.
8. Update `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

## Automatic Repair Decision

Schematic is safe for limited automatic cleanup only after backup:

- Field visibility cleanup.
- Adding explicit status fields that preserve current unresolved status.
- Visual-block config tuning.
- Report/status updates.

Schematic is not safe for automatic footprint/MPN/policy completion. Those require datasheet/package drawing evidence or human review.
