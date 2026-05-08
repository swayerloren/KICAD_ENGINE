# Uncertainty Log - Golden Path Sample Gate Run

Date: `2026-05-03`

## Unverified Items

| Item | Status | Required resolution |
| --- | --- | --- |
| `J1` USB-A shield policy | `UNVERIFIED` | Human must decide shield/chassis/GND/no-connect policy and re-run ERC. |
| `J1` Molex 48037-0001 footprint | `UNVERIFIED` | Compare custom footprint to exact manufacturer drawing. |
| `J2` programming header orientation | `UNVERIFIED` | Verify mating connector/keying/pinout. |
| `U2` AMS1117 package/pin mapping | `UNVERIFIED` | Confirm exact package drawing and regulator pin mapping. |
| Diode and LED polarity | `UNVERIFIED` | Human visual/orientation review. |
| DRC parity conflicts | `UNVERIFIED_ROOT_CAUSE` | Determine whether board needs update-from-schematic, net renames, or accepted legacy-state notes. |
| BOM source data | `UNVERIFIED` | Create locked BOM/supplier source records if this is to become a scored benchmark. |

## Quality Gate

`BLOCKED_UNTIL_HUMAN_REVIEW`
