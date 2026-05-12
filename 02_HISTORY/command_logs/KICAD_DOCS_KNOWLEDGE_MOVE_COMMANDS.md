# KiCad Docs Knowledge Move Commands

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
# Read migration inputs and inspect source folders
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content 03_TOOLS\scripts\knowledge_migration\README.md
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv -TotalCount 40
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md
Get-ChildItem knowledge_scrape\01_kicad_core -File -Recurse
Get-ChildItem knowledge_scrape\02_kicad_python_api -File -Recurse
Get-ChildItem knowledge_scrape\03_kicad_file_formats -File -Recurse
Get-ChildItem knowledge_scrape\04_kicad_libraries_symbols_footprints -File -Recurse

# Inspect current destination surfaces and representative source pages
Get-Content 03_TOOLS\scripts\kicad_api\README.md
Get-Content 11_LIBRARY_FACTORY\README.md
Get-Content 09_ACCURACY_ENGINE\verification_rules\ERC_DRC_REQUIRED_RULES.md
Get-Content 09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_ANNOTATION_RULES.md
Get-Content 09_ACCURACY_ENGINE\schematic_rules\NATIVE_ANNOTATION_REQUIRED_RULES.md
Get-Content 09_ACCURACY_ENGINE\pcb_rules\FOOTPRINT_SELECTION_RULES.md
Get-Content 03_TOOLS\kicad\KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md
Get-Content knowledge_scrape\03_kicad_file_formats\url_000018--dev-docs.kicad.org-en-file-formats-sexpr-intro-index.html.md
Get-Content knowledge_scrape\03_kicad_file_formats\url_000019--dev-docs.kicad.org-en-file-formats-sexpr-pcb-index.html.md
Get-Content knowledge_scrape\03_kicad_file_formats\url_000020--dev-docs.kicad.org-en-file-formats-sexpr-schematic-index.html.md
Get-Content knowledge_scrape\04_kicad_libraries_symbols_footprints\url_007038--kicad.org-libraries-klc.md

# Create canonical docs and helper surfaces
apply_patch

# Reclassify 01-04 source folders for quarantine/history movement
apply_patch
python 03_TOOLS\scripts\knowledge_migration\classify_knowledge_scrape_items.py --repo-root . --source-root knowledge_scrape --inventory 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv --config 03_TOOLS\scripts\knowledge_migration\knowledge_migration_config.json --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv --destination-map 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md --status 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md

# Apply all target moves for folders 01-04
@'...batch move script...'@ | python -

# Post-move report/status/index refresh
@'...post-move ledger/status/master-index update script...'@ | python -

# Validation
python -m py_compile 03_TOOLS\scripts\kicad_api\safe_pcbnew_helpers.py
rg -n "url_00|Source Registry References" 10_KNOWLEDGE_BASE\kicad_core 10_KNOWLEDGE_BASE\kicad_python_api 10_KNOWLEDGE_BASE\kicad_file_formats 10_KNOWLEDGE_BASE\kicad_libraries
Get-ChildItem knowledge_scrape -File -Recurse | Measure-Object
Get-ChildItem knowledge_scrape -Directory
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PROJECT_STATE.json -TotalCount 80
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'

