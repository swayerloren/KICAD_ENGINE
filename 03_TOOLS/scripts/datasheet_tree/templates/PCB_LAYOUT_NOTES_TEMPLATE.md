# {representative_part} PCB Layout Notes

Date: {date}
Status: `AI_PLANNING_CHECKLIST`

These notes define PCB layout review topics for `{representative_part}`. They are not placement, routing, or fabrication approval until exact source evidence and human review are recorded.

## Evidence Labels

{evidence_labels}

## Layout Topics To Verify

| Topic | Required Evidence | Status |
| --- | --- | --- |
| package courtyard | exact package drawing and footprint review | `NEEDS_HUMAN_REVIEW` |
| decoupling placement | datasheet/reference-design placement guidance | `NEEDS_HUMAN_REVIEW` |
| clock layout | oscillator/crystal routing and load capacitor guidance, if used | `NEEDS_HUMAN_REVIEW` |
| reset/boot access | accessible test/debug points and deterministic strap defaults | `NEEDS_HUMAN_REVIEW` |
| debug connector | programmer clearance, orientation, and target-voltage notes | `NEEDS_HUMAN_REVIEW` |
| high-speed interfaces | USB/CAN/RF/ethernet-specific layout rules, if used | `NEEDS_HUMAN_REVIEW` |
| analog pins | ADC/reference/analog-ground treatment, if used | `NEEDS_HUMAN_REVIEW` |
| thermal behavior | package thermal pad, exposed pad, copper, and via requirements | `UNKNOWN_REQUIRES_SOURCE` |
| manufacturing limits | fab trace/space/drill/annular ring rules | `NEEDS_HUMAN_REVIEW` |

## Do Not Guess

- Do not infer footprint geometry from package name alone.
- Do not assume a dev-board layout is licensed or correct for reuse.
- Do not route high-speed or RF nets without source-backed layout constraints.
- Do not treat DRC pass as proof that package orientation, pin 1, or connector mating direction is correct.
