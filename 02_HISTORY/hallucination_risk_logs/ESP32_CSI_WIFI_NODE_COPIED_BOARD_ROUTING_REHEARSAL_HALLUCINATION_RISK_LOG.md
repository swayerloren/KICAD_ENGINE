# Hallucination Risk Log - ESP32_CSI_WIFI_NODE Copied Board Routing Rehearsal

Date: `2026-05-10`

- Risk: overstating copied-board improvement as real-board readiness.
  Mitigation: final classification stayed `COPIED_ROUTING_BLOCKED`.
- Risk: treating heuristic unrouted-net reduction as full electrical success.
  Mitigation: DRC unconnected-item counts and explicit remaining open nets were
  reported.
- Risk: confusing the safest control candidate with the best routed candidate.
  Mitigation: reports separate `candidate_A_baseline` from
  `candidate_C_targeted_local_repair`.
