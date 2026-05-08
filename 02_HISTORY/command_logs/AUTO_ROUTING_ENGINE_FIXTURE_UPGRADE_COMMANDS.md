# AUTO_ROUTING_ENGINE_FIXTURE_UPGRADE_COMMANDS

Date: `2026-05-07`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content -Path "AGENTS.md" -TotalCount 260
Get-Content -Path "README_GPT.md" -TotalCount 220
Get-Content -Path "FOR CHAT GPT.MD" -TotalCount 220
Get-Content -Path "00_CODEX_START/START_HERE.md","00_CODEX_START/SESSION_START_CHECKLIST.md","00_CODEX_START/STRUCTURE_STANDARD.md","00_CODEX_START/FOLDER_ROUTING_RULES.md","00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md","00_CODEX_START/MEMORY_INDEX.md","00_CODEX_START/HISTORY_INDEX.md" -TotalCount 120
Get-Content -Path "00_CODEX_START/WORKFLOW_RULES.md","00_CODEX_START/SAFETY_RULES.md","00_CODEX_START/CONTROL_PLANES.md","00_CODEX_START/REPO_STRUCTURE_INDEX.md","00_CODEX_START/CURRENT_PROJECT.md","00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md","00_CODEX_START/AI_RESPONSE_QUALITY_GATE.md" -TotalCount 120
Get-Content -Path "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md","04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md" -TotalCount 160
Get-Content -Path "14_LAYOUT_AUTOMATION/AUTO_ROUTING_ENGINE.md","14_LAYOUT_AUTOMATION/TRACE_PLANNING_RULES.md","14_LAYOUT_AUTOMATION/CRITICAL_NET_ROUTING_RULES.md","14_LAYOUT_AUTOMATION/POWER_TRACE_RULES.md","14_LAYOUT_AUTOMATION/USB_TRACE_RULES.md","14_LAYOUT_AUTOMATION/RF_KEEP_OUT_TRACE_RULES.md","14_LAYOUT_AUTOMATION/VIA_STRATEGY_RULES.md","14_LAYOUT_AUTOMATION/GROUND_STITCHING_RULES.md","14_LAYOUT_AUTOMATION/TRACE_BY_TRACE_VERIFICATION_RULES.md" -TotalCount 220
Get-Content -Path "14_LAYOUT_AUTOMATION/scripts/README.md","14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py","14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py","14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py" -TotalCount 260
Get-Content -Path "14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py","14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py","14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py" -TotalCount 260
Get-Content -Path "14_LAYOUT_AUTOMATION/scripts/_routing_common.py" -TotalCount 320
python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_routing_common.py 14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py 14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py 14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
```

Fixture execution sequence:

```powershell
python 14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py <fixture.json> <routing_plan.json> --markdown <routing_plan.md>
python 14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py <routing_plan.json> <critical_plan.json> --markdown <critical_plan.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py <fixture.json> <unrouted.json> --markdown <unrouted.md>
python 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py <fixture.json> <keepouts.json> --markdown <keepouts.md>
python 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py <fixture.json> <trace_audit.json> --markdown <trace_audit.md>
python 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py <fixture.json> <routing_plan.json> <critical_plan.json> <unrouted.json> <keepouts.json> <trace_audit.json> <score.json> --markdown <score.md>
```

Final validation:

```powershell
python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_routing_common.py 14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py 14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py 14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py
Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb","04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch","04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro"
```

## Key Results

- Prompt counter: `2 -> 3`
- Maintenance due: `NO`
- Script syntax check: `PASS`
- Fixture matrix: `3 PASS`, `1 AUTO_BLOCKED_BAD_LAYOUT`
- No KiCad design files edited
