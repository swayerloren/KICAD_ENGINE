# Issue Log - Schematic Execution Contract Gap

- Date: `2026-05-08`
- Status: `OPEN`
- Severity: `MEDIUM`

## Issue

The execution-contract hardening layer currently defines strong task types for docs, audits, live-state reconciliation, placement edits, routing edits, PCB edits, and GitHub-docs-only work, but it still lacks a dedicated schematic-edit task type.

## Why It Matters

- README prompt guidance cannot honestly point users to a schematic-specific contract class yet.
- Schematic-edit sessions still rely more on startup rules and human discipline than on a first-class contract validator.

## Recommended Follow-Up

- add `SCHEMATIC_EDIT_REQUIRED` or an equivalent contract class
- define required ERC evidence, backup proof, target-file proof, and downstream PCB-sync expectations
- wire that contract into startup guidance and closeout validation
