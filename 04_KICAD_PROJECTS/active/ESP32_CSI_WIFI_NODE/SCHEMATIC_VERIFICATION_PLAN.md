# ESP32_CSI_WIFI_NODE Schematic Verification Plan

Status: pre-schematic plan. ERC cannot be run yet because no KiCad schematic exists.

## Verification Goal

Before any PCB layout or manufacturing-style output, verify that the schematic is electrically coherent, matches datasheets, supports safe power/debug operation, and preserves the project constraints: complete custom PCB, ESP32-S3-WROOM-1U module, external certified 5 V supply, no 120 VAC, no development board.

## Pre-Schematic Checks

- Confirm selected ESP32-S3-WROOM-1U module variant and datasheet revision.
- Confirm whether USB programming/debug uses native ESP32-S3 USB or a USB-to-UART bridge.
- Confirm power source behavior: barrel-only, USB-only, or dual-source restrictions.
- Confirm input current budget and regulator current/thermal margin.
- Confirm antenna pigtail and SMA mechanical concept before module placement assumptions are locked.
- Confirm board size, mounting hole dimensions, and enclosure constraints.

## Block-Level Schematic Checks

- Barrel input:
  - Verify connector pin numbering and center-positive polarity.
  - Verify fuse/polyfuse voltage and current ratings.
  - Verify reverse-polarity protection behavior and heat.
  - Verify TVS working voltage, clamp behavior, and ground return.
  - Verify bulk capacitor voltage rating and derating.

- 3.3 V regulator:
  - Verify input/output capacitor values and ESR requirements.
  - Verify inductor/diode/feedback network if using a buck regulator.
  - Verify load current margin for ESP32-S3 WiFi operation.
  - Verify power-good or enable behavior if used.

- ESP32-S3 module:
  - Verify power pins and decoupling.
  - Verify EN/RESET circuit.
  - Verify BOOT/strapping pin states.
  - Verify USB pins, GPIO allocation, LED GPIO, and unavailable/reserved pins.
  - Verify module footprint, pin numbering, keepouts, and antenna connector access.

- USB-C:
  - Verify CC resistor configuration.
  - Verify D+/D- connectivity and ESD placement.
  - Verify shield/shell grounding decision.
  - Verify no unsafe backfeed between barrel 5 V and USB 5 V.

- LEDs/buttons/test pads:
  - Verify resistor values and GPIO current limits.
  - Verify button pull-up/pull-down behavior.
  - Verify test pads are on correct nets and clearly labeled.

## ERC Plan

After schematic creation:

1. Run KiCad ERC through the approved workspace verification workflow.
2. Save ERC output under project reports or approved `02_HISTORY\erc_drc_reports`.
3. Classify every ERC warning/error as fixed, intentional, waived with evidence, or blocked.
4. Do not proceed to PCB layout until ERC findings are addressed or explicitly accepted for a documented reason.

## Datasheet And Footprint Review

- Compare each symbol pinout against the manufacturer datasheet.
- Compare each footprint against the manufacturer land pattern or mechanical drawing.
- Verify polarity/orientation for barrel jack, TVS, LEDs, capacitors, buttons, USB-C, regulator, and ESP32 module.
- Verify connector shell/shield pins and mounting tabs.
- Verify mounting holes are NPTH/PTH according to mechanical intent.

## BOM Review

- Confirm manufacturer part number, package, ratings, and lifecycle for each selected part.
- Confirm sourcing availability and alternates for the ESP32 module, regulator, USB-C connector, barrel jack, and protection parts.
- Mark unverified substitutes as not approved.

## Release Gate

The design is not fabrication-ready until all of these pass:

- Schematic ERC.
- PCB DRC.
- BOM review.
- Footprint review.
- Netlist/cross-probe review.
- Datasheet review.
- Connector and polarity/orientation review.
- Power input/protection review.
- Antenna mechanical clearance review.
- Enclosure/mounting review.
- Visual review.

Generated outputs must remain `NOT_FINAL` until the full gate passes.

