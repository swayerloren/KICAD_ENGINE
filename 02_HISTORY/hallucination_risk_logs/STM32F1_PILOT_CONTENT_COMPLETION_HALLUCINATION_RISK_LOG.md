# STM32F1 Pilot Content Completion Hallucination Risk Log

Date: 2026-05-03
Risk label: `MEDIUM_RISK`

## Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| AI treats KiCad stock footprint as verified package match. | High | Match record states candidate-only and human review required. |
| AI uses Blue Pill notes as official ST reference. | High | Dev-board notes mark Blue Pill as third-party and variant-prone. |
| AI guesses BOOT0/BOOT1 or USB behavior from memory. | High | Boot/debug and USB items are marked `NEEDS_HUMAN_REVIEW`. |
| AI copies product-page specs into final design without datasheet sections. | Medium | Files distinguish `VERIFIED_SOURCE_LINK` from `VERIFIED_FROM_DATASHEET`. |
| AI assumes no errata risk. | Medium | Errata remains `UNVERIFIED` in needs-review backlog. |

## Closeout Status

No unsupported design-approval claims should be made from this pilot content.
