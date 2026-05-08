# Datasheet To Footprint Workflow

Use this workflow when creating, selecting, or verifying a KiCad footprint from a package drawing, land pattern, or connector mechanical drawing.

Required companion standards:

- `11_LIBRARY_FACTORY/README.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_CREATION_STANDARD.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_PAD_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_COURTYARD_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_SILKSCREEN_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_FAB_LAYER_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_ORIGIN_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_3D_MODEL_RULES.md`
- `11_LIBRARY_FACTORY/footprints/CONNECTOR_FOOTPRINT_RULES.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md`
- `11_LIBRARY_FACTORY/mapping/SYMBOL_TO_FOOTPRINT_MAPPING_STANDARD.md`
- `11_LIBRARY_FACTORY/mapping/PROJECT_LOCAL_LIBRARY_RULES.md`

## Hard Rules

- Do not approve a footprint from package name, pin count, or pitch alone.
- Connector footprints require the exact manufacturer drawing.
- Pin 1 orientation must be explicitly documented.
- Do not modify installed KiCad footprint libraries.
- Prefer project-local `.pretty` libraries for generated/custom footprints.
- Keep status `UNVERIFIED_FOOTPRINT` until exact package or connector drawing evidence is checked.

## Steps

1. Identify exact part number and package code.
2. Collect package drawing and land pattern.
3. For connectors, collect exact manufacturer mechanical drawing, mating connector/cable information, and orientation evidence.
4. Choose a stock footprint candidate or create a project-local footprint.
5. Compare pad count, pad numbering, pitch, pad dimensions, drill sizes, slots, exposed pads, body outline, courtyard, fab outline, silkscreen, origin, and pin 1.
6. Add or verify a 3D model if useful, but keep 3D status separate from footprint verification.
7. Compare symbol pin numbers to footprint pad numbers.
8. Record source evidence, package code, drawing page/section, footprint name, and verification status.
9. Run `11_LIBRARY_FACTORY/scripts/validate_footprint_file.py` if a footprint file exists.
10. If metadata exists, run `11_LIBRARY_FACTORY/scripts/compare_footprint_to_metadata.py`.
11. Mark connector, polarity, RF, USB, CAN, high-current, thermal, and PNP rotation risks.

## Required Review Questions

- Does the footprint match the exact package or connector drawing?
- Is pin 1 orientation documented and visible?
- Do pad numbers match symbol pin numbers?
- Are pad sizes, drills, slots, and exposed pads source-backed?
- Does the courtyard cover body, pads, and mechanical features?
- Does the fab layer show body outline and orientation?
- Does silkscreen avoid pads and mark orientation where useful?
- Is the origin intentional for placement and PNP review?
- Does the 3D model match scale, side, rotation, and offset?

## Failure Conditions

Keep status `UNVERIFIED_FOOTPRINT` or `REJECTED_FOOTPRINT` if:

- The exact drawing is missing.
- Connector manufacturer part number is unknown.
- Pin 1 is uncertain.
- Pad numbering does not match the symbol or source.
- Drill or slot data is guessed.
- Courtyard, fab layer, or silkscreen is missing without documented exception.
- The footprint comes from an unknown third-party source.

## Exit Criteria

Footprint status remains `UNVERIFIED_FOOTPRINT` until exact manufacturer drawing evidence is checked.

Script output is supporting evidence only. It does not replace human/source review.
