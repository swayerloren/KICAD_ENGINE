# Manufacturing Revision Folder Rules

Status: `ACTIVE_RULES`

## Required Rule

Never overwrite old manufacturing revision folders.

## Standard Layout

```text
manufacturing\
  rev_A\
    jlcpcb\
    pcbway\
    review\
```

Use a new revision folder for every export attempt. If an export is regenerated after a correction, create the next revision or a clearly dated review folder.

## Folder Meanings

- `jlcpcb`: JLCPCB-specific Gerber zip, BOM, CPL, and assembly notes.
- `pcbway`: PCBWay-specific Gerber zip, BOM, centroid, and assembly notes.
- `review`: screenshots, Gerber-viewer evidence, 3D evidence, and orientation checks.

All files remain `NOT_FINAL` until LJ approves upload.

