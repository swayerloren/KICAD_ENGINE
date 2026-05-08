# Fab Profiles Index

Status: `ACTIVE_SCAFFOLD`

## Folder Map

- `00_INDEX/`: fab profile schema and output rules.
- `JLCPCB/`: JLCPCB-specific profile drafts and sourced profiles.
- `PCBWAY/`: PCBWay-specific profile drafts and sourced profiles.
- `OSHPARK/`: OSH Park-specific profile drafts and sourced profiles.
- `MACROFAB/`: MacroFab-specific profile drafts and sourced profiles.
- `GENERIC_FAB_OUTPUTS/`: generic output package rules and placeholders.

## Core Files

- `00_INDEX/FAB_PROFILE_SCHEMA.md`
- `00_INDEX/GERBER_DRILL_RULES.md`
- `00_INDEX/BOM_CPL_PNP_RULES.md`
- `00_INDEX/ASSEMBLY_NOTES_RULES.md`
- `00_INDEX/NOT_FINAL_OUTPUT_RULES.md`

## Starter Placeholder Profiles

- `JLCPCB/JLCPCB_GENERIC_OUTPUT_PROFILE.md`
- `PCBWAY/PCBWAY_GENERIC_OUTPUT_PROFILE.md`

## PURPOSE

Store fabrication-house profile guidance and NOT_FINAL manufacturing export rules.

## WHAT_BELONGS_HERE

Generic and fab-house-specific profile drafts, DFM notes, output naming rules, and review gates.

## WHAT_DOES_NOT_BELONG_HERE

Private fab credentials, live order data, final approval claims, or unverified board-house rules.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to `02_HISTORY/`, `05_OUTPUTS/`, or project history unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
