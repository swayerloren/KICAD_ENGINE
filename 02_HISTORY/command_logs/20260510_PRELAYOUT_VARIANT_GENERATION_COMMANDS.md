# Prelayout Variant Generation Commands

## Commands Run

- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/pcb_prelayout/run_prelayout_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/prelayout_variants/20260510_093811/engine_gate`
- `python 03_TOOLS/scripts/mechanical_orientation/audit_connector_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json ... --markdown ...`
- `python 03_TOOLS/scripts/mechanical_orientation/audit_barrel_jack_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json ... --markdown ...`
- `python 03_TOOLS/scripts/mechanical_orientation/audit_usb_c_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json ... --markdown ...`
- `python 03_TOOLS/scripts/mechanical_orientation/audit_esp32_antenna_orientation.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-json ... --markdown ...`
- `python 03_TOOLS/scripts/pcb_geometry/audit_trace_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --output-dir 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/prelayout_variants/20260510_093811/live_trace_geometry`
- `python -m py_compile 03_TOOLS/scripts/pcb_prelayout/_prelayout_common.py 03_TOOLS/scripts/pcb_prelayout/generate_placement_variants.py 03_TOOLS/scripts/pcb_prelayout/project_routes_45deg.py 03_TOOLS/scripts/pcb_prelayout/render_variant_preview.py 03_TOOLS/scripts/pcb_prelayout/compare_variants.py`
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`

## Important Results

- Maintenance due check: `NO`
- Prompt counter increment: `2 -> 3`
- Live-state validation: routing phase remains blocked by 13 unconnected items and 3 detectable unrouted nets
- Prelayout gate: `BLOCKED`, selected `VARIANT_B`
- Orientation audits: `J1 NEEDS_HUMAN_REVIEW`, `J2 PASS`, `U2 PASS`
- Live trace geometry audit: `FAIL` with 39 findings
- No `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` changes detected by git diff
