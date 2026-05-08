# PCB Variant Scoring System Needs First Live Project Run

Date: `2026-05-07`

## Issue

The new PCB variant scoring scripts were syntax-checked and documented, but they were not yet exercised on a real three-variant project report set.

## Impact

- Low immediate repo risk.
- First live usage may still expose small schema or ergonomics issues in the fenced-JSON workflow.

## Required Follow-Up

1. Run `score_layout_variant.py` on one real variant report.
2. Run `compare_layout_variants.py` on one real three-variant report set.
3. Record any field/schema friction in history before widening usage.

## Status

`OPEN`
