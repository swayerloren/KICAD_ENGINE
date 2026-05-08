# PIC Reset And Oscillator Rules

Date: 2026-05-02

Status: design-rule snippet for PIC, PIC24, PIC32, and dsPIC schematic review.

## MCLR And Reset

- Check whether MCLR is enabled, disabled, or multiplexed for the exact device.
- If MCLR is used, verify pullup, optional series resistance, ESD exposure, reset switch, and programming-voltage compatibility.
- Do not add large capacitance to MCLR unless the programming specification allows it.
- Do not assume brownout reset, power-on reset, watchdog, or configuration-bit defaults.

## Oscillator

- Verify internal oscillator capability, accuracy, startup, and clock-source configuration bits.
- For external crystals or resonators, use the exact Microchip oscillator guidance and crystal vendor data.
- Place crystal and load capacitors close to OSC pins with a quiet return path.
- USB-capable PIC parts often need tighter clock accuracy than simple GPIO designs.
- CAN/CAN FD timing should be reviewed with oscillator tolerance and transceiver requirements.

## Voltage And IO

- Distinguish older 5 V PIC designs from 3.3 V or lower-voltage parts.
- Do not assume 5 V tolerance on 3.3 V devices.
- Verify analog rails, VREF, AVDD/AVSS, VCAP/core regulator pins, and any USB or CAN supply pins.

## KiCad Review Checklist

- Reset net is named clearly and tied to the correct pin.
- OSC pins match the chosen clock source and package pinout.
- Configuration-bit assumptions are written in project notes.
- Decoupling exists for every VDD/VSS pair and analog supply.
- Any USB, CAN, oscillator, and programming support parts are kept near the MCU pins they serve.

## Common Mistakes

- Copying reset/oscillator circuits from a dev board without checking configuration bits.
- Using an Arduino/PIC demo board crystal value as proof.
- Missing VCAP or core regulator pins on PIC32/dsPIC devices.
- Ignoring MCLR/VPP constraints when adding reset supervisors or RC delay networks.
