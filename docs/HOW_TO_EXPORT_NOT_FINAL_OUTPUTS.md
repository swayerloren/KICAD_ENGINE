# How To Export NOT_FINAL Outputs

KiCad Engine can generate review outputs and manufacturing-style outputs for inspection. These outputs must remain `NOT_FINAL` until all review gates pass.

## Review Outputs

Review outputs may include:

- ERC report.
- DRC report.
- BOM CSV.
- Schematic PDF.
- PCB plots.
- STEP model.
- Screenshots.

## Manufacturing-Style Outputs

Manufacturing-style outputs include:

- Gerbers.
- Drill files.
- Pick-and-place files.
- Assembly drawings.
- Fabrication BOM.
- Fabrication package zip.

These must be named or stored with `NOT_FINAL` unless the full release gate is complete.

## VS Code Task

```text
KiCad Engine: Export NOT_FINAL Review Package
```

## Before Exporting

Confirm:

- Active project path.
- Source files.
- Output folder.
- ERC status.
- DRC status.
- BOM review status.
- Footprint and connector review status.

Do not send `NOT_FINAL` outputs to fabrication as approved manufacturing files.
