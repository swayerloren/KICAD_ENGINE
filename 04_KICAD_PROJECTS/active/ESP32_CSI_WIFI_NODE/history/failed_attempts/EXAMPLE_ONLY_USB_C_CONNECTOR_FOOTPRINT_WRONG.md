# EXAMPLE_ONLY Failed Attempt: USB-C Connector Footprint Was Wrong

Status: `EXAMPLE_ONLY`

This record demonstrates the required format. It is not a claim about an actual `ESP32_CSI_WIFI_NODE` event.

## Summary

- Scope: `PROJECT`
- Project: `ESP32_CSI_WIFI_NODE`
- Attempt: The agent selected or approved a USB-C connector footprint.

## Expected Result

- The selected footprint should match the exact connector manufacturer drawing, pin numbering, mechanical orientation, shell tab geometry, and board-edge relationship.

## Actual Result

- User reported: "The USB-C connector footprint was wrong and the board did not fit the connector."

## Root Cause

- `EXAMPLE_ONLY`: Agent likely relied on a generic footprint or unverified library candidate without exact manufacturer drawing and human orientation review.

## Recovery Taken

- Mark the connector footprint decision as failed.
- Create a user correction record.
- Create an open issue requiring exact connector MPN, drawing, KiCad footprint comparison, 3D/mechanical review, and human confirmation.

## Do Not Repeat

- Do not approve USB-C connector footprints from generic names or 3D appearance alone.

