# Open Sample Intake Scripts

These scripts support controlled intake of open KiCad sample projects.

Default behavior:
- Dry-run first.
- No web scraping.
- No login bypass.
- No repository cloning.
- No PDF downloads.
- No writes to active user projects.
- No direct edits to `imported_originals/`.

Scripts:
- `find_candidate_projects.py`: builds candidate plans from local CSV/JSON source lists.
- `create_candidate_record.py`: creates candidate metadata records after source URL and license status are known.
- `import_sample_project.py`: copies a local, pre-screened source folder into `imported_originals/` only with `--apply`.
- `create_normalized_copy.py`: creates an editable review copy from an imported original only with `--apply`.
- `audit_sample_project_files.py`: read-only KiCad file and generated-output inventory.
- `build_sample_index.py`: builds markdown/JSON intake indexes.
- `license_screen_sample.py`: practical license triage from local files; not legal advice.

Every script must preserve uncertainty and must not promote a sample to public payload without license review.
