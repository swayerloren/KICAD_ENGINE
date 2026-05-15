# ESP32 Boot Reset Rules

## Mandatory Rules

- `EN`, `BOOT`, reset switch, boot switch, and their pull components must read as one local control block.
- Use local wires where they make the control path clearer than repeated labels.
- Keep strap-related components visually near the ESP32 pins they affect.
- Show button intent clearly; do not bury reset/boot behavior inside random notes or remote labels.
- Do not guess strap polarity or resistor intent.
- Use physical local wiring for `EN`, `BOOT0`, local pull parts, local
  switches, and nearby status/control LEDs when the wire can stay short and
  readable.

## `RESET_BOOT_TOPOLOGY_SANITY`

- Reset switch topology must not create a direct `+3V3` to `GND` short path.
- Boot switch topology must not create a direct `+3V3` to `GND` short path.
- Pullup/pulldown behavior must match the intended ESP32 datasheet or reference
  circuit behavior.
- Any capacitor-to-ground or capacitor-to-return path in the control cluster
  must return to the intended node.
- Labels, wires, or notes must not obscure which node each switch or capacitor
  actually touches.
- If a local label remains in the control cluster, the report must justify why
  a physical wire would be worse.

## Blocking Conditions

- reset/boot block is visually detached from the ESP32
- local label-only wiring hides the control behavior
- strap resistors or switches are undocumented or ambiguous
- the visual wiring obscures whether a switch would short power directly to
  ground
- capacitor return intent is ambiguous

## Source Registry References

- `url_000043` - Espressif ESP32-S3 schematic-checklist page
- `url_000040` - Espressif ESP32-S3 hardware-design-guideline index
