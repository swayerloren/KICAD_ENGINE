# Uncertainty Log

Session: `REAL_PROJECT_ROUTING_WORKFLOW_DEFINED`

Date: `2026-05-07`

## Known Uncertainties

1. `14_LAYOUT_AUTOMATION/README.md` may need a later cleanup pass because embedded null bytes make direct patching fragile.
2. The new real-project routing workflow has not yet been exercised on a copied KiCad board.
3. Differential-pair and DRC-coupled route scoring still need real-board evidence.

## Handling

- The workflow docs and audit explicitly keep real-board routing blocked until the missing integrations exist.
