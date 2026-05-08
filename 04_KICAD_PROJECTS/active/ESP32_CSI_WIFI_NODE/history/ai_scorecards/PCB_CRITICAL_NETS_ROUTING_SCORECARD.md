# PCB Critical Nets Routing Response Scorecard

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

Overall score: `92/100`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 20/20 | Blocked status is supported by local reports and file listing. |
| KiCad-specific correctness | 20/20 | Correctly avoided PCB routing because preconditions failed. |
| Datasheet/component accuracy | 13/15 | Did not invent component, footprint, USB, RF, or regulator details. |
| Safety/compliance with repo rules | 15/15 | Backup created; no KiCad design files edited; no routing attempted. |
| Memory/history routing correctness | 9/10 | Project and global closeout records created. |
| Uncertainty disclosure | 10/10 | Unverified routing constraints are explicit. |
| End-user usefulness | 5/10 | Useful blocker report, but requested routing cannot be performed. |

## Gate Result

`CRITICAL_ROUTING_FAIL`

