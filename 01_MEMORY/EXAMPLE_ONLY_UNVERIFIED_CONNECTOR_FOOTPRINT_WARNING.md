# EXAMPLE_ONLY Global Warning: Unverified Connector Footprints

Status: `EXAMPLE_ONLY`

## Warning

Unverified connector footprints are a global high-risk AI failure mode.

## Rule

USB-C, U.FL, SMA, board-edge, automotive, terminal-block, and other mechanical connectors must not be approved from generic library names alone. Exact manufacturer drawing and human orientation review are required.

## Gate

Mark work `BLOCKED_UNTIL_HUMAN_REVIEW` when connector footprint or orientation is not verified.

