# Hallucination Risk Log: Schematic Visual Autocrop Setup

Record kind: `hallucination_risk_log`
Created: `2026-05-03T08:10:00`
Scope: `global`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Risk

An agent may mistake automatically generated crops for completed visual review or approval to move into PCB layout.

## Mitigation

- `CLOSE_UP_REVIEW.md` sets each human visual result to `NOT_REVIEWED`.
- The accuracy rule says visual review remains incomplete if crops miss intended blocks or unresolved field/reference risks remain.
- Active project quality-gate failure was logged because the generated review status is `FAIL`.

## Evidence

- `09_ACCURACY_ENGINE/verification_rules/CLOSE_UP_VISUAL_REVIEW_RULES.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/CLOSE_UP_REVIEW.md`
- `02_HISTORY/quality_gate_failures/ESP32_CSI_WIFI_NODE_CLOSE_UP_VISUAL_REVIEW_FAIL.md`
