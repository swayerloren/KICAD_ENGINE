# Wire Vs Net Label Rules

## `ORIENT_SYMBOLS_BEFORE_LABELS`

1. Before using a local label, decide whether rotating, flipping, mirroring, or
   repositioning symbols would allow cleaner physical wiring.
2. If orientation fixes the local readability problem, do that first.
3. Labels are not allowed as a shortcut for poor symbol orientation.

## `LOCAL_WIRE_BEFORE_NET_LABEL`

1. Use wires for local same-block connections when the wire can stay short,
   orthogonal, and readable.
2. Use labels for cross-block, cross-sheet, long-distance, power-rail, or
   debug/test-anchor nets when a direct wire would clearly reduce readability.
3. Do not replace readable local wiring with repeated isolated labels.
4. Do not put a label at every local pin when a short wire would read more
   clearly.
5. Excessive repeated labels inside one block are a readability failure.
6. Three or more repeated local labels inside the same functional block should
   trigger a cleanup review.
7. Local label-only wiring is allowed only when a direct wire would clearly
   reduce readability.

## `MCU_LOCAL_SUPPORT_PHYSICAL_WIRING`

1. Local MCU or module support circuits should usually be physically wired when
   close to the controlled pins.
2. This includes `EN`, `RESET`, `ESP_EN`, `BOOT0`, `IO0`, strap pins, local
   switches, pullups/pulldowns, local LEDs, and local decoupling.
3. If a label remains in one of these local support circuits, the review report
   must justify why the physical wire would be worse.

## Local Path Quality

1. Short local control paths should not use loopback or S-shaped routing when a
   direct readable path is available.
2. Floating labels or duplicate labels on both ends of a short local path are a
   readability failure.

## Source Registry References

- `url_009667` - TI USB-C / interface app note context for readable local support blocks
- `url_010082` - ROHM buck layout note context for tight local support grouping
- `url_000043` - Espressif ESP32-S3 schematic-checklist page
