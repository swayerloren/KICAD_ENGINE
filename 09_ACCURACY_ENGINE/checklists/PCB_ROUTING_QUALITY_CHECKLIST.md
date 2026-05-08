# PCB Routing Quality Checklist

Use this checklist after any meaningful PCB routing pass.

## Geometry

- [ ] No obvious 90-degree bends.
- [ ] No acute-angle bends.
- [ ] Normal routing uses 45-degree bends.
- [ ] High-speed, RF, and sensitive nets use smooth or rounded routing where practical.
- [ ] No excessive zigzags or awkward scripted-looking pathing.

## Topology And Flow

- [ ] No giant unnecessary U-shaped routes.
- [ ] No long diagonal routes through unrelated circuit areas.
- [ ] No unnecessary vias.
- [ ] Wide power traces enter pads cleanly.
- [ ] Local component movement was considered before forcing ugly traces.

## Critical Nets

- [ ] `BUCK_SW` is short and local.
- [ ] Regulator switching loops are compact.
- [ ] USB routes are short, clean, parallel where practical, and avoid stubs.
- [ ] Traces avoid RF keepout.
- [ ] Traces avoid mounting holes and connector keepouts.

## Verification

- [ ] DRC passes or remaining violations are explicitly classified.
- [ ] Routing quality was visually reviewed; DRC pass alone was not treated as approval.

