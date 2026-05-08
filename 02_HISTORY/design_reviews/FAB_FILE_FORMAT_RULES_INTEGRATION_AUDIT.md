# Fab File Format Rules Integration Audit

Status: `COMPLETE`

Generated: `2026-05-07`

Source: `T_E_M_P\file format.md`

Scope: documentation, schema, template, validator, prompt-pack, memory, and history integration only. No KiCad schematic files, PCB files, Gerbers, drill files, BOM/CPL outputs from an active PCB, JLCPCB packages, PCBWay packages, or production outputs were generated.

## Source Facts Integrated

| Area | Integrated rule |
|---|---|
| JLCPCB BOM | `Comment,Designator,Footprint,LCSC Part #,Quantity,Manufacturer,Manufacturer Part Number,Notes` |
| JLCPCB CPL | `Designator,Mid X,Mid Y,Layer,Rotation` |
| PCBWay BOM | `Line #,Quantity Per Part Number,Reference Designator,Part Number,Part Description,Package,Type,Manufacturer Name,Manufacturer Part Number,Distributor Part Number,Notes` |
| PCBWay centroid | `Designator,Mid X,Mid Y,Rotation,Layer` |
| Universal BOM | `Line #,Comment,Quantity,Designator,Footprint,Package,Type,LCSC Part #,Manufacturer,Manufacturer Part Number,Distributor,Distributor Part Number,Part Description,Notes,DNP` |
| Universal pick-and-place | `Designator,Mid X,Mid Y,Layer,Rotation` |
| Package layout | Separate `jlcpcb`, `pcbway`, and `review` folders under each manufacturing revision |
| Pre-upload checks | DRC, Gerbers, drills, external viewer, BOM, placement, connector orientation, pin 1, polarity, paste, outline, holes/slots, assembly notes |

## Integration Result

- `24_FAB_PROFILES` now contains active JLCPCB, PCBWay, universal PCBA, revision-folder, connector-orientation, and NOT_FINAL export rules.
- `17_RELEASE_BUILD\schemas` contains JSON metadata schemas for all requested CSV formats.
- `17_RELEASE_BUILD\templates` contains CSV and markdown templates.
- `03_TOOLS\scripts\fabrication` contains validators for BOM/CPL/centroid/universal files and PCBA package folder structure.
- `09_ACCURACY_ENGINE` contains export validation rules and pre-upload checklists.
- `.prompts\kicad_pipeline` now requires fab profiles, validators, assembly notes, orientation checks, and NOT_FINAL marking.
- `START_HERE_FOR_AI_AGENTS.md` now routes JLCPCB/export/production tasks to the new fab profiles and PCBA export gate checklist.
- Global memory records the JLCPCB/PCBWay separate-format rule and the warning that CSV validation is not upload approval.

## Validation Summary

- Python syntax check: `PASS`
- JSON schema parse check: `PASS`
- Template CSV validation: `PASS_WITH_WARNINGS`
- Warnings are expected because connector orientation, polarity, pin 1, and placement rotations still require manual/proof review.

## Hard Safety Result

- KiCad design files changed: `NO`
- Manufacturing output package generated: `NO`
- Gerbers generated: `NO`
- Active-PCB BOM/CPL generated: `NO`
- Production-ready claim made: `NO`

Current rule: JLCPCB/PCBWay export remains blocked until final PCB/export gates pass and LJ approves.

