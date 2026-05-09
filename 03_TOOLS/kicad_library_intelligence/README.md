# KiCad Library Intelligence

Purpose: give Codex, Claude, and similar VS Code agents a read-only way to inspect the symbols, footprints, 3D models, and library tables available in the current user's installed KiCad app.

## What This Folder Contains

- policy docs for symbol, footprint, 3D model, and library-table inspection
- scripts under `03_TOOLS/scripts/kicad_libraries/` that generate local indexes and candidate-search outputs
- a placeholder-only `GENERATED_INDEXES/README.md` explaining why generated payloads are not tracked

## Important Portability Rule

Generated library indexes are local-machine outputs, not portable repo truth.

- do not assume generated counts, install roots, or candidate results from another machine are current
- do not treat shipped generated JSON as authoritative
- regenerate library indexes on the current machine before using them as evidence

The portable tracked file in that folder is:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/README.md`

## Typical Local Roots

These are common locations the scripts inspect on Windows when present:

- KiCad stock symbols under the detected KiCad `share/kicad/symbols` root
- KiCad stock footprints under the detected KiCad `share/kicad/footprints` root
- KiCad stock 3D models under the detected KiCad `share/kicad/3dmodels` root
- stock library-table templates under the detected KiCad `share/kicad/template` root
- user-global KiCad settings and library tables under `%APPDATA%/kicad/<version>`

The exact resolved paths depend on the current machine and KiCad install.

## Regeneration Commands

Run from the repo root:

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_symbols.py
python 03_TOOLS/scripts/kicad_libraries/index_footprints.py
python 03_TOOLS/scripts/kicad_libraries/index_3d_models.py
python 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py "ESP32-S3-WROOM-1"
python 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py "USB-C connector generic"
```

Optional overrides:

- `--kicad-root` for a non-default install root
- `--version` for KiCad config version selection
- `--output-dir` for a custom generated output folder

The scripts refuse to write generated output inside the KiCad install root or KiCad user config root.

## Safety Policy

- read KiCad stock libraries
- read user-global library tables
- do not write into the KiCad install
- do not write into user-global KiCad config folders
- do not modify project-local library tables unless active project, backup, rollback, and verification are confirmed
- candidate matches are search results only; they are not approved symbols or footprints
