# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| Final validation allowed emptying | `KNOWLEDGE_SCRAPE_FINAL_VALIDATION_REPORT.md` classified `READY_TO_EMPTY_KNOWLEDGE_SCRAPE` |
| A backup of the current folder shell was created before deletion | `Copy-Item knowledge_scrape -> 99_BACKUPS/knowledge_scrape_pre_empty/20260512_150034/knowledge_scrape` succeeded and `BACKUP_EXISTS=True` |
| `99_BACKUPS` is ignored by Git | `git check-ignore -v 99_BACKUPS/knowledge_scrape_pre_empty/testprobe` matched `.gitignore:65:99_BACKUPS/*` |
| `knowledge_scrape/` was removed from the live repo tree | `Test-Path knowledge_scrape` returned `False` after removal |
| No required routing surface depends on `knowledge_scrape/` | `rg -n "knowledge_scrape"` on `START_HERE_FOR_AI_AGENTS.md`, `00_CODEX_START/TASK_ROUTER.md`, `10_KNOWLEDGE_BASE/INDEX.md`, `10_KNOWLEDGE_BASE/retrieval_indexes/MASTER_KNOWLEDGE_INDEX.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and `AGENTS.md` showed only retired-folder notices or historical references |
| Canonical migrated files still exist | direct existence checks passed for source-registry files, migration ledger, migration status, final validation report, script drain record, and quarantine index |
| Public payload surfaces do not include raw quarantine or rejected content | `rg -n "knowledge_scrape_quarantine|rejected_low_value" 17_RELEASE_BUILD 23_PACKAGE_PROFILES 24_FAB_PROFILES` returned no hits |
| No KiCad design files changed in this task | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` still showed only the preexisting dirty schematic path |
