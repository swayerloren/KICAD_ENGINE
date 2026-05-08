# Barrel Jack Orientation Confusion

Status: `USER_CONFIRMED_AGENT_MISTAKE`

Generated: `2026-05-07`

## Mistake

Codex previously confused the 3-pin solder-leg side of a horizontal DC barrel jack with the female barrel opening/front side.

## Correct Rule

For horizontal DC barrel jacks:

- female circular opening is the front/mating side
- 3-pin solder-leg side is the back/rear side
- edge-mounted opening faces off-board
- bottom-edge opening faces down/off-board
- bottom-edge solder/back side faces up/inward

## Avoidance Rule

Do not approve barrel jack orientation from coordinates alone. Require footprint geometry plus physical orientation evidence, and 3D proof when the exact model is available.

## Rule Patch Evidence

- `09_ACCURACY_ENGINE\pcb_rules\BARREL_JACK_ORIENTATION_RULES.md`
- `09_ACCURACY_ENGINE\pcb_rules\CONNECTOR_EDGE_ORIENTATION_RULES.md`
- `10_KNOWLEDGE_BASE\connectors\BARREL_JACK_ORIENTATION_GUIDE.md`

