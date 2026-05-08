# Integration With 28_SUPPLIER_INGESTION

The Playwright pipeline complements supplier ingestion but does not replace official APIs or user-provided CSV workflows.

## Preferred Path

1. Official supplier API.
2. User-provided CSV export.
3. Manual source-link record.
4. Playwright public-page evidence only when allowed.

## Dry-Run Rule

Scripts in this pipeline must not write into `28_SUPPLIER_INGESTION/normalized` or `reports` unless a future explicit apply mode is reviewed.

## Live Browser Rule

Do not use Playwright to bypass supplier API requirements, login walls, rate limits, or anti-bot controls.

