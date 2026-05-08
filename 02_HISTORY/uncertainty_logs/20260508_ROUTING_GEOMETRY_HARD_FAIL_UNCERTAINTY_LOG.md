# Uncertainty Log - Routing Geometry Hard Fail

Date: `2026-05-08`

## Low Uncertainty Items

- Script syntax validity was checked directly.
- Standalone geometry checks were validated directly on dedicated fixtures.
- Integration with the trace audit and scorecard was validated directly.

## Remaining Uncertainty

- Pad-entry quality is inferred from runout geometry rather than full pad-shape
  extraction.
- Real-board extraction may later expose additional geometry edge cases not
  covered by the current fixture set.
