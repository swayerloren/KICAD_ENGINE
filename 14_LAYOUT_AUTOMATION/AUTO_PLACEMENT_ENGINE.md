# Auto Placement Engine

## Purpose

Define the automatic PCB component-placement intelligence layer used before real KiCad placement work.

This layer is for evidence-based planning and staged placement proposals. It is not a claim of complete automatic layout.

## Scope

The engine may:

- generate normalized placement constraints
- classify components into placement stages
- place fixed mechanical parts deterministically
- place component groups in a constrained order
- detect collisions and edge-clearance failures
- score placement quality before real KiCad edits

The engine may not:

- dump random placements
- ignore connector orientation or RF keepouts
- approve courtyard overlap
- approve impossible routing
- replace human review on high-risk connectors, RF, USB, or power layouts

## Placement Order

Use this exact order:

1. board outline
2. mounting holes
3. edge connectors
4. RF/antenna module and keepout
5. power input path
6. regulator/power components
7. USB/ESD/series/CC components
8. MCU/module support passives
9. reset/boot
10. LEDs
11. test pads
12. remaining low-risk passives

## Core Rules

- USB-C and barrel jack or other input connectors are fixed mechanical parts.
- ESP32 antenna keepout must be established before nearby placement.
- Power path must be placed in physical current-flow order.
- USB ESD must be near the USB connector.
- Decoupling capacitors must be near IC power pins.
- Test pads must remain accessible after assembly.
- Courtyard overlap is a failure.
- Board edge clearance must be checked.
- Placement is not approved if routing becomes obviously impossible.

## Required Inputs

- board dimensions and edge-clearance rules
- selected sandbox layout plan
- connector-orientation evidence
- antenna-keepout evidence
- footprint dimensions / courtyard dimensions
- component role metadata
- grouping metadata

## Required Outputs

- placement constraints
- fixed mechanical placement proposal
- grouped placement proposal
- collision / edge-clearance report
- placement score
- exact blocked reasons when the result is not acceptable

## Review Status

Use the placement engine for:

- planning
- pre-placement reasoning
- precheck scoring
- copied-board experimentation when explicitly allowed

Do not claim professional placement quality until:

- sandbox and schematic gates pass
- placement precheck passes
- DRC passes
- visual review passes
- routing feasibility remains credible
