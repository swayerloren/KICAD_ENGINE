# Assembly Notes Rules

## Purpose

Assembly notes communicate intent that may not be obvious from Gerbers, BOM, or pick-and-place files.

## Include When Needed

- DNP parts.
- Hand-soldered parts.
- Orientation-sensitive connectors.
- Special polarity notes.
- Mechanical hardware.
- Jumper configuration.
- Programming or test instructions.
- Conformal coating, adhesive, or staking requirements.

## KiCad Engine Rules

- Assembly notes must be dated and tied to an export folder.
- Manufacturing-style notes remain `NOT_FINAL` until reviewed.
- Do not hide unresolved issues in notes.
- Use clear reference designators.

## Common Mistakes

- Failing to document connector orientation.
- Omitting manual assembly steps.
- Providing notes that contradict the BOM or PNP.
- Calling a package final without reviewer signoff.

## Human Review Gate

Assembly notes must be read by the human reviewer before any manufacturing order.

