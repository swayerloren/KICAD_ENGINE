# Schematic Layout Engine Commands

Date: `2026-05-10`
Task type: `AUDIT_ONLY`

## Commands Run

```powershell
Get-Content START_HERE_FOR_AI_AGENTS.md -TotalCount 220
Get-Content AGENTS.md -TotalCount 320
Get-Content 00_CODEX_START\TASK_ROUTER.md -TotalCount 260
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Get-Content 34_SCHEMATIC_QUALITY_ENGINE\README.md -TotalCount 260
Get-Content 34_SCHEMATIC_QUALITY_ENGINE\SCHEMATIC_READABILITY_STANDARD.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md -TotalCount 220
Get-Content 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md -TotalCount 220
Get-ChildItem .prompts\kicad_pipeline | Select-Object Name
Get-ChildItem 03_TOOLS\scripts\schematic_quality | Select-Object Name,Length
Get-Content 03_TOOLS\scripts\schematic_quality\schematic_quality_common.py -TotalCount 360
Get-Content 03_TOOLS\scripts\schematic_quality\audit_wire_vs_label_balance.py -TotalCount 260
Get-Content 03_TOOLS\scripts\schematic_quality\audit_schematic_block_layout.py -TotalCount 260
Get-Content 09_ACCURACY_ENGINE\checklists\SCHEMATIC_READY_FOR_PCB_CHECKLIST.md -TotalCount 260
Get-Content 09_ACCURACY_ENGINE\schematic_rules\READABLE_SCHEMATIC_FLOW_RULES.md -TotalCount 220
Get-Content 09_ACCURACY_ENGINE\schematic_rules\WIRE_VS_NET_LABEL_RULES.md -TotalCount 220
Get-Content 03_TOOLS\scripts\execution_contract\README.md -TotalCount 260
Get-ChildItem 03_TOOLS\scripts\schematic_layout
git status --short
Get-ChildItem 03_TOOLS\scripts\schematic_layout | Select-Object Name,Length
Get-ChildItem 34_SCHEMATIC_QUALITY_ENGINE | Select-Object Name,Length
Get-Content 03_TOOLS\scripts\schematic_layout\README.md -TotalCount 260
Get-ChildItem .prompts\kicad_pipeline | Where-Object { $_.Name -like '02_*' -or $_.Name -like '03_*' } | Select-Object Name
Get-Content 03_TOOLS\scripts\schematic_layout\schematic_layout_common.py -TotalCount 340
Get-Content 03_TOOLS\scripts\schematic_layout\extract_schematic_layout.py -TotalCount 260
Get-Content 03_TOOLS\scripts\schematic_layout\audit_visual_flow.py -TotalCount 320
Get-Content 03_TOOLS\scripts\schematic_layout\audit_local_wire_usage.py -TotalCount 260
Get-Content .prompts\kicad_pipeline\03_schematic_visual_repair.md -TotalCount 240
Get-Content .prompts\kicad_pipeline\04_schematic_electrical_audit.md -TotalCount 240
Get-Content README_GPT.md -TotalCount 260
Get-Content "FOR CHAT GPT.MD" -TotalCount 260
Get-Content 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md -TotalCount 220
Get-ChildItem 03_TOOLS\scripts\schematic_layout\*.py | ForEach-Object { python -m py_compile $_.FullName }
python 03_TOOLS\scripts\schematic_layout\render_schematic_review_pages.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --no-fail
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_layout\20260510_113053\SCHEMATIC_LAYOUT_REVIEW.md -TotalCount 240
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_layout\20260510_113053\schematic_readability_score.md -TotalCount 320
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_layout\20260510_113053\visual_flow.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_layout\20260510_113053\local_wire_usage.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROJECT_MEMORY.md -TotalCount 260
Get-Content 01_MEMORY\DESIGN_RULES_MEMORY.md -TotalCount 220
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md -TotalCount 220
```

## Closeout Commands

