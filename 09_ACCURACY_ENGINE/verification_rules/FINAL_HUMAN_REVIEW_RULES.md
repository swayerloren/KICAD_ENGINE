# Final Human Review Rules

## Prime Rule

AI review is not fabrication approval.

## Required Gates

- ERC reviewed.
- DRC reviewed.
- BOM reviewed.
- Symbol pinouts reviewed.
- Footprints matched to drawings.
- Connector orientation reviewed.
- Polarity and assembly reviewed.
- USB/CAN/RF/power layout reviewed where present.
- Mechanical fit reviewed.
- Gerbers and drills reviewed.
- PNP reviewed where assembly is intended.
- User explicitly approves release.

## Output Status

Until every gate is complete, manufacturing-style output remains:

```text
NOT_FINAL
```

Do not remove `NOT_FINAL` labels without explicit human approval and recorded evidence.
