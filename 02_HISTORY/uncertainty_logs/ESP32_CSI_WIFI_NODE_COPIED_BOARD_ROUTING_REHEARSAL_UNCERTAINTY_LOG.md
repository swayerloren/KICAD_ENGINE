# Uncertainty Log - ESP32_CSI_WIFI_NODE Copied Board Routing Rehearsal

Date: `2026-05-10`

- The copied routing scripts changed copper on the rehearsal boards, but not
  every added segment was manually inspected one by one. Acceptance status was
  based on DRC and quality-gate outputs.
- `candidate_C_targeted_local_repair` is the least-bad routed attempt, not a
  proven near-final route.
- `J1` orientation remains `NEEDS_HUMAN_REVIEW`, so even a cleaner copied route
  would still require that mechanical proof before real-board promotion.