```powershell
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-10_schematic_layout_engine_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-10_schematic_layout_engine_task_contract.json --output 02_HISTORY\sessions\2026-05-10_schematic_layout_engine_task_contract_report.md
python 03_TOOLS\scripts\ai_quality\create_ai_self_review.py --repo-root . --scope global --title "Schematic Layout Engine Self Review" --summary "Completed the requested schematic layout engine, prompt wiring, and read-only validation without editing any KiCad design files." --details "The run finished the schematic-layout script layer, added block-template and scorecard docs, produced a read-only review packet for ESP32_CSI_WIFI_NODE, and recorded the resulting readability blockers into project memory. Residual risk remains in heuristic block assignment and overlap estimation, so human visual review is still required." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/schematic_layout/; 34_SCHEMATIC_QUALITY_ENGINE/; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/." --issue "The active schematic still fails readability at 39/100 and remains blocked for professional schematic cleanup readiness."
python 03_TOOLS\scripts\ai_quality\create_response_scorecard.py --repo-root . --scope global --title "Schematic Layout Engine Scorecard" --summary "Repo tooling and read-only validation completed; the active schematic was correctly classified as failing readability." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "Python syntax passed and the read-only review packet was generated at reports/schematic_layout/20260510_113053/." --issue "Layout scoring uses heuristics and the active schematic remains blocked on real readability cleanup." --overall-score 93 --evidence-support 19 --kicad-correctness 19 --datasheet-accuracy 12 --safety-compliance 15 --memory-routing 9 --uncertainty-disclosure 9 --usefulness 10
python 03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py --repo-root . --scope global --title "Schematic Layout Engine Claim Evidence Matrix" --summary "The repo now has a schematic layout engine that extracts, audits, scores, and plans schematic cleanup in read-only mode." --details "The claim is supported by the new schematic-layout scripts, the new 34-series layout docs, prompt updates, and the generated project review packet." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/schematic_layout/; 34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md; 34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/SCHEMATIC_LAYOUT_REVIEW.md" --issue "Apply-mode schematic rewriting remains intentionally blocked and the active schematic still fails readability."
python 03_TOOLS\scripts\ai_quality\create_uncertainty_log.py --repo-root . --scope global --title "Schematic Layout Engine Uncertainty Log" --summary "The layout engine uses heuristic block assignment, approximate region scoring, and estimated text-overlap geometry." --details "The scoring and layout-plan logic are intentionally conservative. Human visual review is still required before treating the schematic as professionally readable, and native KiCad annotation proof remains a separate authoritative gate." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "03_TOOLS/scripts/schematic_layout/schematic_layout_common.py; 03_TOOLS/scripts/schematic_layout/score_schematic_readability.py; reports/schematic_layout/20260510_113053/." --issue "Do not treat automated layout score alone as a replacement for human visual review."
python 03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py --repo-root . --scope global --title "Schematic Layout Engine Hallucination Risk Log" --summary "Schematic cleanup claims can drift if the agent over-trusts local labels, ERC, or inferred geometry instead of rendered evidence and project gates." --details "This run reduces that risk by forcing direct .kicad_sch parsing, local-wire audits, block-flow audits, scorecard evidence, and explicit dry-run-only rewrite behavior. Residual risk remains because the engine does not render native KiCad images itself and does not rewrite the schematic." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS --human-review-required YES --evidence "34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md; 03_TOOLS/scripts/schematic_layout/rewrite_schematic_layout_safe.py; reports/schematic_layout/20260510_113053/SCHEMATIC_LAYOUT_REVIEW.md" --issue "The active project still needs human-driven schematic visual cleanup before any later schematic-to-PCB claim."
python 03_TOOLS\scripts\ai_quality\create_quality_gate_failure.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Schematic Layout Gate Failure" --summary "The new schematic layout review packet classified the active schematic as FAIL at 39/100." --details "Visual flow failed, local wire usage failed, and the schematic still shows label-heavy local presentation in the ESP32, reset/boot, and test/debug blocks. This is a readability and layout-organization block, not an ERC block." --severity HIGH --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label BLOCKED_UNTIL_HUMAN_REVIEW --gate-result FAIL --human-review-required YES --evidence "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/SCHEMATIC_LAYOUT_REVIEW.md; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/schematic_readability_score.md" --issue "Schematic readability cleanup is still required before future schematic-to-PCB-readiness claims should be upgraded."
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git diff --cached --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

## Closeout Results

- Task contract validation: `PASS`
- Task contract recommended final status: `VALID_TASK_CONTRACT`
- Quality-gate failure record created for the active schematic layout fail
- Repo, memory, history, AI-quality, and known-problem indexes rebuilt
- No tracked or staged `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files changed
