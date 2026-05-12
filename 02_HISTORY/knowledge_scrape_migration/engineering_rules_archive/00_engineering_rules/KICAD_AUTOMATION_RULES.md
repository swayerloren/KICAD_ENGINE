# KiCad Automation Rules

- Start in `../01_kicad_core/`, `../02_kicad_python_api/`, `../03_kicad_file_formats/`, and `../04_kicad_libraries_symbols_footprints/`.
- Prefer official KiCad manuals, dev docs, source trees, and KLC before third-party commentary.
- Use `../URL_INDEX.csv` to verify the source URL and trust level before relying on a file.
- Treat repo, tree, and API index pages as routing aids, not as proof that a live edit is safe.
- Cross-check file-format assumptions with `../03_kicad_file_formats/` before scripted edits.
- Cite local file paths and `url_index_id` when using KiCad docs, source trees, or Python API references.
- Never modify active KiCad project files until the repo sandbox and verification gates pass.
