# RS485 Layout Rules

Date: 2026-05-02

Status: AI guidance for RS485 and RS422 PCB work. Verify against the selected transceiver and bus requirements before release.

## Core Rule

RS485 reliability depends on topology, termination, biasing, common-mode limits, protection, and connector wiring. Do not treat it as generic UART with longer wires.

## Required Questions

- Is the bus half-duplex or full-duplex.
- Is the board an endpoint, middle node, or configurable node.
- What data rate, cable length, and node count are required.
- Is there a shared ground or isolated interface.
- Which pins control driver enable and receiver enable.
- Is fail-safe biasing internal, external, or provided elsewhere.

## Termination And Bias

- Terminate only where the bus topology requires it, typically at the ends of a multidrop bus.
- Make termination selectable when board position may vary.
- Fail-safe biasing must be coordinated across the whole bus, not blindly repeated on every node.
- Verify transceiver internal fail-safe behavior before omitting external biasing.
- Check whether connector pin labels use A/B polarity consistently with the chosen transceiver and system convention.

## Routing And Placement

- Route differential bus traces together.
- Keep stubs short.
- Place the transceiver close to the connector when practical.
- Place ESD/TVS protection close to the connector.
- Keep bus traces away from switching power nodes, crystals, and sensitive analog inputs.
- Provide a defined return or reference strategy, especially over long cables.

## Protection

- Select TVS/ESD devices for RS485 common-mode, surge, and capacitance requirements.
- Consider common-mode chokes only when the EMC requirement and source guidance justify them.
- For industrial or automotive environments, define surge, ESD, EFT, ground offset, and isolation requirements before part selection.

## Common Mistakes

- Reversing A and B labels.
- Adding termination to every node.
- Omitting driver-enable control.
- Leaving receiver-enable state ambiguous.
- Omitting fail-safe bias on an idle multidrop bus when the design needs it.
- Assuming a 3.3V RS485 transceiver can tolerate any field wiring fault.

## Verification Gate

- Datasheet source link recorded.
- Half-duplex/full-duplex mode documented.
- Termination and bias strategy documented.
- Connector pinout visually reviewed.
- Protection part selected and placed at connector.
- ERC and DRC run after implementation.
