# Memory History Maintenance Workflow

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `03_TOOLS/scripts/memory_maintenance`.

Current relevance: required workflow for compiling current truth without replacing history.

## Purpose

Maintain the existing `01_MEMORY`, `02_HISTORY`, and project memory/history folders after repeated agent sessions.

## Workflow

1. Read startup, memory, history, and accuracy-engine rules.
2. Run maintenance in dry-run mode.
3. Review duplicate blocker topics, stale reports, false-pass incidents, and unresolved relative dates.
4. Run apply mode only for markdown/index/status outputs.
5. Rebuild memory and history indexes.
6. Confirm no KiCad design files changed.
7. Create a validation report.

## Hard Limits

- Do not create a replacement memory/history system.
- Do not delete old history.
- Do not edit KiCad design files.
- Do not hide failures.
- Do not treat current-state compilation as engineering progress on a KiCad design.
