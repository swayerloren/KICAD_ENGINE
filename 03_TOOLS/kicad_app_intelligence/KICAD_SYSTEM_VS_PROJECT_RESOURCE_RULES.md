# KiCad System Vs Project Resource Rules

Date: 2026-05-03

Purpose: define how AI agents should treat installed KiCad resources versus project-owned resources.

## Definitions

System resources:

- Installed KiCad executables.
- Installed KiCad runtime libraries.
- Installed stock symbols.
- Installed stock footprints.
- Installed stock 3D models.
- Installed templates, demos, schemas, docs, and scripts.
- User-global KiCad config and library tables.

Project resources:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- Project-local `sym-lib-table`
- Project-local `fp-lib-table`
- Project-local `design-block-lib-table`
- Project-local `.kicad_sym` libraries
- Project-local `.pretty` footprint libraries
- Project-local 3D models
- Project reports and review outputs

## System Resource Rules

Installed KiCad folders are read-only reference material.

Agents may:

- Read metadata.
- Index names and paths.
- Inspect stock symbol/footprint/3D model content.
- Run `kicad-cli version/help`.
- Read installed examples.

Agents must not:

- Modify installed files.
- Save demos or templates in place.
- Patch stock symbols or footprints.
- Install Python packages into bundled KiCad Python.
- Add generated outputs to installed folders.
- Change user-global library tables as a side effect.

## Project Resource Rules

Project resources are engineering source.

Before any project source edit:

1. Confirm active project.
2. Confirm target file paths are inside the active project.
3. Create or confirm backup.
4. State rollback plan.
5. State verification plan.
6. Record history.

Project validation can be read-only, but source edits require the full gate.

## Library Table Rules

Project-local library tables usually live beside the `.kicad_pro` file:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

User-global library tables usually live in user config:

- Windows: `%APPDATA%\kicad\<version>\`
- macOS: `~/Library/Preferences/kicad/<version>/` or `~/Library/Application Support/kicad/<version>/` depending on KiCad/version packaging
- Linux: `~/.config/kicad/<version>/`

Agent resolution order:

1. Project-local library tables.
2. User-global tables, read-only.
3. Installed stock library locations.

Never "fix" a project by editing the user's global library table unless the user explicitly requested global KiCad configuration changes and a backup exists.

## When To Copy Stock Resources Into Project Libraries

Copy selected stock resources when:

- A symbol needs project-specific fields or edits.
- A footprint needs project-specific pad, outline, keepout, or 3D changes.
- A project must preserve a known-good library version.
- A high-risk footprint has been verified and should be frozen.
- A design must be portable without requiring private global libraries.

Suggested project-local structure:

```text
project/
  libs/
    symbols/
      project_symbols.kicad_sym
    footprints/
      project_footprints.pretty/
    3dmodels/
```

Use `${KIPRJMOD}` in project-local library tables so the project remains portable.

## What Not To Copy

Do not copy:

- Entire KiCad install folders.
- Runtime DLLs, libraries, or executables.
- Bundled Python.
- Stock template folders unless creating a new project from a copied template.
- Installed demos unless creating a disposable example copy.
- Copyrighted docs into a public repo without redistribution review.

## Footprint And Connector Special Rule

Connector, RF, module, USB-C, automotive, and board-edge footprints are high-risk.

For these parts:

- Do not trust stock footprint names alone.
- Verify exact manufacturer part number.
- Verify package drawing and land pattern.
- Verify orientation and pin numbering.
- Consider copying the verified footprint into a project-local library and recording the source drawing.

## Report Language

Use:

- `SYSTEM_RESOURCE_READ_ONLY`
- `PROJECT_RESOURCE_REQUIRES_BACKUP`
- `PROJECT_LOCAL_COPY_RECOMMENDED`
- `GLOBAL_LIBRARY_DEPENDENCY`
- `STOCK_LIBRARY_CANDIDATE_NOT_VERIFIED`
- `FOOTPRINT_VERIFIED_AGAINST_DRAWING`

Do not use final approval language unless human review has accepted the evidence.
