# Claim Evidence Matrix - PCB Trace Geometry Audit

Date: `2026-05-10`
Task type: `DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| The repo now has a dedicated read-only PCB geometry audit toolchain. | New files under `03_TOOLS/scripts/pcb_geometry/`. |
| The tool no longer relies only on net-wide track buckets; it extracts real routed path branches. | `tracks.json` and `tracks.md` show `39` extracted path branches with path lengths and direct lengths. |
| Routing-quality rules now require the geometry audit before calling a routed region acceptable. | Updated `TRACE_ANGLE_ROUTING_RULES.md`, `PCB_ROUTING_QUALITY_RULES.md`, `PCB_ROUTING_QUALITY_CHECKLIST.md`, `TRACE_PROJECTION_RULES.md`, `START_HERE_FOR_AI_AGENTS.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`. |
| The live `ESP32_CSI_WIFI_NODE` board fails the new geometry gate. | `trace_quality.json` and `trace_quality.md` report `status = FAIL`. |
| The live board currently has `29` right-angle findings and `1` acute-jog finding. | `trace_angles.json` and `trace_quality.json`. |
| The live board currently has `4` zigzag findings, `2` detour-ratio failures, and `3` TP stubs longer than `5 mm`. | `trace_quality.json` and `trace_quality.md`. |
| No tracked KiCad schematic or PCB source files changed in this task. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned no files; `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'` returned no tracked modifications. |
