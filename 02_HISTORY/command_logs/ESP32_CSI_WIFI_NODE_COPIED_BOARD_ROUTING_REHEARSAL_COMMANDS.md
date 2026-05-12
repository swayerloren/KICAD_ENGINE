# ESP32_CSI_WIFI_NODE Copied Board Routing Rehearsal Commands

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Core Commands

### Placement-readiness precheck

Reviewed:

- `reports/PLACEMENT_READINESS_SCORECARD.md`
- `config/pcb_routing_constraints.yaml`
- `pcb_intelligence/ROUTING_SEQUENCE_PLAN.md`
- `pcb_intelligence/USB_ROUTING_PLAN.md`
- `pcb_intelligence/POWER_TREE_AND_RETURN_PATHS.md`
- `pcb_intelligence/TRACE_WIDTH_AND_NET_CLASS_PLAN.md`

### Tool availability

Reviewed tool availability for:

- `kicad-cli`
- `java`
- `KiCadRoutingTools`
- `FreeRouting`

### Copied-board routing candidates

Executed on copied boards:

```powershell
python 03_TOOLS\scripts\pcb_routing\esp32_csi_grid_route_pass.py <candidate_B_pcb>
python 03_TOOLS\scripts\pcb_routing\esp32_csi_esp_routing_via_repair_20260509.py <candidate_C_pcb> apply
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py <candidate_C_pcb> dp_e_manual
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py <candidate_C_pcb> usb_top
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py <candidate_C_pcb> tp1_diag
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py <candidate_D_pcb> controls_rework
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py <candidate_D_pcb> usb_top
```

### Candidate audit and quality gate

Executed for each copied candidate:

```powershell
python 14_LAYOUT_AUTOMATION\scripts\run_real_board_routing_audit.py <candidate_pcb> <candidate_routing_audit_dir> --report-json <candidate_summary_json> --report-markdown <candidate_summary_md>
python 03_TOOLS\scripts\pcb_quality\run_pcb_quality_gate.py --project <candidate_root> --output-dir <candidate_gate_dir> --no-fail
```

### Visual export

Executed for copied routed candidate previews:

```powershell
kicad-cli pcb render --side top <candidate_pcb> --output <preview_top_png>
kicad-cli pcb render --side bottom <candidate_pcb> --output <preview_bottom_png>
```

### Post-run verification

Executed:

```powershell
Get-FileHash <real_pcb> -Algorithm SHA256
Get-FileHash <real_sch> -Algorithm SHA256
Get-FileHash <real_pro> -Algorithm SHA256
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```
