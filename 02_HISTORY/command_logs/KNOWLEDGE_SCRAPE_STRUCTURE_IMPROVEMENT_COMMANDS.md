# Knowledge Scrape Structure Improvement Commands

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
# Startup, routing, and repo-context inspection
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content "FOR CHAT GPT.MD"
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
Get-Content 00_CODEX_START\USER_CORRECTION_CAPTURE_RULES.md
Get-Content 00_CODEX_START\FAILED_ATTEMPT_CAPTURE_RULES.md
Get-Content 00_CODEX_START\ISSUE_TRACKING_RULES.md
Get-Content 00_CODEX_START\AI_SELF_REVIEW_RULES.md
Get-Content 00_CODEX_START\AI_TRUTHFULNESS_SCORING.md
Get-Content 00_CODEX_START\AI_HALLUCINATION_RISK_RULES.md
Get-Content 00_CODEX_START\AI_RESPONSE_QUALITY_GATE.md
Get-Content 00_CODEX_START\AI_EVIDENCE_REQUIREMENTS.md
Get-Content 00_CODEX_START\AI_UNCERTAINTY_DISCLOSURE_RULES.md
Get-Content 00_CODEX_START\AI_ENGINEERING_CLAIM_RULES.md
Get-Content 00_CODEX_START\AI_CLOSEOUT_SCORECARD_RULES.md
Get-Content 00_CODEX_START\TASK_ROUTER.md
Get-Content 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md
Get-Content 00_CODEX_START\TASK_TYPE_TO_ALLOWED_ACTIONS.md
Get-Content 00_CODEX_START\TASK_TYPE_TO_BLOCKERS.md
Get-Content 00_CODEX_START\TASK_TYPE_TO_OUTPUTS.md
Get-Content 00_CODEX_START\KICAD_ENGINE_CRITICAL_PATH.md
Get-Content 00_CODEX_START\AI_AGENT_FAST_CONTEXT.md
Get-Content 03_TOOLS\scripts\execution_contract\README.md
git status --short

# Task contract
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-10_knowledge_scrape_structure_improvement_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-10_knowledge_scrape_structure_improvement_task_contract.json --output 02_HISTORY\sessions\2026-05-10_knowledge_scrape_structure_improvement_task_contract_report.md

# knowledge_scrape audit and recovery
Get-Content knowledge_scrape\README.md
Get-Content knowledge_scrape\INDEX.md
Get-Content knowledge_scrape\URL_INDEX.md
Get-Content knowledge_scrape\FINAL_KNOWLEDGE_SCRAPE_REPORT.md
Get-Content knowledge_scrape\_scripts\02_build_url_registry.ps1
Get-Content knowledge_scrape\_scripts\06_build_category_indexes.ps1
@'
# Inline Python recovery pass:
# - scanned knowledge_scrape/91_rejected_low_value
# - matched recoverable files by source/domain/topic signals
# - moved useful files into category folders
# - updated frontmatter knowledge_category / notes
# - updated URL_INDEX.csv and URL_INDEX.json
# - wrote knowledge_scrape/_logs/rejected_recovery_audit.json
# - wrote knowledge_scrape/_logs/rejected_recovery_audit.csv
'@ | python -
powershell -NoProfile -ExecutionPolicy Bypass -File knowledge_scrape\_scripts\06_build_category_indexes.ps1

# Post-recovery validation and stats
Get-Content -Raw knowledge_scrape\_logs\rejected_recovery_audit.json
Get-Content -Raw knowledge_scrape\URL_INDEX.md
Get-Content -Raw knowledge_scrape\FINAL_KNOWLEDGE_SCRAPE_REPORT.md
Get-Content -Raw README_GPT.md
Get-Content -Raw "FOR CHAT GPT.MD"
Get-Content -Raw CLAUDE.md
@'
# Inline Python stats checks against URL_INDEX.csv, MANIFEST.json,
# and knowledge_scrape/_logs/rejected_recovery_audit.json
'@ | python -

