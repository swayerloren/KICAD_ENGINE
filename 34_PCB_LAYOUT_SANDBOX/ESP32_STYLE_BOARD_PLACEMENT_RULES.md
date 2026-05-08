# ESP32 Style Board Placement Rules

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Codex must use project requirements first.

## Purpose

Provide a sandbox-level placement rule pack for ESP32-style boards before any real PCB placement or routing begins.

## Core Rules

- The ESP32 module antenna must be at the board edge or in a clear keepout area unless the project uses an external-antenna module.
- Do not place copper, traces, mounting holes, connectors, test pads, shields, or tall components under the antenna keepout.
- USB-C usually belongs on a board edge with shell tabs and board-edge relationship verified.
- Barrel jack inputs usually belong on a board edge with insertion direction verified.
- Buttons must remain user-accessible after enclosure and cable insertion.
- LEDs must remain visible and should not be hidden by connector bodies or inserted cables.
- Test pads must remain accessible after assembly and should not be trapped under connectors or tall parts.
- Mounting holes must be spaced for real hardware and must have component, copper, and screw-head clearance checked.
- Keep switching regulators, inductors, and noisy power-input parts away from the antenna edge.
- Keep the power path and USB/data path plausible during placement planning, not after the board is crowded.

## Variant Failure Signals

- Antenna keepout blocked.
- Connector insertion direction unproven.
- USB-C or barrel jack left inboard with no mechanical reason.
- Buttons blocked by connector bodies, cables, or enclosure walls.
- LEDs not visible in the intended use orientation.
- Test pads inaccessible after assembly.
- Mounting holes too close to the antenna, connectors, or tall parts.
- Board outline selected without explaining why it supports the antenna, connectors, and routing.

## Required Variant Evidence

- module orientation
- keepout size and board-edge relationship
- connector edge plan
- button and LED access notes
- test-pad access notes
- mounting-hole spacing and clearance notes
- power-path and USB/data-path projection

## Review Gate

Human review is required for antenna clearance, connector orientation, hole placement, and final board-shape justification.
