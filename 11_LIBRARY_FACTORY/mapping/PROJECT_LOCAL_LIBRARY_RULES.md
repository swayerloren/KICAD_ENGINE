# Project Local Library Rules

## Purpose

Keep generated/custom library content portable, auditable, and safe.

## Recommended Structure

Inside an active project, use a clear local library structure such as:

```text
project_libraries/
  symbols/
    PROJECT_CUSTOM.kicad_sym
  footprints/
    PROJECT_CUSTOM.pretty/
      PART_NAME.kicad_mod
  3dmodels/
```

Use the actual project convention if one already exists.

## Rules

- Keep custom symbols and footprints under the active project folder.
- Do not modify installed KiCad libraries.
- Do not mix unverified and verified items without status fields or documentation.
- Keep source evidence in component records or project history.
- Use library nicknames that make project-local status obvious.

## Backup Rule

Before editing project-local libraries, create or confirm a backup under `99_BACKUPS/pre_codex_edits/`.

## Review Gate

Project-local libraries are still KiCad source files. They require the same active-project, backup, rollback, and verification gates as `.kicad_sch` and `.kicad_pcb` edits.

