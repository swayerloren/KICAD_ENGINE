# KiCad Engine Prompt Failures To Avoid

Date: 2026-05-06  
Status: MANDATORY_PROMPT_GUIDANCE

## Banned Prompt Patterns

Do not use prompts that say or imply:

1. "Run the visual script and mark visual pass if it exits successfully."
2. "If `CLOSE_UP_REVIEW.md` exists, visual review is complete."
3. "If no `?` references are detected, the schematic is visually clean."
4. "If footprint/library fields are hidden, the schematic is human-readable."
5. "If ERC passes, the schematic is ready for LJ visual review."
6. "If automated crops pass, proceed to schematic-to-PCB gate."
7. "Create a human review packet from generated crops without inspecting the images."
8. "Perform a visual repair and mark pass if ERC and crop generation pass."
9. "Use long `NEEDS_REVIEW` values directly on components even if they clutter the drawing."
10. "Put review notes inside active circuitry to keep them near the parts."

## Required Replacement Wording

Use prompts that require:

- Rendered full-page image inspection.
- Rendered crop inspection for every configured block.
- Block-by-block table with `VISUAL_PASS`, `VISUAL_FAIL`, or `VISUAL_NOT_VERIFIED`.
- Explicit separation between automated crop generation and human-readable visual inspection.
- Automatic failure for any visible text/value/reference/net-label overlap.
- Automatic failure for labels touching wires, pins, symbols, or power symbols.
- Automatic failure for clipped crops or crops that include the wrong block.
- PCB update blocked unless the visual row is exactly `VISUAL_PASS`.

## Safe Prompt Template Fragment

```text
Run the visual export and crop generator. Treat the tool status as AUTOMATED_CROP_PASS_ONLY unless you inspect the rendered full-page PNG and every crop. Create a block-by-block human-readability table. If any text, value, reference, net label, wire, pin, symbol body, power symbol, or note overlaps/touches/crosses/clips/crowds in any crop, return VISUAL_FAIL. Do not claim READY_FOR_LJ_VISUAL_REVIEW unless every block is VISUAL_PASS.
```

## Why This Exists

The ESP32_CSI_WIFI_NODE schematic demonstrated that many reports and folders do not protect the project when prompts let agents over-read automated status labels. Prompt wording must now force the actual judgment required by the gate.
