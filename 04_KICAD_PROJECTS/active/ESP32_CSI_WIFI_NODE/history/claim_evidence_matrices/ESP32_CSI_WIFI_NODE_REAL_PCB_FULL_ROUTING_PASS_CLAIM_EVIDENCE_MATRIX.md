# Claim Evidence Matrix

| claim | evidence |
|---|---|
| The live PCB changed in this pass. | before hash `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`; after hash `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6` |
| The accepted live subset held `0` DRC violations. | `reports/REAL_PCB_FULL_ROUTING_PASS_DRC.json` |
| The pass reduced unconnected items from `49` to `44`. | `reports/REAL_PCB_CRITICAL_ROUTING_PASS_1_DRC.json`; `reports/REAL_PCB_FULL_ROUTING_PASS_DRC.json` |
| `/PLED`, `/SLED`, `/STATUS_LED`, `/U0TXD`, and `unconnected-(J2-VBUS-PadA4)` were routed live. | live routing script output captured in `reports/REAL_PCB_FULL_ROUTING_PASS_REPORT.md` |
| Remaining blockers are real board-state blockers, not stale markdown blockers. | copied-board trial results plus post-save DRC connectivity buckets in `reports/REAL_PCB_FULL_ROUTING_PASS_DRC.json` |
