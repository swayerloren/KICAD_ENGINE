# Hallucination Risk Log: ESP32 CSI Actual KiCad Annotation Repair

Date: `2026-05-06`

Risk label: `MEDIUM_RISK`

## Risk

The main risk is overclaiming annotation success beyond the evidence. The current evidence proves saved-file and local `kicad-cli` ERC status, but not live KiCad GUI state if the GUI has stale cached content.

## Controls Applied

- Did not rely on prior PASS reports.
- Did not rely only on regex scans.
- Parsed placed-symbol structures and added instance refs.
- Ran local KiCad CLI ERC.
- Created final reference table and duplicate summaries.
- Kept schematic-to-PCB gate failed.
- Explicitly stated GUI reload requirement.

## Claims Not Made

- Did not claim visual readability pass.
- Did not claim footprint verification pass.
- Did not claim PCB update is allowed.
- Did not claim manufacturing readiness.

## Final Status

Annotation evidence: `PASS_BY_KICAD_CLI_ERC_AND_STRUCTURED_REFERENCE_TABLE`

Project gate: `BLOCKED_UNTIL_HUMAN_REVIEW`
