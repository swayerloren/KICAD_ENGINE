# Hallucination Risk Log - Golden Path Sample Gate Run

Date: `2026-05-03`

Risk level: `MEDIUM`

## Risks

- Visual crop generation can be mistaken for completed human visual approval. It is only evidence generation.
- Project-local footprint mapping can be mistaken for exact footprint verification. It only resolves the library nickname.
- Zero unconnected pads can be mistaken for DRC pass. DRC still fails.
- BOM export can be mistaken for a locked purchasing BOM. It is only a KiCad field export.

## Controls Applied

- Reports mark final result as `GOLDEN_PATH_PARTIAL`.
- Quality gate is `BLOCKED_UNTIL_HUMAN_REVIEW`.
- No fabrication outputs were generated.
- Unverified package, orientation, shield, polarity, and BOM items remain listed as blockers.
