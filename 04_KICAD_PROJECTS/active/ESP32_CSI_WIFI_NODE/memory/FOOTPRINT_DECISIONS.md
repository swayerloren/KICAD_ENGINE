# Footprint Decisions

Status: `UNVERIFIED_PROJECT_MEMORY`

Record project-specific footprint decisions and review status.

## Rules

- Every footprint must map to an exact manufacturer package or connector drawing.
- Connector orientation requires human review unless exact drawing, pin numbering, board edge relation, and 3D/mechanical evidence are verified.
- Generic connector footprints remain `UNVERIFIED_FOOTPRINT`.

## Current Records

No new footprint decisions were added by this learning-system setup.

## 2026-05-03 Footprint Package Audit

Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

Audit artifact: `reports/FOOTPRINT_PACKAGE_AUDIT.md`

Durable project memory:

- No project footprint assignments are currently accepted as verified.
- Read-only schematic parsing found `43` physical schematic symbols, `0` assigned footprints, and `0` populated schematic datasheet fields.
- The PCB update gate must remain blocked until every physical component has a source-backed footprint assignment.
- `J2` USB-C connector, `J1` barrel jack, `Q1` AO3401A-class PMOS, `U2` ESP32-S3 module, `U3` USB ESD, `U1` AP63203 regulator, switches, test pads, and mounting holes require exact package/mechanical evidence before layout.
- Connector orientation and pin numbering must be human-reviewed after exact manufacturer MPNs and drawings are selected.

No footprint decision was approved by this audit.

## 2026-05-06 Schematic Real Repair Footprint Assignment

Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

Evidence:

- `reports/FOOTPRINT_ASSIGNMENT_PLAN.md`
- `reports/SCHEMATIC_VERIFICATION_REPORT.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`

Durable project memory:

- All 43 physical schematic symbols now have populated candidate footprint fields in the schematic.
- These assignments are for LJ visual/package review only.
- No footprint is verified against an exact manufacturer package drawing.
- High-risk items remain blocked for PCB update: `J1`, `J2`, `Q1`, `U1`, `U2`, `U3`, `L1`, `D1`, `D2`, `D3`, `SW1`, `SW2`, and mounting holes.
- Do not treat the footprint-assigned schematic as PCB-ready until `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is explicitly `PASS`.
