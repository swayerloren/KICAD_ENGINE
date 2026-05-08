# TASK 005: 12V Automotive Input

Status: `NOT_RUN`.

## Objective

Ask an AI agent to plan or review a 12 V automotive input power stage. The task measures conservative handling of automotive transients, reverse polarity, fuse/protection, regulator thermal limits, and human review gates.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- Official regulator, TVS, fuse, MOSFET/diode, connector, and application note sources.
- Public automotive transient standards summaries only when appropriately cited and not treated as complete certification proof.
- User-provided load current, environment, connector, fuse location, and certification expectations.

## Expected Outputs

- Power-stage design plan or review report.
- Protection block diagram.
- Component list with verification status.
- Thermal and layout warnings.
- Connector/polarity review flags.
- ERC/DRC evidence if a project is created or supplied.
- Clear statement that automotive compliance requires human/specialist review.

## Required Evidence

- Input voltage range and transient assumptions marked source-backed or unverified.
- Fuse/polyfuse and TVS placement strategy.
- Reverse-polarity protection strategy.
- Buck/LDO/boost regulator thermal warnings.
- Input/output capacitor requirements marked source-backed or unverified.
- Connector and polarity-sensitive part orientation flags.

## Scoring Focus

- Power design correctness.
- Protection completeness.
- Layout warnings.
- Human review flags.
- No unsupported automotive compliance claims.

## Failure Modes

- Treating nominal 12 V as the only input condition.
- Omitting reverse polarity or transient protection discussion.
- Ignoring regulator thermal dissipation.
- Claiming standards compliance without test evidence.
