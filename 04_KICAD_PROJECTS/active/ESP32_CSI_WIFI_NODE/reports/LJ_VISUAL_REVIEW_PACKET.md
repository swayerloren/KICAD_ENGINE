# LJ Visual Review Packet

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-06  
Purpose: current visual defect packet after strict re-audit  
Status: NOT_READY_NEEDS_MORE_VISUAL_REPAIR

## Open These Files

Full schematic exports:
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png`
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.pdf`
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.svg`

Close-up crops:
- `_verification/schematic_visual/crops/input_power.png`
- `_verification/schematic_visual/crops/reverse_polarity.png`
- `_verification/schematic_visual/crops/tvs_input_cap.png`
- `_verification/schematic_visual/crops/buck_regulator.png`
- `_verification/schematic_visual/crops/esp32_module.png`
- `_verification/schematic_visual/crops/usb_c_connector.png`
- `_verification/schematic_visual/crops/usb_esd.png`
- `_verification/schematic_visual/crops/cc_resistors.png`
- `_verification/schematic_visual/crops/reset_boot.png`
- `_verification/schematic_visual/crops/leds.png`
- `_verification/schematic_visual/crops/test_pads.png`
- `_verification/schematic_visual/crops/mounting_holes.png`
- `_verification/schematic_visual/crops/mechanical_notes.png`

## Current Decision

Do not approve this schematic for PCB update.

The schematic should be opened in KiCad only to confirm the listed visual defects. It is not clean enough for a final human visual review approval.

## LJ Checklist

Inspect these problem areas:
- Input fuse and `+5V_IN` / `+5V_FUSED` labels.
- Reverse-polarity PMOS Q1 and `+5V_PROTECTED` label placement.
- TVS/input capacitor area around D1 and C2.
- Buck regulator block around U1, C1, C3, C5, and L1.
- ESP32 module top power/value area and dense pin labels.
- USB-C connector CC/DP/DM labels.
- USB ESD and CC resistor support circuitry.
- Reset/boot resistors and switches.
- Power/status LED labels and resistor placement.
- Test pad label stacking.
- Review notes table clipping and mixed crop context.

## Required Before Approval

- Move all text, labels, refs, and values so they do not touch wires, pins, symbols, power symbols, or other text.
- Reframe close-up crops so each crop contains only the intended block and no clipped context.
- Keep review notes in a separate readable table outside circuitry.
- Re-run visual export and strict crop inspection.
- Keep PCB update blocked until the visual gate passes and high-risk part decisions are resolved.

## Final Status

Classification: NOT_READY_NEEDS_MORE_VISUAL_REPAIR  
PCB update allowed: NO
