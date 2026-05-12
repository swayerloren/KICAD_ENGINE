# Case Study / Training Knowledge Move Commands

## Commands Run

1. Inspected the six source folders, existing migration config, and destination
   surfaces under `10_KNOWLEDGE_BASE/`, `26_AGENT_QUALITY/`, and
   `09_ACCURACY_ENGINE/verification_rules/`.
2. Created canonical training, peer-review, case-study, and AI-quality docs.
3. Ran a ledger-driven apply script to:
   - retarget `214` ledger rows
   - move raw captures into license quarantine
   - move low-risk metadata into migration history
   - prune emptied source folders
4. Regenerated:
   - `KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
   - `KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
5. Validated:
   - target source folders removed
   - target ledger rows marked `MOVED_VALIDATED`
   - no KiCad design-file changes in this task
6. Ran:
   - `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`

## Key Results

- `MOVE_AS_HISTORY_ONLY = 8`
- `MOVE_TO_LICENSE_QUARANTINE = 206`
- remaining `knowledge_scrape` file count: `831`

