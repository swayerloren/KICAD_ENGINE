# ESD And TVS Rules

Date: 2026-05-02

Status: rule snippet for AI-assisted schematic and PCB review.

## Selection Rules

- Select the protection part for the exact voltage domain and interface type.
- Verify reverse working voltage, clamping behavior, capacitance, leakage, surge rating, directionality, and package.
- For high-speed data, verify capacitance and differential insertion-loss behavior from the datasheet or vendor application note.
- For power inputs, verify standoff voltage, surge energy, thermal limits, and coordination with fuse or current-limit devices.
- For automotive or long-cable interfaces, use the product requirements and applicable surge/load-dump assumptions instead of a generic USB-style ESD part.

## Placement Rules

- Place ESD and TVS parts close to the connector or board entry point.
- Route the transient current path to ground or chassis as short and wide as practical.
- Avoid long stubs between the connector and protection device.
- Keep protected traces from passing sensitive IC pins before reaching protection.
- Use nearby ground vias or chassis strategy appropriate to the product grounding plan.

## KiCad Review Checklist

- Symbol direction and pin names match the selected part.
- Footprint pin numbering matches the manufacturer drawing.
- Ground pad, exposed pad, or shield pin connection is intentional.
- Differential pair routing does not detour through avoidable stubs.
- Protection component is placed before the vulnerable IC from the connector perspective.
- DRC constraints match package clearance and board-edge placement needs.

## AI Warnings

- Do not claim ESD compliance from part presence alone.
- Do not mix unidirectional and bidirectional TVS behavior without reviewing the signal bias.
- Do not use a generic SOT-23 or SOD footprint for an ESD array until the exact package drawing is checked.
