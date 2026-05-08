# NEEDS_REVIEW Blocker Rules

## Purpose

`NEEDS_REVIEW` is a blocking state for uncertain KiCad engineering decisions. It prevents false confidence when an AI agent has not verified a high-risk electrical, mechanical, library, or manufacturing detail.

## Status Meaning

Use `NEEDS_REVIEW` when an item is known to require confirmation but has not yet been resolved with evidence or human approval.

Use `BLOCKED` when a `NEEDS_REVIEW` item prevents the next workflow step.

Use `PASS` only when the item is verified by source evidence, KiCad evidence, command output, or explicit human confirmation.

## High-Risk NEEDS_REVIEW Items

The schematic-to-PCB gate is blocked by any unresolved `NEEDS_REVIEW` on:

- Power input path.
- Reverse polarity protection.
- Polyfuse, fuse, TVS, ESD, or surge protection.
- Regulator topology, passives, feedback, thermal assumptions, or enable behavior.
- AO3401A or any MOSFET symbol-to-footprint pin mapping.
- USB-C connector selection, pin numbering, CC wiring, VBUS policy, shield policy, ESD placement, or D+/D- series resistors.
- ESP32 EN, BOOT, strapping pins, USB pins, module footprint, keepout, antenna path, or power pins.
- Connector footprint, mating connector, orientation, pin 1, shell, shield, mounting tabs, or mechanical fit.
- Polarity-sensitive parts such as diodes, LEDs, electrolytic/tantalum capacitors, MOSFETs, regulators, ICs, and polarized connectors.
- RF connectors, antenna keepouts, feedlines, module keepouts, or pigtail/mechanical clearance.
- CAN, USB, RF, automotive, or high-current nets.
- Footprint assignments not verified to exact package drawings.
- BOM lock mismatches.
- Fabrication, assembly, drill, pick-and-place, or STEP output assumptions.

## Low-Risk NEEDS_REVIEW Items

Low-risk `NEEDS_REVIEW` items may remain only if:

- They do not affect electrical correctness, package fit, connector orientation, safety, manufacturing, or PCB layout.
- They are listed in the gate status file.
- They are explicitly classified as non-blocking.
- A human reviewer accepts the classification.

If unsure, treat the item as high risk.

## Project-Specific Required Review Items

For `ESP32_CSI_WIFI_NODE`, these items are always high-risk until resolved:

- AO3401A symbol/footprint pin mapping.
- USB VBUS source and backfeed policy.
- USB shield/shell policy.
- Power rail naming standard.
- Regulator input/output passives.
- USB-C CC resistor wiring.
- USB ESD wiring.
- USB D+/D- series resistor wiring if used.
- ESP32 EN circuit.
- ESP32 BOOT and strapping behavior.
- ESP32 module footprint, keepout, and antenna connector access.
- All connectors and mating connector orientation.
- Polarity-sensitive protection and power parts.

## Required Record Fields

Every `NEEDS_REVIEW` item must record:

- Item name.
- Location or schematic block.
- Risk category.
- Why review is needed.
- Evidence currently available.
- Evidence missing.
- Owner or reviewer.
- Blocking status.
- Resolution requirement.
- Date opened.
- Date closed, if applicable.

## Resolution Rules

A `NEEDS_REVIEW` item may be closed only when:

- Exact source evidence is recorded, or
- KiCad file evidence and command output support the decision, or
- The user explicitly confirms the decision and the confirmation is recorded in project history.

Do not close `NEEDS_REVIEW` by inference, pattern matching, component popularity, or generic library availability.
