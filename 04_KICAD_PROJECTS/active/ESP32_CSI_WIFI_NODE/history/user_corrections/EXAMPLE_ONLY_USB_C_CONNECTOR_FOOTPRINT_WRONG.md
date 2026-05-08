# EXAMPLE_ONLY User Correction: USB-C Connector Footprint

Status: `EXAMPLE_ONLY`

This record demonstrates the required format. It is not a claim about an actual `ESP32_CSI_WIFI_NODE` event.

## Correction

- Scope: `PROJECT`
- Project: `ESP32_CSI_WIFI_NODE`
- User correction: "The USB-C connector footprint was wrong and the board did not fit the connector."

## What Was Wrong

- `EXAMPLE_ONLY`: The connector footprint was treated as acceptable before exact manufacturer drawing and orientation verification.

## Required Behavior Change

- USB-C connector footprints must be marked `UNVERIFIED_FOOTPRINT` until an exact manufacturer part number and drawing are matched to the KiCad footprint.
- Human orientation review is required before layout freeze or fabrication output.

## Memory Updates

- Project memory update required: yes.
- Global memory update required: yes, because this is a reusable connector-footprint mistake pattern.

## Open Issue Needed

- Yes. Create an issue requiring exact connector footprint verification.

