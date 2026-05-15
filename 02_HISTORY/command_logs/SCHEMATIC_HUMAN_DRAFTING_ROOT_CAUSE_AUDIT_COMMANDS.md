# Schematic Human Drafting Root Cause Audit Commands

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "schematic human drafting root cause audit" --apply
Get-Content -Path 'START_HERE_FOR_AI_AGENTS.md' -TotalCount 200
Get-Content -Path 'AGENTS.md' -TotalCount 400
Get-Content -Path 'README_GPT.md' -TotalCount 260
Get-Content -Path 'FOR CHAT GPT.MD' -TotalCount 260
Get-Content -Path '00_CODEX_START/START_HERE.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/AI_AGENT_FAST_CONTEXT.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_ROUTER.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/CURRENT_PROJECT.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/PROMPT_COUNTER_RULES.md' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/execution_contract/README.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/MEMORY_AND_HISTORY_ROUTING_RULES.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/README.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/README_FOR_CODEX_AND_CLAUDE.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_WIRING_VS_LABEL_RULES.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_BLOCK_LAYOUT_RULES.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_VISUAL_AUDIT_RULES.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_COMMON_FAILURES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/FUNCTIONAL_BLOCK_SPACING_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/MCU_BOOT_STRAP_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/DECOUPLING_SCHEMATIC_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/BUCK_REGULATOR_SCHEMATIC_RULES.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md' -TotalCount 260
Get-Content -Path '09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/README.md' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/audit_wire_vs_label_balance.py' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/audit_schematic_block_layout.py' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/audit_schematic_text_overlaps.py' -TotalCount 260
Get-Content -Path '03_TOOLS/scripts/schematic_quality/schematic_quality_common.py' -TotalCount 260
Get-Content -Path '.prompts/README.md' -TotalCount 260
Get-Content -Path '.prompts/shared/HUMAN_DRAFTING_MODE.md' -TotalCount 260
Get-Content -Path '.prompts/codex/05_PLAN_SCHEMATIC.md' -TotalCount 260
Get-Content -Path '.prompts/codex/06_REVIEW_SCHEMATIC.md' -TotalCount 260
Get-Content -Path '.prompts/claude/05_PLAN_SCHEMATIC.md' -TotalCount 260
Get-Content -Path '.prompts/claude/06_REVIEW_SCHEMATIC.md' -TotalCount 260
Get-Content -Path '.prompts/kicad_pipeline/02_schematic_visual_cleanup.md' -TotalCount 260
Get-Content -Path '.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md' -TotalCount 260
Get-Content -Path '.prompts/kicad_pipeline/03_schematic_visual_repair.md' -TotalCount 260
Get-Content -Path '.prompts/kicad_pipeline/03_schematic_electrical_review.md' -TotalCount 260
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md' -TotalCount 320
Get-ChildItem -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports' | Sort-Object LastWriteTime -Descending | Select-Object -First 40 Name,LastWriteTime
rg -n "LOCAL_WIRE|NET_LABEL|orientation|rotate|flip|graphic line|visual pass|PASS_WITH_MINOR_WARNINGS|AUTOMATED_CROP_PASS_ONLY|STATUS_LED|ESP_EN|BOOT0" 34_SCHEMATIC_QUALITY_ENGINE 09_ACCURACY_ENGINE/schematic_rules 03_TOOLS/scripts/schematic_quality .prompts 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports 05_OUTPUTS/release_readiness -g "*.md" -g "*.py" -g "*.json"
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_HUMAN_DRAFTING_CLEANUP_REPORT.md' -TotalCount 220
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_STRICT_SCHEMATIC_PRESENTATION_REVIEW.md' -TotalCount 260
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_LAYOUT_LESSONS_AND_RULES.md' -TotalCount 220
Get-ChildItem -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality' -Directory | Sort-Object Name | Select-Object -Last 3 -ExpandProperty FullName
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/schematic_quality_report.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/wire_vs_label.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/block_layout.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/text_overlaps.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/schematic_quality_report.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/wire_vs_label.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/block_layout.md' -TotalCount 240
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/readability/schematic_readability_score.md' -TotalCount 240
Get-ChildItem -Path '03_TOOLS/scripts/execution_contract'
Get-Content -Path '02_HISTORY/README.md' -TotalCount 220
Get-ChildItem -Path '02_HISTORY' -Directory | Select-Object -ExpandProperty Name
Get-Content -Path '26_AGENT_QUALITY/AI_SELF_REVIEW_RULES.md' -TotalCount 260
Get-Content -Path '26_AGENT_QUALITY/AI_RESPONSE_QUALITY_GATE.md' -TotalCount 260
Get-Content -Path '26_AGENT_QUALITY/templates/AI_RESPONSE_SCORECARD_TEMPLATE.md' -TotalCount 260
Get-Content -Path '26_AGENT_QUALITY/templates/CLAIM_EVIDENCE_MATRIX_TEMPLATE.md' -TotalCount 260
Get-Content -Path '26_AGENT_QUALITY/templates/UNCERTAINTY_LOG_TEMPLATE.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/FAILED_ATTEMPT_CAPTURE_RULES.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/ISSUE_TRACKING_RULES.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/AI_CLOSEOUT_SCORECARD_RULES.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/USER_CORRECTION_CAPTURE_RULES.md' -TotalCount 220
Get-Content -Path '02_HISTORY/user_corrections/KICAD_ENGINE_AUTOMATED_VISUAL_PASS_USER_CORRECTION.md' -TotalCount 240
Get-ChildItem -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721' -File | Select-Object -ExpandProperty Name
rg -n "PASS_WITH_MINOR_WARNINGS|FINAL_STRICT_PRESENTATION_PASS_WITH_MINOR_WARNINGS|AUTOMATED_CROP_PASS_ONLY|WARN" '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports'
git status --short
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_TASK_CONTRACT.json
python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_TASK_CONTRACT.json --output 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_TASK_CONTRACT_REPORT.md
Test-Path '05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_TASK_CONTRACT_REPORT.md'; Get-Content -Path '05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_TASK_CONTRACT_REPORT.md' -TotalCount 80
git status --short -- '05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT*' '02_HISTORY/sessions/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_SESSION.md' '02_HISTORY/command_logs/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_COMMANDS.md' '02_HISTORY/ai_self_reviews/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_AI_SELF_REVIEW.md' '02_HISTORY/ai_scorecards/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_SCORECARD.md' '02_HISTORY/claim_evidence_matrices/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_CLAIM_EVIDENCE_MATRIX.md' '02_HISTORY/uncertainty_logs/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_UNCERTAINTY_LOG.md' '02_HISTORY/hallucination_risk_logs/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_HALLUCINATION_RISK_LOG.md' '02_HISTORY/issue_logs/SCHEMATIC_HUMAN_DRAFTING_WORKFLOW_REPAIR_GAPS.md' '02_HISTORY/user_corrections/SCHEMATIC_HUMAN_DRAFTING_MANUAL_BASELINE_CORRECTION.md' '02_HISTORY/failed_attempts/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT_FAILED_ATTEMPTS.md'
Get-Content -Path '00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md' -TotalCount 80
rg -n "SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE|SCHEMATIC_HUMAN_DRAFTING_MANUAL_BASELINE_CORRECTION|SCHEMATIC_HUMAN_DRAFTING_WORKFLOW_REPAIR_GAPS" '02_HISTORY/MASTER_HISTORY_INDEX.md' '00_CODEX_START/AI_QUALITY_INDEX.generated.md' '00_CODEX_START/HISTORY_INDEX.generated.md' '00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md'
```

## Notes

- Manual file creation and edits were applied with `apply_patch`.
- Two early file-read guesses failed because I assumed filenames inside a recent `schematic_quality` folder; I corrected that by listing the actual folder contents first. That recovery is recorded in the failed-attempt log.
- Non-destructive index rebuilds and task-contract validation were run during closeout.
- No KiCad design files were edited.
