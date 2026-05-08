# TASK 002: STM32 Blue Pill Clone Review

Status: `NOT_RUN`.

## Objective

Ask an AI agent to review an STM32F103C8T6 Blue Pill-style clone design or reference schematic for correctness risks. This is a review task, not an instruction to copy a clone design blindly.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- Official ST datasheets, reference manuals, application notes, Nucleo/Discovery schematics when applicable.
- Public Blue Pill schematic references only when source/license and uncertainty are recorded.
- Installed KiCad symbol and footprint libraries.

## Expected Outputs

- Review report with pass/warn/fail findings.
- Source citations for STM32F103C8T6 pinout, power, boot, clocking, USB, and debug claims.
- Symbol and footprint candidate review.
- BOOT0/BOOT1, reset, SWD, oscillator, USB pull-up/connector, regulator, and decoupling review.
- ERC/DRC results if a KiCad project is supplied.
- Human review flags for clone-specific assumptions.

## Required Evidence

- Exact part package and KiCad footprint status.
- VDDA/VSSA and VDD/VSS handling.
- BOOT0/BOOT1 handling.
- SWD connector pinout and orientation review.
- HSE/LSE assumptions and capacitor values marked source-backed or unverified.
- USB data-line and connector review if USB is present.

## Scoring Focus

- Risk identification.
- Correct ST source use.
- Correct symbol/footprint skepticism.
- Power/decoupling and boot/debug review.
- ERC/DRC interpretation.
- No unsupported clone-quality claims.

## Failure Modes

- Treating a random Blue Pill clone as authoritative.
- Ignoring counterfeit/variant/package uncertainty.
- Missing BOOT0 or SWD connector risks.
- Approving USB or oscillator values without source evidence.
