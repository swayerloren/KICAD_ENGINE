# DFM Assembly Validation Rules

## Hard Rules

1. Fab package validation is not assembly approval.
2. BOM/CPL structural checks do not verify orientation or polarity.
3. Pick-and-place rotation requires visual/human review.
4. Connector orientation must be verified before export.
5. IC pin 1, diode polarity, LED polarity, capacitor polarity, and connector mating direction must be checked.
6. Nothing is `FAB_READY` unless final gates pass and LJ approves.
7. All exports remain `NOT_FINAL` until approved.
