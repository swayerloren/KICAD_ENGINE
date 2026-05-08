# KiCad Schematic Checks

## Purpose

This folder contains read-only schematic screeners for annotation, completeness, BOM-lock alignment, and unresolved review markers. Codex/Claude must use these before treating a schematic as ready for PCB update or layout.

The scripts parse `.kicad_sch` files directly. They do not edit KiCad design files, do not update PCB files, do not assign footprints, and do not approve fabrication outputs.

## Scripts

- `check_schematic_annotation.py`: checks reference designators, duplicate references, blank values, missing fields, footprint assignment, category/reference mismatches, and high-risk parts without verification status.
- `check_schematic_completeness.py`: checks required functional blocks such as power input, protection, regulator, MCU/module, USB-C when required, ESD, boot/reset, test pads, mounting holes, notes, and expected BOM lock items.
- `check_bom_lock_alignment.py`: compares parseable BOM lock reference designators against schematic references.
- `check_needs_review_markers.py`: finds unresolved `NEEDS_REVIEW`, `BLOCKED`, `UNVERIFIED`, `TODO`, or `TBD` markers and high-risk symbols without explicit review/verification state.

## Example

```powershell
python .\03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py `
  --schematic ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --bom-lock ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\PRE_SCHEMATIC_BOM_LOCK.md" `
  --output ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ANNOTATION_CHECK.md" `
  --json-output ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ANNOTATION_CHECK.json"
```

Add `--no-fail` when generating exploratory reports during setup. Without `--no-fail`, scripts return a non-zero exit code if blocking failures are found.

## Gate Rule

The schematic-to-PCB gate must remain blocked if any required checker reports `FAIL`, missing evidence, unresolved `NEEDS_REVIEW`, missing BOM-lock coverage, duplicated references, unassigned footprints, or high-risk parts without verification status.

## Limits

- The parser is intentionally conservative and read-only.
- BOM-lock parsing is heuristic because project BOM-lock formats may vary.
- These scripts do not prove footprint correctness, connector orientation, pinout correctness, ERC cleanliness, DRC cleanliness, or fabrication readiness.
- Human review is still required for connector orientation, polarity-sensitive parts, exact package drawings, USB/RF/CAN layout details, and manufacturing output approval.
