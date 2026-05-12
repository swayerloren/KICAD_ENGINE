# False Pass Patterns

Status: `ACTIVE_GUIDANCE`

## Never Call These A Pass

- a forum answer agrees with the layout
- a YouTube channel or lecture mentions the same topic
- a case study "looks similar"
- an autorouter connects things but produces ugly geometry
- DRC is clean but open nets remain
- a footprint exists but the package evidence is missing
- the connector sits near an edge but the real mating direction is unproven
- the schematic renders without ERC errors but is still unreadable

## Escalation Rule

If a pass depends on forum, video, training, or case-study material without
official or live-design corroboration, the correct result is:

- `UNVERIFIED`, or
- `NEEDS_HUMAN_REVIEW`

