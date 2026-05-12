# Readable Schematic Flow Rules

1. Functional blocks must be recognizable and intentionally grouped:
   - input power and protection
   - buck regulator
   - ESP32 module
   - USB-C, ESD, CC, and data resistors
   - reset and boot
   - LEDs
   - test pads and debug
   - mounting or mechanical notes
2. The drawing must read left-to-right or top-to-bottom.
3. Power entry must appear before regulation and distribution.
4. Interface connectors must stay with their local protection and support parts.
5. The MCU or module must remain visually tied to its local support circuitry.
6. Inputs generally belong left, outputs generally right, power generally top, and ground generally bottom unless a better readable layout is proven.
7. Detached single parts or random clusters are a readability failure even if ERC still passes.
8. Use real wires inside local blocks unless a wire would clearly reduce readability.
9. ERC pass does not override bad flow.

## Source Registry References

- `url_009667` - TI USB-C / interface app note context for connector block grouping
- `url_010082` - ROHM buck layout note context for power-path grouping
- `url_000043` - Espressif ESP32-S3 schematic-checklist page
