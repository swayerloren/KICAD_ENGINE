# ESP32_CSI_WIFI_NODE_EXISTING_TRACE_AUDIT_COMMANDS

Date: `2026-05-07`

## Key Commands

```powershell
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/current_existing_trace_audit_drc.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/current_existing_trace_audit --report-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/current_existing_trace_audit_summary.json --report-markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/current_existing_trace_audit_summary.md
```

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "existing trace audit on live PCB" --apply
```

```powershell
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
```

## Notes

- No KiCad design-file writes were performed.
- The refreshed trace audit reproduced the same live routing blockers as the earlier truth audit.
