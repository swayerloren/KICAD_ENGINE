# Schematic Human Drafting Checker Commands

Date: `2026-05-14`

## Key Commands

1. Startup and routing reads
   - `Get-Content START_HERE_FOR_AI_AGENTS.md`
   - `Get-Content AGENTS.md`
   - `Get-Content 00_CODEX_START\START_HERE.md`
   - `Get-Content 00_CODEX_START\TASK_ROUTER.md`
   - `Get-Content 00_CODEX_START\CURRENT_PROJECT.md`
   - `Get-Content 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md`
   - `Get-Content 00_CODEX_START\TASK_TYPE_TO_ALLOWED_ACTIONS.md`
   - `Get-Content 00_CODEX_START\TASK_TYPE_TO_BLOCKERS.md`
   - `Get-Content 00_CODEX_START\TASK_TYPE_TO_OUTPUTS.md`

2. Prompt-counter maintenance check
   - `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - result: `PROMPT_COUNT=2`, `MAINTENANCE_DUE=NO`

3. Prompt-counter increment
   - `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "schematic human drafting checker" --apply`
   - result: `2 -> 3`

4. Existing tool-layer inspection
   - `Get-ChildItem 03_TOOLS\scripts\schematic_quality`
   - `Get-Content 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py`
   - `Get-Content 03_TOOLS\scripts\schematic_quality\schematic_quality_common.py`
   - `Get-Content 03_TOOLS\scripts\schematic_quality\audit_wire_vs_label_balance.py`
   - `Get-Content 03_TOOLS\scripts\schematic_quality\audit_schematic_block_layout.py`
   - `Get-Content 03_TOOLS\scripts\schematic_quality\audit_schematic_text_overlaps.py`

5. Active schematic inspection
   - `rg -n "ESP_EN|BOOT0|STATUS_LED|GND|\+3V3|D1|D2|SW1|SW2|C3|C4|C6|R3|R4|U2|IO0|EN" 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
   - targeted `Get-Content` line-range reads around the reset/boot and LED cluster
   - `kicad-cli sch export netlist --format kicadxml --output <temp> 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

6. Checker validation
   - `python 03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --warn-only`
   - result: reports written to `reports/schematic_quality/20260514_165956/`
   - `python 03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/human_drafting_exitcode_check`
   - result: `EXIT_CODE: 1`

7. Health check
   - `python health_check.py --repo-root . --no-write`
   - result: `PASS=18 WARN=2 FAIL=0`

8. Worktree inspection
   - `git status --short -- 03_TOOLS/scripts/schematic_quality 34_SCHEMATIC_QUALITY_ENGINE .prompts 05_OUTPUTS/release_readiness 02_HISTORY 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE '*.kicad_sch' '*.kicad_pcb' fabrication`
   - result: repo already dirty; no KiCad design-file edits were introduced by this task

9. Task-contract validation
   - `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_TASK_CONTRACT.json`
   - result: `valid=true`, `recommended_final_status=VALID_TASK_CONTRACT`
   - `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_TASK_CONTRACT.json --output 05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_TASK_CONTRACT_REPORT.md`
   - result: report written successfully

10. Closeout index rebuild
   - `python 03_TOOLS/scripts/indexing/build_repo_index.py`
   - `python 03_TOOLS/scripts/indexing/build_memory_index.py`
   - `python 03_TOOLS/scripts/indexing/build_history_index.py`
   - `python 03_TOOLS/scripts/indexing/build_known_problems.py`
   - result: closeout indexes and known-problem surfaces rebuilt successfully
