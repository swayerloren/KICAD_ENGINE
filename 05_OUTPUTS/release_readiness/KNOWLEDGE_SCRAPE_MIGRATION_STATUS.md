# Knowledge Scrape Migration Status

Status: `KNOWLEDGE_SCRAPE_REMOVED_AFTER_BACKUP`

Generated: `2026-05-12`

- Ledger row count: `2546`
- Source files moved: `2546`
- Remaining knowledge_scrape file count: `0`
- Remaining knowledge_scrape directory count: `0`
- knowledge_scrape removable now: `N/A_ALREADY_REMOVED`

## Validation

- `knowledge_scrape/_scripts` has been drained and removed.
- The previous `43` stale already-moved rows were reconciled and validated.
- The final `7` live `_scripts` rows were moved to history-only storage and validated.
- The empty-tree validator now reports `EMPTY_OR_REMOVABLE`.
- Normal agent routing still does not require `knowledge_scrape/`.
- The empty folder shell was backed up to
  `99_BACKUPS\knowledge_scrape_pre_empty\20260512_150034\knowledge_scrape`
  and then removed from the live repo tree.

## Validation Status Counts

| Validation Status | Count |
| --- | ---: |
| `MOVED_VALIDATED` | 2546 |

## Action Counts

| Action | Count |
| --- | ---: |
| `MOVE_AS_HISTORY_ONLY` | 333 |
| `MOVE_TO_LICENSE_QUARANTINE` | 2213 |

## License Risk Counts

| License Risk | Count |
| --- | ---: |
| `HIGH` | 1210 |
| `LOW` | 349 |
| `MEDIUM` | 987 |

## Script-Drain Delta

- unresolved ledger rows before: `50`
- unresolved ledger rows after: `0`
- `_scripts` rows resolved in this phase: `7`
- stale finalized rows reconciled in this phase: `43`

## Remaining knowledge_scrape Top-Level File Counts

Folder removed.

## Remaining Folders

None. `knowledge_scrape/` no longer exists in the live repo tree.
