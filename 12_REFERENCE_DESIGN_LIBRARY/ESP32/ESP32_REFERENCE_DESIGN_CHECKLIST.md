# ESP32 Reference Design Checklist

## Source And License

- Source owner identified.
- License recorded.
- Redistribution status recorded.
- Link-only unless copying is explicitly permitted.

## Technical Review

- Exact ESP32 family and module identified.
- EN/reset behavior reviewed.
- Boot/strapping pins reviewed against exact part.
- Programming/debug path identified.
- Power and decoupling reviewed.
- USB support reviewed for exact part.
- Antenna keepout and RF placement reviewed.
- Module footprint and pin numbering reviewed.

## Reuse Warnings

- Do not copy WROOM/WROVER/MINI footprints interchangeably.
- Do not assume ESP32, ESP32-S3, ESP32-C3, and ESP32-C6 boot pins match.
- Do not reuse RF/antenna layout without stackup and enclosure review.

## Human Review Needed

- RF/module placement.
- Boot strap defaults.
- USB/programming circuit.
- Footprint and pin numbering.

