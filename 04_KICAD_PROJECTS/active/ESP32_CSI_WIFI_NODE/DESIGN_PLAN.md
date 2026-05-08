# ESP32_CSI_WIFI_NODE Design Plan

Status: planning only. No schematic, PCB layout, or manufacturing outputs exist yet.

## Design Goal

Create a complete custom ESP32-S3 CSI WiFi node PCB that is compact, robust, low-cost, long-term reliable, easy to assemble, easy to mount in a 3D printed enclosure, and easy for others to power and use.

## Architecture Summary

- Power enters through a 5.5 mm x 2.1 mm center-positive DC barrel jack from an external certified 5 V wall supply.
- Input protection handles overcurrent, reverse polarity, and 5 V transient events before the board 5 V node feeds local circuitry.
- A 3.3 V regulator powers the ESP32-S3-WROOM-1U module and low-voltage support components.
- USB-C provides programming/debug access and must include USB ESD protection and correct USB-C configuration.
- BOOT and RESET / EN buttons provide local recovery and programming control.
- Power/status indicators provide basic user feedback.
- Test pads expose 5 V, 3.3 V, and GND for bring-up and field troubleshooting.
- The ESP32-S3-WROOM-1U module provides WiFi and uses an external antenna through U.FL/IPEX-to-SMA pigtail routing into the enclosure.

## Schematic Block Plan

1. Power input and protection.
2. 3.3 V regulation.
3. ESP32-S3-WROOM-1U module.
4. USB-C programming/debug.
5. BOOT and RESET / EN controls.
6. Power LED and status LED or RGB LED.
7. 5 V, 3.3 V, and GND test pads.
8. Mounting holes and antenna mechanical clearance.

## Layout Direction

- Keep the board compact and rectangular.
- Place barrel jack and USB-C on enclosure-facing edges.
- Place four mounting holes near corners with screw/standoff keepouts.
- Keep protection parts close to external connectors.
- Keep regulator current loop short and thermally practical.
- Keep USB D+/D- short, paired, and away from noisy regulator nodes.
- Respect ESP32 module keepouts, ground guidance, and antenna connector access.
- Reserve pigtail bend radius and SMA hardware clearance early in mechanical placement.
- Maintain silkscreen labels for polarity, connector identity, BOOT, RESET, power LED, status LED, 5 V, 3.3 V, and GND.

## Work Phases

1. Component research and datasheet capture.
2. Schematic planning and block-level pin assignment.
3. Create KiCad project source files after active project and backup gate are confirmed.
4. Schematic capture.
5. ERC and schematic review.
6. PCB placement and routing.
7. DRC and visual/mechanical review.
8. BOM, footprint, datasheet, connector, polarity, antenna, and enclosure review.
9. Generate review-only outputs marked `NOT_FINAL`.
10. Fabrication readiness review only after all gates pass.

## Current Boundaries

- Do not create schematic yet.
- Do not create PCB layout yet.
- Do not create Gerbers or manufacturing outputs.
- Do not edit finished PCB reference projects.
- Do not install tools or clone repositories.

