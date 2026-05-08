# Schematic Completeness Check

Status: `WARN`

Generated: `2026-05-06T15:42:16`
Schematic: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Summary

- Pass: 10
- Warn: 1
- Fail: 0

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `PASS` | `POWER_INPUT_PRESENT` | `` | power input appears present. | `5v_in, 5v input, vbus, barrel, jack, usb-c, +5v_in, 5v_raw` |
| `PASS` | `PROTECTION_PRESENT` | `` | input/protection appears present. | `polyfuse, ptc, fuse, tvs, esd, reverse polarity, pmos, smaj` |
| `PASS` | `REGULATOR_PRESENT` | `` | regulator appears present. | `regulator, buck, ldo, +3v3, 3v3, ap63203, ams1117, mp1584` |
| `PASS` | `MCU_OR_MODULE_PRESENT` | `` | MCU/module appears present. | `esp32, stm32, pic, rp2040, mcu, module` |
| `PASS` | `ESD_PRESENT` | `` | ESD protection appears present. | `esd, tvs, tpd, usblc, protection diode` |
| `PASS` | `BOOT_RESET_PRESENT` | `` | boot/reset appears present. | `boot, reset, en, gpio0, nrst, mclr` |
| `PASS` | `TEST_PADS_PRESENT` | `` | test pads appears present. | `testpoint, test point, testpad, tp_` |
| `PASS` | `MOUNTING_HOLES_PRESENT` | `` | mounting holes appears present. | `mountinghole, mounting hole, mh1, mh2` |
| `PASS` | `USB_C_SECTION_PRESENT` | `` | Project appears to require USB-C and USB-C-related schematic content was found. | `` |
| `PASS` | `PROJECT_MECHANICAL_NOTES_PRESENT` | `` | Mechanical/project notes appear present. | `` |
| `WARN` | `NO_BOM_LOCK_PROVIDED` | `` | No BOM lock path was provided; expected-items check was skipped. | `` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
