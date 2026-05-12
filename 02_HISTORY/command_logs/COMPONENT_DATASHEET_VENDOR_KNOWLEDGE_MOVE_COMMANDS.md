# Component / Datasheet / Vendor Knowledge Move Commands

## Commands Run

1. Inspected source folders, destination surfaces, ledger rows, and migration config.
2. Patched `03_TOOLS/scripts/knowledge_migration/knowledge_migration_config.json`.
3. Created canonical datasheet, component, vendor, footprint-gap, and CAD-model docs.
4. Ran a ledger-driven apply script to:
   - retarget `596` ledger rows
   - move files with `git mv` where tracked
   - move untracked files with filesystem moves
   - prune emptied source folders
   - mark all target rows `MOVED_VALIDATED`
5. Regenerated:
   - `KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
   - `KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
6. Validated JSON parsing and CSV header readability.
7. Ran:
   - `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
8. Checked:
   - target source folders removed
   - no new KiCad design-file changes

## Key Results

- `MOVE_AS_HISTORY_ONLY = 221`
- `MOVE_TO_LICENSE_QUARANTINE = 375`
- remaining `knowledge_scrape` file count: `1109`
