# Footprint Assignment Workflow

## Purpose

Define the required order for footprint/package proof before PCB update.

## Workflow

1. Extract physical symbols from the saved schematic.
2. Create or update `SCHEMATIC_READY_PARTS_LIST.md`.
3. Create or update `FOOTPRINT_LOCK.csv`.
4. Record per-part package evidence, source link, and risk classification.
5. Run the blank-footprint audit.
6. Run the footprint-lock audit.
7. Run the high-risk footprint audit.
8. Run the combined footprint/package gate.
9. Fix every fail or carry it explicitly as `BLOCKED_UNTIL_HUMAN_REVIEW`.
10. Only after gate `PASS`, allow schematic-to-PCB progression.

## Required Evidence Per Physical Symbol

- reference
- value
- manufacturer part number when known
- package name
- KiCad symbol
- KiCad footprint
- source link or datasheet path
- package drawing checked
- pin mapping checked when applicable
- 3D model status when applicable
- risk classification
- human review status

## Lock File Authority

`FOOTPRINT_LOCK.csv` is the authoritative project-local proof record.

Do not treat a schematic footprint field alone as proof.

## High-Risk Review Order

Review these first:

1. USB-C connectors
2. barrel jacks and other edge connectors
3. MCU and RF modules
4. PMOS / reverse-polarity parts
5. regulators, ESD, inductors, fuses
6. polarized parts, diodes, LEDs, switches
7. test pads and mounting holes

## PCB Transition Gate

The footprint/package engine must pass before:

- schematic-to-PCB update
- PCB creation
- PCB placement
- PCB routing
- fabrication-style output
