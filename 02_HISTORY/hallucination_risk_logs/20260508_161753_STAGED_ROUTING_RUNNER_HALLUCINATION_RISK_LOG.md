# Hallucination Risk Log

- Risk source: inferring edit-required progress from Markdown routing reports.
- Mitigation:
  - replay detector against real ESP32 report history
  - require explicit final-state metric labels where available
  - ignore sidecar DRC-only reports in edit-run history
  - emit `BLOCKED_REPAIR_MODE` only after validated pair comparison
- Residual risk: future free-form report wording may require parser updates.
