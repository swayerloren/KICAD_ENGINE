# Missing Datasheets

Status: `ACTIVE_SOURCE_GAP_TRACKER`

This file tracks missing or weak source evidence for the datasheet library. It is not a shopping list for mass PDF downloads. Prefer official source links, metadata, and summaries. Store PDFs only when redistribution rights are confirmed or the file is kept outside public release scope.

## How Agents Should Use This File

Before creating or approving a component record, check this tracker and the part-family `MISSING.md`. If the exact datasheet, package drawing, errata, reference manual, or board schematic is missing, keep the downstream component record `UNVERIFIED` or `SOURCE_LINK_ONLY`. Do not infer electrical limits, pinouts, package dimensions, connector orientation, or layout rules from memory.

When a gap is resolved, add the source link and verification note to the target family `SOURCE_LINKS.md`, update `MASTER_DATASHEET_INDEX.md`, and leave a review-history note rather than deleting the old row.

## Required Row Fields

| Field | Required | Guidance |
| --- | --- | --- |
| `priority` | Yes | `P0_BLOCKING`, `P1_HIGH_RISK`, `P2_USEFUL`, or `P3_BACKGROUND`. |
| `category` | Yes | Repo-relative datasheet category folder. |
| `part_or_topic` | Yes | Exact MPN, module, dev board, connector family, or document topic. |
| `needed_document` | Yes | Datasheet, reference manual, errata, package drawing, schematic, app note, user manual, or vendor design guide. |
| `why_needed` | Yes | State the engineering gate it blocks. |
| `candidate_source` | Yes | Official vendor page, distributor page, user-provided file, or public reference. |
| `redistribution_status` | Yes | `LINK_ONLY`, `REDISTRIBUTION_CONFIRMED`, `LOCAL_PRIVATE_ONLY`, or `UNKNOWN_REQUIRES_REVIEW`. |
| `verification_status` | Yes | `MISSING`, `SOURCE_LINK_ONLY`, `PARTIALLY_VERIFIED`, `VERIFIED_BY_DATASHEET`, or `NEEDS_HUMAN_REVIEW`. |
| `next_action` | Yes | Concrete next step, not generic "research later". |

## Global Missing-Document Table

| Priority | Category | Part / Topic | Needed Document | Why Needed | Candidate Source | Redistribution Status | Verification Status | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1_HIGH_RISK | 01_MICROCONTROLLERS/ESPRESSIF/ESP32_S3 | ESP32-S3-WROOM-1U | Official module datasheet, revision, package/mechanical drawing, antenna/keepout guidance | Module land pattern, antenna keepout, and U.FL variant cannot be approved from a generic module name. | Espressif official documentation portal | LINK_ONLY | SOURCE_LINK_ONLY | Record exact official source URL and package drawing status; keep footprint approval blocked until reviewed. |
| P1_HIGH_RISK | 05_CONNECTORS | Generic USB-C receptacles | Exact manufacturer datasheet and mechanical drawing for selected MPN | USB-C footprints and shell/tab orientation are high-risk and cannot be verified generically. | Selected connector vendor official page | UNKNOWN_REQUIRES_REVIEW | MISSING | Replace generic connector with exact MPN before footprint approval. |
| P1_HIGH_RISK | 04_COMMUNICATION | CAN/CAN FD transceivers | Datasheet and package drawing for selected MPN | Termination, protection, voltage-domain, and package decisions need exact source evidence. | Manufacturer official page | LINK_ONLY | SOURCE_LINK_ONLY | Add per-part source records for the chosen transceiver. |
| P2_USEFUL | 03_POWER | Regulator family records | Datasheets, layout recommendations, and package drawings | Thermal, capacitor, and switching-node rules are part-specific. | Manufacturer official page | LINK_ONLY | SOURCE_LINK_ONLY | Prioritize regulators used in active projects first. |

## Promotion Rule

A row may move out of `MISSING` only when the target record includes the source URL, retrieval date, document type, redistribution status, and the specific claim verified. A captured browser page or supplier listing is evidence, not truth, until checked against an official source or human review.
