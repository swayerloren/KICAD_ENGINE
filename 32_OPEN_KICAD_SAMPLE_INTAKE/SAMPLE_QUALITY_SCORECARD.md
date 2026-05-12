# Sample Quality Scorecard

Status: `ACTIVE_REFERENCE_SCORECARD`

## Purpose

Score whether an open-source KiCad sample is useful as learning material.

## Categories

Use a `0-100` score with these categories:

- source and license clarity: `0-20`
- schematic readability: `0-20`
- schematic completeness: `0-10`
- PCB layout quality: `0-20`
- connector/mechanical correctness evidence: `0-10`
- ERC/DRC evidence: `0-10`
- reuse safety and attribution quality: `0-10`

## Status Bands

- `REFERENCE_READY`: `85-100`
- `REFERENCE_LIMITED_USE`: `70-84`
- `FAILURE_FIXTURE_ONLY`: `40-69`
- `DO_NOT_USE_AS_REFERENCE`: `<40`

## Hard Downgrade Rules

Any of these forces `FAILURE_FIXTURE_ONLY` or worse:

- unclear or restricted license
- unreadable schematic structure
- obvious connector orientation mistakes
- serious DRC or ERC failures
- missing attribution
- no KiCad source files

## Use Rules By Status

- `REFERENCE_READY`: may inform style comparison and review prompts
- `REFERENCE_LIMITED_USE`: may inform comparison with explicit caveats
- `FAILURE_FIXTURE_ONLY`: useful only as a regression or blocker example
- `DO_NOT_USE_AS_REFERENCE`: keep for audit/history only

## Current Repo Reality

Existing imported samples may still be useful, but until they score well they
should not be treated as gold-standard examples.
