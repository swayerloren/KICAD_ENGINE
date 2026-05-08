# Library Table Guide

Date: 2026-05-02

Purpose: explain how agents should resolve KiCad symbol, footprint, and 3D model library references without modifying global or project library tables.

## Stock Table Templates

Observed KiCad 9 stock table templates:

- `C:\Program Files\KiCad\9.0\share\kicad\template\sym-lib-table`
- `C:\Program Files\KiCad\9.0\share\kicad\template\fp-lib-table`

These are installed templates. Agents may read them. Agents must not edit them.

## User-Global Tables

Typical KiCad 9 user-global path on Windows:

`%APPDATA%\kicad\9.0`

Observed user-global files:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`
- `kicad_common.json`
- `kicad.json`
- `eeschema.json`
- `pcbnew.json`

Agents may read user-global tables to resolve library nicknames. Agents must not modify these files unless the user explicitly asks for a global configuration change and a backup plan is confirmed.

## Project Tables

Project-local library tables may be present beside a KiCad project:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

Project-local entries should prefer `${KIPRJMOD}` paths for portability.

Example:

```text
${KIPRJMOD}/symbols/ProjectSymbols.kicad_sym
${KIPRJMOD}/footprints/ProjectFootprints.pretty
${KIPRJMOD}/3dmodels/CustomPart.step
```

Do not inspect or edit project-local tables until the active project is confirmed under the repo workflow.

## Common Variables

| Variable | Typical Meaning |
| --- | --- |
| `${KICAD9_SYMBOL_DIR}` | KiCad 9 stock symbols root. |
| `${KICAD9_FOOTPRINT_DIR}` | KiCad 9 stock footprints root. |
| `${KICAD9_3DMODEL_DIR}` | KiCad 9 stock 3D models root. |
| `${KIPRJMOD}` | Active KiCad project directory. |

## Resolution Workflow

1. Identify active project root if project files are involved.
2. Read project-local tables if allowed by the active-project rules.
3. Read user-global tables under `%APPDATA%\kicad\<version>`.
4. Read stock table templates under the installed KiCad root.
5. Resolve variables from the detected install root and project root.
6. Confirm referenced file or folder exists.
7. Inspect symbol/footprint/model content directly before making claims.

## Do Not Modify

- `C:\Program Files\KiCad\9.0\share\kicad\template\sym-lib-table`
- `C:\Program Files\KiCad\9.0\share\kicad\template\fp-lib-table`
- `%APPDATA%\kicad\9.0\sym-lib-table`
- `%APPDATA%\kicad\9.0\fp-lib-table`
- project-local library tables unless active project, backup, rollback, and verification are confirmed
