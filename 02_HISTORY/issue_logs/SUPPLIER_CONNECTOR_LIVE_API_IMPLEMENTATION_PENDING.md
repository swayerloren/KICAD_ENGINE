# Issue: Supplier Connector Live API Implementation Pending

Date: 2026-05-03

Status: `OPEN`

Severity: `MEDIUM`

## Summary

Digi-Key, Mouser, JLCPCB, and LCSC now have safe dry-run connector stubs, but live supplier API implementations are not complete or tested.

## Affected Area

- `28_SUPPLIER_INGESTION/connectors/digikey/digikey_connector.py`
- `28_SUPPLIER_INGESTION/connectors/mouser/mouser_connector.py`
- `28_SUPPLIER_INGESTION/connectors/jlcpcb/jlcpcb_connector.py`
- `28_SUPPLIER_INGESTION/connectors/lcsc/lcsc_connector.py`

## Required Before Closing

- Confirm official API/data-feed terms for each supplier.
- Implement live API calls only behind explicit `--live`.
- Read credentials only from environment variables or ignored local config.
- Add rate-limit handling.
- Add tests using mock responses or user-approved sample fixtures.
- Confirm no secrets are printed, cached, or written to logs.
- Confirm datasheet PDFs are not downloaded by default.
- Confirm normalized outputs preserve source URL and retrieval date.

## Current Safe Behavior

Default mode remains `DRY_RUN`. Live mode is guarded and no live call is made by these stubs.
