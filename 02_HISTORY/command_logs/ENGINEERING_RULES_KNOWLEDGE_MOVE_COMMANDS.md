# Engineering Rules Knowledge Move Commands

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
# Startup and routing
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content "FOR CHAT GPT.MD"
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 03_TOOLS\scripts\knowledge_migration\README.md
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv -TotalCount 40
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md

# Source-folder triage
Get-ChildItem knowledge_scrape\00_engineering_rules -Recurse -File
Get-ChildItem knowledge_scrape\07_usb_c_high_speed_esd -Recurse -File
Get-ChildItem knowledge_scrape\08_power_buck_regulators -Recurse -File
Get-ChildItem knowledge_scrape\09_pcb_layout_grounding_emi_si -Recurse -File
Get-ChildItem knowledge_scrape\20_manufacturer_layout_guides -Recurse -File
Get-ChildItem knowledge_scrape\23_rf_wifi_antenna_layout -Recurse -File
Get-ChildItem knowledge_scrape\24_power_integrity_decoupling -Recurse -File
Get-ChildItem knowledge_scrape\25_signal_integrity_high_speed -Recurse -File
Get-ChildItem knowledge_scrape\26_thermal_mechanical_enclosure -Recurse -File
Get-ChildItem knowledge_scrape\27_test_debug_validation -Recurse -File
rg -n "url_009659|url_009667|url_009899|url_009900|url_009901|url_010082|url_010083|url_009915|url_009918|url_000005|url_004540|url_006903" 10_KNOWLEDGE_BASE\source_registry\SOURCE_REGISTRY.csv

# Canonical rule/checklist/doc creation
New-Item -ItemType Directory -Force -Path 10_KNOWLEDGE_BASE\summaries,10_KNOWLEDGE_BASE\pcb_layout,10_KNOWLEDGE_BASE\usb_c,10_KNOWLEDGE_BASE\power_integrity,10_KNOWLEDGE_BASE\rf_wifi,10_KNOWLEDGE_BASE\thermal_mechanical
apply_patch
apply_patch
apply_patch
apply_patch

# Controller alignment and actual move apply
apply_patch
@'...target-folder batch move script...'@ | python -
@'...migration status rebuild script...'@ | python -

# Validation
python 03_TOOLS\scripts\knowledge_migration\validate_knowledge_scrape_empty.py --repo-root . --source-root knowledge_scrape
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
rg -n "Source Registry References|url_" 09_ACCURACY_ENGINE\pcb_rules 09_ACCURACY_ENGINE\schematic_rules 09_ACCURACY_ENGINE\checklists 10_KNOWLEDGE_BASE\summaries 10_KNOWLEDGE_BASE\pcb_layout 10_KNOWLEDGE_BASE\usb_c 10_KNOWLEDGE_BASE\power_integrity 10_KNOWLEDGE_BASE\rf_wifi 10_KNOWLEDGE_BASE\thermal_mechanical
rg -n "09_ACCURACY_ENGINE/.+rules/.+\\.md|34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md" 09_ACCURACY_ENGINE\checklists
@'...target-row/action-count script...'@ | python -
@'...hash proof script...'@ | python -

# Closeout and index rebuild
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-11_engineering_rules_knowledge_move_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-11_engineering_rules_knowledge_move_task_contract.json --output 02_HISTORY\sessions\2026-05-11_engineering_rules_knowledge_move_task_contract_report.md
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .
```
