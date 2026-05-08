# Digi-Key Dry-Run Examples

Status: `SAFE_TO_RUN_OFFLINE`

## Query Placeholder

```powershell
python 28_SUPPLIER_INGESTION/connectors/digikey/digikey_connector.py --query STM32F103C8T6
```

## Normalize Local Sample JSON

```powershell
python 28_SUPPLIER_INGESTION/connectors/digikey/digikey_connector.py `
  --input-json 28_SUPPLIER_INGESTION/connectors/digikey/sample_input.example.json `
  --output 28_SUPPLIER_INGESTION/reports/digikey_dry_run_output.json
```

## Cache Non-Secret Normalized Output

```powershell
python 28_SUPPLIER_INGESTION/connectors/digikey/digikey_connector.py --query MCP2562FD --cache
```

## Safety Expectations

- `mode` is `DRY_RUN`.
- `live_call_made` is `false`.
- `pdfs_downloaded` is `false`.
- `verification_status` is `UNVERIFIED`.
- No API keys are read, printed, or saved.
