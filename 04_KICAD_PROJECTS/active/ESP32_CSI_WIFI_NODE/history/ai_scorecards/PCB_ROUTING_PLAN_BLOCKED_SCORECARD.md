# PCB Routing Plan Response Scorecard

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Overall score: `91/100`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 19/20 | Plan is tied to local reports and rule files. |
| KiCad-specific correctness | 19/20 | Correctly avoided routing because the PCB gate is failed and no PCB exists. |
| Datasheet/component accuracy | 13/15 | Did not invent component or datasheet values; left exact values blocked. |
| Safety/compliance with repo rules | 15/15 | No KiCad design files edited; no routing or manufacturing outputs. |
| Memory/history routing correctness | 9/10 | Project and global closeout records created. |
| Uncertainty disclosure | 10/10 | Exact routing constraints and high-risk items marked unverified/blocked. |
| End-user usefulness | 6/10 | Useful routing plan, but execution is blocked until prior gates pass. |

## Gate Result

`ROUTING_PLAN_BLOCKED`

