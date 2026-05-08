# ESP32_CSI_WIFI_NODE Enclosure Fit Risk Report

Date: 2026-05-07

Mode: `READ_ONLY`

Output status: `NOT_FINAL`

Final classification: `MECHANICAL_REVIEW_BLOCKED`

## Summary

Enclosure fit cannot be verified from the current project state. The project has no PCB file, no board outline, no real component placement, no mounting hole geometry, no STEP export, and no enclosure model.

## Enclosure Risk Register

| ID | Risk | Severity | Status | Evidence | Closure requirement |
|---|---|---:|---:|---|---|
| MECH-001 | No PCB or STEP model exists | `CRITICAL` | `OPEN` | `.kicad_pcb` path check returned `False`; final PCB audit says no PCB. | Create PCB after gate pass and export NOT_FINAL STEP for review. |
| MECH-002 | Barrel jack panel fit unknown | `HIGH` | `OPEN` | J1 exact MPN/drawing and edge position unresolved. | Select exact jack, verify plug clearance, overhang, centerline, nut/body clearance if applicable. |
| MECH-003 | USB-C panel fit unknown | `HIGH` | `OPEN` | J2 exact suffix/drawing and shell/mechanical tabs unresolved. | Verify connector drawing, edge setback, shell tabs, cable plug clearance, and enclosure cutout. |
| MECH-004 | Barrel jack and USB-C spacing unknown | `HIGH` | `OPEN` | Plan B places both on the same edge, but no board outline/placement exists. | Check simultaneous cable insertion, finger clearance, label space, and panel structural web. |
| MECH-005 | ESP32 U.FL/pigtail/SMA path unknown | `HIGH` | `OPEN` | U2 RF path and pigtail bend clearance remain open; no keepout/3D model exists. | Define pigtail exit route, bend radius, SMA bulkhead location, and strain relief. |
| MECH-006 | ESP32 module keepout could be blocked | `HIGH` | `OPEN` | No copper/mechanical keepout exists; WROOM-1U footprint compatibility still needs review. | Verify footprint, keepout, enclosure material clearance, and antenna connector access. |
| MECH-007 | Mounting hole screw/standoff fit unknown | `HIGH` | `OPEN` | MH1-MH4 still require screw size, NPTH/PTH intent, washer/standoff clearance. | Confirm screw size, hole diameter, standoff OD, washer OD, edge offsets, and copper keepouts. |
| MECH-008 | Board thickness may conflict with connector fit | `MEDIUM` | `OPEN` | Board thickness is not locked. | Select board thickness and verify against USB-C/barrel jack drawings and enclosure slot height. |
| MECH-009 | Tall components may collide with enclosure | `HIGH` | `OPEN` | Exact connector, inductor, capacitor, switch, and module heights are not verified. | Select exact MPNs and inspect STEP/enclosure stack height. |
| MECH-010 | Test pads may be inaccessible | `MEDIUM` | `OPEN` | TP1-TP9 access not placed or checked against enclosure. | Place pads for probe access and define whether enclosure is open during test. |
| MECH-011 | LEDs may not be visible | `MEDIUM` | `OPEN` | LED exact parts and enclosure/window placement unresolved. | Define LED positions, color/intensity, viewing angle, light pipe or aperture. |
| MECH-012 | Reset/boot buttons may be inaccessible | `HIGH` | `OPEN` | SW1/SW2 exact switches and actuator direction unresolved. | Select switches and verify access method with enclosure. |
| MECH-013 | Silkscreen labels may be hidden or misoriented | `LOW` | `OPEN` | No PCB silkscreen exists. | Place readable labels after connector orientation is known. |

## Required Mechanical Inputs Before Pass

- Exact enclosure internal dimensions or target enclosure model.
- Exact barrel jack datasheet and plug dimensions.
- Exact USB-C receptacle datasheet and expected cable plug envelope.
- ESP32-S3-WROOM-1U RF connector/pigtail/SMA routing plan.
- Mounting screw size, standoff diameter, washer clearance, and board-edge offsets.
- Board thickness target.
- Max component height limit.
- Test/bring-up access requirement with enclosure open or closed.
- LED visibility and button access requirements.

## Decision

Enclosure fit may not be approved.

Final classification: `MECHANICAL_REVIEW_BLOCKED`
