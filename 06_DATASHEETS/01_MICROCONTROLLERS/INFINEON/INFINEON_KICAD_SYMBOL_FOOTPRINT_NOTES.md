# INFINEON KiCad Symbol And Footprint Notes

Date: 2026-05-03
Status: `CANDIDATE_ONLY`

This file records KiCad library candidates for `INFINEON`. Candidate existence is not datasheet verification.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## Candidate Evidence

| Candidate | Local Evidence | Status |
| --- | --- | --- |
| symbol | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| footprint | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| 3D model | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |

## What Is Not Verified

- symbol pin numbers;
- hidden power pins;
- electrical pin types;
- exact package mapping;
- footprint pad geometry;
- courtyard, fab, silkscreen, and pin-1 marker;
- 3D model orientation.

## AI Agent Rule

Do not promote any candidate beyond `UNVERIFIED` until exact source evidence and human review are recorded.
