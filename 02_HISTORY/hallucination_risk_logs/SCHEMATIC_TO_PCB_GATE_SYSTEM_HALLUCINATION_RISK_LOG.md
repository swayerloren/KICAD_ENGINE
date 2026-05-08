# Hallucination Risk Log - Schematic To PCB Gate System

## Session

- Date: 2026-05-03
- Risk label: `MEDIUM_RISK`

## Risk Summary

The main hallucination risk is future agents treating a schematic as ready for PCB because a `.kicad_sch` file exists. The gate now prevents that by requiring report-backed evidence before PCB update or layout work.

## Risk Items

| Risk | Severity | Mitigation |
|---|---|---|
| Agent claims ERC passed without running ERC. | HIGH | Gate requires ERC report path before `PASS`. |
| Agent claims schematic is visually reviewed without full-page and close-up exports. | HIGH | Gate requires visual export and close-up review evidence. |
| Agent assumes generic footprints are acceptable. | HIGH | Gate requires exact package drawing verification. |
| Agent ignores connector orientation or polarity. | HIGH | Gate requires connector and polarity review. |
| Agent proceeds despite `NEEDS_REVIEW`. | HIGH | `NEEDS_REVIEW_BLOCKER_RULES.md` blocks high-risk items. |
| Agent relies on Git diff in a folder without `.git`. | MEDIUM | Command failure is recorded; timestamp inspection was used, and Git proof remains unavailable. |

## Outcome

Gate system added. Active project transition remains `BLOCKED_UNTIL_HUMAN_REVIEW`.
