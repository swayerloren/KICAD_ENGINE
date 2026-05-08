# PCB_MECHANICAL_SETUP_BLOCKED_HALLUCINATION_RISK_LOG

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Risk label: `HIGH_RISK`

## Risk

Inferring board outline, mounting holes, connector edge placement, antenna keepout, barrel jack clearance, USB-C clearance, or test-pad access geometry would be unsafe because the project lacks a PCB file and confirmed mechanical dimensions.

## Required Agent Behavior

- Do not invent board dimensions.
- Do not create a PCB outline from generic assumptions.
- Do not place connectors or mounting holes without exact mechanical constraints.
- Keep the mechanical setup blocked until user-confirmed constraints are available.

