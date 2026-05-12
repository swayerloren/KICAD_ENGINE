# ESP32 RF Antenna Layout Rules

## Canonical Status

This file is the canonical PCB rule surface for ESP32 module antenna edges and
RF keepouts.

## Mandatory Rules

- The ESP32 antenna end must face the intended free edge.
- No copper, vias, traces, components, silkscreen clutter, or mechanical hardware may intrude into the antenna keepout.
- Do not place mounting holes, connector shells, or shield structures in the RF clearance zone.
- Keep noisy switching copper and USB routing away from the antenna edge.
- Treat module orientation as a mechanical truth item, not a guess from XY/rotation alone.

## Blocking Conditions

- antenna does not face the intended free edge
- any copper, via, or component intrudes into the RF keepout
- mounting hardware or connector metal crowds the antenna region
- routing uses the antenna corridor as spare space

## Source Registry References

- `url_000040` - Espressif ESP32-S3 hardware-design-guideline index
- `url_000041` - Espressif ESP32-S3 PCB layout design page
- `url_004540` - JLCPCB PCB design-guideline reference
