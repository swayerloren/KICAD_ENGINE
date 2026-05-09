# PCB Routing Audit Plan Commands

Date: `2026-05-09`
Task type: `AUDIT_ONLY`

## Commands Run

1. `python health_check.py --no-write`
   - Result: `PASS=18 WARN=2 FAIL=0`
2. `python 03_TOOLS\scripts\kicad_api\pcbnew_import_check.py`
   - Result: `WARN`
   - Current Python `pcbnew`: `False`
   - KiCad Python `pcbnew`: `True`
3. `python 03_TOOLS\scripts\kicad_api\kicad_python_context.py`
   - Result: `AVAILABLE_IN_KICAD_PYTHON`
4. `git status --short --branch`
   - Result at first capture: dirty worktree with generated maintenance/index files; no `.kicad_pcb` modification shown
5. `python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: required maintenance completed and prompt counter reset to `0`
6. `python 03_TOOLS\scripts\project_state\validate_live_state_before_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: live-state validation completed
7. `python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8`
   - Result: `BLOCKED`
   - Live blockers: `17` unconnected items and `4` detectable unrouted nets
8. `python 14_LAYOUT_AUTOMATION\scripts\extract_kicad_pcb_to_routing_schema.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_routing_schema_live.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_routing_schema_live.md`
   - Result: live routing schema extracted
9. `python 14_LAYOUT_AUTOMATION\scripts\trace_by_trace_audit.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_routing_schema_live.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_trace_audit_live.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_trace_audit_live.md`
   - Result: trace-by-trace audit generated
10. `python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_routing_schema_live.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_geometry_live.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_geometry_live.md`
    - Result: geometry hard-fail report generated
11. `python 14_LAYOUT_AUTOMATION\scripts\run_real_board_routing_audit.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit --report-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit_summary.json --report-markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit_summary.md`
    - Result: aggregate routing audit generated with `AUTO_BLOCKED_BAD_LAYOUT`
12. KiCad Python inline query against the live board for footprint positions and net names in the audited areas
    - Result: confirmed live references and pad nets for `J2`, `U3`, `U2`, `U1`, `L1`, `F1`, `Q1`, `SW1`, `SW2`, `TP1` through `TP9`, `R2`, `R3`, `R4`, `R8`, and `R9`
13. KiCad Python inline query for `GND` vias and zone count near `U2`
    - Result: confirmed `2` `GND` zones and sparse explicit local `GND` via population near the module region
14. `(Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256).Hash`
    - Result before closeout: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`
15. `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "pcb routing audit plan" --apply`
    - Result: prompt counter `0 -> 1`
16. `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .`
    - Result: repo index rebuilt
17. `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .`
    - Result: memory index rebuilt
18. `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .`
    - Result: history index rebuilt
19. `python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .`
    - Result: `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt
20. `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .`
    - Result: AI quality index rebuilt
21. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/PCB_ROUTING_AUDIT_PLAN_TASK_CONTRACT.json`
    - Result: valid `AUDIT_ONLY` contract, recommended final status `VALID_TASK_CONTRACT`
22. `git status --short --branch`
    - Result at closeout: branch `main...origin/main [behind 1]`; generated/index/history/report files changed; `.kicad_pcb` still not modified
23. `(Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256).Hash`
    - Result after closeout: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`

## KiCad Design File Result

- `ESP32_CSI_WIFI_NODE.kicad_pcb`: unchanged
- `ESP32_CSI_WIFI_NODE.kicad_sch`: unchanged
