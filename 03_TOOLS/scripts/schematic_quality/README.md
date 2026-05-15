# Schematic Quality Scripts

This folder contains the read-only script layer for the schematic quality
engine.

## Purpose

These scripts enforce more than ERC:

- readable functional-block flow
- local wiring where appropriate
- controlled net-label use
- annotation sanity
- footprint readiness
- estimated text overlap detection
- explicit human-visual and native-annotation gate checks before PCB update

## Read-Only Rule

- Audit scripts never edit KiCad design files by default.
- This folder currently provides audit and report scripts only.
- If future cleanup helpers are added, they must require explicit `--apply`.
- Audit scripts must not accept silent write modes.

## Scripts

- `extract_schematic_symbols.py`
- `audit_schematic_annotation.py`
- `audit_schematic_footprints.py`
- `audit_schematic_text_overlaps.py`
- `audit_schematic_block_layout.py`
- `audit_wire_vs_label_balance.py`
- `check_schematic_human_drafting_quality.py`
- `generate_schematic_quality_report.py`
- `run_schematic_quality_gate.py`

## Example

```powershell
python 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --no-fail

python 03_TOOLS\scripts\schematic_quality\check_schematic_human_drafting_quality.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --output-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_quality\human_drafting `
  --warn-only
```

## Output

The gate writes per-audit JSON and Markdown plus a combined quality report
under:

`reports/schematic_quality/<timestamp>/`

The human-drafting checker writes paired JSON and Markdown reports and focuses
on:

- top-level graphic items near electrical nets
- local label classification and avoidable label shortcuts
- orientation-before-label heuristics
- MCU local support physical-wiring review
- reset/boot topology sanity beyond ERC
- reference/value text ownership heuristics
- suspicious local loopback or S-shaped wires
- local return clusters that visually read like GND but are not on GND
