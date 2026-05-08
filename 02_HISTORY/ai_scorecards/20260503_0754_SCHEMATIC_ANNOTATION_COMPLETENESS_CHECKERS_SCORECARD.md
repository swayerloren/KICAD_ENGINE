# AI Response Scorecard: Schematic Annotation/Completeness Checkers

Record kind: `ai_scorecard`
Created: `2026-05-03T07:54:00`
Scope: `global`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `92/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `18/20`
- Datasheet/component accuracy: `14/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `8/10`

## Evidence

- Scripts compiled with `python -m py_compile`.
- Scripts generated Markdown and JSON reports from the active schematic without modifying KiCad files.
- Updated gate docs and startup docs reference the new checker system.
- Command log: `02_HISTORY/command_logs/SCHEMATIC_ANNOTATION_COMPLETENESS_CHECKERS_COMMANDS.md`.

## Deductions

- The active-project reports are failing because the project has unresolved blockers and a missing BOM lock.
- BOM-lock parsing is heuristic until the repo has a stricter machine-readable BOM-lock schema.
- The requested visual verification workflow path is missing.
