# Mounting Hole Mechanical Rules

## Canonical Status

This file is the canonical rule surface for mounting-hole placement on compact
boards.

## Mandatory Rules

- Mounting holes must not collide with RF keepouts, connector openings, or important routing corridors.
- Do not place holes so close to the board edge or connector shell that assembly/mechanical fit becomes ambiguous.
- Mounting-hole decisions on narrow boards require explicit clearance proof, not habit.
- If four-hole placement creates dead space or crowding on a narrow board, reduce hole count or change board shape.

## Blocking Conditions

- hole intrudes into RF keepout
- hole crowds connector mouth or shell
- hole choice creates unexplained dead area or impossible routing
- hole courtyard or hardware clearance overlaps components or silkscreen refs

## Source Registry References

- `url_004538` - JLCPCB assembly design-requirements reference
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
