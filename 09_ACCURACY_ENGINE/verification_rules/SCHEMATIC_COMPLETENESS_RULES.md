# Schematic Completeness Rules

## Purpose

These rules define the minimum schematic completeness checks required before PCB update or layout work. The goal is to prevent agents from treating an annotated schematic as layout-ready when required functional blocks or locked BOM items are still missing.

## Required Checkers

Run the completeness, BOM-lock alignment, and review-marker checkers:

```powershell
python .\03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py --schematic "<project>.kicad_sch" --project-root "<active-project-root>" --bom-lock "<bom-lock-or-ready-parts-file>" --output "<report>.md" --json-output "<report>.json"
python .\03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py --schematic "<project>.kicad_sch" --bom-lock "<bom-lock-or-ready-parts-file>" --output "<report>.md" --json-output "<report>.json"
python .\03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py --schematic "<project>.kicad_sch" --output "<report>.md" --json-output "<report>.json"
```

All generated reports must be linked from `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

## Required Functional Blocks

The completeness checker must verify, at minimum:

- Power input.
- Input protection.
- Regulator or power conversion path.
- MCU, processor, or module.
- USB-C section when project requirements call for USB-C.
- ESD/protection section.
- Boot/reset circuitry.
- Test pads.
- Mounting holes.
- Project notes or mechanical notes.
- All expected BOM-lock items appear in the schematic.

## Blocking Findings

The schematic-to-PCB gate is blocked when:

- Required functional blocks are missing.
- The BOM lock file is missing when the project claims a locked BOM exists.
- Parseable BOM-lock references are missing from the schematic.
- Schematic references are not represented in the BOM lock and are not explicitly excluded.
- `NEEDS_REVIEW`, `BLOCKED`, `UNVERIFIED`, `TODO`, or `TBD` markers remain on high-risk parts.
- Any high-risk symbol lacks a verified, blocked, or needs-review status.

## Limits

These checks are screeners. They do not prove ERC pass, footprint accuracy, pinout accuracy, package drawing match, connector orientation, DRC pass, or manufacturing readiness.

## Gate Rule

If any completeness, BOM alignment, or review-marker checker reports `FAIL`, the project-level `SCHEMATIC_TO_PCB_GATE_STATUS.md` must remain `FAIL` or `BLOCKED`.
