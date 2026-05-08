# ESP32_CSI_WIFI_NODE Real PCB Full Routing Pass Commands

Date: `2026-05-08`

## Key Commands

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

```powershell
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> leds
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> status
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> uart
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> esp_en
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> boot0
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> p5v_tp
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> usb_low
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py <copied_board> usb_vbus
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output <trial>\drc.json <copied_board>
```

```powershell
C:\Program Files\KiCad\9.0\bin\python.exe 03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb leds status uart_tx usb_vbus
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_FULL_ROUTING_PASS_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_top.svg --layers F.Cu,F.Mask,F.Silkscreen,Edge.Cuts --fit-page-to-board --exclude-drawing-sheet 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb export svg --mode-single --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_bottom.svg --layers B.Cu,B.Mask,B.Silkscreen,Edge.Cuts --mirror --fit-page-to-board --exclude-drawing-sheet 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_top.png --side top --width 2200 --height 3400 --quality high --background opaque 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_bottom.png --side bottom --width 2200 --height 3400 --quality high --background opaque 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```
