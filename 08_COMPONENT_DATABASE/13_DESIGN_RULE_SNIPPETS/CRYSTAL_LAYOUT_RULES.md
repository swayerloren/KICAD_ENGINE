# Crystal Layout Rules

Date: 2026-05-02

Status: rule snippet for AI-assisted schematic and PCB review.

## Selection Rules

- Verify oscillator frequency from the MCU, radio, USB, RTC, or timing IC datasheet.
- Verify load capacitance, ESR, drive level, tolerance, stability, aging, and package.
- Calculate load capacitors from the selected crystal CL and estimated board/input stray capacitance.
- Treat nominal 22pF load capacitors as a placeholder until the source documents justify them.
- Confirm whether the target IC expects a crystal, ceramic resonator, MEMS oscillator, or external clock input.

## Layout Rules

- Place the crystal and load capacitors close to the oscillator pins.
- Keep crystal traces short, symmetric where practical, and away from high-current or fast-switching nets.
- Keep USB, RF, switch-node, motor, relay, and high-current traces away from crystal nodes.
- Avoid routing unrelated signals under or between crystal components unless the IC vendor layout guide permits it.
- Connect load capacitor grounds with a short, quiet return path.
- Follow the IC vendor's recommendation for guard rings, copper keepouts, or ground pour around crystal pins.

## KiCad Review Checklist

- Crystal footprint matches exact package drawing and pad layout.
- Load capacitors are tied to the intended local ground.
- Crystal pins are connected to the correct oscillator pins, not GPIO alternatives.
- No copper pour or traces violate a documented crystal keepout.
- ERC does not hide oscillator pin power or passive pin warnings without review.

## AI Warnings

- Do not copy crystal capacitor values from an unrelated dev board as final evidence.
- Do not assume an internal oscillator is accurate enough for USB, RF, CAN timing, or precise baud-rate needs.
- Do not add a 40 MHz crystal to an RF module that already includes its own crystal without checking the module datasheet.
