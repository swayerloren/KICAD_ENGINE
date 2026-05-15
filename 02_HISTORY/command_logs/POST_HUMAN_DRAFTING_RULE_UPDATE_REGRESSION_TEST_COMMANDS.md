# POST_HUMAN_DRAFTING_RULE_UPDATE_REGRESSION_TEST_COMMANDS

Date: `2026-05-14`
Status: `COMPLETED`

## Commands And Tool Actions

| Step | Command Or Tool | Purpose | Result |
| --- | --- | --- | --- |
| 1 | `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | Check prompt-counter maintenance state before meaningful work | Completed; `PROMPT_COUNT=4`, `MAINTENANCE_DUE=NO` |
| 2 | `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "post human drafting rule update regression test" --apply` | Increment prompt counter for this task | Completed; `4 -> 5`, maintenance due |
| 3 | `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | Run required maintenance before engineering verification continued | Completed; counter reset `5 -> 0` |
| 4 | `kicad-cli sch erc --format report --severity-all --output .../validation/erc.rpt ...ESP32_CSI_WIFI_NODE.kicad_sch` | Run read-only ERC | Completed; `0` violations |
| 5 | `python 03_TOOLS/scripts/schematic_quality/audit_schematic_text_overlaps.py --schematic ... --output .../validation/text_overlaps.md --json-output .../validation/text_overlaps.json --no-fail` | Run text overlap audit | Completed; `FAIL=1 WARN=7` |
| 6 | `python 03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py --schematic ... --output .../validation/annotation.md --json-output .../validation/annotation.json --no-fail` | Run unresolved reference / annotation check | Completed; `PASS=159 WARN=0 FAIL=0` |
| 7 | `python 03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir .../schematic_quality_gate --no-fail` | Run schematic readability gate | Completed; gate `FAIL` |
| 8 | `python 03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir .../human_drafting --warn-only` | Run human-drafting checker | Completed; `FAIL=4 WARN=9 INFO=9` |
| 9 | `powershell -ExecutionPolicy Bypass -File 03_TOOLS/kicad/run_schematic_visual_check.ps1 -ProjectRoot ... -SchematicPath ... -OutputRoot .../visual -NoFailOnFindings` | Run visual-only schematic gate | Completed; `AUTOMATED_CROP_PASS_ONLY`, human visual `NOT_VERIFIED` |
| 10 | `python health_check.py --repo-root . --no-write` | Run repo health check | Completed; `PASS=18 WARN=2 FAIL=0` |
| 11 | `Get-Content` on generated JSON/Markdown outputs | Read fresh audit results before report write-up | Completed |
| 12 | `apply_patch` | Create regression report and closeout artifacts | Completed |
| 13 | `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 05_OUTPUTS/release_readiness/POST_HUMAN_DRAFTING_RULE_UPDATE_REGRESSION_TEST_TASK_CONTRACT.json` | Validate the audit-only task contract | Completed; `valid=true`, `recommended_final_status=VALID_TASK_CONTRACT` |
| 14 | `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 05_OUTPUTS/release_readiness/POST_HUMAN_DRAFTING_RULE_UPDATE_REGRESSION_TEST_TASK_CONTRACT.json --output 05_OUTPUTS/release_readiness/POST_HUMAN_DRAFTING_RULE_UPDATE_REGRESSION_TEST_TASK_CONTRACT_REPORT.md` | Write Markdown contract report | Completed |
| 15 | `python 03_TOOLS/scripts/indexing/build_repo_index.py` | Refresh repo index after adding new artifacts | Completed |
| 16 | `python 03_TOOLS/scripts/indexing/build_memory_index.py` | Refresh memory index after maintenance and closeout | Completed |
| 17 | `python 03_TOOLS/scripts/indexing/build_history_index.py` | Refresh history index after session artifacts were added | Completed |
| 18 | `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py` | Refresh AI-quality index after AI artifacts were added | Completed |
| 19 | `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py` | Refresh current known problems after closeout | Completed |
