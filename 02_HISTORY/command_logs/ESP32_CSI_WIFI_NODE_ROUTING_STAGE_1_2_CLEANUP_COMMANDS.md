# ESP32_CSI_WIFI_NODE Routing Stage 1/2 Cleanup Commands

Date: `2026-05-07`

## Main Commands Run

Prompt / maintenance:

- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8`

GUI / safety:

- `33_KICAD_GUI_AUTOMATION/scripts/windows/detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath ... -Json`
- process check for `kicad|pcbnew|eeschema`

Baseline:

- backup copy into `99_BACKUPS/pre_codex_edits/20260507_150607_ESP32_CSI_WIFI_NODE_stage1_stage2_cleanup_reroute`
- KiCad Python baseline count script
- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/ROUTING_STAGE_1_2_CLEANUP_BASELINE_DRC.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Routing edits:

- multiple KiCad Python reroute iterations applied to `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- final cleanup-net state:
  - `/+5V_IN`: 3 segments
  - `/+5V_FUSED`: 2 segments
  - `/+5V_PROTECTED`: 11 segments
  - `/BUCK_SW`: 4 segments
  - `/BUCK_BST`: 1 segment
  - `+3V3`: 5 segments, 2 vias

Final verification:

- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
- KiCad Python track/via/zone/angle-audit script
- `kicad-cli pcb export svg ... routing_stage_1_2_cleanup_top.svg`
- `kicad-cli pcb export svg ... routing_stage_1_2_cleanup_bottom.svg`
- `kicad-cli pcb render --side top ... routing_stage_1_2_cleanup_3d_top.png`
- `kicad-cli pcb render --side bottom ... routing_stage_1_2_cleanup_3d_bottom.png`
- Python SVG crop generation for:
  - `routing_stage_1_2_cleanup_power_input_closeup.svg`
  - `routing_stage_1_2_cleanup_buck_closeup.svg`

## Notes

- `kicad-cli` output-path handling was inconsistent during intermediate reroute iterations; the final authoritative DRC report for this session is `ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt`.
