# ESP32_CSI_WIFI_NODE Full Routing And Copper Command Log

Date: 2026-05-07

## Startup / Gate Commands

- `Get-Content START_HERE_FOR_AI_AGENTS.md`
- `Get-Content AGENTS.md`
- `Get-Content "FOR CHAT GPT.MD"`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8`

Phase gate output was blocked by older state records. LJ's prompt supplied explicit authorization to continue first-pass routing unless true hard blockers appeared.

## Backup

- Created `99_BACKUPS/pre_codex_edits/20260507_144140_ESP32_CSI_WIFI_NODE_pre_full_routing_and_copper`
- Copied `.kicad_pcb`, `.kicad_pro`, and `.kicad_sch`.

## Baseline Verification

- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/FULL_ROUTING_BASELINE_DRC.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- Result: 12 U2 drill violations, 78 unconnected items, 0 schematic parity issues.

## Routing Attempts

- Ran `esp32_csi_full_route_pass.py`.
- DRC found many shorts/crossings; board was restored from backup.
- Ran `esp32_csi_grid_route_pass.py`.
- DRC still found shorts/crossings; board was restored from backup.
- Ran `esp32_csi_safe_partial_route.py`.
- Q1 local `/+5V_FUSED` route caused crossing/clearance in one pass, then a revised pass caused short risk near C5/Q1.
- Final kept safe route removed the risky `/+5V_FUSED` segment.

## Final Verification

- `kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- Result: 12 DRC violations, 67 unconnected items, 0 schematic parity issues, 0 footprint errors.

## Review Image Exports

- `kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.SilkS,F.Mask,Edge.Cuts -o _verification/pcb_visual/full_routing_partial_top.svg kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- `kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.SilkS,B.Mask,Edge.Cuts -o _verification/pcb_visual/full_routing_partial_bottom.svg kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- `kicad-cli pcb render --side top --width 1600 --height 1200 --background opaque --quality basic -o _verification/pcb_visual/full_routing_partial_3d_top.png kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- `kicad-cli pcb render --side front --width 1600 --height 1200 --background opaque --quality basic -o _verification/pcb_visual/full_routing_partial_3d_bottom_connector.png kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Outputs Not Generated

- Gerbers: NO
- Drill files: NO
- BOM: NO
- CPL: NO
- STEP: NO
- JLCPCB/PCBWay packages: NO

