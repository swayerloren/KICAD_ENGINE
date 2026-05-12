# PCB Fab Constraints Summary

## Canonical Guidance

- Treat fab-house capability pages as source-specific context, not universal
  truth.
- Keep board outline, drill, slot, cutout, and mounting-hole review in the
  export gate.
- Do not mark a package `FAB_READY` from CSV/Gerber structural checks alone.
- Keep all exports `NOT_FINAL` until the final routed-board review passes and
  LJ approves.
