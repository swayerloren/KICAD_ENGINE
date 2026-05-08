# Human Review Gate Rules

## Purpose

Define when KiCad Engine must stop and require human engineering review.

## Always Require Human Review

- Exact connector orientation is not verified.
- Exact footprint is not verified against package drawing.
- Symbol pinout is not verified against source.
- Datasheet source is missing.
- A generic connector or generic protection part is used.
- A polarity-sensitive component is placed or oriented.
- RF feedlines, antennas, U.FL/IPEX/SMA connectors, or module keepouts are involved.
- USB-C, USB high-speed, CAN, CAN FD, automotive, battery, or high-current power paths are involved.
- Manufacturing-style outputs are generated.
- Source documents conflict.
- The agent is uncertain about an electrical or mechanical decision.

## Human Review Status Labels

- `HUMAN_REVIEW_NOT_REQUIRED_FOR_THIS_DOC_ONLY`
- `HUMAN_REVIEW_REQUIRED`
- `BLOCKED_UNTIL_HUMAN_REVIEW`
- `HUMAN_REVIEW_COMPLETED_BY_USER`

## Rule For Agents

Do not turn absence of a warning into approval. If a high-risk item has not been reviewed, mark it blocked.

