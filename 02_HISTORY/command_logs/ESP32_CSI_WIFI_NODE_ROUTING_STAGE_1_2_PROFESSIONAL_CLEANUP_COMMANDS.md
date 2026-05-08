# ESP32_CSI_WIFI_NODE Routing Stage 1/2 Professional Cleanup Commands

Date: `2026-05-07`

## Main Commands Run

Prompt / maintenance:

- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8`

GUI / safety:

- `33_KICAD_GUI_AUTOMATION/scripts/windows/detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath ... -Json`
- process checks for `kicad|pcbnew|eeschema`

Baseline:

- backup copy into `99_BACKUPS/pre_codex_edits/20260507_160629_ESP32_CSI_WIFI_NODE_stage1_2_professional_cleanup`
- KiCad Python baseline count script
- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output ...\\ROUTING_STAGE_1_2_PROFESSIONAL_BASELINE_DRC.rpt ...\\ESP32_CSI_WIFI_NODE.kicad_pcb`

Trial routing work:

- KiCad Python reroute trials against `%TEMP%\\ESP32_CSI_WIFI_NODE_stage1_2_trial.kicad_pcb`
- trial DRC runs used to confirm removal of the `SW/BST` crossing and local copper violations before touching the active board

Final active-board edit:

- KiCad Python direct edit of `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- local footprint corrections:
  - `Q1 -> 180 deg`
  - `C2 -> 0 deg`
  - `C5 -> 0 deg`
  - `C6 -> move to (32.400, 68.725), 90 deg`

Final verification:

- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output ...\\ROUTING_STAGE_1_2_PROFESSIONAL_DRC_LIVE.rpt ...\\ESP32_CSI_WIFI_NODE.kicad_pcb`
- KiCad Python track/via/zone count script
- KiCad Python angle-quality audit script
- `kicad-cli pcb render --side top --width 2200 --height 1600 --output ...\\routing_stage_1_2_professional_top.png ...\\ESP32_CSI_WIFI_NODE.kicad_pcb`
- `kicad-cli pcb render --side bottom --width 2200 --height 1600 --output ...\\routing_stage_1_2_professional_bottom.png ...\\ESP32_CSI_WIFI_NODE.kicad_pcb`
- KiCad Python image-generation script for:
  - `routing_stage_1_2_professional_input_power_closeup.png`
  - `routing_stage_1_2_professional_buck_closeup.png`
  - `routing_stage_1_2_professional_3v3_closeup.png`

## Final Routed-Net State

- `/+5V_IN`: `3` segments
- `/+5V_FUSED`: `2` segments
- `/+5V_PROTECTED`: `10` segments
- `/BUCK_SW`: `2` segments
- `/BUCK_BST`: `2` segments
- `+3V3`: `5` segments, `2` vias

## Notes

- The active-board DRC is authoritative; temporary-board DRCs were used only as routing trials.
- Schematic parity remained `0` on the active project DRC run.
