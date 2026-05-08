# EXAMPLE_ONLY Open Issue: Verify USB-C Connector Footprint

Status: `EXAMPLE_ONLY_OPEN`

This record demonstrates the required format. It is not a claim about an actual `ESP32_CSI_WIFI_NODE` event.

## Issue

- Scope: `PROJECT`
- Project: `ESP32_CSI_WIFI_NODE`
- Severity: `HIGH`
- Title: USB-C connector footprint must be reverified against exact manufacturer drawing.

## Description

The user reported that the USB-C connector footprint was wrong and the board did not fit the connector.

## Risk

- Connector cannot be assembled.
- Pin numbering or orientation may be wrong.
- Board edge, shell tabs, or mounting pads may not match the connector.
- Fabrication package may be unusable.

## Required Fix Or Decision

- Select exact USB-C connector MPN.
- Obtain manufacturer drawing.
- Compare drawing to KiCad footprint pad geometry, holes, shell tabs, courtyard, fab outline, and board-edge relation.
- Confirm 3D/mechanical fit.
- Obtain human review before closing.

## Close Criteria

- Footprint verification checklist complete.
- Human orientation review complete.
- Project memory updated.
- Any revised schematic/PCB passes required ERC/DRC gates.

