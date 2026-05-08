# PCB Variant Scoring System Audit

Date: `2026-05-07`

## Scope

Repo workflow, templates, scripts, and startup-memory handoff only. No KiCad schematic, PCB, or manufacturing files were edited.

## Files Updated

- `34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/templates/VARIANT_SCORECARD_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py`
- `34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Scoring System Summary

- Base score categories now total `100` points across mechanical correctness, connector orientation correctness, antenna/RF keepout correctness, power path quality, USB/data routing quality, component grouping quality, and routing feasibility.
- Human-review risk is now a defined penalty instead of an undefined comment.
- Each variant now resolves to exactly one status: `PASS`, `FAIL`, or `NEEDS_HUMAN_REVIEW`.
- Hard-fail conditions now explicitly block wrong-edge USB-C, wrong-facing barrel jacks, blocked ESP32 keepout, missing required mounting holes, unreviewed high-risk connector orientation, unassigned footprints, weak exact-package proof for high-risk connectors, routing projections crossing RF keepout, nonsensical power paths, and guessed board dimensions.
- Variant selection now requires the highest-scoring non-failed candidate, lowest human-review risk among score ties, and explicit justification.

## Script Behavior

- `score_layout_variant.py` scores one variant from either JSON or Markdown containing a fenced `json` block.
- `compare_layout_variants.py` requires at least three variants, rejects manual selection that violates the scoring rule, and reports whether the selected candidate is actually ready for real PCB edits.

## Validation

- Python syntax check passed for both scripts with `python -m py_compile`.
- Reference scans confirmed the new scorer is recorded in startup/handoff memory.
- No KiCad design files changed during this repo-only task.

## Residual Risk

- The scripts were syntax-checked but not yet exercised on a real project's three-variant report set.
- A first live use should confirm the chosen JSON/Markdown input pattern is comfortable enough for future project reports.
