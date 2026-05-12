# Knowledge Scrape Unsorted / Rejected Drain Commands

Date: `2026-05-11`

## Key Commands

1. Read startup, router, migration-controller, and classification files with
   `Get-Content`.
2. Enumerated `knowledge_scrape/90_unsorted_review` and
   `knowledge_scrape/91_rejected_low_value` with `Get-ChildItem`.
3. Retargeted migration-config rules for the final 90/91 drain with a config
   patch.
4. Rewrote the targeted ledger rows with an inline Python CSV update.
5. Applied the actual file moves in bulk with an inline Python move pass using
   `git mv` when tracked and filesystem moves otherwise.
6. Confirmed source-folder removal with `Test-Path`.
7. Validated remaining `knowledge_scrape` state with:
   `python 03_TOOLS/scripts/knowledge_migration/validate_knowledge_scrape_empty.py`
8. Refreshed the destination map and migration status with an inline Python
   controller-output rewrite.
9. Checked targeted ledger counts and validation status with inline Python.
10. Checked KiCad design-file diff state with:
    `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
11. Validated the execution contract with:
    `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py`
12. Wrote the execution-contract report with:
    `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py`
13. Rebuilt repo, memory, history, AI-quality, and known-problem indexes with:
    `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
