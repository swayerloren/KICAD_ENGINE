# Routing Sequence Plan

Stage 1/2 local power and buck cleanup is complete. Copper pours remain blocked. The next routing phase is Stage 3 USB.

## Strict Sequence

1. Re-read `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`.
2. Re-read `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`.
3. Preserve the accepted Stage 1 input and Stage 2 buck/local `+3V3` routing.
4. Route USB D+/D-: `J2 -> U3 -> R8/R9 -> U2`.
5. Route CC resistors `R6/R7`.
6. Route reset/boot.
7. Route LEDs.
8. Route test pads/debug.
9. Add and refill GND zones only after the remaining routing scope is complete.
10. Run DRC.
11. Perform visual trace-angle and routing-quality audit.

## Gate

- Do not start USB routing unless Stage 1/2 classification is `STAGE_1_2_PROFESSIONAL_ROUTING_READY_FOR_USB`.
- Do not create copper zones during Stage 3 USB-only work.
- Do not advance a routed phase if it visually contains crude 90-degree, acute-angle, or awkward routing.
