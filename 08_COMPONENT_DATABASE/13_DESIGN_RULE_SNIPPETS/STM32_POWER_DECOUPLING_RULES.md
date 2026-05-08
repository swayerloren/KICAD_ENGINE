# STM32 Power And Decoupling Rules

Date: 2026-05-02

Status: AI design-rule snippet. Exact capacitor values, power sequencing, and package-specific requirements must come from the selected STM32 datasheet and hardware application notes.

## Source Baseline

- Exact STM32 datasheet and package drawing.
- Exact family reference manual.
- ST hardware getting-started application notes such as AN4488 for STM32F4 hardware development.
- Nucleo/Discovery schematics only as examples, not universal circuits.

## Rules

- Connect and decouple every VDD/VSS pair required by the package. Do not omit power pins because a KiCad symbol groups or hides them.
- Place local high-frequency decoupling close to MCU power pins with short return paths.
- Add bulk capacitance near the MCU power region and near noisy load transitions; size from system current profile.
- Treat VDDA and VSSA as analog-domain pins. Filter VDDA when analog performance matters and keep analog return currents controlled.
- Treat VREF+ as a precision node when ADC/DAC accuracy matters; verify whether it is tied to VDDA, filtered, or driven by a reference.
- Check VBAT, VCAP, VCORE, SMPS, USB supply, backup-domain, and independent analog supply pins for the exact family.
- STM32H7/U5/H5-class parts can have regulator and supply options that are not present on simpler STM32F1/F4 designs.
- Do not route high-current switching loops, USB, crystal, or RF traces through analog/reference areas.

## Common Mistakes

- Copying a Blue Pill or Nucleo minimum circuit onto a different STM32 family.
- Missing VCAP or SMPS pins on high-performance/low-power parts.
- Connecting VDDA without filtering in noise-sensitive analog designs.
- Assuming all GPIOs are 5 V tolerant.
- Assuming power pins are already handled by the KiCad symbol.

## Verification Checklist

- Datasheet power pin table checked.
- Package pinout checked against symbol.
- All VDD/VSS/VDDA/VSSA/VREF+/VBAT/VCAP/SMPS pins accounted for.
- ERC power pins reviewed.
- Analog performance requirements documented.
