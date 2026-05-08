# STM32U5 Common Mistakes

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Mistakes To Avoid

- Selecting a symbol by family name without exact order-code pinout verification.
- Assigning a footprint because the package text looks similar but not checking the mechanical drawing.
- Copying Blue Pill, Black Pill, Nucleo, or Discovery circuits without matching board revision and part package.
- Forgetting VDDA/VSSA/VREF/VBAT/VCAP/SMPS/LDO pins or hiding them behind symbol defaults.
- Using BOOT0/SWD pins for LEDs or connectors that block recovery/debug.
- Assuming USB or CAN/FDCAN exists on every part in the family.
- Choosing crystal/load capacitors from memory instead of AN2867 and the crystal datasheet.
- Treating STM32CubeMX output as source proof instead of a planning aid.
- Failing to check errata before committing a peripheral choice.

## Family-Specific High-Risk Areas

- SMPS versus LDO order codes
- TrustZone/debug policy
- low-power measurement design
- complex power pins

## Corrective Rule For AI Agents

When any exact value, pin, package, or peripheral claim cannot be traced to official ST documentation or a project-approved source, write `UNKNOWN_REQUIRES_SOURCE` and stop short of schematic/footprint approval.
