# PIC ICSP Rules

Date: 2026-05-02

Status: design-rule snippet for AI-assisted KiCad review. Exact pin names, voltages, and programming entry rules require the exact Microchip programming specification.

## Core Rule

PIC programming is family- and part-specific. Codex must not infer ICSP pin behavior from another PIC family or from a dev board header.

## Required Checks

- Identify exact part number, `F`/`LF` variant, package, and programming tool.
- Find the exact programming specification or device data-sheet programming section.
- Confirm MCLR/VPP behavior, ICSPDAT/PGD, ICSPCLK/PGC, VDD, VSS, and any PGM or low-voltage programming pin.
- Keep programming pins accessible at a connector or pads.
- Avoid strong loads, LEDs, large capacitors, bus contention, or external drivers on programming pins unless isolated.
- Confirm whether target power is supplied externally or by the programmer.
- Confirm debug support separately from programming support; some devices/programmers differ.

## KiCad Review Checklist

- ICSP connector pin 1 and orientation are explicit.
- Net labels match the exact Microchip names or documented aliases.
- MCLR/VPP route is not blocked by an RC network or clamp that violates programming mode.
- PGC/PGD pins are not swapped.
- Target voltage reference is present for the programmer.
- Production board has a recovery path if ICSP pins are also application pins.

## Common Mistakes

- Copying a PICkit header from a different PIC family.
- Treating MCLR as an ordinary reset pin when high-voltage programming may be required.
- Leaving PGC/PGD connected to heavy loads.
- Forgetting that debug may reserve memory, pins, or resources.
- Assuming low-voltage programming is enabled, safe, or desirable.

## Required Sources Before Approval

- Exact device datasheet.
- Exact device programming specification.
- PICkit/ICD/ICE user guide for the selected tool.
- KiCad symbol pinout and footprint cross-check.
