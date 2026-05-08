# ESP32 Layout Common Mistakes

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## High-Risk Mistakes

- Treating the antenna keepout as optional.
- Putting copper, traces, test pads, connectors, or mounting holes under the antenna keepout.
- Rotating the module away from the board edge without a documented external-antenna reason.
- Packing switching regulators or noisy power-input parts near the antenna edge.
- Hiding boot or reset buttons where the user cannot reach them.
- Letting USB cables block status LEDs or buttons.
- Forcing a small rectangular outline even when it crowds the antenna or connector access.

## Agent Checks

- Verify the exact ESP32 module type and antenna style.
- Verify the antenna keepout and its board-edge relationship.
- Verify connector access after cable insertion.
- Verify user access to boot and reset controls.
- Verify test-pad reachability after assembly.

## Required Human Review

Human review is required for antenna clearance, module orientation, connector access, and board-shape justification.
