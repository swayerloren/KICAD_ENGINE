# Failed Attempts - Stage 1/2 Cleanup

Date: `2026-05-07`

## Failed / Reworked Items

1. Initial direct replacement traces introduced multiple shorts and clearance failures by cutting through opposite pads in the J1/Q1/C2/C5/U1 area.
2. Several intermediate buck reroute attempts still created `SW/BST` conflicts in the `U1/C6/L1` cluster.
3. Intermediate `kicad-cli` relative-path report writes were unreliable enough that the final pass was re-run to a fresh absolute-path filename.

## Current Status

- The board is improved and stable enough for review.
- One buck-cluster crossing still remains open.
