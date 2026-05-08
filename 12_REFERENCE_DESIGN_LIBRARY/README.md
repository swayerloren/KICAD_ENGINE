# Reference Design Library

Status: source-aware reference design system for AI-assisted KiCad engineering.

`12_REFERENCE_DESIGN_LIBRARY/` stores links, summaries, verification notes, and license records for reference designs that Codex, Claude, and similar agents can learn from without blindly copying.

## Purpose

Reference designs help agents understand proven circuit blocks, layout constraints, component choices, and review risks. They are evidence inputs, not automatic approval.

Use this library to:

- Track official vendor reference designs.
- Track open hardware projects with compatible licenses.
- Record what can be learned from a design.
- Record what must not be copied.
- Preserve license and attribution context.
- Identify human review requirements before applying a pattern to KiCad work.

## Core Rules

- Do not copy proprietary designs without permission.
- Prefer official vendor reference designs and open hardware projects with compatible licenses.
- Store links, summaries, and verification notes by default.
- If files are copied, track source, license, attribution, and redistribution status.
- Do not treat a reference design as approval for a new design.
- Do not assume a reference design's footprint, connector orientation, BOM, or layout is correct for a different board.

## Relationship To Other Layers

- `06_DATASHEETS/`: stores datasheet/reference-document links and summaries.
- `08_COMPONENT_DATABASE/`: stores part-level records.
- `09_ACCURACY_ENGINE/`: defines source and verification gates.
- `10_KNOWLEDGE_BASE/`: stores reusable circuit and review patterns.
- `11_LIBRARY_FACTORY/`: defines symbol/footprint and mapping standards.
- `32_OPEN_KICAD_SAMPLE_INTAKE/`: screens real open KiCad project candidates before any copied sample is used as reference-design evidence. Imported originals stay read-only there; only reviewed link records or approved normalized sample summaries should be promoted here.

## Recommended Agent Workflow

1. Search this library for a category-specific reference.
2. Read the record, source URL, license, and verification level.
3. Extract only the lesson or pattern needed.
4. Verify the exact components, pinouts, footprints, and layout constraints for the active design.
5. Mark copied or adapted ideas in project history.
6. Require human review for connector orientation, RF, USB, CAN, automotive, power, footprints, and manufacturing outputs.

If the reference is a complete KiCad project found on the web, first route it through `32_OPEN_KICAD_SAMPLE_INTAKE/`. Do not copy project files directly into this library without source URL, license screening, attribution, file audit, and public-bundle eligibility status.

## What Belongs Here

- Reference design records.
- Public source links.
- License and redistribution notes.
- Circuit-block summaries.
- Review checklists.
- Known issue notes.

## What Does Not Belong Here

- Secrets or credentials.
- Unlicensed copied vendor design files.
- Full proprietary design archives.
- Active KiCad project source files.
- Manufacturing outputs.
- Claims that a reference design is approved for a new project without verification.


## PURPOSE

Store curated reference design records with source, license, verification level, and human-review requirements.

## WHAT_BELONGS_HERE

Reference records, source rules, category checklists, and verification templates.

## WHAT_DOES_NOT_BELONG_HERE

Unlicensed copied design archives, active project files, final fab outputs, or automatic approval claims.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
