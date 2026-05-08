# Issue Log - Golden Path Sample Remaining Blockers

Status: `OPEN`

Created: `2026-05-03`

Sample: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board`

## Open Blockers

1. ERC error: `J1` USB-A shield pin is not connected.
2. DRC reports 15 violations.
3. DRC schematic parity reports 13 issues.
4. `J1` Molex 48037-0001 footprint requires exact drawing/orientation review.
5. `J2` programming header requires pinout and mating orientation review.
6. `U2` AMS1117 package/pin mapping/thermal assumptions require source verification.
7. Diode and LED polarity require visual/human review.
8. No locked purchasing BOM or supplier-source evidence exists.

## Required Before Clean Pass

- Resolve or explicitly accept USB shield policy.
- Re-run ERC and DRC.
- Verify exact high-risk footprints against source drawings.
- Complete human orientation/polarity review.
- Create a locked BOM or document why the demo does not need one.
- Keep generated outputs `NOT_FINAL`.
