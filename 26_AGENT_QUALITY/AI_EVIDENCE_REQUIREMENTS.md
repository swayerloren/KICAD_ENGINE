# AI Evidence Requirements

## Purpose

Define what counts as acceptable evidence for KiCad Engine engineering claims.

## Acceptable Evidence

- User-provided facts in the current task.
- Local file inspection.
- Command output.
- KiCad CLI reports.
- KiCad project file evidence.
- Official datasheets or reference manuals.
- Official vendor product pages or reference designs.
- Installed KiCad library inspection.
- Project-local library inspection.
- Human confirmation recorded with scope and date.

## Not Sufficient Alone

- AI memory.
- Similar part names.
- Generic package names.
- Search snippets without source review.
- 3D model presence.
- A clean ERC result for footprint correctness.
- A clean DRC result for schematic correctness.
- A prior finished PCB unless reviewed as evidence.

## Evidence Status Labels

- `VERIFIED_BY_FILE`
- `VERIFIED_BY_COMMAND`
- `VERIFIED_BY_DATASHEET`
- `VERIFIED_BY_KICAD_LIBRARY`
- `VERIFIED_BY_USER`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `CONTRADICTED`
- `REQUIRES_HUMAN_REVIEW`

## Claim Matrix Rule

Every major engineering claim must appear in a claim/evidence matrix with one of the evidence status labels above.

