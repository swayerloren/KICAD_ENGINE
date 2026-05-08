# STM32G4 Package And Footprint Notes

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Package Families Seen At Family Level

- UFQFPN/QFN
- LQFP
- BGA on selected parts

These are not approved footprints. Exact package approval requires source verification.

## Required Evidence Before Footprint Approval

| Evidence | Status | Notes |
| --- | --- | --- |
| Exact order code | `UNKNOWN_REQUIRES_SOURCE` | Include package suffix and temperature/lifecycle variants. |
| Official package drawing | `UNKNOWN_REQUIRES_SOURCE` | Must show body size, lead pitch, exposed pad, and pin-1 orientation. |
| KiCad footprint candidate | `UNKNOWN_REQUIRES_SOURCE` | Candidate only until compared with drawing. |
| Pin count and pad count | `UNKNOWN_REQUIRES_SOURCE` | Must match exact package. |
| Exposed pad policy | `UNKNOWN_REQUIRES_SOURCE` | Thermal/electrical connection must be documented. |
| 3D model | `UNKNOWN_REQUIRES_SOURCE` | Useful for mechanical review, not proof of footprint correctness. |

## KiCad Risks

- Similar STM32 symbols may share names but differ by package or pinout.
- Hidden power pins can hide missing supply-net errors.
- Multi-unit symbols can hide analog, power, or oscillator pins if not reviewed.
- QFN/BGA/WLCSP packages need courtyard, assembly, via-in-pad, and fab capability review.
- Connector/dev-board footprints must not be inferred from MCU package names.

## Human Review Required

Every `STM32G4` footprint selection is `HUMAN_REVIEW_REQUIRED` until exact package drawing comparison is complete.
