# False Pass Prevention Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `01_MEMORY/AGENT_MISTAKES_TO_AVOID.md`, project ESP32 history and reports.

Current relevance: mandatory rule for preventing overclaimed gate results.

## False-Pass Patterns

Never treat these as a real pass:

- Annotation `PASS` from regex or text scan alone.
- Visual `PASS` from crop generation alone.
- Placement `PASS` because footprints are merely on the board.
- JLCPCB, mechanical, BOM, production, export, upload feedback, or signoff review before a PCB exists.
- Routing before placement audit and LJ placement approval.
- Production-ready claims before DRC pass, no-unrouted proof, JLCPCB review, BOM/CPL review, and human approval.

## Required Status

If an old report contains a false-pass pattern, preserve it but mark it through maintenance as:

`FALSE_PASS`

If uncertain, use:

`NEEDS_HUMAN_REVIEW`
