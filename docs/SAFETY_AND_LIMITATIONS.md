# Safety And Limitations

KiCad Engine is AI-assisted engineering support. It is not certified engineering approval.

## Main Limits

- AI agents can misunderstand KiCad files.
- Datasheet records may be incomplete.
- Component records may be placeholders.
- KiCad symbols may not match the selected package.
- Footprints may be wrong for the exact manufacturer part.
- Connectors may be rotated, mirrored, or numbered differently than expected.
- ERC and DRC do not prove manufacturing readiness.
- Exported fabrication files may be incomplete or wrong.

## Human Review Required

Human review is required for:

- Schematic intent.
- Power budget.
- Datasheet values.
- Symbol pinout.
- Footprint match.
- Connector orientation.
- Polarity and assembly direction.
- Mechanical fit.
- Fab-house requirements.
- Final manufacturing release.

## Unsafe AI Behaviors To Reject

Reject output where an agent:

- Claims a board is fab-ready from ERC or DRC alone.
- Invents datasheet values.
- Approves a footprint by name only.
- Writes KiCad files without backup and approval.
- Modifies installed KiCad folders.
- Stores API keys or credentials.
- Removes `NOT_FINAL` labels without evidence.

## Safe Status Language

Prefer:

- `READ_ONLY_INSPECTION`
- `REPORT_GENERATED`
- `PASS_BY_KICAD_CLI`
- `HUMAN_REVIEW_REQUIRED`
- `UNKNOWN_REQUIRES_SOURCE_VERIFICATION`
- `EXPORTED_NOT_FINAL`

Use final approval language only when the user has accepted the complete verification evidence.
