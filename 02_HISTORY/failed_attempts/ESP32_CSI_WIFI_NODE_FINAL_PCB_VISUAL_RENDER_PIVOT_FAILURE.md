# ESP32_CSI_WIFI_NODE Final PCB Visual Render Pivot Failure

Date: `2026-05-08`

Status: `RECOVERED`

## Failed Attempt

Tried to build the final LJ close-up packet directly from `kicad-cli pcb render` camera crops using `--zoom` plus `--pivot`.

## What Failed

- Negative pivot values such as `-1.8,3.25,0` were interpreted badly in the PowerShell-to-KiCad CLI path and surfaced as `Unknown argument`.
- Some positive-pivot renders technically succeeded but did not frame the intended target area for top-down human review. The first USB-C area render landed on the top antenna region instead of the connector area.

## Recovery

- Kept the fresh full-board top and bottom renders.
- Switched the final packet to deterministic Pillow-based crops derived from the full-board renders.
- Spot-checked the replacement crops before writing the review package.

## Reusable Lesson

For top-down PCB human-review packets, prefer fresh full-board renders plus deterministic coordinate crops over camera-pivot 3D framing when exact target regions matter.
