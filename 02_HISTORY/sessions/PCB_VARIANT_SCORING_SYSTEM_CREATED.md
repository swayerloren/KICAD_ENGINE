# PCB Variant Scoring System Created

Date: `2026-05-07`

## Summary

Added a concrete scoring system for comparing at least three PCB layout variants before any real KiCad PCB edit. The patch defined weighted category scoring, hard-fail conditions, risk penalties, a machine-readable scorecard template, and two helper scripts for single-variant scoring and multi-variant comparison.

## Work Performed

1. Read the current sandbox workflow and scoring docs plus required startup/handoff files.
2. Incremented the active project prompt counter and confirmed maintenance was not due.
3. Captured baseline hashes for the active project's `.kicad_pcb`, `.kicad_sch`, and `.kicad_pro` files.
4. Replaced the loose variant-scoring notes with a strict weighted rule set.
5. Replaced the simple scorecard template with a human-plus-machine template that includes a fenced JSON payload.
6. Added `score_layout_variant.py` and `compare_layout_variants.py`.
7. Updated durable memory and handoff docs so future agents see the new scoring gate.
8. Syntax-checked both Python scripts and confirmed no KiCad design-file changes.

## Result

- Variant scoring rules: `UPDATED`
- Variant scorecard template: `UPDATED`
- Scoring helper scripts: `CREATED`
- Startup/memory handoff: `UPDATED`
- KiCad design file changes: `NONE`

## Follow-Up

- Use the fenced JSON block in each project variant report so the scripts can score and compare the variants directly.
- Run the new scripts on the first real three-variant project report set and record any ergonomics issues in history.
