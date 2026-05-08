# Fixed Mechanical Placement Rules

## Purpose

Define the fixed-first placement rules for components that control the board edge, cable direction, access, or mounting envelope.

## Fixed Mechanical Classes

- mounting holes
- USB-C connectors
- barrel jacks and edge power connectors
- RF connectors
- switches or buttons that must hit an enclosure edge

## Rules

- Mounting holes place before nearby functional components.
- USB-C and barrel jack or other input connectors are fixed mechanical parts.
- Edge connectors must align to the intended board edge and face off-board.
- RF connectors must preserve cable and keepout clearance.
- Mechanical parts define no-go zones for later placement.

## Placement Quality Rule

If a connector or hole placement makes sane routing impossible, reject the placement or revise the board outline before forcing random placement elsewhere.
