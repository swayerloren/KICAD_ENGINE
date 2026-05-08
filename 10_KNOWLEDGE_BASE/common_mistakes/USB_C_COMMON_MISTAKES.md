# USB-C Common Mistakes

## High-Risk Mistakes

- Leaving CC pins floating.
- Using a USB-C connector footprint for the wrong manufacturer part.
- Swapping D+ and D-.
- Forgetting VBUS sense where required.
- Assuming a power-only USB-C circuit can draw any current.
- Placing ESD protection too far from the connector.
- Misunderstanding shield, shell, and mounting-pad connections.

## Agent Checks

- Verify connector pinout and footprint drawing.
- Verify CC resistor behavior for the intended role.
- Verify USB data routing and ESD placement.
- Verify VBUS current path and trace width.
- Check connector orientation in PCB and 3D view.

## Required Human Review

Human review is required for connector orientation, CC implementation, shield strategy, and any current advertisement claim.

