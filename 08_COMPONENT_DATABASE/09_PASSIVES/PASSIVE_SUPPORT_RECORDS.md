# Passive Support Records

Date: 2026-05-02

Status: generic placeholders. These records express common design intent for AI review. They are not approved BOM selections and must be promoted only with exact source evidence.

## Records

| Record ID | Part / Topic | Family | Status | Primary Checks |
| --- | --- | --- | --- | --- |
| `PASSIVE_CAP_0_1UF_DECOUPLING_GENERIC` | 0.1uF decoupling capacitor generic | MLCC decoupling | `UNVERIFIED_PLACEHOLDER` | Voltage, dielectric, package, effective capacitance, placement |
| `PASSIVE_CAP_10UF_BULK_GENERIC` | 10uF bulk capacitor generic | Bulk capacitor | `UNVERIFIED_PLACEHOLDER` | Effective capacitance, voltage derating, ESR, ripple/load behavior |
| `PASSIVE_CAP_22PF_CRYSTAL_LOAD_GENERIC` | 22pF crystal load capacitor generic | Crystal load capacitor | `UNVERIFIED_PLACEHOLDER` | Crystal CL math, stray capacitance, MCU oscillator guidance |
| `PASSIVE_RES_10K_PULLUP_GENERIC` | 10k pull-up resistor generic | Pull resistor | `UNVERIFIED_PLACEHOLDER` | Voltage domain, leakage, boot strap, bus timing |
| `PASSIVE_RES_0R_JUMPER_GENERIC` | 0 ohm jumper resistor generic | Jumper/link | `UNVERIFIED_PLACEHOLDER` | Current rating, package, assembly intent, test/rework plan |
| `PASSIVE_FERRITE_BEAD_GENERIC` | Ferrite bead generic | EMI filtering | `UNVERIFIED_PLACEHOLDER` | Impedance curve, DC current, DCR, resonance, target noise band |
| `PASSIVE_COMMON_MODE_CHOKE_GENERIC` | Common mode choke generic | EMI filtering | `UNVERIFIED_PLACEHOLDER` | Common-mode impedance, differential insertion loss, current, interface |
| `CLOCK_CRYSTAL_8MHZ_GENERIC` | 8 MHz crystal generic | Crystal | `UNVERIFIED_PLACEHOLDER` | CL, ESR, tolerance, drive level, package, MCU oscillator |
| `CLOCK_CRYSTAL_16MHZ_GENERIC` | 16 MHz crystal generic | Crystal | `UNVERIFIED_PLACEHOLDER` | CL, ESR, tolerance, drive level, package, MCU oscillator |
| `CLOCK_CRYSTAL_40MHZ_GENERIC` | 40 MHz crystal generic | Crystal | `UNVERIFIED_PLACEHOLDER` | RF/radio requirements, CL, ESR, tolerance, layout |
| `CLOCK_CRYSTAL_32_768KHZ_GENERIC` | 32.768 kHz crystal generic | Watch crystal | `UNVERIFIED_PLACEHOLDER` | Low-power oscillator suitability, CL, ESR, leakage, layout |

## Generic Passive Rules

- Do not treat nominal value as a complete component choice.
- Verify exact voltage, package, tolerance, temperature behavior, and power/current where applicable.
- Match every KiCad footprint candidate to the exact manufacturer package drawing.
- Keep layout notes visible in schematic/PCB review where part placement affects behavior.

## Crystal-Specific Rules

- Frequency alone is not enough.
- Load capacitors must be calculated from the selected crystal load capacitance and estimated stray capacitance.
- Drive level and ESR must be compatible with the target oscillator.
- Crystal layout should follow the target IC or module hardware guide.

## Promotion Checklist

- Manufacturer part selected.
- Datasheet and source URL recorded.
- Verification flags updated only for evidence actually checked.
- Footprint and 3D model checked against package drawing.
- Electrical and layout constraints copied into the design review notes.
