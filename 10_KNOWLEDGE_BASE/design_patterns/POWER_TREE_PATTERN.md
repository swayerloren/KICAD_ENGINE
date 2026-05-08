# Power Tree Pattern

## Purpose

Make board power rails explicit before schematic or PCB work.

## Required Inputs

- Input source and voltage range.
- Load list with estimated current.
- Always-on and switched rails.
- Sequencing requirements.
- Noise-sensitive rails.
- Fault and protection requirements.

## Pattern

- Define input nets first.
- Define protection before regulation.
- Define regulators in dependency order.
- Name every rail with voltage and role.
- Add current estimate fields to the planning document.
- Track which components consume each rail.

## KiCad Agent Rules

- Do not place a regulator without capacitor and layout requirements from the datasheet.
- Do not assume a regulator can supply the load without thermal review.
- Do not tie analog and noisy digital rails together accidentally.
- Mark unknown current as `Unknown - requires source verification`.

## Review Gate

Power tree approval requires current estimates, regulator source evidence, protection strategy, and thermal/layout review.

