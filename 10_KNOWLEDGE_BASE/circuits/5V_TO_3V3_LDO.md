# 5 V To 3.3 V LDO Circuit

## Use Case

Use this pattern for low-current, low-noise, or simple 5 V to 3.3 V conversion when heat dissipation is acceptable.

## Required Evidence

- Exact LDO datasheet.
- Load current estimate.
- Dropout requirement.
- Input/output capacitor type, value, ESR, and placement requirements.
- Thermal package data.

## Typical Schematic Block

- 5 V input net.
- LDO with enable pin handled if present.
- Input capacitor near input pin.
- Output capacitor near output pin.
- Optional power-good or noise-bypass components per datasheet.

## PCB Review Points

- Check heat dissipation from voltage drop times load current.
- Place capacitors close to pins.
- Verify output capacitor ESR stability requirements.
- Use enough copper for thermal packages.

## Common Mistakes

- Using an LDO where power loss is too high.
- Missing required output capacitor or ESR range.
- Assuming all pin-compatible LDOs have the same capacitor requirements.
- Ignoring thermal shutdown margin.

## Verification Gate

Do not approve until load current, dropout, capacitor requirements, pinout, and thermal dissipation are verified.

