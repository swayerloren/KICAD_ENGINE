# ESP32_CSI_WIFI_NODE PCB Batch 04 Control Net Routing Commands

Date: `2026-05-08`

## Commands Run

1. Re-read the Batch 03 reports, routing-work logs, and routing rules for the current board state.
2. Confirmed the live PCB exists and recorded the pre-edit hash:
   - `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
3. Created fresh backup:
   - `99_BACKUPS\pre_codex_edits\20260508_114318_ESP32_CSI_WIFI_NODE_batch_04_control_net_routing`
4. Created the Batch 04 trial folder:
   - `routing_work\20260508_091428\batch04_control_trials\20260508_114318`
5. Appended Batch 04 start markers to:
   - `ROUTING_MASTER_LOG.md`
   - `ROUTING_DECISION_LOG.md`
   - `BEFORE_AFTER_HASH_LOG.md`
   - `TRACE_CHANGE_LOG.md`
6. Built copied-board rehearsal sweeps for `/U0RXD`, `/BOOT0`, and `/ESP_EN` under:
   - `routing_work\20260508_091428\batch04_control_trials\20260508_114318\*`
7. Created and syntax-checked:
   - `python -m py_compile 03_TOOLS\scripts\pcb_routing\esp32_csi_control_batch_04.py`
8. Revalidated the selected `/U0RXD` candidate on a copied board:
   - `C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_control_batch_04.py <trial-board> apply`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output <trial>\drc.json <trial-board>`
9. Applied the proven subset to the live board:
   - `C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_control_batch_04.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb apply`
10. Ran live DRC:
    - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output reports\PCB_BATCH_04_CONTROL_NET_ROUTING_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
11. Rebuilt live project state:
    - `python 03_TOOLS\scripts\project_state\build_live_project_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply`
12. Exported board visuals:
    - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output _verification\pcb_visual\pcb_batch_04_control_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
    - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output _verification\pcb_visual\pcb_batch_04_control_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
    - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side top --width 1800 --height 1200 --quality basic --background transparent --output _verification\pcb_visual\pcb_batch_04_control_top.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
    - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side bottom --width 1800 --height 1200 --quality basic --background transparent --output _verification\pcb_visual\pcb_batch_04_control_bottom.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
