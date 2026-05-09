# Claim / Evidence Matrix - KiCad Library Index Portability Cleanup

| Claim | Evidence |
| --- | --- |
| `GENERATED_INDEXES` held tracked generated payloads, not just source docs | `git ls-files 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` returned 22 tracked files |
| The payload was machine-local rather than portable | path-pattern search found drive-path data, `AppData` references, and exact KiCad install roots inside the generated files |
| The payload was removed from Git tracking only | `git rm -r --cached -- 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` plus `Test-Path` confirmed the folder remained on disk |
| The repo now keeps a placeholder-only folder | `.gitignore` rules plus tracked `GENERATED_INDEXES/README.md` |
| Local regeneration still works | successful temp-output runs of `index_symbols.py`, `index_footprints.py`, `index_3d_models.py`, `find_symbol_candidates.py`, and `find_footprint_candidates.py` |
