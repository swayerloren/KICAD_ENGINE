# Decoupling Schematic Rules

## Mandatory Rules

- Show decoupling capacitors near the IC power pins they support in the drawing when possible.
- Group local decoupling with the IC or regulator block it belongs to.
- Do not collapse all supply support parts into remote unlabeled capacitor farms.
- Use enough wiring or labeling that the supported rail and pin context is readable.

## Blocking Conditions

- decoupling is visually detached from the part it supports
- rail intent is ambiguous
- capacitor grouping hides which device or rail is being supported

## Source Registry References

- `url_010082` - ROHM buck layout note
- `url_010083` - onsemi converter layout note
- `url_000043` - Espressif ESP32-S3 schematic-checklist page
