# Rejected Low Value Classification

Status: `FINAL_DRAIN_COMPLETE`

Date: `2026-05-11`

## Source Folder

- `knowledge_scrape/91_rejected_low_value`

## Policy Used

The folder name identified these captures as low-value or junk, but the raw
files are still copied web content. Because of that, raw-payload copyright risk
outranked low-value archival convenience.

Result:

- metadata files were archived to migration history
- raw copied captures were moved to license quarantine
- no raw rejected payload was promoted into canonical knowledge docs

## Classification Totals

- `MOVE_AS_HISTORY_ONLY`: `2`
- `MOVE_TO_LICENSE_QUARANTINE`: `780`
- `MOVE_TO_REJECTED_LOW_VALUE`: `0`
- `MOVE_TO_CANONICAL_DESTINATION`: `0`
- `DUPLICATE_OF_EXISTING`: `0`
- `NEEDS_HUMAN_REVIEW`: `0`

## Metadata Files

| File | Classification | Destination |
| --- | --- | --- |
| `.gitkeep` | `MOVE_TO_HISTORY_ONLY` | `02_HISTORY/knowledge_scrape_migration/rejected_low_value/91_rejected_low_value/.gitkeep` |
| `_CATEGORY_INDEX.md` | `MOVE_TO_HISTORY_ONLY` | `02_HISTORY/knowledge_scrape_migration/rejected_low_value/91_rejected_low_value/_CATEGORY_INDEX.md` |

## Raw Capture Disposition

- All `780` raw capture files from `91_rejected_low_value/` were classified as
  `MOVE_TO_LICENSE_QUARANTINE`
- Destination:
  `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/91_rejected_low_value/`

## Result

`knowledge_scrape/91_rejected_low_value` was removed.

