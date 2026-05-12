# Uncertainty Log - Mechanical Orientation Truth

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Uncertainties

- The initial truth catalog covers the connector/RF families needed for this task, not every connector family in the repo.
- `J1` is blocked because the 3D model reference does not resolve on this machine; another machine with a matching installed model may change the evidence status.
- Generic dry-runs on unrelated sample boards can legitimately return `NEEDS_HUMAN_REVIEW` when footprints are unknown to the truth catalog or model proof is missing.

## Impact

These uncertainties do not change the verified outcome of this task: the new layer exists, validates cleanly, and now blocks routing when connector orientation proof is incomplete.
