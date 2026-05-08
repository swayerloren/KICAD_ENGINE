# Memory History Cleanup Commands

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:42:00-04:00`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: command outputs observed during cleanup.

Current relevance: command log for the requested cleanup/classification/indexing run.

## Commands Run

```powershell
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply --json-output 05_OUTPUTS\release_readiness\memory_history_cleanup_apply_result.json
```

Result: apply succeeded.

```text
Duplicate topics: routing 287, pcb_update 172, no_pcb 140, footprint 552, jlcpcb 63, not_final 33, placement 169, q1 22, visual_pass 10, schematic_gate 3, pcb_sync 16.
Stale/superseded reports: 94.
False-pass incidents: 58.
Relative-date hits: 422.
```

```powershell
python 03_TOOLS\scripts\memory_maintenance\rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS\scripts\memory_maintenance\rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
```

Result: memory/history indexes and current-known-problems were rebuilt.

```powershell
Get-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch,
         04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb,
         04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro
```

Result: design-file timestamps predate the cleanup writes. No KiCad design-edit commands were run.

## Safety Notes

- No `.kicad_sch` files edited.
- No `.kicad_pcb` files edited.
- No `.kicad_pro` files edited.
- No routing.
- No zones.
- No fabrication outputs.
