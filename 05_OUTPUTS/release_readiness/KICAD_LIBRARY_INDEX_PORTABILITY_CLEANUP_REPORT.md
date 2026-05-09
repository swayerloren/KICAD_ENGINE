# KiCad Library Index Portability Cleanup Report

Date: `2026-05-09`
Task type: `AUDIT_ONLY`

## Goal

Remove machine-local generated KiCad library index payloads from Git tracking so GitHub ZIP users do not inherit stale local install/library-table paths as portable repo truth.

## Folder Audited

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/`

## Tracked Generated Files Found

Tracked files before cleanup: `22`

Tracked size before cleanup: `30991902` bytes (`29.56 MiB`)

Files found:

- `3d_model_index.json`
- `3d_model_summary.md`
- `footprint_candidates_esp32_s3_wroom_1.json`
- `footprint_candidates_esp32_s3_wroom_1.md`
- `footprint_candidates_mcp2562fd.json`
- `footprint_candidates_mcp2562fd.md`
- `footprint_candidates_stm32f103c8t6.json`
- `footprint_candidates_stm32f103c8t6.md`
- `footprint_candidates_usb_c_connector_generic.json`
- `footprint_candidates_usb_c_connector_generic.md`
- `footprint_index.json`
- `footprint_index_summary.md`
- `symbol_candidates_esp32_s3_wroom_1.json`
- `symbol_candidates_esp32_s3_wroom_1.md`
- `symbol_candidates_mcp2562fd.json`
- `symbol_candidates_mcp2562fd.md`
- `symbol_candidates_stm32f103c8t6.json`
- `symbol_candidates_stm32f103c8t6.md`
- `symbol_candidates_usb_c_connector_generic.json`
- `symbol_candidates_usb_c_connector_generic.md`
- `symbol_index.json`
- `symbol_index_summary.md`

## Machine-Local Path Findings

- `symbol_index.json` and `footprint_index.json` contained user-config-root evidence including `AppData` paths.
- Large generated JSON inventories and summary Markdown files contained machine-specific drive-path data.
- Summary Markdown files embedded exact install roots such as `C:\Program Files\KiCad\9.0`.
- Candidate JSON outputs contained exact machine-local stock-library file paths.

Conclusion: these files are local generated inventory, not portable templates or source-of-truth repo assets.

## Git Cleanup Applied

- Removed all `22` generated payload files from Git tracking with `git rm --cached`.
- Kept the folder visible in Git using `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/README.md`.
- Left local files on disk.

## .gitignore Policy Applied

Added placeholder-only rules:

- ignore `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*`
- unignore `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/README.md`

## Docs Updated

- `03_TOOLS/kicad_library_intelligence/README.md`
- `03_TOOLS/kicad_library_intelligence/SYMBOL_LIBRARY_INDEX.md`
- `03_TOOLS/kicad_library_intelligence/FOOTPRINT_LIBRARY_INDEX.md`
- `03_TOOLS/kicad_library_intelligence/THREE_D_MODEL_INDEX.md`

These docs now describe generated indexes as local outputs that must be regenerated per machine instead of shipped repo truth.

## Regeneration Validation

Read-only regeneration smoke test passed with temp output under `T_E_M_P/kicad_library_regen_smoke`:

- `python 03_TOOLS/scripts/kicad_libraries/index_symbols.py --output-dir T_E_M_P/kicad_library_regen_smoke`
- `python 03_TOOLS/scripts/kicad_libraries/index_footprints.py --output-dir T_E_M_P/kicad_library_regen_smoke`
- `python 03_TOOLS/scripts/kicad_libraries/index_3d_models.py --output-dir T_E_M_P/kicad_library_regen_smoke`
- `python 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py "USB-C connector generic" --output-dir T_E_M_P/kicad_library_regen_smoke`
- `python 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py "USB-C connector generic" --output-dir T_E_M_P/kicad_library_regen_smoke`

One initial `index_footprints.py` attempt hit a timeout and was retried successfully with a longer timeout.

## Validation Summary

- No `.kicad_sch` files changed.
- No `.kicad_pcb` files changed.
- No source scripts were removed.
- The cleanup removed generated local index outputs only.
- The placeholder README remains tracked.

## Expected GitHub Result

GitHub should show `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/` as a placeholder folder with `README.md` only.
