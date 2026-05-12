# Schematic Annotation Rules

## Purpose

These rules define the required automated and human checks for KiCad schematic annotation before any PCB update, placement, routing, zone work, or manufacturing-style output.

## Required Checker

Run:

```powershell
python .\03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py --schematic "<project>.kicad_sch" --bom-lock "<bom-lock-or-ready-parts-file>" --output "<report>.md" --json-output "<report>.json"
```

The generated report must be linked from the active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

## Authoritative Proof Rule

Saved-file scans and regex checks are useful blockers, but they are not by
themselves authoritative proof that annotation happened correctly in the live
KiCad GUI. When annotation is disputed or unfinished, use the native KiCad GUI
workflow or LJ-confirmed manual annotation.

## Blocking Findings

The schematic-to-PCB gate must remain blocked if any of these are present:

- Any physical reference ending in `?`, including `C?`, `R?`, `U?`, `D?`, `SW?`, `J?`, `TP?`, `MH?`, `F?`, or `Q?`.
- Duplicate physical references.
- Missing `Reference` fields.
- Blank `Value` fields.
- Vague values such as `generic`, `TBD`, `unknown`, or `connector` when an exact MPN exists in the BOM lock.
- Missing required fields on physical symbols where the project standard expects them.
- Component category inconsistent with reference prefix.
- Physical symbols with no footprint assigned.
- High-risk connector, PMOS, ESD/protection, regulator, RF, USB, CAN, or polarity-sensitive parts without explicit verification status.

## Required Human Review

Automated annotation checks do not approve:

- Exact footprint correctness.
- Connector orientation.
- MOSFET source/gate/drain mapping.
- ESD/TVS diode package and direction.
- Regulator thermal/layout requirements.
- Pinout correctness.

These must still be reviewed against datasheets, package drawings, KiCad library evidence, and project notes.

## Status Handling

- `PASS`: no blocking annotation findings were detected.
- `WARN`: a finding needs human review but may not block if explicitly accepted.
- `FAIL`: schematic-to-PCB gate is blocked until fixed or formally carried as a human-reviewed blocker.

Do not mark the active project schematic-to-PCB gate as `PASS` unless the annotation report is current, linked, and free of unresolved `FAIL` findings.