# History and AI-quality closeout records
python 03_TOOLS\scripts\memory_history\create_session_log.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Session" --summary "Recovered useful files from knowledge_scrape/91_rejected_low_value, added source-of-truth routing layers, refreshed registry/report docs, and updated repo handoff guidance without touching KiCad project files." --details "The session audited rejected knowledge_scrape content, moved 660 useful files into the correct topic folders, created the 00_source_of_truth, 00_engineering_rules, and 00_retrieval_indexes layers, refreshed URL_INDEX.md, MANIFEST.json, FINAL_KNOWLEDGE_SCRAPE_REPORT.md, and STRUCTURE_IMPROVEMENT_REPORT.md, and updated repo-root agent guidance for future Codex/Claude sessions. No active KiCad design files or C:\KICAD_SCRAPE files were modified." --status COMPLETED --source user_request
python 03_TOOLS\scripts\memory_history\create_issue_log.py --repo-root . --scope global --title "knowledge_scrape Remaining Rescrape And Cleanup Gaps" --summary "The structure pass improved routing and recovery, but linked rows still need cleanup and some useful source classes are still weak or incomplete." --details "Remaining concerns include 496 linked URL rows still marked needs_rescrape, 251 linked rows still marked rejected, 57 cleaned Markdown files with residual raw HTML, 3 PDF extraction failures, and rejected EEVBlog/MPS captures that are not strong engineering evidence. Future work should prioritize better official captures for blocked pages and real thread-level peer-review content where needed." --status OPEN --source knowledge_scrape/STRUCTURE_IMPROVEMENT_REPORT.md
python 03_TOOLS\scripts\ai_quality\create_ai_self_review.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Self Review" --summary "The structure-improvement pass completed safely, improved knowledge routing materially, and kept all changes outside active KiCad design files." --details "The session recovered 660 useful files from the rejected folder, created source-of-truth and retrieval routing layers, refreshed registry/report surfaces, and updated repo handoff docs. The remaining weakness is source-quality heterogeneity inside the scrape corpus, so the final docs continue to require URL_INDEX checks and original-PDF verification for exact engineering decisions." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "knowledge_scrape/_logs/rejected_recovery_audit.json; knowledge_scrape/URL_INDEX.csv; knowledge_scrape/URL_INDEX.md; knowledge_scrape/FINAL_KNOWLEDGE_SCRAPE_REPORT.md; knowledge_scrape/STRUCTURE_IMPROVEMENT_REPORT.md; AGENTS.md; CLAUDE.md" --issue "The scrape corpus is more usable now, but future engineering work still needs row-level source validation and original-PDF checks."
python 03_TOOLS\scripts\ai_quality\create_response_scorecard.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Scorecard" --summary "The requested structural recovery and routing improvements were completed, and the final docs now point future agents toward higher-trust local sources first." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "The recovery audit, registry, manifest, and report files now agree on the recovered-count and current category counts." --issue "Recovered files still vary in trust and scrape quality, so the corpus is safer than before but not self-verifying." --overall-score 94 --evidence-support 19 --kicad-correctness 18 --datasheet-accuracy 13 --safety-compliance 15 --memory-routing 9 --uncertainty-disclosure 10 --usefulness 10
python 03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Claim Evidence Matrix" --summary "knowledge_scrape is now a usable local knowledge-routing layer with source-of-truth routing docs, recovered topic content, and refreshed registry/report surfaces." --details "This claim is supported by the rejected recovery audit, the new 00_* routing folders, the refreshed registry summary, the refreshed manifest, and the updated agent handoff docs." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "knowledge_scrape/_logs/rejected_recovery_audit.json; knowledge_scrape/00_source_of_truth/; knowledge_scrape/00_engineering_rules/; knowledge_scrape/00_retrieval_indexes/; knowledge_scrape/URL_INDEX.md; knowledge_scrape/MANIFEST.json; README_GPT.md; FOR CHAT GPT.MD; CLAUDE.md" --issue "Usable routing does not make every recovered source authoritative; row-level validation still matters."
python 03_TOOLS\scripts\ai_quality\create_uncertainty_log.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Uncertainty Log" --summary "Recovered scrape files are more discoverable now, but not all of them are equally trustworthy or equally clean." --details "Recovered rows can still carry needs_rescrape or rejected scrape status, extracted PDF Markdown remains secondary to original PDFs, some peer-review sources are index pages rather than thread-level evidence, and blocked-site captures remain poor inputs until replaced. The routing docs explicitly preserve those boundaries." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "knowledge_scrape/URL_INDEX.csv; knowledge_scrape/URL_INDEX.md; knowledge_scrape/00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md; knowledge_scrape/STRUCTURE_IMPROVEMENT_REPORT.md" --issue "Future engineering decisions still need URL_INDEX row checks and original-source confirmation for exact values or drawings."
python 03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py --repo-root . --scope global --title "Knowledge Scrape Structure Improvement Hallucination Risk Log" --summary "The main risk is over-trusting recovered scrape material after the folder structure improves." --details "This session reduces that risk by requiring URL_INDEX-first lookup, source-of-truth routing, original-PDF priority for exact package/pin/layout details, and explicit low-trust handling for rejected or low-value captures. Residual risk remains if a future agent cites recovered Markdown without checking the registry row and the original source tier." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "AGENTS.md; CLAUDE.md; knowledge_scrape/00_ai_entrypoints/AI_START_HERE.md; knowledge_scrape/00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md; knowledge_scrape/URL_INDEX.md" --issue "Folder cleanup improves retrieval, not truth by itself."
python 03_TOOLS\scripts\memory_history\create_failed_attempt.py --repo-root . --scope global --title "knowledge_scrape Closeout Prep Lookup Misses" --summary "A few exploratory closeout commands used the wrong assumption about UTF-8 BOM handling or expected helper-file locations, but the task work was not blocked." --details "The first before/after stats read of rejected_recovery_audit.json used plain UTF-8 instead of UTF-8-SIG, one inspection looked for a non-existent 02_HISTORY/claims folder instead of claim_evidence_matrices, and one sample self-review path used the wrong filename pattern. Each issue was corrected immediately and did not affect the recovery, doc updates, or final counts." --status RESOLVED --source shell_exploration

# Memory, history, and index rebuild
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "knowledge_scrape structure improvement" --apply
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE

# Safety verification
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git diff --cached --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

## Closeout Results

- Task contract validation: `PASS`
- Prompt counter: `0 -> 1`
- Maintenance due after increment: `NO`
- Repo, memory, history, AI-quality, and current-known-problems indexes rebuilt
- No tracked or staged `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files changed
