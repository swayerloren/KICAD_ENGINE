# Script Drain Record

Status: `COMPLETE_PENDING_FINAL_VALIDATION_RERUN`

Generated: `2026-05-12`

## Scope

Finalize the last unresolved `knowledge_scrape\_scripts\` migration rows and
remove the `_scripts` source residue from the migration blocker list.

## Start-State Observation

- `knowledge_scrape/` existed
- `knowledge_scrape/_scripts/` existed and contained `7` live PowerShell files
- the migration ledger still carried `7` unresolved `_scripts` rows and `43`
  stale unresolved rows whose destinations already existed

## Resolution Method

The final drain used a history-only migration for the remaining PowerShell
scripts:

1. inspect each script body plus migrated entrypoint metadata
2. classify each script as obsolete legacy tooling
3. move each `.ps1` file into
   `02_HISTORY\knowledge_scrape_migration\obsolete_scripts\`
4. keep one provenance note per moved script
5. redirect each `_scripts` ledger row to the moved `.ps1` file
6. mark all `43` stale already-moved rows as `MOVED_VALIDATED`
7. update migration status to reflect zero remaining files under
   `knowledge_scrape/`

## Final Script Dispositions

- `01_build_raw_inventory.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `02_build_url_registry.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `03_classify_copy_markdown.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `04_convert_pdfs_to_markdown.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `05_clean_markdown_for_ai.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `06_build_category_indexes.ps1` -> `MOVE_TO_HISTORY_ONLY`
- `10_import_ingest_v2.ps1` -> `MOVE_TO_HISTORY_ONLY`

## Outcome

- unresolved ledger rows before: `50`
- unresolved ledger rows after reconciliation: `0`
- remaining `knowledge_scrape/` file count: `0`
- final validation may be rerun: `YES`
