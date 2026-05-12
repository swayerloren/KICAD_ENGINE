# Knowledge Scrape Migration Controller Commands

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
# Startup and repo routing reads
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content "FOR CHAT GPT.MD"
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 00_CODEX_START\SESSION_START_CHECKLIST.md
Get-Content 00_CODEX_START\STRUCTURE_STANDARD.md
Get-Content 00_CODEX_START\FOLDER_ROUTING_RULES.md
Get-Content 00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md
Get-Content 00_CODEX_START\MEMORY_INDEX.md
Get-Content 00_CODEX_START\HISTORY_INDEX.md
Get-Content 00_CODEX_START\WORKFLOW_RULES.md
Get-Content 00_CODEX_START\SAFETY_RULES.md
Get-Content 00_CODEX_START\CONTROL_PLANES.md
Get-Content 00_CODEX_START\REPO_MAP.md
Get-Content 00_CODEX_START\REPO_STRUCTURE_INDEX.md
Get-Content 00_CODEX_START\TOOL_INDEX.md
Get-Content 00_CODEX_START\PROJECT_INDEX.md
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
Get-Content 00_CODEX_START\SESSION_CLOSEOUT_CHECKLIST.md
Get-Content 00_CODEX_START\LEARNING_LOOP_RULES.md
Get-Content 00_CODEX_START\MEMORY_AND_HISTORY_ROUTING_RULES.md
Get-Content 00_CODEX_START\AI_SELF_REVIEW_RULES.md
Get-Content 00_CODEX_START\AI_RESPONSE_QUALITY_GATE.md
Get-Content 00_CODEX_START\AI_EVIDENCE_REQUIREMENTS.md
Get-Content 00_CODEX_START\AI_CLOSEOUT_SCORECARD_RULES.md
Get-Content knowledge_scrape\00_ai_entrypoints\AI_START_HERE.md
Get-Content knowledge_scrape\INDEX.md
Get-Content knowledge_scrape\URL_INDEX.csv -TotalCount 80

# Structure and baseline inspection
Get-ChildItem -Force 03_TOOLS\scripts | Select-Object Name,Mode
Get-ChildItem -Force 05_OUTPUTS\release_readiness | Select-Object Name,Mode
Get-ChildItem -Recurse -File knowledge_scrape | Measure-Object
Get-ChildItem -Recurse -Directory knowledge_scrape
Get-ChildItem knowledge_scrape -Directory
Get-Content 03_TOOLS\scripts\execution_contract\README.md
Get-Content 02_HISTORY\sessions\2026-05-10_knowledge_scrape_structure_improvement_task_contract.json
Get-Content 02_HISTORY\command_logs\KNOWLEDGE_SCRAPE_STRUCTURE_IMPROVEMENT_COMMANDS.md

# Controller validation and generation
python -m py_compile 03_TOOLS\scripts\knowledge_migration\inventory_knowledge_scrape.py 03_TOOLS\scripts\knowledge_migration\classify_knowledge_scrape_items.py 03_TOOLS\scripts\knowledge_migration\move_knowledge_item.py 03_TOOLS\scripts\knowledge_migration\validate_knowledge_scrape_empty.py 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py
python 03_TOOLS\scripts\knowledge_migration\inventory_knowledge_scrape.py --repo-root . --source-root knowledge_scrape --output 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv
python 03_TOOLS\scripts\knowledge_migration\classify_knowledge_scrape_items.py --repo-root . --source-root knowledge_scrape --inventory 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv --config 03_TOOLS\scripts\knowledge_migration\knowledge_migration_config.json --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv --destination-map 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md --status 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md

# Task contract
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-11_knowledge_scrape_migration_controller_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-11_knowledge_scrape_migration_controller_task_contract.json --output 02_HISTORY\sessions\2026-05-11_knowledge_scrape_migration_controller_task_contract_report.md

