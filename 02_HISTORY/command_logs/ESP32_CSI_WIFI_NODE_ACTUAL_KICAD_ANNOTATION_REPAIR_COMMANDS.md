# ESP32_CSI_WIFI_NODE Actual KiCad Annotation Repair Commands

Date: `2026-05-06`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Startup Reads

```powershell
Get-Content -Path 'AGENTS.md' -Raw
Get-Content -Path 'README_GPT.md' -Raw
Get-Content -Path 'FOR CHAT GPT.MD' -Raw
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ERC_AFTER_ANNOTATION_REPAIR.md' -Raw
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\EMERGENCY_ANNOTATION_REPAIR_REPORT.md' -Raw
Get-Content -Path '02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_EMERGENCY_ANNOTATION_REPAIR_COMMANDS.md' -Raw
```

## Native Annotation Availability Check

```powershell
kicad-cli sch --help
```

Result: no schematic annotation subcommand was exposed by local `kicad-cli`.

## Backup And Hash

```powershell
New-Item -ItemType Directory -Force -Path '99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair'
Copy-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' '99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair\ESP32_CSI_WIFI_NODE.kicad_sch'
Copy-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' '99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair\ESP32_CSI_WIFI_NODE.kicad_pro'
Get-FileHash -Algorithm SHA256 '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-FileHash -Algorithm SHA256 '99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result:

- current pre-repair hash: `E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7`
- backup hash: `E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7`

## Structured S-Expression Repair

```powershell
# Inline Python script parsed placed-symbol S-expressions, updated actual Reference properties,
# added matching instances blocks, and wrote reports/ANNOTATION_REPAIR_ACTUAL_KICAD_CHANGES.json.
```

Result:

```json
{
  "placed_symbols": 79,
  "changed_count": 79,
  "pwr": 33,
  "flg": 3
}
```

Post-repair hash:

`D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`

## ERC

```powershell
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: `Found 0 violations`

## Reference Validation

```powershell
rg -n '(J\?|R\?|C\?|D\?|U\?|Q\?|F\?|SW\?|TP\?|MH\?|L\?|Y\?|#PWR\?|#FLG\?)' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: no matches.

```powershell
# Inline Python script exported placed symbol table and duplicate summary to:
# reports/ANNOTATION_REFERENCE_TABLE_FINAL.md
# reports/ANNOTATION_REFERENCE_TABLE_FINAL.json
```

Result summary:

- placed symbols: `79`
- physical symbols: `43`
- power symbols: `33`
- PWR_FLAG symbols: `3`
- unresolved question refs: `0`
- missing instances: `0`
- instance mismatches: `0`
- duplicate physical refs: `0`
- duplicate `#PWR` refs: `0`
- duplicate `#FLG` refs: `0`

## Schematic Exports

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '03_TOOLS\kicad\run_schematic_visual_check.ps1' -ProjectRoot '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE' -SchematicPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' -NoFailOnFindings
```

Result:

- full SVG/PDF/PNG exports generated
- close-up crops generated
- automated crop status only: `AUTOMATED_CROP_PASS_ONLY`
- human-readable visual status: `NOT_VERIFIED`

## Final Report Writes

```powershell
# Created/updated:
# reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md
# reports/SCHEMATIC_TO_PCB_GATE_STATUS.md
# 02_HISTORY/sessions/ESP32_CSI_WIFI_NODE_ACTUAL_KICAD_ANNOTATION_REPAIR_SESSION.md
# 02_HISTORY/command_logs/ESP32_CSI_WIFI_NODE_ACTUAL_KICAD_ANNOTATION_REPAIR_COMMANDS.md
# 02_HISTORY/quality_gate_failures/ESP32_CSI_PRIOR_FALSE_ANNOTATION_PASS_CONFIRMED.md
```

## Final Validation

```powershell
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
rg -n '(J\?|R\?|C\?|D\?|U\?|Q\?|F\?|SW\?|TP\?|MH\?|L\?|Y\?|#PWR\?|#FLG\?)' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-Content '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REFERENCE_TABLE_FINAL.json' -Raw | ConvertFrom-Json
```

Result:

- KiCad ERC: `Found 0 violations`
- unresolved reference `rg` scan: no matches
- reference table summary: 79 placed symbols, 43 physical symbols, 33 power symbols, 3 PWR_FLAG symbols, 0 unresolved refs, 0 missing instances, 0 instance mismatches, 0 duplicate physical refs, 0 duplicate `#PWR` refs, 0 duplicate `#FLG` refs.
