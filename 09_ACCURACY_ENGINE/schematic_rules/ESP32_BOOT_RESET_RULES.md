# ESP32 Boot Reset Rules

## Mandatory Rules

- `EN`, `BOOT`, reset switch, boot switch, and their pull components must read as one local control block.
- Use local wires where they make the control path clearer than repeated labels.
- Keep strap-related components visually near the ESP32 pins they affect.
- Show button intent clearly; do not bury reset/boot behavior inside random notes or remote labels.
- Do not guess strap polarity or resistor intent.

## Blocking Conditions

- reset/boot block is visually detached from the ESP32
- local label-only wiring hides the control behavior
- strap resistors or switches are undocumented or ambiguous

## Source Registry References

- `url_000043` - Espressif ESP32-S3 schematic-checklist page
- `url_000040` - Espressif ESP32-S3 hardware-design-guideline index
