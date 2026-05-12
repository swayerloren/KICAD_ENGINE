# ESP32 Dev Board Reference Rules

Status: `REFERENCE_RULES_ACTIVE`

## Purpose

Guide comparison of ESP32-style dev boards against open-source examples.

## Compare

- antenna keepout facing outward
- USB connector aligned to the board edge
- reset/boot controls near the module signals they serve
- test pads grouped as a service/debug cluster
- buck or regulator path kept short to the module supply entry
- readable schematic grouping around the ESP32 module

## Do Not Assume

- every ESP32 board should use the same outline
- every ESP32 board should use four mounting holes
- every sample's antenna clearance is correct

## Hard Rule

A reference sample may inform what looks common, but it may not override the
repo's ESP32 RF keepout, connector-orientation, or prelayout gate rules.
