# Schematic Completeness Check

Status: `FAIL`

Generated: `2026-05-03T14:56:57`
Schematic: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`

## Summary

- Pass: 3
- Warn: 3
- Fail: 5

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `FAIL` | `POWER_INPUT_PRESENT` | `` | power input was not detected by symbol/text scan. | `5v_in, 5v input, vbus, barrel, jack, usb-c, +5v_in, 5v_raw` |
| `FAIL` | `PROTECTION_PRESENT` | `` | input/protection was not detected by symbol/text scan. | `polyfuse, ptc, fuse, tvs, esd, reverse polarity, pmos, smaj` |
| `PASS` | `REGULATOR_PRESENT` | `` | regulator appears present. | `regulator, buck, ldo, +3v3, 3v3, ap63203, ams1117, mp1584` |
| `PASS` | `MCU_OR_MODULE_PRESENT` | `` | MCU/module appears present. | `esp32, stm32, pic, rp2040, mcu, module` |
| `FAIL` | `ESD_PRESENT` | `` | ESD protection was not detected by symbol/text scan. | `esd, tvs, tpd, usblc, protection diode` |
| `PASS` | `BOOT_RESET_PRESENT` | `` | boot/reset appears present. | `boot, reset, en, gpio0, nrst, mclr` |
| `FAIL` | `TEST_PADS_PRESENT` | `` | test pads was not detected by symbol/text scan. | `testpoint, test point, testpad, tp_` |
| `FAIL` | `MOUNTING_HOLES_PRESENT` | `` | mounting holes was not detected by symbol/text scan. | `mountinghole, mounting hole, mh1, mh2` |
| `WARN` | `USB_C_REQUIREMENT_NOT_DETECTED` | `` | USB-C requirement was not detected from schematic/project notes; verify manually if this project should include USB-C. | `` |
| `WARN` | `PROJECT_MECHANICAL_NOTES_NOT_DETECTED` | `` | Project notes/mechanical notes were not detected in schematic text. | `` |
| `WARN` | `NO_BOM_LOCK_PROVIDED` | `` | No BOM lock path was provided; expected-items check was skipped. | `` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
