# KiCad Symbol Footprint Match Index

Date: 2026-05-03
Status: `CANDIDATE_MATCH_INDEX`

Records in this folder connect component database entries to KiCad symbol, footprint, and 3D model candidates. A match is not approved until exact datasheet/package drawing review and human review are recorded.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact pinout/package drawing checked.
- `INFERRED_FROM_COMMON_DESIGN`: common match pattern only.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: required before schematic/PCB/fab use.

| Part | Match Record | Current Status | Notes |
| --- | --- | --- | --- |
| STM32F103C8T6 | `STM32F103C8T6_MATCH.md` | `CANDIDATE_ONLY`, `NEEDS_HUMAN_REVIEW` | KiCad 9 symbol, footprint, and 3D model candidate existence found; exact package/pinout not verified. |
