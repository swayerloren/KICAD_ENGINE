# RF And Antenna Guide

Date: 2026-05-02

Status: AI-readable starter guide. RF entries require exact part numbers, board stackup, and vendor layout evidence before use.

## Scope

This guide covers antenna pigtails, PCB antenna keepouts, board-side RF connectors, cable transitions, and RF feedline review.

## What Agents Should Verify

| Item | Required Evidence |
| --- | --- |
| Frequency range | Exact antenna, cable, connector, and radio band. |
| Connector family | Exact U.FL/IPEX/MHF/SMA/RP-SMA variant and gender. |
| Board stackup | Dielectric thickness, copper thickness, soldermask, impedance target. |
| Feedline geometry | Calculator or fab-supported impedance result for the stackup. |
| Antenna keepout | Vendor drawing or module hardware design guide. |
| Matching network | Reference design and tuning plan. |
| Mechanical strain relief | Cable bend radius, retention, enclosure clearance. |

## KiCad Workflow

1. Identify the RF source: module pin, chip antenna, U.FL connector, SMA edge launch, or pigtail.
2. Determine whether the board needs a controlled-impedance feedline.
3. Record the PCB stackup before calculating trace width or clearance.
4. Add keepout zones based on the antenna or module source document.
5. Treat RF connector footprints as mechanical drawings, not generic pin headers.
6. Review 3D model, connector orientation, enclosure clearance, and cable routing.

## Common Mistakes

- Copying a 50 ohm trace width from a different board stackup.
- Placing copper pour or mounting hardware inside an antenna keepout.
- Mixing SMA and RP-SMA gender assumptions.
- Treating a U.FL pigtail as if it defines the board-side connector footprint.
- Omitting an RF matching network when the antenna or module reference design expects one.

## Placeholder Policy

Generic RF records remain `UNVERIFIED_PLACEHOLDER` until a selected vendor part, drawing, source URL, stackup, and footprint review are recorded.
