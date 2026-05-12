# AI Entrypoint / Retrieval / Tool Knowledge Move Commands

Date: `2026-05-11`

## Key Commands

1. Read startup, router, migration-controller, and source-folder files with
   `Get-Content`.
2. Enumerated target-folder files with `Get-ChildItem`.
3. Created canonical calculator folders with `New-Item -ItemType Directory`.
4. Updated targeted ledger rows with an inline Python CSV/JSON rewrite.
5. Applied actual file moves with:
   `python 03_TOOLS/scripts/knowledge_migration/move_knowledge_item.py --apply`
6. Compiled calculator scripts with:
   `python -m py_compile 03_TOOLS/calculators/*.py`
7. Validated remaining `knowledge_scrape` state with:
   `python 03_TOOLS/scripts/knowledge_migration/validate_knowledge_scrape_empty.py`
8. Refreshed destination map and migration status with an inline Python
   controller-output rewrite.
9. Checked KiCad design-file diff state with:
   `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
10. Validated the execution contract with:
   `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py`
11. Wrote the execution-contract report with:
   `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py`
12. Rebuilt repo, memory, history, AI-quality, and known-problem indexes with:
   `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
