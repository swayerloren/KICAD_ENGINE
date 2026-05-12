# Schematic Layout Algorithm

## Purpose

Define the read-only layout extraction, scoring, planning, and safe-rewrite
flow used by `03_TOOLS/scripts/schematic_layout/`.

## Inputs

- saved `.kicad_sch`
- current project `reports/SCHEMATIC_*.md` when present
- current close-up visual evidence when present
- current native-annotation evidence when present

## Algorithm

1. Parse the saved `.kicad_sch` directly.
2. Extract symbols, visible text, labels, headings, and wire segments.
3. Assign symbols into functional blocks using:
   - block headings
   - reference/value/library keywords
   - proximity to the block heading
4. Compute per-block bounding boxes, centroids, symbol counts, wire counts, and
   label counts.
5. Classify each block into a diagram region:
   - upper-left
   - upper-center
   - upper-right
   - middle-left
   - middle-center
   - middle-right
   - lower-left
   - lower-center
   - lower-right
6. Audit visual flow:
   - block presence
   - region suitability
   - left-to-right or top-to-bottom main flow
   - power-path ordering
   - detached-symbol risk
7. Audit local wire usage:
   - wires inside local blocks
   - repeated local labels
   - labels placed directly at many pins
8. Reuse the schematic-quality layer for:
   - unresolved references
   - duplicate references
   - visible `NEEDS_REVIEW` markers
   - missing footprints
   - estimated overlap risk
   - fresh ERC
   - native annotation evidence
9. Convert the results into a readability scorecard.
10. Emit a block-layout plan and safe rewrite plan.

## Hard Rules

- Default mode is read-only.
- `rewrite_schematic_layout_safe.py` must not write a schematic unless
  `--apply` is explicitly used.
- Current rewrite support is planning-only; lack of a writer is safer than a
  guessed raw-text rewrite.
- ERC pass alone is not enough.
- Native annotation proof, footprint readiness, and human visual review remain
  required gates before PCB update.

## Outputs

- layout extract JSON and Markdown
- visual-flow audit JSON and Markdown
- local-wire-usage audit JSON and Markdown
- readability score JSON and Markdown
- block-layout plan JSON and Markdown
- safe rewrite probe JSON and Markdown
- combined review packet under `reports/schematic_layout/<timestamp>/`
