# Uncertainty Log: Supplier Connector Stubs

Date: 2026-05-03

Status: `OPEN_UNCERTAINTIES_RECORDED`

## Uncertainties

| Item | Confidence | Human Review Required | Notes |
| --- | --- | --- | --- |
| Official live API implementation details for Digi-Key. | `MEDIUM` | Yes | Requires terms/API review and credential-safe implementation. |
| Official live API implementation details for Mouser. | `MEDIUM` | Yes | Requires terms/API review and credential-safe implementation. |
| Approved live JLCPCB API/data-feed path. | `LOW` | Yes | Current connector refuses live mode. |
| Approved live LCSC API/data-feed path. | `LOW` | Yes | Current connector refuses live mode. |
| Supplier field mappings against real API responses. | `MEDIUM` | Yes | Dry-run mappings use common/sample field candidates and need real fixture review. |
| Functional dry-run smoke test behavior. | `MEDIUM` | No | Test helper exists but was not run because the user requested syntax validation only. |

## Required Follow-Up

- Add mock fixture tests before production live work.
- Review supplier terms/rate limits.
- Keep all live behavior behind explicit `--live`.
- Keep all records `UNVERIFIED` until source evidence and import date are recorded.
