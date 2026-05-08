# TASK 006: Connector Footprint Verification

Status: `NOT_RUN`.

## Objective

Ask an AI agent to verify whether a connector footprint is suitable for an exact connector part number. This benchmark is intentionally high-risk because connector mistakes are common, expensive, and hard for text-only AI agents to catch.

## Allowed Inputs

- Exact manufacturer connector part number.
- Manufacturer datasheet or mechanical drawing.
- KiCad footprint file or installed KiCad footprint candidate.
- 3D model if available.
- Mating connector/cable drawing if available.

## Expected Outputs

- Footprint verification report.
- Exact connector MPN and drawing citation.
- Pad, drill, slot, pitch, mechanical peg, shell, courtyard, fab, silkscreen, and pin-1 checks.
- 3D model status.
- Mating connector status.
- Human orientation review flag.
- Final status: `VERIFIED_WITH_HUMAN_REVIEW`, `UNVERIFIED_FOOTPRINT`, or `REJECTED`.

## Required Evidence

- Manufacturer drawing source.
- KiCad footprint source path.
- Pad-to-drawing comparison notes.
- Pin numbering and pin 1 orientation notes.
- Board-edge, insertion direction, and cable-exit assumptions.
- Any mismatch or uncertainty explicitly listed.

## Scoring Focus

- Correct footprint evidence.
- Connector orientation verification.
- 3D/mechanical review discipline.
- Human review flags.
- No unverified approval.

## Failure Modes

- Approving a footprint by name match only.
- Ignoring pin numbering direction.
- Ignoring mechanical tabs, shell pads, locating pegs, or board-edge constraints.
- Missing mating connector/cable orientation.
