# ESP32_CSI_WIFI_NODE Q1 PMOS Pin Mapping Repair Command Log

Date: 2026-05-07  
Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read / Discovery

- Read required startup files and project reports.
- Searched project records for `AO3401A`.
- Reviewed Q1 schematic block in `ESP32_CSI_WIFI_NODE.kicad_sch`.
- Reviewed KiCad standard symbol `Transistor_FET:Q_PMOS_GSD`.
- Reviewed KiCad SOT-23 footprint pad numbering.

## Backup

```powershell
$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$src = Resolve-Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE'
$dst = Join-Path (Resolve-Path '99_BACKUPS\pre_codex_edits') "${ts}_ESP32_CSI_WIFI_NODE_pre_q1_pmos_pinmap_repair"
New-Item -ItemType Directory -Force -Path $dst
Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
```

Output:

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_102307_ESP32_CSI_WIFI_NODE_pre_q1_pmos_pinmap_repair`

## KiCad Commands

Before final verification, the open KiCad schematic and PCB editor windows were detected for the active project with no unsaved-title marker. They were closed gracefully because the open Eeschema session was overwriting the raw schematic repair back to the stale `Device:Q_PMOS` symbol.

ERC:

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch erc --format report --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\Q1_PMOS_PIN_MAPPING_REPAIR_ERC.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result:

```text
ERC messages: 0  Errors 0  Warnings 0
```

Netlist export:

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch export netlist --format kicadxml --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\Q1_PMOS_PIN_MAPPING_REPAIR.net' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Q1 netlist result:

```text
Q1 pin 1 = GND
Q1 pin 2 = /+5V_PROTECTED
Q1 pin 3 = /+5V_FUSED
```

PCB sync:

```powershell
# KiCad bundled Python / pcbnew
# Loaded PCB, loaded schematic netlist XML, updated footprint paths and pad nets, saved PCB.
```

PCB sync result:

```text
footprints_on_board=43
missing=
Q1 pad 1 net GND
Q1 pad 2 net /+5V_PROTECTED
Q1 pad 3 net /+5V_FUSED
updated_pads=146
```

DRC:

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb drc --schematic-parity --severity-all --format report --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_INITIAL_DRC_REPORT.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb'
```

Result:

```text
Found 13 violations
Found 78 unconnected items
Found 0 schematic parity issues
```

## Notes

No component placement, routing, copper zones, Gerbers, drills, BOM/CPL, STEP, or other fabrication outputs were generated.
