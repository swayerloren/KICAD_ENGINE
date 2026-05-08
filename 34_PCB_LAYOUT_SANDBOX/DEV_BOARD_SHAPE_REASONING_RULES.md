# Dev Board Shape Reasoning Rules

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Codex must use project requirements first.

## Purpose

Stop the AI from assuming every dev board should be a rectangle or square before connector, RF, mounting, and usability constraints are understood.

## Required Inputs

- connector locations and insertion directions
- antenna or RF keepout constraints
- mounting-hole requirements
- enclosure or mounting surface constraints
- user-access needs for buttons, LEDs, and test points
- projected power and USB/data routing paths

## Rules

- The AI must justify board shape; it must not assume it.
- The AI must not force a rectangle or square PCB when connector, mechanical, or RF requirements suggest another shape.
- Use the simplest shape that still preserves connector access, RF clearance, hole spacing, and routing feasibility.
- If a more complex shape solves a real mechanical or usability problem, record the reason explicitly.
- If shape simplification harms connector access, antenna clearance, or test access, reject that variant.

## Typical Acceptable Shapes

- rectangle when mechanics and routing support it cleanly
- pill or rounded rectangle for narrow dev boards
- stepped outline when one connector or RF section needs extra clearance
- connector-biased extension when insertion hardware needs body or cable space

## Variant Failure Signals

- board dimensions unknown but guessed anyway
- shape chosen only because it is familiar
- outline clips antenna keepout
- outline crowds connector bodies or cable insertion
- outline leaves buttons or test pads unusable
- outline creates obvious routing bottlenecks with no benefit

## Required Variant Notes

- why this shape was chosen
- what mechanical or usability problem it solves
- why a simpler shape was rejected if not used
- whether the shape helps or hurts routing feasibility

## Review Gate

Human review is required for final board shape when enclosure fit, cable insertion, RF clearance, or mounting behavior materially drive the outline.
