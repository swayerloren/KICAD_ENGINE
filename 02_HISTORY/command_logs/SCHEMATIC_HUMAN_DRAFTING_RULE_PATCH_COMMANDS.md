# Schematic Human Drafting Rule Patch Commands

## Commands Run

```powershell
Get-Content -Path 'START_HERE_FOR_AI_AGENTS.md' -TotalCount 200
Get-Content -Path 'AGENTS.md' -TotalCount 260
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content -Path '00_CODEX_START/TASK_ROUTER.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/CURRENT_PROJECT.md' -TotalCount 200
Get-Content -Path '03_TOOLS/scripts/execution_contract/README.md' -TotalCount 220
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "schematic human drafting rule patch" --apply
Get-Content -Path 'README_GPT.md' -TotalCount 220
Get-Content -Path 'FOR CHAT GPT.MD' -TotalCount 220
Get-Content -Path '00_CODEX_START/START_HERE.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/AI_AGENT_FAST_CONTEXT.md' -TotalCount 220
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md' -TotalCount 260
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md' -TotalCount 320
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md' -TotalCount 320
Get-Content -Path '00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md' -TotalCount 220
Get-Content -Path '05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT.md' -TotalCount 320
Get-Content -Path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md' -TotalCount 320
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/README.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_WIRING_VS_LABEL_RULES.md' -TotalCount 320
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md' -TotalCount 320
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_BLOCK_LAYOUT_RULES.md' -TotalCount 320
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_VISUAL_AUDIT_RULES.md' -TotalCount 320
Get-Content -Path '.prompts/shared/HUMAN_DRAFTING_MODE.md' -TotalCount 320
Get-Content -Path '.prompts/kicad_pipeline/02_schematic_visual_cleanup.md' -TotalCount 320
Get-Content -Path '.prompts/codex/05_PLAN_SCHEMATIC.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md' -TotalCount 320
Get-Content -Path '.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md' -TotalCount 320
Get-Content -Path '.prompts/kicad_pipeline/03_schematic_visual_repair.md' -TotalCount 320
Get-Content -Path '.prompts/kicad_pipeline/03_schematic_electrical_review.md' -TotalCount 320
Get-Content -Path '.prompts/codex/06_REVIEW_SCHEMATIC.md' -TotalCount 320
Get-Content -Path '.prompts/claude/05_PLAN_SCHEMATIC.md' -TotalCount 320
Get-Content -Path '.prompts/claude/06_REVIEW_SCHEMATIC.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md' -TotalCount 320
Get-Content -Path '09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md' -TotalCount 320
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md' -TotalCount 260
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md' -TotalCount 260
rg -n "ORIENT_SYMBOLS_BEFORE_LABELS|LOCAL_WIRE_BEFORE_NET_LABEL|MCU_LOCAL_SUPPORT_PHYSICAL_WIRING|GRAPHIC_LINES_ARE_NOT_ELECTRICAL_WIRES|RESET_BOOT_TOPOLOGY_SANITY|TEXT_OWNERSHIP_REQUIRED|HUMAN_PRESENTATION_REVIEW_REQUIRED|GROUND_AND_POWER_RAIL_PRESENTATION" 34_SCHEMATIC_QUALITY_ENGINE 09_ACCURACY_ENGINE .prompts README_GPT.md "FOR CHAT GPT.MD"
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/README.md' -TotalCount 120
Get-Content -Path '34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md' -TotalCount 180
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md' -TotalCount 80
Get-Content -Path '00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md' -TotalCount 120
python health_check.py --repo-root . --no-write
rg -n "orientation|local wire|graphic|topology|presentation review|rail" .prompts/shared/HUMAN_DRAFTING_MODE.md .prompts/kicad_pipeline/02_schematic_visual_cleanup.md .prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md .prompts/kicad_pipeline/03_schematic_visual_repair.md .prompts/kicad_pipeline/03_schematic_electrical_review.md .prompts/codex/05_PLAN_SCHEMATIC.md .prompts/codex/06_REVIEW_SCHEMATIC.md .prompts/claude/05_PLAN_SCHEMATIC.md .prompts/claude/06_REVIEW_SCHEMATIC.md
rg -n "READABLE_SCHEMATIC_FLOW_RULES|WIRE_VS_NET_LABEL_RULES|REFERENCE_VALUE_TEXT_PLACEMENT_RULES|ESP32_BOOT_RESET_RULES|SCHEMATIC_BLOCK_LAYOUT_RULES|SCHEMATIC_VISUAL_AUDIT_RULES" 00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md 00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md
git status --short -- 34_SCHEMATIC_QUALITY_ENGINE 09_ACCURACY_ENGINE .prompts README_GPT.md "FOR CHAT GPT.MD" 00_CODEX_START 05_OUTPUTS/release_readiness 02_HISTORY
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_TASK_CONTRACT.json
python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_TASK_CONTRACT.json --output 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_TASK_CONTRACT_REPORT.md
git status --short -- 34_SCHEMATIC_QUALITY_ENGINE 09_ACCURACY_ENGINE .prompts README_GPT.md "FOR CHAT GPT.MD" 00_CODEX_START 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH* 02_HISTORY/sessions/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_SESSION.md 02_HISTORY/command_logs/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_COMMANDS.md 02_HISTORY/ai_self_reviews/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_AI_SELF_REVIEW.md 02_HISTORY/ai_scorecards/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_SCORECARD.md 02_HISTORY/claim_evidence_matrices/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_CLAIM_EVIDENCE_MATRIX.md 02_HISTORY/uncertainty_logs/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_UNCERTAINTY_LOG.md 02_HISTORY/hallucination_risk_logs/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_HALLUCINATION_RISK_LOG.md 02_HISTORY/issue_logs/SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_TOOLING_FOLLOWUP.md
rg -n "SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH|SCHEMATIC_HUMAN_DRAFTING_RULE_PATCH_TOOLING_FOLLOWUP" 02_HISTORY/MASTER_HISTORY_INDEX.md 00_CODEX_START/AI_QUALITY_INDEX.generated.md 00_CODEX_START/HISTORY_INDEX.generated.md 00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md
```

## Notes

- Manual edits were applied with `apply_patch`.
- No KiCad design files, PCB files, or fabrication outputs were edited.
- Index rebuilds and task-contract validation were run during closeout.
