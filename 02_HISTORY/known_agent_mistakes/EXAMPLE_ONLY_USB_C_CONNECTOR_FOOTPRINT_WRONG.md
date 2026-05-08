# EXAMPLE_ONLY Known Agent Mistake: USB-C Connector Footprint

Status: `EXAMPLE_ONLY`

This record demonstrates the global mistake-capture format. It is not a claim about an actual KiCad Engine project event.

## Mistake

The agent accepted or selected a USB-C connector footprint without exact manufacturer drawing verification and human orientation review.

## User Correction

"The USB-C connector footprint was wrong and the board did not fit the connector."

## Global Avoidance Rule

Connector footprints, especially USB-C, U.FL, SMA, board-edge, automotive, and terminal connectors, must remain unverified until matched to an exact manufacturer drawing and reviewed for mechanical orientation.

## Memory Update

Global durable avoidance rule belongs in `01_MEMORY/AGENT_MISTAKES_TO_AVOID.md`.

