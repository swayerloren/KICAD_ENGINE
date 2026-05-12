# ESP32_CSI_WIFI_NODE Schematic Visual Cleanup Commands

Date: `2026-05-10`
Project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Commands

1. Increment prompt counter:
   `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply`
2. Verify GUI state before live edit:
   `python 33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py --project ... --schematic ... --dry-run`
3. Dry-run the native annotation workflow:
   `03_TOOLS\python_envs\windows_gui\Scripts\python.exe 33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py --project ... --schematic ...`
4. Create backup and record pre-edit schematic hash.
5. Apply live cleanup pass:
   `python 03_TOOLS\scripts\schematic_layout\apply_esp32_visual_cleanup.py`
6. Attempt live native annotation proof:
   `03_TOOLS\python_envs\windows_gui\Scripts\python.exe 33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py --project ... --schematic ... --live --allow-annotation --allow-save --allow-gui-erc --evidence-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\native_annotation_after_visual_cleanup`
7. Export full-page schematic visuals and crops:
   `powershell -ExecutionPolicy Bypass -File 03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -NoFailOnFindings`
8. Run first live ERC / quality / readability checks.
9. Repair local post-cleanup regressions:
   `python 03_TOOLS\scripts\schematic_layout\fix_post_cleanup_regressions.py`
10. Rerun final ERC:
   `kicad-cli sch erc --format report --severity-all --units mm -o 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_visual_cleanup_20260510_1319\erc_after_visual_cleanup.report.txt 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
11. Rerun final schematic quality gate:
   `python 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_visual_cleanup_20260510_1319\quality_gate --no-fail`
12. Rerun final readability score:
   `python 03_TOOLS\scripts\schematic_layout\score_schematic_readability.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --report-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_visual_cleanup_20260510_1319\readability --no-fail`

## Important Results

- Native annotation live attempt result: `BLOCKED_EESCHEMA_NOT_READY`
- Final ERC result: `PASS`
- Final readability score: `74 / 100`
- Final quality gate result: `FAIL`
