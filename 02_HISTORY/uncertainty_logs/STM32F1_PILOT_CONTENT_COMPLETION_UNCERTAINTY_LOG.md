# STM32F1 Pilot Content Completion Uncertainty Log

Date: 2026-05-03
Risk label: `MEDIUM_RISK`

## Uncertainties

| Item | Confidence | Human Review Required | Notes |
| --- | --- | --- | --- |
| exact STM32F103C8T6 package/order-code mapping | Low | yes | Candidate LQFP-48 noted but not approved. |
| KiCad symbol pinout correctness | Low | yes | Symbol exists locally; pin audit not done. |
| KiCad footprint correctness | Low | yes | Footprint exists locally; package drawing comparison not done. |
| 3D model mechanical orientation | Low | yes | STEP exists locally; orientation not reviewed. |
| BOOT0/BOOT1 exact behavior | Medium | yes | AN2606/RM0008 source links recorded; exact section extraction pending. |
| USB hardware policy | Medium | yes | AN4879 link recorded; exact schematic policy pending. |
| VDDA/VSSA/VREF rules | Low | yes | Needs datasheet/AN2586 extraction. |
| Blue Pill board assumptions | Low | yes | Third-party page only; variants differ. |

## Required Rule

Keep STM32F103C8T6 records blocked for PCB/fab use until the above uncertainties are closed.
