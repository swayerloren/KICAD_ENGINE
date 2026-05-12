# ESP32_CSI_WIFI_NODE Footprint Assignment Commands

Date: `2026-05-10`

## Commands Run

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256
python 03_TOOLS\scripts\footprint_package\extract_physical_symbols.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_assignment_live_physical_symbols.json --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_assignment_live_physical_symbols.md
python 03_TOOLS\scripts\footprint_package\audit_blank_footprints.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_assignment_blank_footprints.json --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_assignment_blank_footprints.md --no-fail
python 33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro --schematic C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe sch erc --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\erc_after_footprint_lock.raw.txt 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
python 03_TOOLS\scripts\footprint_package\run_footprint_package_gate.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_package\20260510_footprint_lock_apply --no-fail
python 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_quality\20260510_footprint_lock_apply --no-fail
powershell -ExecutionPolicy Bypass -File 03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -NoFailOnFindings
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-10_esp32_csi_wifi_node_footprint_assignment_task_contract.json
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-10_esp32_csi_wifi_node_footprint_assignment_task_contract.json --output 02_HISTORY\sessions\2026-05-10_esp32_csi_wifi_node_footprint_assignment_task_contract_report.md
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
```

## Command Results Summary

- Prompt counter increment: `PASS`, maintenance due `NO`
- Live schematic blank-footprint audit: `PASS`, blank footprint count `0`
- GUI window-state check: `DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA`
- ERC: `PASS`, `0` errors, `0` warnings
- Footprint package gate: `NEEDS_HUMAN_REVIEW`
- Schematic quality gate: `FAIL`
- Schematic visual export: `PASS`, human visual status still `AUTOMATED_CROP_PASS_ONLY`
- Repo, memory, history, AI-quality, and known-problem indexes: `PASS`
