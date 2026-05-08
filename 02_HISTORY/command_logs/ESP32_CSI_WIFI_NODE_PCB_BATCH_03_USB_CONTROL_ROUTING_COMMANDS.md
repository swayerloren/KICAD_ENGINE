# ESP32_CSI_WIFI_NODE PCB Batch 03 USB Control Routing Commands

Date: `2026-05-08`

## Commands Run

1. Confirmed the live PCB hash and inspected the interrupted batch-03 routing script and routing-work logs.
2. Created fresh backup:
   - `99_BACKUPS\pre_codex_edits\20260508_112350_ESP32_CSI_WIFI_NODE_batch_03_usb_control_routing_resume`
3. Syntax-checked the repaired batch-03 script:
   - `python -m py_compile 03_TOOLS\scripts\pcb_routing\esp32_csi_usb_control_batch_03.py`
4. Revalidated the candidate on copied boards with:
   - `C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_usb_control_batch_03.py <copied-board> apply`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output <trial>\drc.json <copied-board>`
5. Applied the proven USB-support subset to the live board:
   - `C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_usb_control_batch_03.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb apply`
6. Ran live DRC:
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output reports\PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FIRST.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output reports\PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FINAL.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
7. Rebuilt live project state:
   - `python 03_TOOLS\scripts\project_state\build_live_project_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply`
8. Exported board visuals:
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output _verification\pcb_visual\pcb_batch_03_usb_control_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output _verification\pcb_visual\pcb_batch_03_usb_control_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side top --width 1800 --height 1200 --quality basic --background transparent --output _verification\pcb_visual\pcb_batch_03_usb_control_top.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
   - `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side bottom --width 1800 --height 1200 --quality basic --background transparent --output _verification\pcb_visual\pcb_batch_03_usb_control_bottom.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
