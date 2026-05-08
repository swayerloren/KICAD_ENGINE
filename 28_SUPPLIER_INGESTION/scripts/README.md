# Supplier Ingestion Scripts

Status: `SAFE_LOCAL_HELPERS`

These scripts are safe local helpers for supplier metadata ingestion. Their job is to normalize user-provided or authorized source metadata, identify gaps, and produce conservative candidate matches. They must not scrape supplier websites, store credentials, or approve footprints.

## Scripts

| Script | Purpose | Default Safety Behavior |
| --- | --- | --- |
| `normalize_supplier_part.py` | Normalize JSON or CSV records into KiCad Engine supplier schema. | Writes normalized metadata only; unreviewed fields stay `UNVERIFIED`. |
| `import_manual_csv.py` | Import user-provided CSV exports. | Expects local files; does not contact supplier sites. |
| `build_supplier_index.py` | Index normalized supplier records. | Outputs Markdown/JSON summaries. |
| `create_supplier_gap_report.py` | Report missing source, package, datasheet, lifecycle, and footprint evidence. | Does not fill missing data by guessing. |
| `match_supplier_parts_to_component_database.py` | Text-match supplier MPNs to component database records. | Candidate matching only. |
| `match_supplier_parts_to_kicad_footprints.py` | Create conservative footprint keyword candidates from package text. | Never marks footprints verified. |

## Command Pattern

Run scripts from the repo root:

```powershell
python 28_SUPPLIER_INGESTION\scripts\import_manual_csv.py --input path\to\sanitized.csv --output 28_SUPPLIER_INGESTION\normalized
python 28_SUPPLIER_INGESTION\scripts\build_supplier_index.py --input 28_SUPPLIER_INGESTION\normalized --output 28_SUPPLIER_INGESTION\reports
python 28_SUPPLIER_INGESTION\scripts\create_supplier_gap_report.py --input 28_SUPPLIER_INGESTION\normalized --output 28_SUPPLIER_INGESTION\reports
```

## Rules

- No blind scraping.
- No live API calls unless a connector explicitly requires `--live`, credentials are in environment variables, and the user approved the run.
- No API keys in files or logs.
- No PDF downloads by default.
- Output generated Markdown and JSON into `normalized/` or `reports/`.
- Mark unverified records `UNVERIFIED`.
- Do not promote package-name matches to footprint approval.

## Failure Behavior

Scripts should fail clearly when inputs are missing, schema fields are absent, output folders cannot be written, or records contain possible secrets. A failed script must not delete or overwrite source data.
