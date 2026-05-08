# Hallucination Risk Log - STM32 Source Link Research

Date: 2026-05-03
Risk: `MEDIUM_RISK`

## Risk

Future agents may mistake source-link presence for verified electrical, package, or footprint approval.

## Controls

- CSV rows include `verification_status`.
- Candidate/prefix rows are marked `NEEDS_REVIEW`.
- Per-family docs state that exact datasheets, reference manuals, errata, package drawings, and KiCad footprint checks remain required.
