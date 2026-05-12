# Knowledge Scrape Script Drain Commands

## Commands Run

- startup and migration-status reads under `00_CODEX_START/`, `05_OUTPUTS/release_readiness/`, and `03_TOOLS/scripts/knowledge_migration/`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `Get-ChildItem knowledge_scrape -Recurse -Force`
- `Get-Content` review of each legacy `_scripts/*.ps1` file
- `Move-Item` of the `7` legacy `_scripts` PowerShell files into `02_HISTORY/knowledge_scrape_migration/obsolete_scripts/`
- `Remove-Item knowledge_scrape\\_scripts`
- `python 03_TOOLS/scripts/knowledge_migration/validate_knowledge_scrape_empty.py --repo-root .`
- Python one-off ledger reconciliation / verification checks
- `rg -n "knowledge_scrape" ...` on routing and retrieval-index surfaces
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
