# Layout Notes Extraction Rules

## Extract Layout Notes For

- Decoupling.
- Thermal pads.
- Switching regulators.
- RF traces and antenna keepouts.
- USB differential pairs.
- CAN/LIN/RS485 bus routing.
- Crystal layout.
- High-current power paths.
- ESD/protection placement.
- Connector mechanical orientation.

## Required Source Types

- Datasheet layout section.
- Hardware design guide.
- Application note.
- Evaluation board layout guide.
- Exact connector or package drawing.

## Rules

- Do not copy layout blindly from a reference board.
- Do not use trace width/spacing without stackup.
- Do not approve RF, USB, CAN, automotive, or high-current layout without human review.
- Mark all missing values explicitly.

## Output

Create a `layout_warnings` list in the component record and summary.

