# Part Ingestion Scripts

These scripts generate placeholder review artifacts from user-provided metadata.

They do not:

- Scrape the web.
- Download datasheets.
- Parse PDFs automatically.
- Redistribute copyrighted files.
- Verify pinouts, electrical limits, symbols, or footprints.

## Scripts

- `create_datasheet_summary_stub.py`
- `create_part_record_stub.py`
- `create_footprint_checklist_stub.py`
- `create_symbol_checklist_stub.py`

## Common Arguments

Most scripts accept:

- `--part-number`
- `--vendor`
- `--family`
- `--category`
- `--package`
- `--datasheet-url`
- `--datasheet-local-path`
- `--output-dir`

Any omitted exact field is written as:

```text
Unknown - requires source verification
```

## Example

```powershell
python 13_PART_INGESTION/scripts/create_part_record_stub.py --part-number MCP2562FD --vendor Microchip --family CAN_FD --category 03_COMMUNICATION --package SOIC-8 --datasheet-url "https://example.com/vendor-page" --output-dir 05_OUTPUTS/part_ingestion/MCP2562FD
python 13_PART_INGESTION/scripts/create_datasheet_summary_stub.py --part-number MCP2562FD --vendor Microchip --output-dir 05_OUTPUTS/part_ingestion/MCP2562FD
python 13_PART_INGESTION/scripts/create_symbol_checklist_stub.py --part-number MCP2562FD --vendor Microchip --output-dir 05_OUTPUTS/part_ingestion/MCP2562FD
python 13_PART_INGESTION/scripts/create_footprint_checklist_stub.py --part-number MCP2562FD --vendor Microchip --package SOIC-8 --output-dir 05_OUTPUTS/part_ingestion/MCP2562FD
```

## Review Rule

Generated stubs are starting points. They must be completed from source evidence before design use.

