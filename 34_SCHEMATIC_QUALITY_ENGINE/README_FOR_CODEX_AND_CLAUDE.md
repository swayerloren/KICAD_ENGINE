# README For Codex And Claude

If the task involves schematic creation, repair, readability cleanup, or
schematic-to-PCB readiness:

1. Read this folder.
2. Read `09_ACCURACY_ENGINE/schematic_rules/`.
3. Read `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`.
4. Run or review:
   - `03_TOOLS/scripts/kicad_schematic_checks/`
   - `03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py`
   - `03_TOOLS/scripts/schematic_layout/`
5. Do not claim PCB-update readiness from ERC alone.

## Canonical Results

- `SCHEMATIC_QUALITY_PASS`
- `SCHEMATIC_QUALITY_FAIL`
- `BLOCKED_UNTIL_HUMAN_REVIEW`
