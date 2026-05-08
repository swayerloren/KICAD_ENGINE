# Human Review Gate

## Purpose

Define when human review is still required after the sandbox has already run objective checks.

## Default Rule

Do not require generic LJ approval before real PCB work if the sandbox can prove the selected variant passes all objective checks.

Human review is now conditional, not automatic.

## Human Review Is Required Only When

- a high-risk footprint is not exact-verified or safe-candidate documented
- connector orientation is still unknown or mechanically weak
- board shape or dimensions remain assumption-only
- RF keepout or service-space evidence remains ambiguous
- routing-feasibility evidence fails or remains inconclusive on a high-risk path
- a DRC/precheck blocker remains
- a selected variant has objective non-hard-fail risk that still needs a human decision

## Human Review Status Labels

- `HUMAN_REVIEW_NOT_REQUIRED`
- `HUMAN_REVIEW_OPTIONAL`
- `HUMAN_REVIEW_REQUIRED_EXACT_MISSING_ITEMS`
- `HUMAN_REVIEW_REQUIRED_HIGH_RISK`

## Not Professional Yet Rule

Even after sandbox auto-approval, the layout is not professional or complete until:

- real placement passes
- routing feasibility survives real placement
- DRC passes
- visual review passes
