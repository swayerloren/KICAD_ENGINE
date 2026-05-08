# Supplier Datasheet Footprint Scorecard

Date: 2026-05-03
Classification: `INTERNAL_ALPHA`

## Scores

| Category | Score | Status | Rationale |
| --- | ---: | --- | --- |
| Supplier ingestion readiness | 74/100 | `INTERNAL_ALPHA` | Strong API-safe scaffolding, dry-run connector stubs, schemas, and no-secret policy. Live APIs are not implemented or tested. |
| STM32 content readiness | 76/100 | `INTERNAL_ALPHA` | STM32F1 pilot is useful and STM32 master indexes exist. Most family content remains source-link/stub level, not verified design data. |
| Datasheet tree usefulness | 78/100 | `PUBLIC_ALPHA_CANDIDATE` | MCU tree has broad AI-readable coverage across 48 folders. Support folders and exact source-section extraction still need work. |
| Footprint gap readiness | 77/100 | `INTERNAL_ALPHA` | Installed KiCad inventory and gap reports exist, but all candidates remain unverified. |
| Supplier-footprint matching readiness | 69/100 | `INTERNAL_ALPHA` | Rules are conservative and useful, but current records are example-only and not production approvals. |
| Legal/security safety | 80/100 | `INTERNAL_ALPHA` | No obvious secrets or scraping. Two legacy PDFs require redistribution review before public release. |
| AI usefulness | 82/100 | `PUBLIC_ALPHA_CANDIDATE` | The systems are highly useful for guiding AI agents away from guessing, with clear uncertainty and human-review gates. |

## Overall

Overall score: `76/100`

Overall classification: `INTERNAL_ALPHA`

The repo is useful for internal AI-assisted KiCad research, planning, and review. It is not ready to claim production-grade supplier intelligence, verified footprint matching, or public-release-safe datasheet redistribution.

## Evidence Used

- `05_OUTPUTS/datasheet_tree/MCU_TREE_COMPLETION_SUMMARY.md`
- `02_HISTORY/design_reviews/STM32F1_PILOT_CONTENT_COMPLETION_REPORT.md`
- `28_SUPPLIER_INGESTION/reports/connector_dry_run/DRY_RUN_TEST_REPORT.md`
- `05_OUTPUTS/footprint_gap_analysis/FOOTPRINT_GAP_SUMMARY.md`
- `30_SUPPLIER_FOOTPRINT_MATCHES/reports/MATCH_INDEX.md`
- Local no-secret scans against `28_SUPPLIER_INGESTION`, `29_FOOTPRINT_GAP_ANALYSIS`, and `30_SUPPLIER_FOOTPRINT_MATCHES`
- Local PDF scan under `06_DATASHEETS`

