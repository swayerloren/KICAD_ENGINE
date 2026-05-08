# KiCad Library Intelligence

Date: 2026-05-02

Purpose: give Codex, Claude, and similar VS Code agents a read-only view of the symbols, footprints, 3D models, and library tables available in the user's installed KiCad app.

## Audited Local Roots

| Path | Role | Agent Use |
| --- | --- | --- |
| `C:\Program Files\KiCad\9.0\share\kicad\symbols` | Stock symbol libraries | Read symbol names, fields, descriptions, keywords, and source library paths. |
| `C:\Program Files\KiCad\9.0\share\kicad\footprints` | Stock footprint libraries | Read footprint names, pad counts, model references, descriptions, and tags. |
| `C:\Program Files\KiCad\9.0\share\kicad\3dmodels` | Stock 3D models | Read model availability for visual/mechanical review. |
| `C:\Program Files\KiCad\9.0\share\kicad\template` | Stock table templates and project templates | Read default library tables and template references. |
| `C:\Program Files\KiCad\9.0\lib` | Program support libraries, ngspice, crashpad, cmake files | Not a stock footprint/symbol source. Read only for app inventory. |
| `C:\Program Files\KiCad\9.0\etc` | Font configuration | Not a stock footprint/symbol source. Read only for app inventory. |
| `%APPDATA%\kicad\9.0` | User-global KiCad settings and library tables | Read library tables only; never modify without explicit request and backup. |

## Generated Outputs

Generated indexes live under:

`03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/`

Current generated samples include:

- `symbol_index_summary.md` and `symbol_index.json`
- `footprint_index_summary.md` and `footprint_index.json`
- `3d_model_summary.md` and `3d_model_index.json`
- Symbol and footprint candidate files for:
  - `ESP32-S3-WROOM-1`
  - `STM32F103C8T6`
  - `USB-C connector generic`
  - `MCP2562FD`

## Scripts

Run from the repo root:

```powershell
python "03_TOOLS\scripts\kicad_libraries\index_symbols.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\index_footprints.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\index_3d_models.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "ESP32-S3-WROOM-1"
python "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py" "USB-C connector generic"
```

All scripts support:

- `--kicad-root` for a non-default install root.
- `--version` for future KiCad config versions.
- `--output-dir` for generated output location.

The scripts refuse to write generated output inside the KiCad install root or KiCad user config root.

## Safety Policy

- Read KiCad stock libraries.
- Read user-global library tables.
- Do not write into `C:\Program Files\KiCad`.
- Do not write into `%APPDATA%\kicad`.
- Do not modify project-local library tables unless active project, backup, rollback, and verification are confirmed.
- Candidate matches are search results only. They are not approved symbols or footprints.
