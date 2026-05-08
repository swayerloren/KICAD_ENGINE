# MAINTENANCE_LAYER_INVESTIGATION_AND_REPAIR_COMMANDS

Date: `2026-05-07`

## Key Commands

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

```powershell
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 2
```

```powershell
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 3
```

```powershell
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 8
```

```powershell
@'
import py_compile
for path in [
    r"03_TOOLS\scripts\project_gate\check_phase_allowed.py",
    r"03_TOOLS\scripts\project_state\project_state_common.py",
    r"03_TOOLS\scripts\project_state\build_live_project_state.py",
    r"03_TOOLS\scripts\project_state\detect_stale_reports.py",
    r"03_TOOLS\scripts\project_state\reconcile_project_gates.py",
    r"03_TOOLS\scripts\project_state\update_phase_status_from_live_state.py",
    r"03_TOOLS\scripts\maintenance\prompt_counter.py",
    r"03_TOOLS\scripts\maintenance\run_maintenance_cycle.py",
    r"03_TOOLS\scripts\ai_quality\build_current_known_problems.py",
    r"03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py",
    r"03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py",
    r"03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py",
    r"03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py",
]:
    py_compile.compile(path, doraise=True)
print("PY_COMPILE_OK")
'@ | python -
```

```powershell
python 03_TOOLS\scripts\memory_history\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\memory_history\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
```

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "maintenance layer investigation and repair" --apply
```

## Notes

- `check_phase_allowed.py --phase 8` returned exit code `1` by design because routing remains blocked by live DRC, unrouted nets, missing zones/GND strategy, and unverified existing routing.
- All commands were read-only with respect to KiCad design files.
