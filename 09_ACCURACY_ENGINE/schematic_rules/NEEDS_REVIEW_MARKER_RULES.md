# NEEDS_REVIEW Marker Rules

1. Do not leave `NEEDS_REVIEW`, `BLOCKED`, or `UNVERIFIED` in visible
   production-symbol values unless the project gate explicitly documents the
   blocker.
2. Any unresolved visible review marker blocks schematic-to-PCB readiness.
3. ERC pass does not override unresolved review markers.
