# Knowledge Scrape Emptying Commands

## Commands Run

- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `Get-Content 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_FINAL_VALIDATION_REPORT.md`
- `Test-Path knowledge_scrape`
- `rg -n "99_BACKUPS|knowledge_scrape|gitkeep" ...` on startup/router/handoff surfaces
- `git check-ignore -v 99_BACKUPS/knowledge_scrape_pre_empty/testprobe`
- `Copy-Item knowledge_scrape -> 99_BACKUPS/knowledge_scrape_pre_empty/20260512_150034`
- `Remove-Item knowledge_scrape -Recurse -Force`
- validation checks:
  - `Test-Path knowledge_scrape`
  - `Test-Path 99_BACKUPS/knowledge_scrape_pre_empty/20260512_150034/knowledge_scrape`
  - `rg -n "knowledge_scrape"` on startup/router/README surfaces
  - canonical destination existence checks
  - `rg -n "knowledge_scrape_quarantine|rejected_low_value" 17_RELEASE_BUILD 23_PACKAGE_PROFILES 24_FAB_PROFILES`
  - `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
  - `Get-FileHash` for live `.kicad_sch`, `.kicad_pcb`, and `.kicad_pro`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-12_knowledge_scrape_emptying_task_contract.json`
- `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 02_HISTORY/sessions/2026-05-12_knowledge_scrape_emptying_task_contract.json --output 02_HISTORY/sessions/2026-05-12_knowledge_scrape_emptying_task_contract_report.md`
- `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
