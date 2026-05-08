# EXAMPLE_ONLY AI Response Scorecard: USB-C Footprint Recommended Without Drawing

Status: `EXAMPLE_ONLY`

## Scenario

Codex recommended a USB-C connector footprint without verifying the exact manufacturer drawing.

## Scores

- Overall score: `18/100`
- Evidence support: `2/20`
- KiCad-specific correctness: `4/20`
- Datasheet/component accuracy: `1/15`
- Safety/compliance with repo rules: `3/15`
- Memory/history routing correctness: `3/10`
- Uncertainty disclosure: `2/10`
- End-user usefulness: `3/10`

## Labels

- Risk label: `HIGH_RISK`
- Gate result: `BLOCKED_UNTIL_HUMAN_REVIEW`
- Human review required: `YES`

## Reason

The claim depends on an exact connector footprint, mechanical orientation, pin numbering, shell tab geometry, and mating fit. None were verified from an exact manufacturer drawing in this example.

## Required Follow-Up

- Select exact USB-C connector part number.
- Obtain datasheet and mechanical drawing.
- Compare drawing to KiCad footprint.
- Verify board-edge relationship and shell tabs.
- Human orientation review required before layout/fabrication.

