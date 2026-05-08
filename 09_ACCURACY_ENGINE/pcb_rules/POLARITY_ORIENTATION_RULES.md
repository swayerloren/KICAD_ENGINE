# Polarity And Orientation Rules

## Purpose

Flag parts that can be assembled backwards or connected with destructive polarity.

## Always Flag

- Diodes and LEDs.
- TVS and ESD arrays.
- Electrolytic and tantalum capacitors.
- Batteries and battery connectors.
- MOSFETs and BJTs.
- ICs with pin 1 orientation.
- Regulators.
- Optocouplers.
- Connectors carrying power.

## Required Checks

- Schematic polarity.
- Footprint pad mapping.
- Silkscreen polarity marker.
- Fab-layer pin 1 marker.
- 3D model orientation.
- Assembly drawing readability.

## Status

Use `POLARITY_HUMAN_REVIEW_REQUIRED` until visual and source evidence are checked.
