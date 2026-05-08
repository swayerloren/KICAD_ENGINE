# Hallucination Risk Log - Sample Project Payload Rules

Date: `2026-05-06`

Risk level: `LOW`

## Risks

| Risk | Mitigation |
| --- | --- |
| Overstating that the ATtiny85 sample is public-release ready. | Policy records preserve `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW` and `BLOCKED_UNTIL_HUMAN_REVIEW`. |
| Treating MIT evidence as final legal approval. | Policy requires human release review before including KiCad source files. |
| Treating generated sample visuals or gate reports as manufacturing outputs. | Policy blocks fabrication-style outputs and `FAB_READY` files by default. |
| Claiming dry-run payload validation passed. | Audit states no safe public dry-run builder exists and no dry-run was executed. |

## Result

No engineering data, datasheet values, footprint matches, or manufacturing
claims were invented.
