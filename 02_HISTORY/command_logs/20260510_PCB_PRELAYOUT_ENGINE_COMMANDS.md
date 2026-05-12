# PCB Prelayout Engine Commands

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Commands Run

1. `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter incremented before meaningful project work.
2. `python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: maintenance due detected.
3. `python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: maintenance completed and prompt counter reset.
4. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_pcb_prelayout_engine_task_contract.json`
   - Result: valid `DOCS_ONLY` contract.
5. `Copy-Item START_HERE_FOR_AI_AGENTS.md, README_GPT.md, 'FOR CHAT GPT.MD', AGENTS.md, 00_CODEX_START\START_HERE.md, 00_CODEX_START\FOLDER_ROUTING_RULES.md, 00_CODEX_START\REPO_STRUCTURE_INDEX.md, 00_CODEX_START\REPO_MAP.md -Destination 99_BACKUPS\pre_codex_edits\20260510_prelayout_engine_doc_updates -Force`
   - Result: startup and handoff docs backed up before edits.
6. `python -m py_compile 03_TOOLS\scripts\pcb_prelayout\_prelayout_common.py 03_TOOLS\scripts\pcb_prelayout\extract_board_digital_twin.py 03_TOOLS\scripts\pcb_prelayout\generate_placement_variants.py 03_TOOLS\scripts\pcb_prelayout\project_routes_45deg.py 03_TOOLS\scripts\pcb_prelayout\score_placement_variant.py 03_TOOLS\scripts\pcb_prelayout\compare_variants.py 03_TOOLS\scripts\pcb_prelayout\render_variant_preview.py 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py`
   - Result: syntax check passed.
7. Inline Python JSON parse loop over `33_PCB_PRELAYOUT_ENGINE/schemas/*.json`
   - Result: `SCHEMA_PARSE_OK 7`.
8. `python 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Initial result before heuristic fixes: no passing variants; see failed-attempt record.
9. `python 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Final result: `PRELAYOUT_VARIANT_COUNT=3`, `PRELAYOUT_PASSING_VARIANTS=1`, `PRELAYOUT_SELECTED_VARIANT=VARIANT_01`, `PRELAYOUT_PLACEMENT_GATE_STATUS=PASS`, `PRELAYOUT_ROUTING_GATE_STATUS=BLOCKED`.
10. `git status --short -- '*.kicad_sch' '*.kicad_pcb'`
    - Result: only untracked backup `.kicad_pcb` files under project `backups/`.
11. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'`
    - Result: no tracked KiCad source diffs.
12. `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'`
    - Result: no tracked KiCad source modifications.
