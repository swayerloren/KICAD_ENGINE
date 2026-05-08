# Failed Attempt Capture Rules

A failed attempt is any workflow, command, script, edit, export, review, or recommendation that did not achieve the intended result.

## Required Capture

Record a failed attempt when:

- A command fails unexpectedly.
- A script produces incorrect or incomplete output.
- A KiCad edit must be backed out or revised.
- A selected symbol, footprint, component, connector, or workflow proves wrong.
- A validation or installer step fails.

## Required Fields

- What was attempted.
- What was expected.
- What happened instead.
- Root cause if known.
- Files or outputs affected.
- Recovery taken.
- What not to repeat.
- Whether memory or issue updates are needed.

## Routing

- Use project `history/failed_attempts/` for project-specific failures.
- Use `02_HISTORY/failed_attempts/` for repo-wide tool or workflow failures.
- Promote only durable avoidance rules to memory.

