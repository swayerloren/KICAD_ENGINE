# AUTO_PCB_START_WORKFLOW_COMMANDS

Date: `2026-05-07`

## Commands Run

1. `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: maintenance not due.

2. `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter `2 -> 3`.

3. Read startup, workflow, sandbox, prompt-pack, and memory files with `Get-Content`.

4. `Get-ChildItem .prompts/kicad_pipeline`
   - Result: confirmed `07_update_pcb_from_schematic.md`, `08_pcb_mechanical_setup.md`, and `09_pcb_placement_pass_1.md` exist.

5. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
   - Result: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

6. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256`
   - Result: `CBF1473DBCD18ED370B1E121B9BCE91F422C269A1FC9D6AF4B369E12476E52C5`

7. `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256`
   - Result: `7F997C2B8B158BE3B837FA6B3C09694507D1AD372CE432C78CA1598EC25D412E`

8. `python 03_TOOLS/scripts/indexing/build_repo_index.py`
   - Result: completed.

9. `python 03_TOOLS/scripts/indexing/build_memory_index.py`
   - Result: completed.

10. `python 03_TOOLS/scripts/indexing/build_history_index.py`
    - Result: completed.

11. `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py`
    - Result: rebuilt `00_CODEX_START/AI_QUALITY_INDEX.generated.*`

12. `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py`
    - Result: rebuilt `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
