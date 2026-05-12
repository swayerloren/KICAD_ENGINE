# Mechanical Orientation Truth Commands

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Commands Run

1. `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter incremented before meaningful project work.
2. `python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: `MAINTENANCE_DUE: NO`.
3. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_mechanical_orientation_truth_task_contract.json`
   - Result: valid `DOCS_ONLY` contract.
4. `python -m py_compile 14_LAYOUT_AUTOMATION\scripts\_placement_common.py 03_TOOLS\scripts\mechanical_orientation\_mechanical_orientation_common.py 03_TOOLS\scripts\mechanical_orientation\audit_connector_orientation.py 03_TOOLS\scripts\mechanical_orientation\audit_barrel_jack_orientation.py 03_TOOLS\scripts\mechanical_orientation\audit_usb_c_orientation.py 03_TOOLS\scripts\mechanical_orientation\audit_esp32_antenna_orientation.py 03_TOOLS\scripts\pcb_prelayout\_prelayout_common.py 03_TOOLS\scripts\pcb_prelayout\score_placement_variant.py`
   - Result: syntax check passed.
5. Inline Python JSON parse for `08_COMPONENT_DATABASE/mechanical_orientation/connector_orientation_truth.json` and the updated prelayout schemas.
   - Result: all targeted JSON files parsed successfully.
6. `python 03_TOOLS\scripts\mechanical_orientation\audit_connector_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: overall connector audit `NEEDS_HUMAN_REVIEW`, routing blocked.
7. `python 03_TOOLS\scripts\mechanical_orientation\audit_barrel_jack_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: barrel-jack audit `NEEDS_HUMAN_REVIEW`, routing blocked.
8. `python 03_TOOLS\scripts\mechanical_orientation\audit_usb_c_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: USB-C audit `PASS`.
9. `python 03_TOOLS\scripts\mechanical_orientation\audit_esp32_antenna_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: ESP32 antenna audit `PASS`.
10. `python 03_TOOLS\scripts\mechanical_orientation\audit_connector_orientation.py --project 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board`
    - Result: dry-run completed with overall status `NEEDS_HUMAN_REVIEW`.
11. `python 03_TOOLS\scripts\mechanical_orientation\audit_connector_orientation.py --project 04_KICAD_PROJECTS/archive/SAMPLE_KICAD_TEST_PROJECT/kicad/demo.kicad_pcb`
    - Result: dry-run completed with overall status `NEEDS_HUMAN_REVIEW`.
12. `python 03_TOOLS\scripts\mechanical_orientation\audit_connector_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_connector_orientation_audit.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_connector_orientation_audit.md`
    - Result: saved connector audit evidence.
13. `python 03_TOOLS\scripts\mechanical_orientation\audit_barrel_jack_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.md`
    - Result: saved barrel-jack audit evidence.
14. `python 03_TOOLS\scripts\mechanical_orientation\audit_usb_c_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_usb_c_orientation_audit.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_usb_c_orientation_audit.md`
    - Result: saved USB-C audit evidence.
15. `python 03_TOOLS\scripts\mechanical_orientation\audit_esp32_antenna_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_esp32_antenna_orientation_audit.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_esp32_antenna_orientation_audit.md`
    - Result: saved ESP32 antenna audit evidence.
16. `python 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
    - Result: latest integrated gate is fully blocked with `0` passing variants because connector proof remains incomplete and open-net blockers remain.
17. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_mechanical_orientation_truth_task_contract.json`
    - Result: updated contract remained valid with `changed_file_count = 35`.
18. `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .`
    - Result: startup repo index rebuilt after structure changes.
19. `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .`
    - Result: memory indexes rebuilt.
20. `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .`
    - Result: history indexes rebuilt.
21. `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .`
    - Result: AI-quality indexes rebuilt.
22. `python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .`
    - Result: `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt.
23. `Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
    - Result: generated Python cache directories removed after validation so they do not remain in the repo diff.
24. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'`
    - Result: no tracked KiCad source diffs.
25. `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'`
    - Result: no tracked KiCad source modifications.
