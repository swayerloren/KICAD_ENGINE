# Schematic Quality Engine

This folder defines the mandatory schematic readability and readiness gate for
KiCad Engine.

## Purpose

ERC alone is not enough. A schematic must also be readable, professionally
grouped, visually clean, natively annotated, footprint-ready, and evidence-backed
before PCB update.

## What This Engine Enforces

- functional blocks grouped intentionally
- left-to-right or top-to-bottom flow
- local wires inside local blocks
- labels reserved for cross-block or long-distance connections
- clean reference/value text placement
- no visible unresolved `?` references
- no visible `NEEDS_REVIEW` values on symbols unless carried intentionally in a
  documented review workflow
- every physical part has a footprint before PCB update
- native KiCad annotation proof
- ERC proof
- human-readable visual proof

## Main Files

- `SCHEMATIC_READABILITY_STANDARD.md`
- `SCHEMATIC_BLOCK_LAYOUT_RULES.md`
- `SCHEMATIC_WIRING_VS_LABEL_RULES.md`
- `SCHEMATIC_LAYOUT_ALGORITHM.md`
- `FUNCTIONAL_BLOCK_TEMPLATES.md`
- `LOCAL_WIRING_STYLE_GUIDE.md`
- `VISUAL_READABILITY_SCORECARD.md`
- `SCHEMATIC_ANNOTATION_GATE.md`
- `SCHEMATIC_FOOTPRINT_GATE.md`
- `SCHEMATIC_VISUAL_AUDIT_RULES.md`
- `SCHEMATIC_TO_PCB_READY_GATE.md`
- `SCHEMATIC_COMMON_FAILURES.md`
- `README_FOR_CODEX_AND_CLAUDE.md`

## Script Layer

The paired read-only script layer lives under:

`03_TOOLS/scripts/schematic_quality/`

The paired schematic-layout planning layer lives under:

`03_TOOLS/scripts/schematic_layout/`

Canonical gate command:

```powershell
python 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --no-fail

python 03_TOOLS\scripts\schematic_layout\render_schematic_review_pages.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --no-fail
```

## Hard Rule

Do not treat a schematic as PCB-update-ready unless:

- annotation is proven by native KiCad workflow or LJ-confirmed manual native
  action
- ERC proof exists
- footprint assignment is complete for physical parts
- visual/readability gate passes
- schematic-to-PCB gate result is exactly `PASS`
