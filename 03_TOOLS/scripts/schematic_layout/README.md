# Schematic Layout Tools

Read-only extraction, scoring, planning, and review helpers for schematic
visual cleanup.

## Purpose

This folder adds a schematic layout engine on top of the existing
`03_TOOLS/scripts/schematic_quality/` parser and gate layer.

Use it to:

- extract current functional-block layout
- score schematic readability with a repeatable scorecard
- plan cleaner block organization
- audit visual flow
- audit local wire usage vs excessive local labels
- render review pages under project `reports/schematic_layout/`
- prepare future rewrite plans without editing schematics by default

## Scripts

- `extract_schematic_layout.py`
- `score_schematic_readability.py`
- `plan_schematic_block_layout.py`
- `rewrite_schematic_layout_safe.py`
- `render_schematic_review_pages.py`
- `audit_visual_flow.py`
- `audit_local_wire_usage.py`
- `schematic_layout_common.py`

## Hard Rules

- Default mode is read-only.
- Do not write a schematic unless `--apply` is explicitly used.
- Current rewrite support is planning-only. Without `--apply`, the rewrite
  wrapper must not write a schematic.
- Do not treat this layer as PCB-update approval by itself.
- ERC, native annotation, footprint readiness, and human visual review remain
  separate required gates.

## Canonical Dry-Run Commands

```powershell
python 03_TOOLS\scripts\schematic_layout\score_schematic_readability.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --no-fail

python 03_TOOLS\scripts\schematic_layout\render_schematic_review_pages.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --no-fail
```

## Safe Rewrite Probe

```powershell
python 03_TOOLS\scripts\schematic_layout\rewrite_schematic_layout_safe.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```
