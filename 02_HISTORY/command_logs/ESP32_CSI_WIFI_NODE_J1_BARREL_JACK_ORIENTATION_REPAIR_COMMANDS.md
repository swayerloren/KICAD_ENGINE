# ESP32_CSI_WIFI_NODE J1 Barrel Jack Orientation Repair Command Log

Date/time: `2026-05-07T13:49:21-04:00`

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

### Startup and rule reads

```powershell
Get-Content -Raw 'START_HERE_FOR_AI_AGENTS.md'
Get-Content -Raw 'AGENTS.md'
Get-Content -Raw 'FOR CHAT GPT.MD'
Get-Content -Raw 'README_GPT.md'
Get-Content -Raw '00_CODEX_START\START_HERE.md'
Get-Content -Raw '00_CODEX_START\CURRENT_PROJECT.md'
Get-Content -Raw '00_CODEX_START\PROMPT_COUNTER_RULES.md'
Get-Content -Raw '09_ACCURACY_ENGINE\pcb_rules\CONNECTOR_EDGE_ORIENTATION_RULES.md'
Get-Content -Raw '09_ACCURACY_ENGINE\pcb_rules\PCB_MECHANICAL_CLEARANCE_RULES.md'
Get-Content -Raw '09_ACCURACY_ENGINE\pcb_rules\PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md'
Get-Content -Raw '09_ACCURACY_ENGINE\checklists\PILL_STYLE_PLACEMENT_CHECKLIST.md'
```

### Prompt counter and maintenance

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result: counter reached `5`, maintenance ran, counter reset to `0`, maintenance due `NO`.

### Backup

```powershell
$ts=Get-Date -Format 'yyyyMMdd_HHmmss'
$src='04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE'
$dst="99_BACKUPS\pre_codex_edits\${ts}_ESP32_CSI_WIFI_NODE_pre_J1_barrel_orientation_repair"
New-Item -ItemType Directory -Path $dst -Force | Out-Null
Copy-Item -Path $src -Destination $dst -Recurse -Force
Write-Output $dst
```

Result: `99_BACKUPS\pre_codex_edits\20260507_134800_ESP32_CSI_WIFI_NODE_pre_J1_barrel_orientation_repair`

### Footprint and model inspection

```powershell
Get-Content -Raw 'C:\Program Files\KiCad\9.0\share\kicad\footprints\Connector_BarrelJack.pretty\BarrelJack_CUI_PJ-102AH_Horizontal.kicad_mod'
```

Result: pads are at local `Y=0`, `Y=3`, `Y=6`; body extends to local `Y=13.7/14.2`.

```powershell
Test-Path 'C:\Program Files\KiCad\9.0\share\kicad\3dmodels\Connector_BarrelJack.3dshapes\BarrelJack_CUI_PJ-102AH_Horizontal.step'
```

Result: `False`

### PCB edit

Edit method: `apply_patch`

Changed only this J1 parent footprint line:

```diff
- (at 14 93.2 180)
+ (at 14 80.8)
```

### DRC

```powershell
kicad-cli pcb drc '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\J1_BARREL_JACK_ORIENTATION_REPAIR_DRC.rpt' --format report --schematic-parity --severity-all
```

Console output was redirected to:

`reports\J1_BARREL_JACK_ORIENTATION_REPAIR_DRC.console.txt`

Result: 12 DRC violations, 78 unconnected items, 0 schematic parity issues.

### Visual evidence

```powershell
kicad-cli pcb export svg '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\j1_barrel_orientation_repair_top.svg' --layers F.Cu,F.Fab,F.SilkS,F.CrtYd,Edge.Cuts --page-size-mode 2
kicad-cli pcb export svg '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\j1_barrel_orientation_repair_bottom.svg' --layers B.Cu,B.Fab,B.SilkS,B.CrtYd,Edge.Cuts --page-size-mode 2
kicad-cli pcb render '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\j1_barrel_orientation_repair_3d_bottom_front.png' --side front --width 1600 --height 900 --quality basic --background opaque --zoom 1.8
kicad-cli pcb render '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\j1_barrel_orientation_repair_3d_top.png' --side top --width 1600 --height 900 --quality basic --background opaque --zoom 1.5
```

Note: an initial `render --pan` attempt failed because KiCad CLI parsed the negative pan vector as an argument. The render was rerun successfully without `--pan`.

## Prohibited Actions

- Schematic edited: `NO`
- Routing performed: `NO`
- Copper zones created: `NO`
- Gerbers/BOM/CPL/drill/STEP/JLCPCB files generated: `NO`

## Final Validation

```powershell
@'
# Read-only PCB parse for J1 transformed coordinates and routing/zone counts.
'@ | python -
```

Result:

- `J1_FINAL at=(14.0,80.8) rotation=0.0`
- `pad1_back=(14.000,80.800)`
- `pad2_back=(14.000,86.800)`
- `pad3_back=(18.700,83.800)`
- `female_opening_fab=(14.000,94.500)`
- `female_opening_courtyard=(14.000,95.000)`
- `top_level_segments 0`
- `top_level_zones 0`
- `top_level_vias 0`

```powershell
$cutoff=Get-Date '2026-05-07 13:47:50'
Get-ChildItem -Recurse -File -Include *.kicad_sch,*.kicad_pcb,*.kicad_pro,*.kicad_sym,*.kicad_mod,sym-lib-table,fp-lib-table | Where-Object { $_.LastWriteTime -gt $cutoff } | Select-Object FullName,LastWriteTime
```

Result: only `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb` changed among KiCad design files after the repair started.

```powershell
git status --short
```

Result: `fatal: not a git repository (or any of the parent directories): .git`

Git status was unavailable from this workspace.
