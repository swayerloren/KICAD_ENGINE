# PCB Trace Geometry Audit Commands

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Commands Run

1. `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - Result: prompt counter incremented before meaningful project work.
2. `python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - Result: `MAINTENANCE_DUE: NO`.
3. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_pcb_trace_geometry_audit_task_contract.json`
   - Result: valid `DOCS_ONLY` contract.
4. `python -m py_compile 03_TOOLS\scripts\pcb_geometry\_pcb_geometry_common.py 03_TOOLS\scripts\pcb_geometry\extract_tracks.py 03_TOOLS\scripts\pcb_geometry\audit_trace_angles.py 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py 03_TOOLS\scripts\pcb_geometry\audit_power_loop_geometry.py 03_TOOLS\scripts\pcb_geometry\audit_usb_pair_geometry.py 03_TOOLS\scripts\pcb_geometry\render_trace_quality_overlays.py`
   - Result: syntax check passed.
5. `python 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit`
   - Result: workflow ran successfully and returned board status `FAIL` with `39` findings.
6. `python 03_TOOLS\scripts\pcb_geometry\audit_trace_angles.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/tracks.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/trace_angles_wrapper.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/trace_angles_wrapper.md`
   - Result: wrapper script ran and returned `FAIL` with `30` angle findings.
7. `python 03_TOOLS\scripts\pcb_geometry\render_trace_quality_overlays.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/tracks.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/trace_quality.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/trace_quality_overlay_wrapper.svg --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_geometry/20260510_trace_geometry_audit/trace_quality_overlay_wrapper.md`
   - Result: wrapper script ran and returned `PASS`.
8. `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_pcb_trace_geometry_audit_task_contract.json`
   - Result: updated contract remained valid with `changed_file_count = 17`.
9. `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .`
   - Result: startup repo index rebuilt after structure changes.
10. `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .`
   - Result: memory indexes rebuilt.
11. `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .`
   - Result: history indexes rebuilt.
12. `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .`
   - Result: AI-quality indexes rebuilt.
13. `python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .`
   - Result: `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt.
14. `Remove-Item -Recurse -Force 03_TOOLS\scripts\pcb_geometry\__pycache__`
   - Result: local Python cache folder removed from the new tool directory after validation.
15. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'`
   - Result: no tracked KiCad source diffs.
16. `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'`
   - Result: no tracked KiCad source modifications.
