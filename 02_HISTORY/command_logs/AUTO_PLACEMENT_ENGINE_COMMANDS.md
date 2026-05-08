# AUTO_PLACEMENT_ENGINE_COMMANDS

Date: `2026-05-07`

## Commands Run

1. `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: maintenance not due.

2. `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter `3 -> 4`.

3. Read requested startup and rule files with `Get-Content`.

4. `Get-ChildItem 14_LAYOUT_AUTOMATION`
   - Result: confirmed current layout-automation folder contents.

5. `Get-ChildItem 34_PCB_LAYOUT_SANDBOX/scripts`
   - Result: confirmed prior sandbox script surface for consistency.

6. `python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_placement_common.py 14_LAYOUT_AUTOMATION/scripts/generate_placement_constraints.py 14_LAYOUT_AUTOMATION/scripts/place_fixed_mechanical_parts.py 14_LAYOUT_AUTOMATION/scripts/place_component_groups.py 14_LAYOUT_AUTOMATION/scripts/detect_placement_collisions.py 14_LAYOUT_AUTOMATION/scripts/score_component_placement.py`
   - Result: passed.

7. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
   - Result: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

8. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256`
   - Result: `CBF1473DBCD18ED370B1E121B9BCE91F422C269A1FC9D6AF4B369E12476E52C5`

9. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256`
   - Result: `7F997C2B8B158BE3B837FA6B3C09694507D1AD372CE432C78CA1598EC25D412E`