# AI-quality and issue records
python 03_TOOLS\scripts\memory_history\create_issue_log.py --repo-root . --scope global --title "Knowledge Scrape Migration Execution Pending" --summary "The migration controller, inventory, and ledger now exist, but no source moves have been applied yet." --details "knowledge_scrape still contains 2546 files. The authoritative next-step inputs are 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv and KNOWLEDGE_SCRAPE_DESTINATION_MAP.md. Future migration prompts should apply ledger-approved moves, quarantine unclear-license captures, archive low-value/history-only content, and then validate knowledge_scrape emptiness." --status OPEN --source "05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md"
python 03_TOOLS\scripts\memory_history\create_failed_attempt.py --repo-root . --scope global --title "Knowledge Scrape Ledger Parallel Classification Race" --summary "The first classify run started before the inventory CSV was fully written because both commands were launched in parallel." --details "The failure produced a file-not-found error for 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv. No source files were moved or modified. The controller was rerun serially: inventory first, classification second, which produced the final 2546-row ledger successfully." --status RESOLVED --source "shell_command parallel execution during this session"
python 03_TOOLS\scripts\ai_quality\create_ai_self_review.py --repo-root . --scope global --title "Knowledge Scrape Migration Controller Self Review" --summary "The controller was created safely and now gives later migration prompts a single authoritative inventory and destination ledger for draining knowledge_scrape." --details "The run created dry-run-first tooling, generated a 2546-file inventory and matching 2546-row ledger, updated handoff/memory notes, and kept all source moves at zero. The main remaining limitation is that actual content movement, normalization, quarantine, and empty-folder cleanup still need later apply-mode prompts." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/knowledge_migration/; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md" --issue "The controller baseline is complete, but knowledge_scrape is not yet drained."
python 03_TOOLS\scripts\ai_quality\create_response_scorecard.py --repo-root . --scope global --title "Knowledge Scrape Migration Controller Scorecard" --summary "The requested migration-controller layer, inventory, ledger, and destination map were created without touching KiCad design files." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "The inventory, ledger, destination map, status report, and contract validation now agree on the 2546-file baseline and zero-move state." --issue "Actual migration application and source drainage still remain." --overall-score 95 --evidence-support 19 --kicad-correctness 20 --datasheet-accuracy 13 --safety-compliance 15 --memory-routing 9 --uncertainty-disclosure 9 --usefulness 10
python 03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py --repo-root . --scope global --title "Knowledge Scrape Migration Controller Claim Evidence Matrix" --summary "A dry-run-first migration controller now exists for draining knowledge_scrape into canonical repo folders, and the initial ledger covers every current source file without applying moves." --details "This claim is supported by the new controller scripts, the generated inventory CSV, the generated migration ledger, the destination map, the migration status report, and the validated DOCS_ONLY task contract." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/knowledge_migration/; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md; 02_HISTORY/sessions/2026-05-11_knowledge_scrape_migration_controller_task_contract.json" --issue "The controller proves readiness to migrate, not completion of the migration itself."
python 03_TOOLS\scripts\ai_quality\create_uncertainty_log.py --repo-root . --scope global --title "Knowledge Scrape Migration Controller Uncertainty Log" --summary "The ledger classification is deterministic and complete, but some future move decisions still need human judgment because license status or value is unclear." --details "The controller marks 285 items for license quarantine and 6 items for explicit human review. Forum captures, standards text, university training material, and some unsorted items should not be normalized into public source-of-truth folders until the next migration step confirms license and value. MOVE_NORMALIZED rows also require a reviewed normalized canonical file during apply mode." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md" --issue "The controller is ready, but not every future move is automatic."
python 03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py --repo-root . --scope global --title "Knowledge Scrape Migration Controller Hallucination Risk Log" --summary "The main risk is over-promoting scraped content into canonical folders without checking license and source quality at move time." --details "This run reduces that risk by forcing every file through an explicit ledger with action, destination, and license-risk fields. Residual risk remains if future migration prompts override MOVE_TO_LICENSE_QUARANTINE, skip MOVE_NORMALIZED review, or treat recovered scrape text as authoritative without using the canonical destination rules." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/knowledge_migration/knowledge_migration_config.json; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md" --issue "Migration quality still depends on future apply-mode discipline."

# Index rebuild
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .

# Final validation
Import-Csv 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv | Group-Object action | Sort-Object Count -Descending | Select-Object Count,Name
Import-Csv 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv | Group-Object license_risk | Sort-Object Count -Descending | Select-Object Count,Name
Import-Csv 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv | Where-Object { $_.moved_yes_no -eq 'YES' } | Measure-Object
Get-ChildItem knowledge_scrape -Directory
Get-ChildItem -Recurse -File knowledge_scrape | Measure-Object
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PROJECT_STATE.json
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git diff --cached --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

## Closeout Results

- Inventory count: `2546`
- Ledger row count: `2546`
- Moved rows: `0`
- Task contract validation: `PASS`
- No KiCad design-file state changed during this task
