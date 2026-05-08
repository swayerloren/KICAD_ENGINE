# Universal PCBA Package Rules

Status: `ACTIVE_RULES`

Source integrated from: `T_E_M_P\file format.md`

## Required Package Layout

```text
manufacturing\
  rev_A\
    jlcpcb\
      gerbers.zip
      BOM_JLCPCB.csv
      CPL_JLCPCB.csv
      Assembly_Notes.md
    pcbway\
      gerbers.zip
      BOM_PCBWay.csv
      Centroid_PCBWay.csv
      Assembly_Notes.md
    review\
      gerber_screenshots\
      3d_screenshots\
      orientation_checks.md
```

Each revision must use a new folder such as `rev_A`, `rev_B`, or a dated revision folder. Never overwrite a prior revision.

## Required Pre-Upload Evidence

- KiCad DRC passes with schematic parity.
- No unrouted nets remain, or every remaining unrouted item has a documented LJ-approved nonblocking reason.
- Gerbers exported.
- Excellon drill files exported.
- Gerbers reviewed in an external viewer.
- BOM cleaned and validated.
- Pick-and-place / CPL / centroid checked and validated.
- Solder paste layers included for assembly.
- Board outline / Edge.Cuts included.
- Mounting holes, slots, and cutouts included.
- Assembly notes created.
- Orientation review created.

## Required Human / Visual Checks

- Barrel jack orientation verified.
- USB-C orientation verified.
- All connector mating directions verified.
- Pin 1 verified on every IC/module.
- Diode and LED polarity verified.
- Capacitor polarity verified.
- Pick-and-place rotations visually checked.

Validation scripts may report `PASS` for CSV structure. That does not approve assembly orientation, polarity, substitution, sourcing, or upload.

