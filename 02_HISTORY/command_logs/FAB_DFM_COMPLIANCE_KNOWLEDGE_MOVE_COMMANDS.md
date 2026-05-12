# Fab / DFM / Compliance Knowledge Move Commands

## Commands Run

1. Inspected source folders, destination surfaces, source-registry coverage, and migration config.
2. Patched `03_TOOLS/scripts/knowledge_migration/knowledge_migration_config.json`.
3. Created canonical DFM, assembly, compliance, standards-policy, and export-checklist docs.
4. Ran a ledger-driven apply script to:
   - retarget `64` ledger rows
   - move files with `git mv` where tracked
   - move untracked files with filesystem moves
   - prune emptied source folders
   - mark all target rows `MOVED_VALIDATED`
5. Regenerated:
   - `KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
   - `KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
6. Validated:
   - target source folders removed
   - no new manufacturing outputs
   - no KiCad design-file changes in this task
7. Ran:
   - `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`

## Key Results

- `MOVE_AS_HISTORY_ONLY = 6`
- `MOVE_TO_LICENSE_QUARANTINE = 58`
- remaining `knowledge_scrape` file count: `1045`
