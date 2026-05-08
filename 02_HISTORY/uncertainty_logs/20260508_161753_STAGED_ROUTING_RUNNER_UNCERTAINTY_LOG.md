# Uncertainty Log

- The no-progress detector relies on routing report labels remaining structurally
  similar to the current ESP32 report set.
- Some early routing reports still do not expose fully symmetric before/after
  metrics, so the detector falls back to prior after-state values where needed.
- A future machine-readable routing-pass schema would reduce parser drift risk.
