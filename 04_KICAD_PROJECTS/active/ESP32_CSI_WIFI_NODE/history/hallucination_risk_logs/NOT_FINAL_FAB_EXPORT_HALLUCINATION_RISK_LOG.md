# NOT_FINAL Fab Export Hallucination Risk Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Risk label: `HIGH_RISK`

## Risk

Future agents may try to create a `NOT_FINAL` package because the user asked for one, even though the required readiness report is blocked.

## Required Behavior

Do not export manufacturing-style files until `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md` is exactly `READY_FOR_NOT_FINAL_FAB_EXPORT`.

## Evidence

- `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`
- `reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md`

