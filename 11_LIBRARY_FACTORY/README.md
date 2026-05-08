# KiCad Library Factory

Status: standards and read-only validation support for project-local KiCad symbols, footprints, package mappings, 3D model links, and library QA.

`11_LIBRARY_FACTORY/` defines how Codex, Claude, and similar VS Code-based agents should create or verify KiCad symbols, footprints, 3D model references, and symbol-to-footprint mappings with fewer mistakes.

## Core Rule

Symbols and footprints must be driven by source evidence.

- Symbol pinouts require exact datasheet or reference-manual evidence.
- Footprints require exact package drawings or manufacturer land-pattern evidence.
- Connector footprints require exact manufacturer drawings and human orientation review.
- Pin 1 orientation must be documented for both symbols and footprints.
- Generated/custom libraries should be project-local by default.
- Installed KiCad global libraries and user-global library tables must not be modified.
- Scripts in this folder are evidence helpers only. They do not approve symbols, footprints, 3D models, or manufacturing readiness.

## Folder Map

- `symbols/`: symbol creation, pin naming, power pins, fields, datasheet links, and QA.
- `footprints/`: footprint creation, pads, courtyard, silkscreen, fab layer, origin, 3D model references, connector footprints, and QA.
- `mapping/`: symbol-to-footprint mapping, package-to-footprint evidence, library tables, and project-local library rules.
- `3d_models/`: 3D model source, path, scale, rotation, and mechanical review guidance.
- `qa/`: cross-cutting library QA workflow, evidence requirements, and review status rules.
- `scripts/`: basic read-only validators. These scripts can flag risks but cannot approve engineering correctness.

## Intended Workflow

1. Identify exact part number and package.
2. Collect datasheet, reference manual, package drawing, and connector drawing where applicable.
3. Decide whether an existing KiCad library item is a candidate or a project-local library item must be created.
4. Use the standards in this folder to create or verify symbol and footprint data.
5. Record symbol, footprint, package, and 3D model status separately.
6. Run the basic validators in `scripts/`.
7. Run KiCad ERC/DRC after project integration.
8. Require human review for connector orientation, polarity, RF, high-current, mechanical fit, and manufacturing outputs.

## What This Folder Does Not Do

- It does not replace KiCad.
- It does not approve a footprint.
- It does not guarantee a pinout.
- It does not modify global KiCad libraries or user-global library tables.
- It does not remove the need for datasheet/package drawing review.


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
