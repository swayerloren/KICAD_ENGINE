# PCB_PLACEMENT_PASS_1_BLOCKED_HALLUCINATION_RISK_LOG

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Risk label: `HIGH_RISK`

## Risk

Inferring placement without a PCB, board outline, verified footprints, and mechanical constraints would be unsafe.

## Required Agent Behavior

- Do not place components from schematic intent alone.
- Do not infer connector edge positions or antenna keepouts.
- Do not claim placement pass 1 exists until the PCB file exists and placement is actually performed.
- Keep placement blocked until PCB creation/update and mechanical setup pass.

