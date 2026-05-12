# Schematic Wiring Vs Label Rules

## Intent

Net labels are a readability tool, not a substitute for local drawing quality.

## Rules

1. Use wires for short local connections within the same functional block.
2. Use labels for cross-block, long-distance, or repeated named nets where
   explicit wires would reduce clarity.
3. Do not replace an entire local block with isolated labels at every pin.
4. Repeating the same label many times within one small block is a readability
   smell and should trigger review.
5. USB, buck, EN/BOOT, LED, and debug blocks should still show obvious local
   wiring even when some named nets leave the block.

## Gate

The schematic quality engine may fail or warn a block when:

- label count exceeds local wire count substantially
- the same label is repeated many times within one block
- a block appears as isolated symbols plus labels instead of a readable circuit
