# Functional Block Templates

## Purpose

Provide deterministic visual block templates so schematic cleanup does not
degrade into random symbol spreading.

## ESP32 Dev Board Template

### Input Power Block

- preferred region: left side or upper-left
- expected order:
  `J1 -> fuse -> PMOS protection -> TVS/input caps -> regulator input`

### Buck Regulator Block

- preferred region: near the input block
- expected clustering:
  - `U1` centered
  - `C6` tight to `BST/SW`
  - `L1` tight to `SW`
  - `C7/C8` at the output side

### ESP32 Module Block

- preferred region: center-right or upper-center
- expected behavior:
  - enough whitespace around module pins
  - local support parts kept readable

### USB-C Block

- preferred region: lower-left or lower-center
- expected order:
  `J2 -> ESD -> R8/R9 -> U2 USB pins`
- `CC` resistors should stay near `J2`

### Reset / Boot Block

- preferred region: near `U2` EN and BOOT pins
- expected style:
  - short wires or minimal local labels
  - avoid detached switch islands

### LED Block

- preferred region: right side or lower-right
- expected style:
  - LEDs grouped together
  - current-limit resistors adjacent

### Test / Debug Block

- preferred region: grouped lower service area
- expected style:
  - test pads and debug pads stay together
  - do not scatter test pads into active circuitry

### Mechanical Notes Block

- preferred region: clearly separated from active circuitry
- expected style:
  - mounting holes and notes are readable
  - no overlap with electrical flow

## Generic Template Rules

- Inputs generally left.
- Outputs generally right.
- Power generally top.
- Ground generally bottom.
- Long-distance cross-block nets may use labels.
- Local same-block nets should prefer wires when that is visually clearer.