# Closeout and index rebuild
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-11_kicad_docs_knowledge_move_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-11_kicad_docs_knowledge_move_task_contract.json --output 02_HISTORY\sessions\2026-05-11_kicad_docs_knowledge_move_task_contract_report.md
python 03_TOOLS\scripts\memory_history\create_issue_log.py --repo-root . --scope global --title "Remaining knowledge_scrape migration after KiCad docs move" --summary "knowledge_scrape folders 01 through 04 are drained, but remaining technical category folders still require migration phases under the shared ledger." --details "Remaining knowledge_scrape file count after this phase is 1854. Future migration prompts should continue from 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv and 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md." --status OPEN --source KICAD_DOCS_KNOWLEDGE_MOVE
python 03_TOOLS\scripts\memory_history\create_failed_attempt.py --repo-root . --scope global --title "KiCad docs move closeout argument validation mismatch" --summary "Initial AI-quality closeout command batch used unsupported claim-status values and out-of-range scorecard subscores." --details "The migration itself succeeded. The failed attempt was limited to closeout script argument formatting. The batch was rerun with repo-accepted claim-status values and 0-20/0-15/0-10 subscore ranges." --status RESOLVED --source KICAD_DOCS_KNOWLEDGE_MOVE
python 03_TOOLS\scripts\ai_quality\create_ai_self_review.py --repo-root . --scope global --title "KiCad Docs Knowledge Move Self Review" --summary "Moved KiCad documentation scrape content out of knowledge_scrape, created canonical normalized docs, and quarantined raw captures with license caution." --details "Strengths: complete drain of folders 01 through 04 and canonical documentation creation. Risk: normalized summaries are condensed from scraped sources and should continue to rely on source registry references rather than raw public redistribution." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "05_OUTPUTS/release_readiness/KICAD_DOCS_KNOWLEDGE_MOVE_REPORT.md;05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv"
python 03_TOOLS\scripts\ai_quality\create_response_scorecard.py --repo-root . --scope global --title "KiCad Docs Knowledge Move Scorecard" --summary "Migration phase completed with actual file movement, canonical doc creation, and ledger updates." --details "The task delivered file movement instead of reports-only output and preserved the no-KiCad-design-edit constraint." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "05_OUTPUTS/release_readiness/KICAD_DOCS_KNOWLEDGE_MOVE_REPORT.md;05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md" --overall-score 95 --evidence-support 19 --kicad-correctness 20 --datasheet-accuracy 14 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 9 --usefulness 10
python 03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py --repo-root . --scope global --title "KiCad Docs Knowledge Move Claim Evidence Matrix" --summary "Evidence matrix for the 01 through 04 knowledge_scrape drain." --details "Claim 1: 649 files moved from the four target folders. Claim 2: source folders 01 through 04 no longer exist. Claim 3: normalized docs created under 10_KNOWLEDGE_BASE. Claim 4: no KiCad design-file state changed." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "05_OUTPUTS/release_readiness/KICAD_DOCS_KNOWLEDGE_MOVE_REPORT.md;05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md;04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LIVE_PROJECT_STATE.json"
python 03_TOOLS\scripts\ai_quality\create_uncertainty_log.py --repo-root . --scope global --title "KiCad Docs Knowledge Move Uncertainty Log" --summary "The migration counts are verified, but the normalized docs remain summaries rather than exhaustive upstream reproductions." --details "Uncertainty is limited to interpretation scope, not move completion. Raw captures were quarantined instead of promoted to canonical knowledge to reduce license risk and avoid treating scraped text as primary source of truth." --severity LOW --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "10_KNOWLEDGE_BASE/kicad_core/README.md;10_KNOWLEDGE_BASE/kicad_python_api/README.md;21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/"
python 03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py --repo-root . --scope global --title "KiCad Docs Knowledge Move Hallucination Risk Log" --summary "Low hallucination risk because this phase is dominated by filesystem evidence and counted moves rather than unsourced engineering claims." --details "Primary risk area is overclaiming what the normalized KiCad summaries prove. The canonical docs explicitly reference source-registry entries and keep raw scraped material quarantined." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv;10_KNOWLEDGE_BASE/retrieval_indexes/MASTER_KNOWLEDGE_INDEX.md"
python 03_TOOLS\scripts\memory_history\build_history_index.py --repo-root .
python 03_TOOLS\scripts\memory_history\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
```

## Key Outcomes

- Source files moved from the four target folders: `649`
- Quarantine moves: `641`
- History/archive moves: `8`
- Four target source folders removed from `knowledge_scrape/`
- Canonical KiCad docs added under `10_KNOWLEDGE_BASE/`
- No KiCad design-file state changed during this task
