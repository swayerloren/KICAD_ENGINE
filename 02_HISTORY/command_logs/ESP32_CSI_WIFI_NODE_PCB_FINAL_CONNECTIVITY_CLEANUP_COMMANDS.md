# ESP32_CSI_WIFI_NODE PCB Final Connectivity Cleanup Commands

Generated: `2026-05-08T12:34:25-04:00`

## Core Commands

1. Read live PCB identity:

```powershell
Get-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

2. Fresh pre-edit DRC:

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_CONNECTIVITY_CLEANUP_DRC_PRECHECK.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

3. Create live backup:

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 99_BACKUPS\pre_codex_edits\20260508_122513_ESP32_CSI_WIFI_NODE_final_connectivity_cleanup\
```

4. Build copied-board rehearsal set:

```powershell
Copy-Item ...\ESP32_CSI_WIFI_NODE.kicad_pcb routing_work\20260508_091428\final_connectivity_cleanup_trials\20260508_122929\
```

5. Rehearse copied-board local cleanup candidates with KiCad Python:

```powershell
C:\Program Files\KiCad\9.0\bin\python.exe - < candidate_control_local script payload
C:\Program Files\KiCad\9.0\bin\python.exe - < candidate_control_usb_local script payload
```

6. Rerun copied-board DRC with the live `.kicad_pro` beside each trial board:

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro ...\candidate_control_local.kicad_pro
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro ...\candidate_control_usb_local.kicad_pro
kicad-cli pcb drc --format json --severity-all --units mm --output ...\candidate_control_local_drc_rerun.json ...\candidate_control_local.kicad_pcb
kicad-cli pcb drc --format json --severity-all --units mm --output ...\candidate_control_usb_local_drc_rerun.json ...\candidate_control_usb_local.kicad_pcb
```

7. Apply the accepted copied-board-proven local cleanup to the live PCB:

```powershell
C:\Program Files\KiCad\9.0\bin\python.exe - < live apply script payload
```

8. Run post-edit DRC and render visuals:

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_CONNECTIVITY_CLEANUP_DRC_POST.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side top --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_final_connectivity_cleanup_top.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side bottom --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\pcb_final_connectivity_cleanup_bottom.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```
