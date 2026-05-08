# Hallucination Risk Log - STM32 Datasheet Tree Content Completion

Date: 2026-05-03
Risk: `MEDIUM_RISK`

## Risk

Family-level summaries can be mistaken for verified part-level facts if future agents ignore the classification.

## Controls Added

- Every family file is marked `SCAFFOLDED_WITH_AI_SUMMARIES`.
- Exact parameters are marked `UNKNOWN_REQUIRES_SOURCE`.
- Footprint approval requires exact package drawing and human review.
- `NEEDS_RESEARCH.md` files list unresolved source work for every family.
- Component database guide tells agents not to use family names as part records.

## Remaining Human Review Gate

Before any STM32 schematic/PCB work, a human or source-backed workflow must select exact part/order code and verify datasheet, reference manual, errata, package drawing, symbol, footprint, and package orientation.
