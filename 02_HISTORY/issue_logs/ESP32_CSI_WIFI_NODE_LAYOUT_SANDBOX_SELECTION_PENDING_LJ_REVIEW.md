# ESP32_CSI_WIFI_NODE Layout Sandbox Selection Pending LJ Review

Date: `2026-05-07`

## Issue

`VARIANT_C_ROUTING_POWER_RF_OPTIMIZED` is the current sandbox front-runner, but it is not approved for real PCB placement or editing yet.

## Blocking Reasons

- Board dimensions remain assumptions.
- Exact `J1` and `J2` package/footprint lock remains unresolved by project gate evidence.
- `U2` `ESP32-S3-WROOM-1U-N16R8` RF connector and pigtail clearance need LJ approval.
- The selected outline is purpose-shaped and needs explicit acceptance.
- Upstream schematic-to-PCB and footprint/package gates remain failed.

## Required Follow-Up

1. LJ review of the selected layout plan.
2. Mechanical dimension confirmation.
3. Exact connector and RF mechanical evidence review.
4. Upstream gate resolution before real PCB placement work.

## Status

`OPEN`
