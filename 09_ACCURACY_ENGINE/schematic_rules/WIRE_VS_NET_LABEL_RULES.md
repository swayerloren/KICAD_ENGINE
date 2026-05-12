# Wire Vs Net Label Rules

1. Use wires for local same-block connections.
2. Use labels for cross-block, cross-sheet, or long-distance nets.
3. Do not replace readable local wiring with repeated isolated labels.
4. Do not put a label at every local pin when a short wire would read more clearly.
5. Excessive repeated labels inside one block are a readability failure.
6. Three or more repeated local labels inside the same functional block should trigger a cleanup review.
7. Local label-only wiring is allowed only when a direct wire would clearly reduce readability.

## Source Registry References

- `url_009667` - TI USB-C / interface app note context for readable local support blocks
- `url_010082` - ROHM buck layout note context for tight local support grouping
- `url_000043` - Espressif ESP32-S3 schematic-checklist page
