# KiCad Library Table Rules

## Purpose

Explain how agents should handle KiCad library tables safely.

## Global Tables

Global symbol and footprint library tables are user configuration. Agents must not modify them unless the user explicitly asks and understands the risk.

Typical Windows global table locations are under the user's KiCad configuration folder, not under the KiCad install folder. Exact paths vary by KiCad version and user profile.

## Project Tables

Project-local `sym-lib-table` and `fp-lib-table` belong beside the KiCad project when project-local libraries are used.

## Rules

- Prefer project-local library entries for generated/custom symbols and footprints.
- Do not write to installed KiCad library folders.
- Do not silently add global library paths.
- Use relative project paths where practical.
- Keep library nicknames stable and readable.
- Record changes in project history before and after edits.

## Review Gate

Any library table edit is a KiCad project/config edit and requires active project confirmation, backup, rollback plan, and verification plan.

