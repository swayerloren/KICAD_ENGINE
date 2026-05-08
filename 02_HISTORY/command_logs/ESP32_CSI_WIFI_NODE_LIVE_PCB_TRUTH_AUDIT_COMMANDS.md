# ESP32_CSI_WIFI_NODE_LIVE_PCB_TRUTH_AUDIT_COMMANDS

Date: `2026-05-07`

## Key Commands

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

```powershell
Get-Item 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb | Select-Object FullName, Length, LastWriteTime
```

```powershell
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/live_pcb_truth_audit/real_board_routing_audit --report-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/live_pcb_truth_audit/real_board_routing_audit_summary.json --report-markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/live_pcb_truth_audit/real_board_routing_audit_summary.md
```

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/live_pcb_truth_audit/LIVE_PCB_TRUTH_AUDIT_DRC.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
kicad-cli pcb export svg --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual/live_pcb_truth_audit/top.svg 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
kicad-cli pcb export svg --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual/live_pcb_truth_audit/bottom.svg 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 2
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 3
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 5
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8
```

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "live PCB truth audit and stale gate reconciliation" --apply
```

```powershell
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
```

```powershell
git status --short
```

## Notes

- DRC ran read-only and reported `12` violations plus `65` unconnected items.
- Visual exports and close-up crops were created for the live board review packet.
- No KiCad design-file writes were performed.
- `git status --short` was attempted for final workspace inspection but failed because `C:\Users\LJ\GitHub\KICAD_ENGINE` is not currently a Git working tree root.
