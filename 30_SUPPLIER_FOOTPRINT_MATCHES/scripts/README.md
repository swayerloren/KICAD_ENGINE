# Supplier Footprint Match Scripts

Safe local scripts for supplier-to-KiCad footprint match records.

## Scripts

| Script | Purpose |
| --- | --- |
| `create_match_record.py` | Create a JSON/Markdown match record from command-line fields. |
| `check_match_confidence.py` | Validate confidence, high-risk, and human-review rules for one record or a folder. |
| `build_match_index.py` | Build Markdown/JSON indexes from match records. |
| `report_unmatched_supplier_parts.py` | Compare supplier normalized records to match records and report missing matches. |

## Safety

- Scripts do not call live supplier APIs.
- Scripts do not store credentials.
- Scripts do not download datasheets.
- Scripts do not edit KiCad project or library files.

