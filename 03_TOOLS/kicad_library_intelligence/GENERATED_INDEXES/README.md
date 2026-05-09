# Generated KiCad Library Indexes

This folder is for local-machine generated KiCad library inventory outputs.

## Purpose

- hold read-only symbol, footprint, and 3D model index files generated from the user's installed KiCad environment
- hold local candidate-search outputs generated from those indexes

## Portability Rule

- the JSON and Markdown payloads in this folder are not portable repo truth
- they may contain machine-specific install roots, user library-table paths, drive letters, and version-specific library counts
- Codex and Claude must regenerate these files on the current user's machine before treating them as current evidence

## Git Policy

- this folder stays visible in Git by this placeholder `README.md` only
- generated payload files in this folder are ignored on purpose
- do not recommit old generated indexes from another machine

## ZIP User Impact

- a ZIP user does not need this folder populated for first use
- the repo scripts can regenerate the indexes locally when KiCad is installed

## Regeneration

Run from the repo root:

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_symbols.py
python 03_TOOLS/scripts/kicad_libraries/index_footprints.py
python 03_TOOLS/scripts/kicad_libraries/index_3d_models.py
python 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py "ESP32-S3-WROOM-1"
python 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py "USB-C connector generic"
```

If auto-detection does not find KiCad, pass an override:

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_symbols.py --kicad-root "C:\Program Files\KiCad\9.0"
```

## Never Treat As Current Portable Truth

- old generated install paths
- old user-global library-table URIs
- old model/library counts
- old candidate-search outputs from another machine
