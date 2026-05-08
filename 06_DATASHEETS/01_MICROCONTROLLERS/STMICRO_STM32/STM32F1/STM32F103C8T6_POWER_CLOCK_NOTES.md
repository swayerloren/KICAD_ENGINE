# STM32F103C8T6 Power And Clock Notes

Date: 2026-05-03
Status: `AI_PLANNING_CHECKLIST`

Use these notes for source-backed power and clock planning. Exact component values, capacitor values, voltage limits, crystal values, and oscillator load capacitors are not approved by this file.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common STM32F1 design practice; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Power Notes

| Area | Guidance | Status |
| --- | --- | --- |
| VDD range | ST product page lists the STM32F103 medium-density family operating from 2.0 V to 3.6 V; verify exact datasheet limits before use. | `VERIFIED_SOURCE_LINK`, `NEEDS_HUMAN_REVIEW` |
| decoupling | Place local capacitors near each VDD/VSS pair and verify AN2586/datasheet recommendations. | `INFERRED_FROM_COMMON_DESIGN` |
| VDDA/VSSA | Treat analog supply and analog ground as explicit design items; verify filtering and connection rules. | `NEEDS_HUMAN_REVIEW` |
| VBAT | Use only if the exact design needs backup domain behavior; verify datasheet pin and supply rules. | `NEEDS_HUMAN_REVIEW` |
| power sequencing | Do not assume simple 3.3 V-only behavior covers USB, analog, reset, and debug edge cases. | `UNVERIFIED` |

## Clock Notes

| Clock Topic | Guidance | Status |
| --- | --- | --- |
| HSI | Internal-clock use may be sufficient for some firmware; exact tolerance and USB suitability require source review. | `NEEDS_HUMAN_REVIEW` |
| HSE | External crystal/resonator circuit must be selected from datasheet, AN2867, and the crystal vendor datasheet. | `NEEDS_HUMAN_REVIEW` |
| LSE | Use only if RTC/low-power timekeeping is required; verify pins, load, and layout. | `NEEDS_HUMAN_REVIEW` |
| USB clock | USB designs require source-backed clock accuracy and USB hardware review. | `NEEDS_HUMAN_REVIEW` |

## Layout Implications

- Keep decoupling loops short.
- Keep oscillator traces short, symmetric where applicable, and away from noisy nets.
- Avoid routing switching regulators, USB, or high-current traces through oscillator or analog areas.
- Check AN2586 and AN2867 before approving board placement/routing.
