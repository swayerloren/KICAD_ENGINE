# Local Wiring Style Guide

## Purpose

Define when a schematic should use actual wires instead of repeated local net
labels.

## Preferred Style

- Use short wires inside each functional block.
- Use junctions where three or more local wires meet.
- Keep local signal flow readable without needing to visually scan many labels.

## Allowed Label Use

- power rails
- cross-block nets
- long-distance nets
- sheet-to-sheet nets
- cases where a direct wire would visibly clutter the drawing

## Disallowed Style

- one label at every local pin when a short wire would be clearer
- many repeated local labels inside the same block
- label-only local interconnect that turns one block into a text cloud
- detached single parts connected only by label spray

## Practical Rules

- If two parts are near each other in the same block, prefer a wire.
- If a label appears three or more times inside one local block, review whether
  the block should be rewired locally.
- If labels sit directly on many local pins, the block likely needs wire-based
  cleanup.
- Local wiring cleanup must not change electrical intent.
