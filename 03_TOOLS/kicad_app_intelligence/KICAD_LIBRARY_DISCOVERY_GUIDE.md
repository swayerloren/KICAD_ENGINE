# KiCad Library Discovery Guide

Date: 2026-05-02
Audited install root: `C:\Program Files\KiCad\9.0`

## Purpose

This guide explains how agents should discover KiCad stock libraries, user-global libraries, and project-specific libraries on Windows without modifying the installed KiCad app or user projects.

## Stock Library Roots

For the audited KiCad 9 install:

| Library type | Stock root | Variable normally used in library references |
| --- | --- | --- |
| Symbols | `C:\Program Files\KiCad\9.0\share\kicad\symbols` | `${KICAD9_SYMBOL_DIR}` |
| Footprints | `C:\Program Files\KiCad\9.0\share\kicad\footprints` | `${KICAD9_FOOTPRINT_DIR}` |
| 3D models | `C:\Program Files\KiCad\9.0\share\kicad\3dmodels` | `${KICAD9_3DMODEL_DIR}` |
| Templates | `C:\Program Files\KiCad\9.0\share\kicad\template` | KiCad internal/template paths |
| Demos | `C:\Program Files\KiCad\9.0\share\kicad\demos` | Direct file paths |

Observed counts:

- 224 stock `.kicad_sym` files.
- 155 stock `.pretty` footprint libraries.
- 15,415 stock `.kicad_mod` footprint files.
- 105 stock `.3dshapes` folders.
- 14,043 stock 3D model files under `3dmodels`.

## Stock Library Tables

Stock global library table templates are installed here:

- `C:\Program Files\KiCad\9.0\share\kicad\template\sym-lib-table`
- `C:\Program Files\KiCad\9.0\share\kicad\template\fp-lib-table`

Observed table entry counts:

- Stock `sym-lib-table`: 223 entries.
- Stock `fp-lib-table`: 155 entries.

These files are templates. Do not edit them.

## User-Global Library Tables

Typical Windows user-global KiCad 9 library table paths:

- `%APPDATA%\kicad\9.0\sym-lib-table`
- `%APPDATA%\kicad\9.0\fp-lib-table`
- `%APPDATA%\kicad\9.0\design-block-lib-table`

Observed on this machine:

- `C:\Users\LJ\AppData\Roaming\kicad\9.0\sym-lib-table`
- `C:\Users\LJ\AppData\Roaming\kicad\9.0\fp-lib-table`
- `C:\Users\LJ\AppData\Roaming\kicad\9.0\design-block-lib-table`

Observed table entry counts:

- User-global `sym-lib-table`: 227 entries.
- User-global `fp-lib-table`: 158 entries.

The user-global tables can contain stock entries, package-manager entries, and user-added libraries. Agents may read them to resolve library names. Agents must not edit user-global tables unless explicitly requested and backed up.

## Project-Specific Library Tables

KiCad projects may include project-local library table files near the project:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

Project-specific tables are the correct place to record project-local symbols, footprints, and design blocks when a project intentionally owns them.

Project-local paths should prefer `${KIPRJMOD}`. Example patterns:

```text
${KIPRJMOD}/symbols/ProjectSymbols.kicad_sym
${KIPRJMOD}/footprints/ProjectFootprints.pretty
${KIPRJMOD}/3dmodels/Part.step
```

Using `${KIPRJMOD}` keeps project libraries portable when the project folder moves. Hardcoded absolute paths should be treated as portability risks.

## Library Resolution Strategy For Agents

When resolving a symbol or footprint:

1. Identify the active project path.
2. Check for project-specific `sym-lib-table` and `fp-lib-table`.
3. Check user-global tables under `%APPDATA%\kicad\<major.minor>`.
4. Resolve stock variables such as `${KICAD9_SYMBOL_DIR}`, `${KICAD9_FOOTPRINT_DIR}`, and `${KICAD9_3DMODEL_DIR}` from the detected install root.
5. Resolve `${KIPRJMOD}` from the active project directory.
6. Verify the referenced file/folder exists.
7. For footprints, inspect `.kicad_mod` pad names, layers, courtyard, paste/mask, and 3D model references.
8. For symbols, inspect `.kicad_sym` pin names, pin numbers, units, power pins, and footprint fields.
9. For 3D models, verify model file existence and note missing models as visual/mechanical review items.

## What Agents May Read

Agents may read:

- Stock symbols under `share\kicad\symbols`.
- Stock footprints under `share\kicad\footprints`.
- Stock 3D model folder listings under `share\kicad\3dmodels`.
- Stock library table templates under `share\kicad\template`.
- User-global library tables under `%APPDATA%\kicad\<version>`.
- Project-local library tables only after active project scope is confirmed.
- Project-local symbol and footprint libraries only after active project scope is confirmed.

## What Agents Must Not Modify

Agents must not modify:

- Any stock installed library under `C:\Program Files\KiCad`.
- User-global library tables unless explicitly requested and backed up.
- Project-specific library tables unless the active project, backup, file scope, rollback plan, and verification plan are confirmed.
- Generated manufacturing outputs unless the user explicitly requests a release/export workflow and output folders are approved.

## Symbol Review Checklist

For any symbol used in a project:

- Confirm library source: stock, user-global, project-local, or external.
- Confirm symbol name and unit count.
- Confirm pin names and pin numbers against datasheet.
- Confirm hidden power pins or passive pins are intentional.
- Confirm footprint field is present and points to an intended footprint.
- Confirm power flags and ERC implications.
- Record unresolved mismatches in project history.

## Footprint Review Checklist

For any footprint used in a project:

- Confirm library source.
- Confirm pad numbers match the symbol and datasheet.
- Confirm package dimensions against datasheet.
- Confirm pad sizes, drill sizes, and annular rings.
- Confirm courtyard and fab layers.
- Confirm paste and mask behavior.
- Confirm pin 1/orientation marks.
- Confirm 3D model path exists when mechanical review depends on it.
- Confirm connector orientation, cable exit direction, and mating part for connectors.

## Future Version Adaptation

For future KiCad versions:

- Detect installed roots under `C:\Program Files\KiCad`.
- Read the matching `%APPDATA%\kicad\<major.minor>` config root.
- Use version-specific stock variables.
- Do not assume KiCad 9 library table entry counts remain valid.
- Re-run `inventory_kicad_libraries.ps1` after KiCad upgrades.
