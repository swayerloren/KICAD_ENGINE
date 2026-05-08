# ESP32 Common Mistakes

## High-Risk Mistakes

- Assuming all ESP32-family parts share the same boot straps.
- Confusing WROOM, WROVER, MINI, U, and PCB-antenna module footprints.
- Ignoring antenna keepout.
- Missing EN/reset requirements.
- Forgetting that USB support varies by family and part.
- Connecting strapping pins to circuits that force the wrong boot mode.
- Routing copper, planes, or components under module antenna keepout.

## Agent Checks

- Identify exact ESP32 family and module.
- Read the module datasheet and hardware design guide.
- Verify boot strapping pins for that exact part.
- Verify programming path: UART, USB, JTAG, or combination.
- Verify footprint against exact module drawing.

## Required Human Review

Human review is required for antenna keepout, RF connector/module orientation, boot strap defaults, and power supply margin.

