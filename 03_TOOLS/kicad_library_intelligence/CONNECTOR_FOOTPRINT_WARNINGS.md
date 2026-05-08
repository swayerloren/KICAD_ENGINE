# Connector Footprint Warnings

Date: 2026-05-02

Purpose: warn agents about connector-specific failure modes in KiCad footprint selection.

## Connector Verification Checklist

- Exact manufacturer part number.
- Exact drawing revision.
- Pin numbering from PCB side and mating side.
- Mating connector or cable assembly.
- Orientation and cable exit direction.
- Top-entry, side-entry, vertical, right-angle, or edge-launch style.
- Shield, shell, mounting peg, and chassis connection requirements.
- Plated and non-plated mechanical holes.
- Courtyard, board edge, panel, enclosure, and keepout constraints.
- 3D model orientation and height.

## USB-C

- Generic USB-C footprints are not safe for final use.
- 6-pin, 14-pin, 16-pin, 22-pin, 24-pin, power-only, USB2-only, USB3/USB4, top-mount, mid-mount, and through-hole-hybrid variants are not interchangeable.
- CC pins, VBUS pins, SBU pins, shield tabs, mounting stakes, and shell pads must be checked.
- The generated sample search finds many `Connector_USB` candidates; none are correct until matched to an exact selected connector.

## JST, Molex, TE, And Similar Wire Connectors

- Pitch alone is not enough.
- Verify series, latch style, side/top entry, pin 1, footprint orientation, and mating housing.
- Watch for clone footprints with same pitch but different peg locations.

## RF Connectors

- U.FL, IPEX, MHF1, MHF3, and MHF4 are not interchangeable.
- SMA and RP-SMA gender must be checked from the connector and cable side.
- Edge-launch connectors require board thickness and controlled-impedance launch review.

## Terminal Blocks

- Verify pitch, wire entry direction, pin 1, current rating, drill sizes, and courtyard.
- Mechanical clearance matters more than symbol similarity.

## Automotive And OEM Harness Connectors

- Treat all generic records as placeholders.
- Verify terminal family, seal, latch, keying, pin numbering, and mating harness.
- Do not create final footprints from photos or marketplace listings alone.
