# PCB Sync Blocked - Q1 Pin Mapping

Date: `2026-05-07`

Status: `OPEN`

## Issue

Phase 2 PCB creation imported all 43 schematic footprints, but schematic parity is not clean because Q1 uses schematic pins `D`, `G`, and `S` while the selected SOT-23 footprint uses numbered pads `1`, `2`, and `3`.

## Impact

Q1 is the AO3401A reverse-polarity PMOS. Incorrect source/drain/gate mapping can break or damage the input power path.

## Required Resolution

LJ must approve a source-backed mapping or the schematic/footprint must be corrected so KiCad can map the pins without guessing.

## Blocked Phases

- Placement planning.
- Mechanical setup.
- Component placement.
- Routing.
- Zones.
- JLCPCB/production/export/signoff phases.

