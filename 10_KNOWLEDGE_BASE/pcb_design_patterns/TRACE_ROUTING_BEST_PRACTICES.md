# Trace Routing Best Practices

## Purpose

This note captures the default routing style KiCad Engine should prefer before any project-specific exceptions are made.

## Default Style

- Use short, direct routing.
- Use two 45-degree bends for ordinary direction changes.
- Avoid obvious 90-degree corners.
- Avoid acute bends sharper than 90 degrees.
- Keep pad entry and exit geometry clean.
- Avoid long diagonal shortcuts through unrelated functional blocks.
- Avoid unnecessary vias.

## Power And Switching

- Power traces may be wider than signal traces, but wide traces still need clean transitions.
- Keep regulator switching loops compact.
- `BUCK_SW` should be kept very short and local.
- When wide traces become awkward because of local placement, improve the local placement instead of forcing ugly copper.

## USB, RF, And Sensitive Nets

- Route USB pairs short and parallel where practical.
- Avoid stubs on data nets.
- Keep sensitive routing away from switching nodes.
- Prefer smoother or filleted-looking geometry where the signal class benefits from it.

## Review Rule

- A routed board can fail quality review even if it passes DRC.
- Visually crude routing must be repaired before the board is described as clean or ready for review.

