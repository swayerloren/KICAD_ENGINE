# TASK 003: CAN Bus Node

Status: `NOT_RUN`.

## Objective

Ask an AI agent to plan or review a CAN or CAN FD node in KiCad. The task measures component selection, transceiver wiring, termination, protection, connector review, and layout-risk awareness.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- Official MCU, CAN controller, CAN transceiver, TVS/protection, connector, and termination documents.
- Installed KiCad symbol and footprint libraries.
- User-provided bus voltage, data rate target, connector style, automotive/non-automotive environment, and termination role.

## Expected Outputs

- Source-backed CAN node design plan or review report.
- Component list with CAN transceiver and protection strategy.
- Symbol and footprint candidates with verification status.
- Termination decision.
- Connector pinout/orientation review flag.
- Layout notes for CANH/CANL routing and protection placement.
- ERC/DRC evidence if a KiCad project is created or supplied.

## Required Evidence

- Transceiver part and voltage-domain compatibility.
- MCU CAN peripheral or external controller assumption.
- CANH/CANL termination strategy.
- ESD/TVS and common-mode protection assumptions.
- Connector pinout source or `HUMAN_REVIEW_REQUIRED`.
- Footprint status for transceiver, protection, and connector.

## Scoring Focus

- Correct component selection.
- CAN/CAN FD compatibility.
- Termination and protection correctness.
- Connector orientation verification.
- Symbol/footprint evidence.
- Human review flags.

## Failure Modes

- Omitting termination decision.
- Mixing 3.3 V and 5 V domains without explanation.
- Treating connector pinout as obvious without drawing review.
- Claiming CAN FD support from a non-CAN-FD transceiver.
