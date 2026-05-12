# Schematic Quality Engine False-Positive Tuning

Date: `2026-05-10`
Status: `RESOLVED_DURING_SESSION`

## Problem

The first overlap/layout heuristics were too aggressive and produced noisy
failures by counting some symbol-owned text against the same symbol body and by
treating estimated block-flow disorder as a hard fail.

## Resolution

- The overlap audit now skips same-symbol body checks for the symbol's own
  visible properties.
- Estimated block-flow disorder was downgraded from hard fail to warning.
- Repeated local labels and estimated symbol-body overlap findings were also
  downgraded to warnings where the evidence is heuristic rather than exact.

## Remaining Risk

- Bounding-box overlap detection is still an estimate.
- Human visual review remains a required gate even when the automated audit is
  clean.
