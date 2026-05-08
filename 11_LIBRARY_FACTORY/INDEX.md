# Library Factory Index

Status: `ACTIVE`

## Key Areas

- `symbols/`: KiCad symbol creation and QA rules.
- `footprints/`: footprint creation, pad, courtyard, silkscreen, fab, origin, and 3D rules.
- `mapping/`: symbol-to-footprint and package-to-footprint rules.
- `3d_models/`: 3D model source, scale, orientation, path, and mechanical-fit review rules.
- `qa/`: cross-cutting library QA workflow and review status rules.
- `scripts/`: basic read-only validation helpers.

## Required Use

Use project-local libraries for generated/custom library work. Do not modify installed KiCad global libraries.

## Core Standards

Symbols:

- `symbols/SYMBOL_CREATION_STANDARD.md`
- `symbols/SYMBOL_PIN_NAMING_RULES.md`
- `symbols/SYMBOL_POWER_PIN_RULES.md`
- `symbols/SYMBOL_FIELD_RULES.md`
- `symbols/SYMBOL_QA_CHECKLIST.md`

Footprints:

- `footprints/FOOTPRINT_CREATION_STANDARD.md`
- `footprints/FOOTPRINT_PAD_RULES.md`
- `footprints/FOOTPRINT_COURTYARD_RULES.md`
- `footprints/FOOTPRINT_SILKSCREEN_RULES.md`
- `footprints/FOOTPRINT_FAB_LAYER_RULES.md`
- `footprints/FOOTPRINT_3D_MODEL_RULES.md`
- `footprints/CONNECTOR_FOOTPRINT_RULES.md`
- `footprints/FOOTPRINT_QA_CHECKLIST.md`

Mappings:

- `mapping/SYMBOL_TO_FOOTPRINT_MAPPING_STANDARD.md`
- `mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md`
- `mapping/PROJECT_LOCAL_LIBRARY_RULES.md`

Support:

- `3d_models/README.md`
- `3d_models/3D_MODEL_REVIEW_RULES.md`
- `qa/README.md`
- `qa/LIBRARY_QA_WORKFLOW.md`


## PURPOSE

Define source-backed standards for KiCad symbols, footprints, package mapping, and project-local libraries.

## WHAT_BELONGS_HERE

Symbol rules, footprint rules, mapping standards, QA checklists, and read-only validation scripts.

## WHAT_DOES_NOT_BELONG_HERE

Installed KiCad global libraries, user-global library tables, active design files, or unverified connector footprints.

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
