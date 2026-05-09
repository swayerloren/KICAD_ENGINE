# KiCad Python Context Fix Commands

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

## Commands And Results

1. `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - result: prompt count `4`, maintenance not due
2. `rg -n --glob '!**/__pycache__/**' '^\s*import pcbnew|^\s*from pcbnew|require_pcbnew_for_cli' 03_TOOLS/scripts 14_LAYOUT_AUTOMATION/scripts`
   - result: identified direct-import callers and existing shared-bridge callers
3. `python health_check.py --no-write`
   - result: `PASS=18 WARN=2 FAIL=0`
4. `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite`
   - result: `PASS=18 WARN=2 FAIL=0`
5. `python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`
   - result: `WARN`; current Python direct import `False`, KiCad Python import `True`, recommended context `KICAD_PYTHON`
6. `python 03_TOOLS/scripts/kicad_api/kicad_python_context.py`
   - result: JSON status `WARN`; current Python `3.12.10`, KiCad Python `3.11.5`, embedded DLL `python311.dll`
7. `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
   - result: `PASS` for KiCad root, GUI, CLI, and `pcbnew`
8. `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`
   - result: `pcbnew.status = AVAILABLE_IN_KICAD_PYTHON`
9. `python -m py_compile health_check.py 03_TOOLS/scripts/kicad_api/kicad_python_context.py 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py 03_TOOLS/scripts/kicad_discovery/find_kicad.py 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py 03_TOOLS/scripts/python_env_check.py 14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py 03_TOOLS/scripts/kicad_pcb_intelligence/repair_esp32_csi_wifi_node_bottom_edge_connectors.py 03_TOOLS/scripts/kicad_pcb_intelligence/repair_esp32_csi_wifi_node_placement.py 03_TOOLS/scripts/pcb_routing/esp32_csi_safe_partial_route.py 03_TOOLS/scripts/pcb_routing/esp32_csi_power_batch_02_reroute.py 03_TOOLS/scripts/pcb_routing/esp32_csi_critical_route_pass_1.py 03_TOOLS/scripts/pcb_routing/esp32_csi_full_route_pass.py 03_TOOLS/scripts/pcb_routing/esp32_csi_full_routing_pass_1.py 03_TOOLS/scripts/pcb_routing/esp32_csi_grid_route_pass.py 03_TOOLS/scripts/pcb_routing/esp32_csi_inspect_board.py`
   - result: pass
10. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
    - result: no KiCad design files changed
11. `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
    - result: prompt counter `4 -> 5`; maintenance due `YES`
12. `python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .`
    - result: repo index rebuilt
13. `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
    - result: memory index rebuilt
14. `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
    - result: history index rebuilt
15. `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .`
    - result: `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt
16. `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
    - result: `00_CODEX_START/AI_QUALITY_INDEX.generated.*` rebuilt
17. `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
    - result: `PROMPT_COUNT: 5`, `MAINTENANCE_DUE: YES`

## Environment Evidence

- KiCad root inspected: `C:\Program Files\KiCad\9.0`
- KiCad bundled Python observed at: `C:\Program Files\KiCad\9.0\bin\python.exe`
- current repo/runtime Python observed at: `C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe`
