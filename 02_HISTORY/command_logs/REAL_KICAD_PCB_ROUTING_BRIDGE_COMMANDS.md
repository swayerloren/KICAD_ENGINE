# REAL_KICAD_PCB_ROUTING_BRIDGE_COMMANDS

Date: `2026-05-07`

## Key Commands

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

```powershell
@'
import pcbnew
print(pcbnew.Version())
'@ | & 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

```powershell
python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py 14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_extract.py 14_LAYOUT_AUTOMATION/scripts/extract_kicad_nets_pads.py 14_LAYOUT_AUTOMATION/scripts/extract_kicad_tracks_vias.py 14_LAYOUT_AUTOMATION/scripts/extract_kicad_zones_keepouts.py 14_LAYOUT_AUTOMATION/scripts/extract_kicad_net_classes.py 14_LAYOUT_AUTOMATION/scripts/extract_kicad_pcb_to_routing_schema.py 14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py 14_LAYOUT_AUTOMATION/scripts/_routing_common.py 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/extract_kicad_tracks_vias.py 32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/m4a1x_tps5430/TPS5430.kicad_pcb 14_LAYOUT_AUTOMATION/real_board_tests/outputs/tps5430_tracks_vias.json --markdown 14_LAYOUT_AUTOMATION/real_board_tests/outputs/tps5430_tracks_vias.md
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/extract_kicad_net_classes.py 32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/m4a1x_tps5430/TPS5430.kicad_pcb 14_LAYOUT_AUTOMATION/real_board_tests/outputs/tps5430_net_classes.json --markdown 14_LAYOUT_AUTOMATION/real_board_tests/outputs/tps5430_net_classes.md
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/extract_kicad_pcb_to_routing_schema.py 32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/hardware/esp-rust-board/esp-rust-board.kicad_pcb 14_LAYOUT_AUTOMATION/real_board_tests/outputs/esp_rust_board/routing_schema.json --markdown 14_LAYOUT_AUTOMATION/real_board_tests/outputs/esp_rust_board/routing_schema.md
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py 32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/hardware/esp-rust-board/esp-rust-board.kicad_pcb 14_LAYOUT_AUTOMATION/real_board_tests/outputs/esp_rust_board --report-json 14_LAYOUT_AUTOMATION/real_board_tests/reports/esp_rust_board_summary.json --report-markdown 14_LAYOUT_AUTOMATION/real_board_tests/reports/esp_rust_board_summary.md
```

```powershell
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256
```

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "real KiCad PCB routing bridge tooling task" --apply
python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
```
