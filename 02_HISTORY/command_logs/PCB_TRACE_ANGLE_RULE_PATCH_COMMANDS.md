# PCB Trace Angle Rule Patch Commands

Date: `2026-05-07`

Status: `ACTIVE_EVIDENCE`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb, 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch, 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro
Get-Content -Raw ...target memory/rule/prompt/intelligence files...
rg -n "TRACE_ANGLE_ROUTING_RULES|PCB_ROUTING_QUALITY_RULES|PCB_ROUTING_QUALITY_CHECKLIST|USER_CORRECTION_PCB_TRACE_ANGLE_ROUTING_QUALITY|GLOBAL_AGENT_MISTAKE_CRUDE_90_DEGREE_SCRIPTED_ROUTING" 01_MEMORY 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/pcb_intelligence .prompts/kicad_pipeline
Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"
Test-Path .prompts/kicad_pipeline/11_route_critical_nets.md
Test-Path .prompts/kicad_pipeline/12_route_remaining_nets.md
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
git diff --name-only -- 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/*.kicad_*
```

## Notes

- Multiple read-only `Get-Content`, `rg`, and `Test-Path` inspections were run across the exact files named in the user request.
- No KiCad design-file write commands were run.
- `git diff` was unavailable because this checkout is not a git working tree, so design-file confirmation relied on the session hash baseline plus the post-edit hash recheck.
