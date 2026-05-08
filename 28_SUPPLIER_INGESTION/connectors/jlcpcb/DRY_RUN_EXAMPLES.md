# JLCPCB Dry-Run Examples

Status: `SAFE_TO_RUN_OFFLINE`

## Query Placeholder

```powershell
python 28_SUPPLIER_INGESTION/connectors/jlcpcb/jlcpcb_connector.py --query C12345
```

## Normalize Local Sample JSON

```powershell
python 28_SUPPLIER_INGESTION/connectors/jlcpcb/jlcpcb_connector.py `
  --input-json 28_SUPPLIER_INGESTION/connectors/jlcpcb/sample_input.example.json `
  --output 28_SUPPLIER_INGESTION/reports/jlcpcb_dry_run_output.json
```

## Cache Non-Secret Normalized Output

```powershell
python 28_SUPPLIER_INGESTION/connectors/jlcpcb/jlcpcb_connector.py --query C12345 --cache
```

## Safety Expectations

- `mode` is `DRY_RUN`.
- `live_call_made` is `false`.
- `pdfs_downloaded` is `false`.
- `verification_status` is `UNVERIFIED`.
- No API keys are read, printed, or saved.
- JLCPCB availability is not treated as footprint or PNP-orientation approval.
