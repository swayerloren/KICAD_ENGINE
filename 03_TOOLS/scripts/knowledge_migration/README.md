# Knowledge Scrape Migration Controller

Status: `DRY_RUN_FIRST`

This tool layer drains `knowledge_scrape/` into the existing canonical KiCad
Engine folders. It is not a replacement knowledge system. Its job is to:

1. inventory every file under `knowledge_scrape/`
2. classify each file into a canonical destination/action
3. maintain a migration ledger that later prompts can continue from
4. move items safely when explicitly told to apply moves
5. prove when `knowledge_scrape/` is empty and removable

## Scripts

- `inventory_knowledge_scrape.py`
  Creates the source-file inventory CSV.
- `classify_knowledge_scrape_items.py`
  Converts the inventory into the migration ledger, destination map, and status
  report.
- `move_knowledge_item.py`
  Applies one ledger move at a time. Dry-run by default.
- `validate_knowledge_scrape_empty.py`
  Confirms whether any files or non-empty folders remain under
  `knowledge_scrape/`.
- `rebuild_knowledge_indexes.py`
  Rebuilds repo/memory/history/AI-quality indexes after migration steps.

## Required Outputs

- `05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv`
- `05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`
- `05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
- `05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`

## Workflow

1. Run inventory:

```powershell
python 03_TOOLS\scripts\knowledge_migration\inventory_knowledge_scrape.py `
  --repo-root . `
  --source-root knowledge_scrape `
  --output 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv
```

2. Classify into the ledger:

```powershell
python 03_TOOLS\scripts\knowledge_migration\classify_knowledge_scrape_items.py `
  --repo-root . `
  --source-root knowledge_scrape `
  --inventory 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv `
  --config 03_TOOLS\scripts\knowledge_migration\knowledge_migration_config.json `
  --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv `
  --destination-map 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md `
  --status 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md
```

3. Review the ledger. Do not move files blindly.

4. Apply an approved move:

```powershell
python 03_TOOLS\scripts\knowledge_migration\move_knowledge_item.py `
  --repo-root . `
  --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv `
  --original-path knowledge_scrape\_logs\classify_copy_log.csv `
  --apply
```

5. Validate emptiness only after moves are complete:

```powershell
python 03_TOOLS\scripts\knowledge_migration\validate_knowledge_scrape_empty.py `
  --repo-root . `
  --source-root knowledge_scrape
```

6. Rebuild indexes after migration work:

```powershell
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .
```

## Safety Rules

- Dry-run first.
- Do not copy a source file and leave the original behind.
- Use the ledger as the source of truth for migration status.
- Treat raw webpage/article captures as license-sensitive until proven safe.
- Route unclear-license or low-value content out of `knowledge_scrape/`, not
  back into another staging folder.
- Do not edit KiCad design files from this workflow.

## Legacy Script Reconciliation

The old `knowledge_scrape\_scripts\` PowerShell pipeline is no longer part of
the live routing path. During the final drain on `2026-05-12`, the remaining
`_scripts` files were inspected, classified as obsolete legacy scrape tooling,
and moved to history-only storage:

- moved script bodies now live in
  `02_HISTORY\knowledge_scrape_migration\obsolete_scripts\`
- their ledger rows are marked `MOVE_AS_HISTORY_ONLY`
- canonical Python replacements or retirement notes are documented in
  `SCRIPT_MIGRATION_NOTES.md`

Use the active Python migration/indexing tools in this folder instead of trying
to revive the legacy PowerShell scrape pipeline.
