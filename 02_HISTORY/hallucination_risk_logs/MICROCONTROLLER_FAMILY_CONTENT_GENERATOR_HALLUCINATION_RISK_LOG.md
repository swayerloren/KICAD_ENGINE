# Microcontroller Family Content Generator Hallucination Risk Log

Date: 2026-05-03
Risk label: `LOW_RISK`

## Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| AI treats generated stubs as verified datasheet content. | Medium | Templates mark unknowns `UNKNOWN_REQUIRES_SOURCE` and `NEEDS_HUMAN_REVIEW`. |
| AI uses representative part as approved BOM choice. | Medium | Part record template marks representative part `UNVERIFIED`. |
| AI approves candidate symbols/footprints from generated files. | High | KiCad template states candidate-only and requires datasheet/package drawing review. |
| AI overwrites completed family content accidentally. | Low | Script skips existing files unless `--force` is explicitly passed. |

## Closeout Status

Risk is acceptable for a safe offline stub generator.
