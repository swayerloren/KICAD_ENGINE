# How To Interpret Gate Results

Status: `PUBLIC_GATE_RESULT_GUIDE`

## What The Gate Runner Does

The project gate runner aggregates existing evidence reports and classifies a
project. It is a reporting tool, not an engineering approval authority.

It does not:

- edit KiCad files
- run ERC/DRC itself
- update PCB from schematic
- place or route parts
- create fabrication outputs

## Final Classifications

| Classification | Meaning | Next Action |
| --- | --- | --- |
| `PASS` | All required gates passed with available evidence. | Still perform human review before fabrication. |
| `FAIL` | One or more required gates failed or required evidence is incomplete. | Fix or generate missing evidence, then rerun. |
| `PARTIAL` | No hard failure was found, but warnings or not-applicable areas remain. | Review warnings and decide whether more evidence is needed. |
| `BLOCKED_UNTIL_HUMAN_REVIEW` | A high-risk electrical, mechanical, footprint, connector, visual, or fab-readiness item needs human review. | Do not proceed to fabrication or later gates until resolved or explicitly accepted. |

## Gate Meanings

| Gate | What It Checks |
| --- | --- |
| `SCHEMATIC_ANNOTATION_GATE` | Annotation report and unresolved/duplicate reference risks. |
| `ERC_GATE` | Existing ERC report errors and warnings. |
| `SCHEMATIC_VISUAL_GATE` | Schematic full-page export, close-up crops, and visual review completion. |
| `FOOTPRINT_AUDIT_GATE` | Footprint/package audit and human-review blockers. |
| `PCB_SYNC_GATE` | PCB existence, schematic-to-PCB parity evidence, and orientation review. |
| `DRC_GATE` | Existing DRC report violations, parity errors, and unconnected pads. |
| `PCB_VISUAL_GATE` | PCB top/bottom visuals, close-up crops, and visual review completion. |
| `UNROUTED_NETS_GATE` | Existing DRC unconnected-pad summary. |
| `FAB_READINESS_GATE` | Whether final PCB verification allows `READY_FOR_NOT_FINAL_FAB_EXPORT`. |

## How To Read Blockers

Every blocker has:

- gate ID
- severity
- blocker text
- evidence path
- required fix

Start with `CRITICAL` blockers, then `HIGH` human-review blockers. A design is
not ready just because some gates pass.

## Current ATtiny85 Sample

The latest gate run for the ATtiny85 fixture reports:

- final classification: `BLOCKED_UNTIL_HUMAN_REVIEW`
- 9 gates checked
- 2 pass
- 3 fail
- 4 blocked
- 14 blockers

Important blockers include:

- `J1` USB-A shield ERC error
- 15 DRC violations
- 13 schematic parity/footprint issues
- `J1`, `J2`, and `U2` footprint/orientation/source review
- unreviewed schematic and PCB close-up crops
- fabrication readiness blocked

This is the expected current result.

## NOT_FINAL Rule

Gate reports and generated review artifacts are not manufacturing approval.
Generated outputs remain `NOT_FINAL` until ERC, DRC, BOM, datasheet, symbol,
footprint, connector, polarity, mechanical, and visual reviews are complete and
human-approved.
