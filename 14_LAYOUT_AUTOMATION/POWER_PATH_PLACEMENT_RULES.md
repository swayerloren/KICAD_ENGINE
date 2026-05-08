# Power Path Placement Rules

## Purpose

Define placement logic for power-entry and regulator clusters.

## Required Order

Place in physical current-flow order:

1. input connector
2. fuse
3. PMOS or reverse-polarity protection
4. TVS and input capacitor cluster
5. regulator
6. inductor / output capacitor cluster
7. local distribution point

## Rules

- Keep the power path physically readable.
- Do not scatter entry protection parts around the board.
- Keep switcher clusters compact.
- Keep noisy switching nodes away from RF and USB regions.
- Decoupling and required stability parts must sit near their target pins.

## Failure Conditions

- nonsensical power-flow order
- long returns between regulator and required capacitors
- protection far from entry point
- regulator loop placement that obviously forces ugly routing
