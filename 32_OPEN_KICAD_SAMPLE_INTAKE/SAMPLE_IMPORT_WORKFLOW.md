# Sample Import Workflow

Status: `DRY_RUN_FIRST`

## Precondition

Before importing a sample:

1. Create a candidate record.
2. Record source URL.
3. Run license screening or mark `NEEDS_HUMAN_LICENSE_REVIEW`.
4. Confirm candidate contains KiCad source files.
5. Confirm the source is not in `DO_NOT_IMPORT_LIST.md`.

## Workflow

1. Use `find_candidate_projects.py` or manual review to identify source links.
2. Use `create_candidate_record.py` to create candidate Markdown/JSON.
3. Use `license_screen_sample.py` on a local source folder or candidate metadata.
4. Run `import_sample_project.py` in default dry-run mode.
5. If import is approved, run `import_sample_project.py --apply --source-path <local-folder-or-archive-extracted-folder>`.
6. Store original content under `imported_originals/<sample_id>_<timestamp>/`.
7. Do not edit the imported original.
8. Create a normalized copy with `create_normalized_copy.py --apply`.
9. Run `audit_sample_project_files.py` on both original and normalized copy.

## Import Source Rule

The import script does not clone or download remote projects. Use it with a user-provided local folder or archive already obtained through an approved source workflow. Remote download support must be a future separate audited task.

## Output Rule

Import reports are written to `review_reports/`. Any generated outputs must be `NOT_FINAL` and must not be used for manufacturing.
