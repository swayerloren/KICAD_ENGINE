# DFM Summary

Status: `NORMALIZED_FROM_FAB_DFM_MIGRATION`

## Source Coverage

- Legacy fabrication / assembly intake drained
- Source file count moved: `16`
- Unique source-registry IDs tied directly to the folder: `3`

## Main Themes

- board capability limits are fabricator-specific
- panelization rules are fab-house specific and must not be assumed universal
- assembly-rule passes validate package structure, not solderability success
- export review must include board outline, drills, slots, and mounting details

## Representative Source IDs

- `url_001056` OSH Park design-tools note
- `url_001057` OSH Park design-tools note
- `url_007014` GigaDevice MCU family page captured in the old bucket

## Canonical Enforcement Surfaces

- `24_FAB_PROFILES/UNIVERSAL_PCBA_PACKAGE_RULES.md`
- `24_FAB_PROFILES/NOT_FINAL_EXPORT_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/DFM_ASSEMBLY_VALIDATION_RULES.md`
- `09_ACCURACY_ENGINE/checklists/DFM_ASSEMBLY_REVIEW_CHECKLIST.md`
