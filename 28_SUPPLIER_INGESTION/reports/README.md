# Supplier Ingestion Reports

Status: `GENERATED_REPORTS_REQUIRE_REVIEW`

Generated supplier ingestion reports belong here. Reports summarize source coverage, normalization results, missing fields, footprint-match gaps, and safety blockers. They do not approve sourcing or assembly.

## Report Types

| Report | Purpose |
| --- | --- |
| `SUPPLIER_INDEX.md` | Lists normalized records by manufacturer, MPN, supplier, and status. |
| `SUPPLIER_GAP_REPORT.md` | Shows missing source URLs, package fields, lifecycle data, datasheet links, and footprint evidence. |
| `COMPONENT_DB_MATCH_REPORT.md` | Shows candidate matches between supplier records and `08_COMPONENT_DATABASE`. |
| `KICAD_FOOTPRINT_MATCH_REPORT.md` | Shows footprint keyword candidates only; exact verification remains blocked. |
| `API_SAFETY_REPORT.md` | Documents whether live mode, credentials, or rate limits were involved. |

## Required Report Fields

- source input path,
- command or script used,
- dry-run/live mode,
- record count,
- records updated or proposed,
- `UNVERIFIED` count,
- high-risk part count,
- blocked sources,
- generated output paths,
- next safe action.

## Rules

- Default reports must come from `DRY_RUN` or user-provided local data.
- Live API/browser results must document authorization and must not store secrets.
- Report stale inventory/price data as snapshots only.
- Footprint and package matches remain candidates unless `30_SUPPLIER_FOOTPRINT_MATCHES` contains verified evidence.
