# Gerber Drill Package Validation Rules

Status: `ACTIVE_RULES`

## Required Before Upload Approval

- KiCad DRC passes with schematic parity.
- No unrouted nets remain unless LJ approved exact nonblocking exceptions.
- Gerbers are exported as review-only `NOT_FINAL` files.
- Drill files are exported in Excellon format.
- Board outline / Edge.Cuts is included.
- Solder paste layers are included for assembly.
- Mounting holes, slots, and cutouts are present.
- Gerbers are opened and reviewed in an external viewer.
- Layer order, copper, solder mask, silkscreen, drill holes, and board dimensions are checked.

## Block Export If

- DRC is missing or failing.
- No-unrouted proof is missing.
- Board outline or drill files are missing.
- Paste layers are missing for an SMT assembly package.
- Gerber viewer review is missing.

