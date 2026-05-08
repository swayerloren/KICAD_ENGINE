# Uncertainty Log: Schematic Annotation/Completeness Checkers

Record kind: `uncertainty_log`
Created: `2026-05-03T07:54:00`
Scope: `global`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Uncertainties

- BOM-lock parsing is heuristic because the active project does not have the requested `PRE_SCHEMATIC_BOM_LOCK.md` file.
- Component category checks use reference prefixes and symbol/value text; they are screeners, not proof.
- Completeness checks detect functional blocks by symbol and text keywords; they cannot prove the circuit is electrically correct.
- `NEEDS_REVIEW` marker detection is intentionally strict and may require project-specific waivers or schema improvements later.
- The requested `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md` file is missing.

## Required Follow-Up

- Define a stricter BOM-lock schema if these checks are used in CI.
- Add project-specific waiver handling only after human review rules are defined.
- Create or relocate the missing visual verification workflow document.
