# STM32 Common Mistakes

## High-Risk Mistakes

- Treating STM32 families as pin-compatible without checking alternate functions.
- Leaving BOOT0 undefined.
- Missing VDDA/VSSA or VCAP pins where required.
- Using crystal values from a development board without checking the chosen crystal.
- Forgetting SWD target voltage reference.
- Choosing a package footprint that matches pin count but not package dimensions.

## Agent Checks

- Verify exact family, part, and package suffix.
- Check power pins and special supply pins.
- Check BOOT0 and reset behavior.
- Check SWD connector pinout.
- Check oscillator choice against datasheet and reference manual.

## Required Human Review

Human review is required for boot configuration, clock tree assumptions, USB pins, CAN/FDCAN pins, and package footprint approval.

