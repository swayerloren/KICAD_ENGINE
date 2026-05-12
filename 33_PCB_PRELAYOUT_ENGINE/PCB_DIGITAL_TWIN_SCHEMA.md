# PCB Digital Twin Schema

## Purpose

Define the read-only digital-twin structure used by the prelayout engine.

## Required Sections

- `project`
- `source_pcb`
- `source_sha256`
- `board_profile`
- `components`
- `connector_truth_candidates`
- `live_board_context`

## Board Profile

The board profile records:

- width and height
- board shape
- board bounding box
- mounting-hole count
- RF-module presence
- source timestamp

## Component Model

Each component record should provide:

- ref
- value
- footprint name
- role
- position
- rotation
- side
- body and courtyard boxes
- edge proximity
- fixed-mechanical flag
- pad-net summary

## Live Board Context

The live context must expose:

- DRC result
- violation count
- unconnected count
- detectable unrouted-net count

The prelayout gate uses this to stop real routing continuation when the current live board is already known incomplete.

