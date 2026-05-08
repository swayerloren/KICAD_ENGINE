# Quality Gate Failure - ESP32_CSI_WIFI_NODE Schematic To PCB Gate

## Status

- Date opened: 2026-05-03
- Scope: `ESP32_CSI_WIFI_NODE`
- Quality gate: `SCHEMATIC_TO_PCB_GATE`
- Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Reason

The schematic-to-PCB gate cannot pass because required evidence is missing:

- Annotation audit.
- ERC report.
- Full-page visual export.
- Close-up visual review.
- Electrical audit.
- BOM lock audit.
- Footprint/package drawing audit.
- Connector orientation review.
- Polarity-sensitive part review.
- High-risk `NEEDS_REVIEW` closure list.
- AO3401A pin mapping resolution.
- USB VBUS/shield policy.
- Regulator passive verification.
- USB-C wiring verification.
- ESP32 EN/BOOT verification.

## Blocked Actions

Until the project gate is `PASS`, agents must not update PCB from schematic, place parts, route traces, create zones, or generate PCB manufacturing outputs.

## Resolution Requirement

Create evidence reports, update `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`, and only mark `PASS` when every required check has evidence.
