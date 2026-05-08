# PCB Routing Quality Rules

## Scope

Use this file with `TRACE_ANGLE_ROUTING_RULES.md` for all PCB routing reviews, routing prompts, and routing automation plans.

## Geometry Rules

- Follow `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`.
- Avoid obvious 90-degree corners and acute-angle bends.
- Use clean pad entry and exit geometry.
- Prefer short, direct routing over decorative or script-generated pathing.
- Avoid giant U-shaped detours and long diagonal shortcuts through unrelated circuit areas.
- Avoid unnecessary zigzags.

## Power Rules

- Wide power traces still need clean transitions and clean pad entry.
- Avoid skinny neckdowns unless the footprint geometry forces them.
- Keep switching loops short and local.
- `BUCK_SW` must remain short, compact, and away from USB and RF keepouts.

## Signal Rules

- USB and other paired signals should remain short, clean, and parallel where practical.
- Avoid long test-pad stubs on data nets.
- Avoid unnecessary vias, especially on critical nets.
- Keep traces out of RF keepouts, mounting-hole clearances, and connector mechanical keepouts.

## Placement And Flow

- Do not force ugly traces around bad local placement.
- If local placement causes awkward routing, move only the local cluster needed to produce a clean route.
- Do not route through unrelated functional areas just because space exists.

## Review Gate

- DRC pass is required, but DRC pass alone is not routing-quality approval.
- Visual routing review is mandatory before calling a routed region acceptable.

