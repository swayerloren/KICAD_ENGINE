# Mechanical Orientation Truth

## Purpose

This folder is the authoritative mechanical-orientation truth layer for connector-facing and antenna-facing PCB decisions.

It exists to stop these common failures:

- mistaking barrel-jack solder pins for the port opening
- treating USB-C XY position or rotation alone as proof that the mouth faces off-board
- treating an ESP32 module as acceptable when its antenna keepout faces inward

## Scope

This layer defines:

- connector front/back meaning
- port-opening direction meaning
- pin-side meaning
- PCB-edge alignment expectations
- when 3D-model evidence is missing
- when routing must remain blocked

## Hard Rules

1. Connector orientation is not proven by XY position or rotation value alone.
2. Barrel jack pin side must not be mistaken for port opening.
3. USB-C mouth/opening must face off-board and align with `Edge.Cuts`.
4. ESP32 antenna keepout must face outward.
5. If a required connector 3D model is missing, mark it `NEEDS_HUMAN_REVIEW`.
6. Do not proceed to routing if connector orientation is not proven.

## Files

- `connector_orientation_truth.json`
- `barrel_jack_orientation_rules.md`
- `usb_c_orientation_rules.md`
- `esp32_module_antenna_orientation_rules.md`
- `connector_orientation_examples.md`

## Agent Rules

- Use `connector_orientation_truth.json` as the machine-readable source of truth.
- Use the Markdown files for human-readable explanation and examples.
- If the footprint family is unknown or the 3D model is missing, do not silently promote the result to `PASS`.
- Route only after the orientation audit returns `PASS`.
