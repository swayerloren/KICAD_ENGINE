# Claim Evidence Matrix - Mechanical Orientation Truth

Date: `2026-05-10`
Task type: `DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| The repo now has a dedicated mechanical orientation truth layer. | New files under `08_COMPONENT_DATABASE/mechanical_orientation/`. |
| The repo now has read-only audit scripts for connector, barrel-jack, USB-C, and ESP32 antenna orientation. | New files under `03_TOOLS/scripts/mechanical_orientation/`; `python -m py_compile ...` passed. |
| Connector truth now distinguishes port opening, pin side, body side, edge direction, and 3D-proof status. | `connector_orientation_truth.json`, `_mechanical_orientation_common.py`, and `33_PCB_PRELAYOUT_ENGINE/CONNECTOR_MECHANICAL_TRUTH_SCHEMA.md`. |
| The active board now treats `J1` differently from `J2` instead of inferring both from XY/rotation alone. | `20260510_connector_orientation_audit.json` shows `J2` `PASS` with `MODEL_PRESENT`, while `J1` is `NEEDS_HUMAN_REVIEW` with `MODEL_FILE_MISSING_OR_UNRESOLVED`. |
| The ESP32 antenna outward-facing rule is enforced. | `20260510_esp32_antenna_orientation_audit.json` records `U2` `PASS` with outward edge `top`. |
| Prelayout scoring now blocks variants when connector proof is incomplete. | `20260510_090120/scores/variant_01.score.json` records `CONNECTOR_ORIENTATION_NEEDS_HUMAN_REVIEW` and `status = FAIL`. |
| No tracked KiCad schematic or PCB source file changed in this task. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned no files; `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'` returned no tracked modifications. |
