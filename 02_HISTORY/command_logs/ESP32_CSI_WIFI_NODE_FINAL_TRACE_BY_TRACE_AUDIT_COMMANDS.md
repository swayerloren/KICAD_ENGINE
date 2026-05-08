# ESP32_CSI_WIFI_NODE Final Trace By Trace Audit Commands

Generated: `2026-05-08T12:59:26-04:00`

## Core Commands

1. Maintenance precheck:

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

2. Backup and before-hash:

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 99_BACKUPS\pre_codex_edits\20260508_124307_ESP32_CSI_WIFI_NODE_final_trace_audit\
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

3. Extract raw track/via/zone inventory from the `.kicad_pcb` text:

```powershell
python - < FINAL_TRACE_AUDIT_PRE_INVENTORY extraction payload
```

4. Pre-audit DRC and audit renders:

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_TRACE_AUDIT_DRC_PRECHECK.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side top --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\final_trace_audit_top_pre.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side bottom --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\final_trace_audit_bottom_pre.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

5. Rehearse copied-board `/+5V_PROTECTED` cleanup:

```powershell
Copy-Item ...\ESP32_CSI_WIFI_NODE.kicad_pcb routing_work\20260508_091428\final_trace_audit_trials\20260508_125541\
Copy-Item ...\ESP32_CSI_WIFI_NODE.kicad_pro routing_work\20260508_091428\final_trace_audit_trials\20260508_125541\
C:\Program Files\KiCad\9.0\bin\python.exe - < candidate_p5v_protected_cleanup payload
kicad-cli pcb drc --format json --severity-all --units mm --output ...\candidate_p5v_protected_cleanup_drc.json ...\candidate_p5v_protected_cleanup.kicad_pcb
```

6. Apply the same repair to the live PCB:

```powershell
C:\Program Files\KiCad\9.0\bin\python.exe - < live /+5V_PROTECTED cleanup payload
```

7. Post-edit DRC, hash, and final visuals:

```powershell
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_TRACE_AUDIT_DRC_POST.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side top --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\final_trace_by_trace_top.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --side bottom --width 1800 --height 1200 --quality basic --background transparent --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\final_trace_by_trace_bottom.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```
