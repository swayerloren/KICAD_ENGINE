# Fab / DFM / Compliance Migration Summary

Status: `KNOWLEDGE_SCRAPE_PHASE_6_NORMALIZED`

## Migration Outcome

- Source folders drained: `10`, `22`, `28`, `29`, `31`
- Files moved: `64`
- Raw capture files quarantined: `58`
- Metadata/history files archived: `6`
- Remaining legacy migration-residue file count after this phase: `1045`

## Canonical Surfaces Added

- `10_KNOWLEDGE_BASE/dfm_assembly/`
- `10_KNOWLEDGE_BASE/compliance_emc_safety/`
- `24_FAB_PROFILES/` rule updates
- `09_ACCURACY_ENGINE/verification_rules/DFM_ASSEMBLY_VALIDATION_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/EMC_PRECOMPLIANCE_REVIEW_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/STANDARDS_LINK_ONLY_RULES.md`
- `09_ACCURACY_ENGINE/checklists/DFM_ASSEMBLY_REVIEW_CHECKLIST.md`
- `09_ACCURACY_ENGINE/checklists/EMC_PRECOMPLIANCE_CHECKLIST.md`

## Key Rules Formalized

- fab package validation is not assembly approval
- pick-and-place rotations require visual review
- connector orientation must be verified before export
- polarity and pin-1 checks are mandatory
- IPC and UL style sources remain link-only unless redistribution is permitted
- all exports remain `NOT_FINAL` until final gates pass and LJ approves
