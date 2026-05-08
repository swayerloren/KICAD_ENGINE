# Final PCB Visual Review Package Commands

Status: `COMPLETED`

Key commands and actions:

- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `kicad-cli pcb render` for fresh full-board top and bottom PNGs
- direct `kicad-cli` close-up attempt using `--zoom` and `--pivot`
- local image spot checks
- deterministic Pillow crop generation from the fresh full-board renders
- `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- fresh `kicad-cli pcb drc --format json`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "final PCB visual review package" --apply`
- `python 03_TOOLS/scripts/memory_history/build_memory_index.py --repo-root .`
- `python 03_TOOLS/scripts/memory_history/build_history_index.py --repo-root .`
- `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .`
