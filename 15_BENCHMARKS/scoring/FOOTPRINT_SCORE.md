# Footprint Score

Default symbol/footprint allocation portion: up to 20 points combined with symbol correctness. Use this file for the footprint-specific part of that score.

## Criteria

| Area | Points | Checks |
| --- | ---: | --- |
| Exact package/drawing match | 5 | Footprint is compared against exact manufacturer package or connector drawing |
| Pad and drill geometry | 4 | Pad size, pitch, hole/slot size, paste/mask, and mechanical pads are checked |
| Pin 1 and orientation | 4 | Pin numbering, rotation, insertion/cable direction, and board-edge assumptions are explicit |
| Courtyard/fab/silkscreen | 3 | Assembly outline, courtyard clearance, silkscreen polarity/pin marks, and fab layer are reviewed |
| 3D/mechanical status | 2 | 3D model presence, alignment, height, mating connector, and enclosure implications are recorded |
| Verification wording | 2 | Status is `VERIFIED_WITH_SOURCE`, `UNVERIFIED_FOOTPRINT`, or `REJECTED`; no ambiguous approval |

## Connector Special Rule

Connector footprints require an exact manufacturer drawing and human orientation review. Generic connector records must remain `UNVERIFIED_PLACEHOLDER` until matched to an exact MPN and drawing.

## Automatic Penalties

- Name-match-only footprint approval: cap at 50 total score.
- Missing pin 1 orientation: subtract up to 4.
- Missing mechanical tab/shell/peg review: subtract up to 4.
- 3D model used as sole proof: subtract up to 3.
- Footprint approved from an incompatible package variant: cap at 40 total score.
