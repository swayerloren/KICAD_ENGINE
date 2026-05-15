# Schematic Wiring Vs Label Rules

## Intent

Net labels are a readability tool, not a substitute for local drawing quality,
symbol orientation, or local topology readability.

## Mandatory Drafting Order

### `ORIENT_SYMBOLS_BEFORE_LABELS`

1. Before using a local label, decide whether rotating, flipping, mirroring, or
   repositioning the involved symbols would allow clean physical wiring.
2. If orientation fixes the local readability problem, do that before labels.
3. Labels are not allowed as a shortcut for poor symbol orientation.

### `LOCAL_WIRE_BEFORE_NET_LABEL`

1. Use wires for short local connections within the same functional block when
   the wire can be short, orthogonal, and readable.
2. Use labels for cross-block, long-distance, power-rail, repeated named-net,
   debug/test, or page-transition cases where explicit wires would reduce
   clarity.
3. Do not replace an entire local block with isolated labels at every pin.
4. Repeating the same label many times within one small block is a readability
   smell and should trigger review.
5. USB, buck, EN/BOOT, LED, and debug blocks should still show obvious local
   wiring even when some named nets leave the block.

### `MCU_LOCAL_SUPPORT_PHYSICAL_WIRING`

1. MCU or module local support circuits should usually be physically wired when
   they are close to the affected pins.
2. This includes `EN`, `RESET`, `ESP_EN`, `BOOT0`, `IO0`, strap pins, local
   reset/boot switches, pullups/pulldowns, local LEDs, and local decoupling.
3. If a label remains in one of these local support circuits, the report must
   justify why a physical wire would be worse.

## Local Path Quality

- Prefer direct orthogonal wire paths inside the block.
- Do not keep short S-shaped or loopback local wiring when a cleaner direct
  path exists.
- Do not use floating labels or duplicate labels on both ends of a short local
  connection.

## Visual Rail Honesty

- A local return or rail drawn to improve readability is acceptable only when
  it is a real schematic wire on the intended net.
- Graphical lines may frame or separate a block, but they are never electrical
  proof.

## Gate

The schematic quality engine may fail or warn a block when:

- label count exceeds local wire count substantially
- the same label is repeated many times within one block
- a block appears as isolated symbols plus labels instead of a readable circuit
- labels remain only because symbol orientation was not improved first
- a short readable local wire was available but a label shortcut was kept
- local MCU support nets stay label-based without justification
- a short control path uses loopback or S-shaped wiring when a direct path
  exists
- a visually emphasized local rail or return path is not proven as a real wire
  on the intended net
