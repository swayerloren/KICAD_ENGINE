# Knowledge Scrape Final Validation Rerun Commands

## Commands Run

- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `Get-Content` review of:
  - `START_HERE_FOR_AI_AGENTS.md`
  - `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_SCRIPT_DRAIN_REPORT.md`
  - `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
  - `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_POST_MIGRATION_INDEX_REPORT.md`
  - `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_REMAINING_REFERENCE_AUDIT.md`
  - `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_EMPTYING_APPROVAL_CHECKLIST.md`
  - prior `KNOWLEDGE_SCRAPE_FINAL_VALIDATION_REPORT.md`
- `python 03_TOOLS/scripts/knowledge_migration/validate_knowledge_scrape_empty.py --repo-root .`
- Python one-off ledger/source-registry/destination validation checks
- `rg -n "knowledge_scrape"` on startup/router/README surfaces
- `rg -n "knowledge_scrape_quarantine|rejected_low_value" 17_RELEASE_BUILD 23_PACKAGE_PROFILES 24_FAB_PROFILES`
- `Get-FileHash` for live `.kicad_sch`, `.kicad_pcb`, and `.kicad_pro`
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
- `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-12_knowledge_scrape_final_validation_rerun_task_contract.json`
- `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 02_HISTORY/sessions/2026-05-12_knowledge_scrape_final_validation_rerun_task_contract.json --output 02_HISTORY/sessions/2026-05-12_knowledge_scrape_final_validation_rerun_task_contract_report.md`
- `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
