# Package Profiles

Status: `ACTIVE_SCAFFOLD`

## PURPOSE

Store reusable component package profile definitions, footprint matching rules, and package verification checklists.

## WHAT_BELONGS_HERE

- Package profile templates.
- Package-to-footprint verification rules.
- Package family notes for QFN, QFP, SOIC, SOT, DFN, BGA, modules, connectors, through-hole parts, and generic packages.
- Human-review checklists for package drawings and land patterns.

## WHAT_DOES_NOT_BELONG_HERE

- Final fab packages without full review.
- Active KiCad source files.
- Board-house credentials.
- User-private manufacturing orders.
- Exact package dimensions without source citations.

## AI_AGENT_RULES

- Treat every package profile as `UNVERIFIED_PLACEHOLDER` until source evidence is recorded.
- Do not map a package to a KiCad footprint by name alone.
- Do not approve connector or module footprints without exact manufacturer drawings and human orientation review.
- Keep profiles generic unless package drawing or land-pattern sources are cited.

## SAFE_EDIT_RULES

- Add profile docs and templates.
- Do not overwrite exported packages.
- Do not submit manufacturing orders.

## PUBLIC_RELEASE_NOTES

Profiles must be clearly marked as templates, not footprint approval or fab approval.
