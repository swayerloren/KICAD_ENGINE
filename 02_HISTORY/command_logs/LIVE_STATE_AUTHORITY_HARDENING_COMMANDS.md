# Live State Authority Hardening Commands

Date: `2026-05-08`
Branch: `hardening/execution-contract`

## Commands Run

```text
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
git status -sb
python -m py_compile 03_TOOLS/scripts/project_state/live_state_authority.py 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py 03_TOOLS/scripts/project_state/live_state_gate_wrapper.py 03_TOOLS/scripts/project_gate/check_phase_allowed.py 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py
python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 2
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 3
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8
```

## Key Results

- Maintenance cycle used `READ_FRESH_LIVE_PROJECT_STATE`.
- Phase `2` allowed from live PCB evidence.
- Phase `3` allowed from live placement evidence.
- Phase `8` blocked by live DRC fail and remaining unrouted nets.
- Stale operational reports were surfaced as `STALE_REPORT_IGNORED`.
