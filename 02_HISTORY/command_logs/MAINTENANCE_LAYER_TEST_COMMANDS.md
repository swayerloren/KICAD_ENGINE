# MAINTENANCE_LAYER_TEST_COMMANDS

Date: `2026-05-07`

## Commands

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
python 03_TOOLS\scripts\memory_history\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\memory_history\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "maintenance layer test" --apply
```

## Notable Output

- maintenance cycle classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
- phase 2: `ALLOWED`
- phase 3: `ALLOWED`
- phase 8: `BLOCKED`
- stale reports ignored during phase checks: `5`
- phase 8 blockers came from live DRC, unrouted nets, no accepted GND strategy, and unverified existing routed geometry
