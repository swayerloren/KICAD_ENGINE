# PCB Final Routing Completion Commands

Date: 2026-05-09
Project: `ESP32_CSI_WIFI_NODE`

## Main Commands Run

```powershell
git status --short
```

```powershell
python - <<'PY'
from pathlib import Path
import hashlib
p = Path(r'c:/Users/LJ/GitHub/KICAD_ENGINE/04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb')
print(hashlib.sha1(p.read_bytes()).hexdigest())
PY
```

```powershell
kicad-cli pcb drc --format json --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_DRC_BASELINE.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

## Copied-Board Trial Pattern

Each copied-board rehearsal used the same basic pattern:

```powershell
New-Item -ItemType Directory -Path $trial
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb $trial\ESP32_CSI_WIFI_NODE.kicad_pcb
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro $trial\ESP32_CSI_WIFI_NODE.kicad_pro
python 03_TOOLS\scripts\pcb_routing\esp32_csi_manual_route_trials_20260509.py $trial\ESP32_CSI_WIFI_NODE.kicad_pcb apply --trial <trial_name>
kicad-cli pcb drc --format json --output $trial\drc.json $trial\ESP32_CSI_WIFI_NODE.kicad_pcb
```

## Trial Names Used

- `usb_top`
- `tp1_diag`
- `tp1_alt`
- `dp_e_manual`
- `boot0_manual`
- `esp_en_manual`
- `controls_rework`
- `right_fanout_rework`

## Additional Read/Inspection Commands

- `Get-Content` on the active routing reports
- `Get-Content` on existing route scripts under `03_TOOLS/scripts/pcb_routing/`
- `rg` searches on the `.kicad_pcb` file for net IDs and segment blocks
- SVG and PNG rendering commands for quick local board visualization

## Final Verification Command

```powershell
kicad-cli pcb drc --format json --output %TEMP%\esp32_live_drc_final_check.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```
