# AUTO_ROUTING_ENGINE_COMMANDS

Date: `2026-05-07`

## Commands Run

1. `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: maintenance not due at counter `4`.

2. `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter `4 -> 5`, maintenance due `YES`.

3. `python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: project maintenance completed and current-state files updated.

4. `python 03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter reset to `0`.

5. Read requested routing/layout rule files with `Get-Content`.

6. `Get-ChildItem 14_LAYOUT_AUTOMATION`
   - Result: confirmed layout-automation surface.

7. `Get-ChildItem 14_LAYOUT_AUTOMATION/scripts`
   - Result: confirmed script surface before adding routing scripts.

8. `Get-ChildItem 03_TOOLS/scripts/pcb_routing`
   - Result: confirmed existing project-specific routing scripts.

9. `python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_routing_common.py 14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py 14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py 14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py 14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py 14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py 14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py`
   - Result: passed.

10. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
    - Result: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

11. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256`
    - Result: `CBF1473DBCD18ED370B1E121B9BCE91F422C269A1FC9D6AF4B369E12476E52C5`

12. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256`
    - Result: `7F997C2B8B158BE3B837FA6B3C09694507D1AD372CE432C78CA1598EC25D412E`
