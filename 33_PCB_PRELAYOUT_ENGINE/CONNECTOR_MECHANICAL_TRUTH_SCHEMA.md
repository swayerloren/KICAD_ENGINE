# Connector Mechanical Truth Schema

## Purpose

Define the connector-truth record used to prove whether a connector is mechanically defensible before routing starts.

## Required Fields

- `ref`
- `connector_type`
- `intended_edge`
- `mating_direction`
- `port_opening_direction`
- `pin_side_direction`
- `body_side_direction`
- `rotation_deg`
- `truth_status`
- `off_board_facing`
- `edge_alignment_required`
- `edge_alignment_verified`
- `three_d_model_status`
- `missing_evidence`
- `routing_blocked`
- `mechanical_conflicts`
- `proof_sources`

## Truth Status Meanings

- `PASS`: connector direction is mechanically defensible
- `FAIL`: connector direction is wrong for the intended edge
- `NEEDS_HUMAN_REVIEW`: edge direction looks plausible but required evidence such as the 3D model is missing
- `UNKNOWN`: evidence is too weak to allow placement/routing start

## Required Failure Cases

Mark `FAIL` when:

- the connector mouth faces inward
- the pin/solder side faces outward at the board edge
- the connector is stranded away from its intended edge
- the footprint `PCB Edge` direction conflicts with the serving edge
- the service envelope conflicts with holes, RF space, or keepouts

Mark `NEEDS_HUMAN_REVIEW` when:

- only XY position or rotation are available as proof
- the exact 3D model is missing or unresolved
- the footprint family is unknown to the mechanical truth layer

Mark `UNKNOWN` when:

- only coordinates exist
- the connector footprint/body relation is unclear
- a board-edge alignment marker cannot be verified

## Hard Rules

1. Connector orientation is not proven by XY position or rotation alone.
2. Barrel jack pin side must not be mistaken for port opening.
3. USB-C mouth/opening must face off-board and align with `Edge.Cuts`.
4. If a required connector 3D model is missing, the connector remains `NEEDS_HUMAN_REVIEW`.
5. Routing remains blocked unless `truth_status` is exactly `PASS`.
