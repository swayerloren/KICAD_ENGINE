# ESP32_CSI_WIFI_NODE Power Routing Repair Batch 02 Commands

Date: `2026-05-08`

## Key Commands

```powershell
Get-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 99_BACKUPS\pre_codex_edits\20260508_101143_ESP32_CSI_WIFI_NODE_batch_02_power_routing_repair
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro 99_BACKUPS\pre_codex_edits\20260508_101143_ESP32_CSI_WIFI_NODE_batch_02_power_routing_repair
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_power_batch_02_reroute.py <board> summary
```

```powershell
@'
import pcbnew
# copied-board rehearsal: remove /+5V_FUSED and /+5V_PROTECTED, add candidate geometry, refill zones, save
'@ | & 'C:\Program Files\KiCad\9.0\bin\python.exe' -
kicad-cli pcb drc --format json --severity-all --units mm --output <trial>\trial_drc_v5.json <trial>\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Copied-board rehearsal conclusion:

- rejected direct `/+5V_IN` simplifications due `J1` GND clearance failures
- rejected flattened `/+5V_PROTECTED` branch due `C2` GND shorting
- selected candidate kept `/+5V_IN` unchanged and only rerouted `/+5V_FUSED` plus the local `C2 -> U1` protected feed

```powershell
@'
import pcbnew
# live apply: remove /+5V_FUSED and /+5V_PROTECTED, add selected geometry, refill zones, save
'@ | & 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

Live apply notable output:

- `removed`
- `added 12`
- `filled`
- `saved`

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_BATCH_02_POWER_ROUTING_REPAIR_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
python 03_TOOLS\scripts\project_state\build_live_project_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
```

```powershell
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_top.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_top.png
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_bottom.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_batch_02_bottom.png
```

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

## Notable Outputs

- PCB hash before: `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`
- PCB hash after: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- DRC after batch 02: `0` violations, `27` unconnected items
- Detectable unrouted nets after batch 02: `10`
- Maintenance cycle after closeout: prompt counter `1 -> 0`
