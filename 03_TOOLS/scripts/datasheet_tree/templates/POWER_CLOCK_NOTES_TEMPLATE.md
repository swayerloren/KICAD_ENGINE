# {representative_part} Power Clock Reset Notes

Date: {date}
Status: `AI_PLANNING_CHECKLIST`

Use this file for source-backed power, clock, and reset planning. Exact values are unknown until verified.

## Evidence Labels

{evidence_labels}

## Power Notes

| Area | Guidance | Status |
| --- | --- | --- |
| operating voltage | `UNKNOWN_REQUIRES_SOURCE` | `NEEDS_HUMAN_REVIEW` |
| supply domains | `UNKNOWN_REQUIRES_SOURCE` | `NEEDS_HUMAN_REVIEW` |
| decoupling | verify value, quantity, voltage rating, and placement | `NEEDS_HUMAN_REVIEW` |
| analog power/reference | verify analog filtering and grounding | `NEEDS_HUMAN_REVIEW` |
| power sequencing | `UNKNOWN_REQUIRES_SOURCE` | `NEEDS_HUMAN_REVIEW` |

## Clock Notes

| Clock Topic | Guidance | Status |
| --- | --- | --- |
| internal oscillator | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| external oscillator | verify component and layout from datasheet/app note | `NEEDS_HUMAN_REVIEW` |
| low-speed oscillator | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| interface clock requirements | USB/CAN/RF/high-speed interfaces require exact review | `NEEDS_HUMAN_REVIEW` |

## Reset Notes

- Reset pin behavior: `UNKNOWN_REQUIRES_SOURCE`.
- Reset circuit values: `UNKNOWN_REQUIRES_SOURCE`.
- Programmer reset requirements: `UNKNOWN_REQUIRES_SOURCE`.
