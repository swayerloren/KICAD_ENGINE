# Human Drafting Mode

Use this standard for every schematic create, repair, visual-cleanup, and
schematic-readiness prompt.

## Purpose

Schematic work must optimize for human readability before relying on net labels,
ERC status, or automated overlap checks.

## Mandatory Questions Before Net Labels

1. Can the involved symbols be rotated, flipped, or repositioned so the circuit
   can be drawn cleanly?
2. Can this local connection be shown with a short orthogonal wire inside the
   same functional block?
3. Is the proposed label compensating for bad symbol orientation, weak block
   layout, or avoidable local wiring?
4. Would a human engineer understand the local circuit immediately at normal
   zoom?
5. Does every visible reference and value clearly belong to its own part?
6. If a dark or emphasized rail is being used for readability, how will it be
   proven as a real wire on the intended net?
7. If this is reset/boot or local control wiring, is the topology still obvious
   and safe when a human reads it directly?

## Required Rules

### `LOCAL_WIRE_BEFORE_NET_LABEL`

- If two connected symbols are in the same local functional block and can be
  connected cleanly with short orthogonal wires, use physical wires.
- Do not use floating labels, duplicate labels on both ends of a short local
  connection, or label-only islands as a shortcut.
- Net labels are allowed for cross-block signals, cross-sheet nets, power rails,
  test/debug anchors, or cases where a physical wire would clearly make the
  drawing uglier or harder to read.

### `ORIENT_SYMBOLS_BEFORE_LABELS`

- Before adding a net label, ask whether rotating, flipping, or repositioning
  the symbols would create cleaner physical wiring.
- If an orientation change fixes the readability problem, change orientation
  first.
- Do not preserve bad symbol orientation and compensate with floating labels.

### `MCU_LOCAL_SUPPORT_PHYSICAL_WIRING`

- MCU or module local support circuits should be physically wired when they are
  close to the controlled pins.
- This includes EN, RESET, BOOT0, BOOT, strap pins, local LED drive,
  pullups/pulldowns, and decoupling.
- Use a label only when the physical wire would create worse readability than a
  clearly owned named-net connection.

### `GRAPHIC_LINES_ARE_NOT_ELECTRICAL_WIRES`

- Graphical lines may frame or separate a block, but they are never electrical
  proof.
- If a power, ground, or common-return rail is drawn for readability, verify
  that it is a real schematic wire/net object on the intended net.
- Do not assume a dark rail is electrical just because it looks more
  presentation-ready.

### `RESET_BOOT_TOPOLOGY_SANITY`

- Reset and boot switches must not create a direct `+3V3` to `GND` short path.
- Pullup/pulldown behavior must match the intended MCU datasheet or reference
  circuit.
- Capacitor-to-ground or capacitor-to-return paths in the local control cluster
  must return to the intended node.
- Labels or wires must not obscure which node each switch or capacitor actually
  touches.

### `TEXT_OWNERSHIP_REQUIRED`

- Every visible reference and value must visually belong to the correct symbol.
- No value or reference may float in blank space or sit closer to a different
  part than its own symbol.
- Wires must not run through references, values, net labels, or symbol bodies.

### `GROUND_AND_POWER_RAIL_PRESENTATION`

- Ground and power rails should read like intentional rails or local return
  paths.
- Power and ground symbols should be oriented naturally for the local flow.
- Common return lines must be real wires, clearly tied to the intended net, and
  not confused with graphics.

### `HUMAN_PRESENTATION_REVIEW_REQUIRED`

- ERC passing is necessary but not sufficient.
- Text-overlap checks are necessary but not sufficient.
- Schematic create/repair loops continue until symbol orientation, signal flow,
  wire paths, label restraint, topology readability, ground/power rail
  presentation, and text ownership look intentionally drafted by a human
  engineer.
- No gate claim is allowed from ERC, overlap checks, or automated crops alone.

## MCU And Connector Guidance

- Keep local control rows readable near the MCU or module pins.
- Choose connector orientation from signal flow first, not from the default
  symbol pose.
- For USB support blocks, rotate or reposition connector, ESD, series
  resistors, and CC resistors before using labels.
- D+ and D- should read as a clean path, not as detached labels hiding weak
  geometry.

## Required Reporting For Create/Repair Work

- State which symbols were rotated, flipped, or repositioned and why.
- State which net labels were kept and why.
- List local labels replaced by physical wires.
- State any remaining local MCU-support labels and why a physical wire would be
  worse.
- Run or review
  `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py`
  when the task claims human-drafting cleanup, visual readiness, or local
  control-cluster improvement.
- State any graphic-line or electrical-wire verification performed for dark or
  emphasized power/ground/return rails.
- State any reset/boot topology sanity proof performed and whether a direct
  `+3V3`-to-`GND` short path is possible through any switch press.
- State ERC result, text-overlap result, and unresolved-reference result when
  those checks are available for the task.
- State whether each repaired block now reads clearly to a human engineer.
- Confirm schematic-to-PCB remains blocked until visual, ERC, annotation,
  footprint, and high-risk review gates all pass.

## Screenshot And Rendered-Image Rule

- If a rendered page, screenshot, or close-up crop still shows bad symbol
  orientation, ugly loopback wiring, label spray, detached text, or ambiguous
  rail/topology presentation, the schematic is not ready.
- Do not claim success because ERC passed, text-overlap passed, or automated
  crops were generated. The image evidence wins the argument about human
  readability.

## ESP32 Lessons To Reuse

- `ESP_EN` physically wired into `U2 EN` is better than a floating local
  `ESP_EN` label.
- `BOOT0` physically wired into `U2 IO0` is better than floating `BOOT0`
  labels or S-shaped loopback wiring.
- `STATUS_LED` may remain label-based only when a drawn wire would be longer or
  uglier; if the LED support circuit is local to the MCU pin, prefer the wire.
- USB `J2` orientation should be chosen for D+/D- flow before labels are
  added.
- `C3/C4` decoupling should read as a real `+3V3 -> capacitor -> GND`
  sub-block, not as isolated label-only capacitors.
