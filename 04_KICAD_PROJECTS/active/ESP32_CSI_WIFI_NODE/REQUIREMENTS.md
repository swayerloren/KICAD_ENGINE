# ESP32_CSI_WIFI_NODE Requirements

Status: initial requirements captured on 2026-05-02.

This is an active design project workspace for a complete custom ESP32-S3 CSI WiFi node PCB. This file records the known requirements and open questions before schematic creation.

## Project Identity

- Project name: `ESP32_CSI_WIFI_NODE`
- Board purpose: compact, robust, low-cost ESP32-S3 node for CSI WiFi sensing and experimentation.
- Design scope: full custom PCB design, including schematic and PCB layout in future work.
- Current phase: requirements, component research, and schematic planning.
- Active project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

## Non-Goals

- Not a carrier board.
- Not a PCB for plugging in an ESP32 development board.
- Do not use a separate ESP32 development board.
- Do not use a bare ESP32-S3 chip for this version.
- Do not include 120 VAC on the PCB.
- Do not create schematic, PCB layout, Gerbers, drill files, pick-and-place files, or manufacturing outputs during workspace creation.

## Core Architecture

- Use an ESP32-S3-WROOM external antenna module soldered directly to the PCB.
- Preferred module: `ESP32-S3-WROOM-1U-N16R8`.
- Acceptable alternate module: `ESP32-S3-WROOM-1U-N8R8`.
- Use external certified 5 V DC wall power supply.
- Use a 5.5 mm x 2.1 mm center-positive DC barrel jack for power input.
- Include USB-C for programming and debug.
- Use external antenna support through the WROOM-1U module antenna connector and a U.FL/IPEX-to-SMA pigtail for a screw-on 2.4 GHz enclosure antenna.

## Required Electrical Blocks

1. 5 V DC barrel jack input.
2. Input fuse or resettable polyfuse.
3. Reverse-polarity protection.
4. 5 V TVS diode.
5. Bulk input capacitor.
6. 3.3 V regulator for the ESP32 module.
7. ESP32-S3-WROOM-1U module.
8. USB-C programming/debug connection.
9. USB ESD protection.
10. BOOT button.
11. RESET / EN button.
12. Power LED.
13. Status LED or RGB LED.
14. 5 V, 3.3 V, and GND test pads.
15. Mounting holes.
16. External antenna mechanical clearance.

## Power Requirements

- Input connector: 5.5 mm x 2.1 mm DC barrel jack.
- Input polarity: center-positive.
- Nominal input voltage: 5 V DC from an external certified wall supply.
- On-board regulated rail: 3.3 V for ESP32-S3-WROOM module and low-voltage support circuitry.
- Protection required: input overcurrent protection, reverse-polarity protection, 5 V transient protection, USB ESD protection.
- 120 VAC exclusion: mains voltage must remain outside the PCB and inside the external certified supply.

## USB Requirements

- Connector: USB-C.
- Role: programming and debug.
- USB protection: ESD protection close to the USB-C connector.
- Schematic decision pending: confirm whether to use ESP32-S3 native USB directly or include a USB-to-UART bridge.
- USB-C configuration pending: confirm connector footprint, CC resistor implementation, shield/chassis treatment, and whether power backfeed must be prevented.

## Mechanical Requirements

- Board shape: compact rectangle.
- Mounting: four mounting holes near corners.
- Enclosure: intended for a custom 3D printed enclosure.
- Barrel jack placement: face enclosure wall.
- USB-C placement: face enclosure wall.
- Antenna: provide enclosure-friendly pigtail/SMA clearance and strain-aware routing.
- Keepouts: reserve mechanical clearance for barrel plug, USB-C plug, pigtail bend radius, SMA nut/washer area, mounting screws, and enclosure standoffs.

## Fabrication And Assembly Requirements

- Target: easy for other people to build, power, mount, and use.
- Assembly style: ESP32-S3-WROOM module soldered directly onto the PCB.
- Manufacturing outputs: not created during workspace setup.
- Fabrication status: not final until ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, antenna clearance, and visual reviews are complete.

## Missing Requirements

- Exact board outline dimensions.
- Layer count and target stackup.
- Preferred fab house and assembly provider.
- Maximum board height and enclosure internal dimensions.
- Mounting hole diameter, screw size, and keepout/standoff geometry.
- Input current budget and required wall adapter current rating.
- 3.3 V regulator topology, current rating, thermal target, and efficiency target.
- Required operating temperature range.
- ESD/transient severity target for barrel input and USB connector.
- Whether USB-C should provide power, debug only, or both.
- Whether native USB is sufficient or a USB-to-UART bridge is required.
- Status LED choice: single-color status LED versus RGB LED.
- Desired debug/test access beyond 5 V, 3.3 V, and GND test pads.
- Exact antenna enclosure location, SMA bulkhead style, and pigtail length.
- Regulatory/certification expectations for redistribution or public build instructions.
- BOM cost target and preferred distributors.
- Lifecycle/availability constraints for module and protection/power parts.

