# PCB Full Routing Response Scorecard

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Overall score: `92/100`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 20/20 | Blocked state is directly supported by local reports and file listing. |
| KiCad-specific correctness | 20/20 | Correctly avoided routing because critical routing failed and no PCB exists. |
| Datasheet/component accuracy | 13/15 | Did not invent trace, clearance, footprint, USB, RF, or routing details. |
| Safety/compliance with repo rules | 15/15 | Backup created; no design files edited; no manufacturing outputs. |
| Memory/history routing correctness | 9/10 | Project/global records created and indexes rebuilt. |
| Uncertainty disclosure | 10/10 | Unverified routing and audit claims are explicitly blocked. |
| End-user usefulness | 5/10 | Useful blocked report, but requested full routing cannot proceed. |

## Gate Result

`FULL_ROUTING_FAIL`

