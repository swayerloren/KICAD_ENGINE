# Uncertainty Log

- Exact MPNs remain unresolved for several package-level parts: fuse, TVS, inductor, switches, LEDs, and most passives.
- The current run did not edit the saved schematic footprint fields because the live schematic already had no blank footprints and the unresolved items are high-risk package-proof issues, not simple empty-field fixes.
- `U2` almost certainly needs the `ESP32-S3-WROOM-1U` land pattern, but I left the saved schematic unchanged in this run and recorded the mismatch for human review.
- `U3` almost certainly needs the TI `Texas_DRT-3` package, but I left the saved schematic unchanged in this run and recorded the mismatch for human review.
