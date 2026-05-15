# Local Wiring Style Guide

## Purpose

Define when a schematic should use actual wires instead of repeated local net
labels.

## Preferred Style

- Use short wires inside each functional block.
- Use junctions where three or more local wires meet.
- Keep local signal flow readable without needing to visually scan many labels.
- Improve symbol orientation before introducing local label shortcuts.
- Keep local MCU support circuits physically wired when the wire is short and
  readable.

## Allowed Label Use

- power rails
- cross-block nets
- long-distance nets
- sheet-to-sheet nets
- debug or test anchors
- cases where a direct wire would visibly clutter the drawing

## Disallowed Style

- one label at every local pin when a short wire would be clearer
- many repeated local labels inside the same block
- label-only local interconnect that turns one block into a text cloud
- detached single parts connected only by label spray
- labels compensating for poor symbol orientation
- short loopback or S-shaped local wire paths kept instead of a cleaner direct
  path
- graphic lines presented as if they prove electrical connectivity

## Practical Rules

- If two parts are near each other in the same block, prefer a wire.
- If EN/RESET/BOOT/strap pins, their pull parts, local LEDs, or local
  decoupling are near the MCU or module pins, prefer physical wiring.
- If a label appears three or more times inside one local block, review whether
  the block should be rewired locally.
- If labels sit directly on many local pins, the block likely needs wire-based
  cleanup.
- If a label remains in a local MCU support circuit, record why a physical wire
  would be worse.
- If a dark or emphasized local rail is used for readability, prove it is a
  real wire on the intended net.
- Local wiring cleanup must not change electrical intent.
