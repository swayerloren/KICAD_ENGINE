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
- symbol orientation improved before local labels are accepted
- local wires inside local blocks
- local MCU support circuits physically wired when they are close to the
  controlled pins
- labels reserved for cross-block or long-distance connections, power rails,
  debug anchors, or cases where a wire would be worse
- clean reference/value text placement with visible text ownership
- graphic lines are never electrical proof
- reset/boot and other local control topology remains readable beyond ERC
- power, ground, and common-return rails read intentionally and are proven as
  real wires on the intended nets
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

python 03_TOOLS\scripts\schematic_quality\check_schematic_human_drafting_quality.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --output-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_quality\human_drafting `
  --warn-only
```

The human-drafting checker is the narrow read-only audit for issues that ERC
and basic overlap checks miss. It targets:

- graphic lines that may be mistaken for rails
- local label overuse and orientation-before-label shortcuts
- local MCU support wiring such as `ESP_EN`, `BOOT0`, local LEDs, and local
  decoupling
- reset/boot switch and support-cap topology sanity
- text ownership drift
- suspicious local loopback wire paths
- local return-style clusters that are not actually on `GND`

It is still heuristic and does not replace human image review or datasheet
proof, but it should run before human-drafting or visual-gate claims are
closed.

## Hard Rule

Do not treat a schematic as PCB-update-ready unless:

- annotation is proven by native KiCad workflow or LJ-confirmed manual native
  action
- ERC proof exists
- footprint assignment is complete for physical parts
- visual/readability gate passes
- schematic-to-PCB gate result is exactly `PASS`
- critical local blocks do not still depend on avoidable labels, ambiguous
  visual rails, or unreadable reset/boot/control topology
