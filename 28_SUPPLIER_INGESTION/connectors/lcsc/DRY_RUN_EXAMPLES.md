# LCSC Dry-Run Examples

Status: `SAFE_TO_RUN_OFFLINE`

## Query Placeholder

```powershell
python 28_SUPPLIER_INGESTION/connectors/lcsc/lcsc_connector.py --query C12345
```

## Normalize Local Sample JSON

```powershell
python 28_SUPPLIER_INGESTION/connectors/lcsc/lcsc_connector.py `
  --input-json 28_SUPPLIER_INGESTION/connectors/lcsc/sample_input.example.json `
  --output 28_SUPPLIER_INGESTION/reports/lcsc_dry_run_output.json
```

## Cache Non-Secret Normalized Output

```powershell
python 28_SUPPLIER_INGESTION/connectors/lcsc/lcsc_connector.py --query C12345 --cache
```

## Safety Expectations

- `mode` is `DRY_RUN`.
- `live_call_made` is `false`.
- `pdfs_downloaded` is `false`.
- `verification_status` is `UNVERIFIED`.
- No API keys are read, printed, or saved.
- LCSC catalog data is not treated as footprint or PNP-orientation approval.
