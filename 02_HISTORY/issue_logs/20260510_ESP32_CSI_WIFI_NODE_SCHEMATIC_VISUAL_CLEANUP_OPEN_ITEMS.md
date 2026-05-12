# Open Items

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Remaining Schematic Cleanup Items

- USB block still has local `DM_C` / `DP_C` label crowding near the ESD symbol pin text.
- Reset RC text spacing still triggers overlap warnings.
- Block-flow audit is still `WARN`.
- Human visual proof is still not complete.

## Process / Tooling Gaps

- The native KiCad GUI annotation auto-open workflow still blocks at schematic-editor detection on this machine.
- The execution-contract schema currently lacks a valid schematic-edit task type, which leaves live schematic-edit sessions without a compliant contract path.
