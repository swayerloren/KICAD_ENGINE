# Claim Evidence Matrix: Supplier Connector Stubs

Date: 2026-05-03

| Claim | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Digi-Key connector stub exists. | `VERIFIED_BY_FILE` | `28_SUPPLIER_INGESTION/connectors/digikey/digikey_connector.py` | Created this session. |
| Mouser connector stub exists. | `VERIFIED_BY_FILE` | `28_SUPPLIER_INGESTION/connectors/mouser/mouser_connector.py` | Created this session. |
| JLCPCB connector stub exists. | `VERIFIED_BY_FILE` | `28_SUPPLIER_INGESTION/connectors/jlcpcb/jlcpcb_connector.py` | Created this session. |
| LCSC connector stub exists. | `VERIFIED_BY_FILE` | `28_SUPPLIER_INGESTION/connectors/lcsc/lcsc_connector.py` | Created this session. |
| Default mode is dry-run. | `VERIFIED_BY_FILE` | Connector argparse paths and payload `mode`. | Dry-run execution was not run because the task requested syntax validation only. |
| Syntax validation passed. | `VERIFIED_BY_COMMAND` | `python -B -m py_compile ...` returned success. | No functional/live tests were run. |
| No targeted secret-pattern matches were found in touched paths. | `VERIFIED_BY_COMMAND` | `rg` scan returned no matches. | This is not a full repository secret audit. |
| No live API calls were made. | `VERIFIED_BY_COMMAND` | Only syntax validation and file inspection commands were run. | Live modes are guarded stubs. |
| No datasheet PDFs were downloaded. | `VERIFIED_BY_FILE` | Connector code has no PDF download path. | No network/download commands were run. |
| Live API integration is production-ready. | `CONTRADICTED` | Connector audit and issue log state live APIs are not implemented. | Must not be claimed. |
