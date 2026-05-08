# Fabrication House Preferences

Durable board fabrication and assembly preferences. Keep placeholder values as `TBD` until confirmed against the selected manufacturer.

## Preferred Board House
- Vendor: TBD.
- Ordering constraints: TBD.
- Notes: Verify current capabilities before each release.

## Default Stackup
- Layers: TBD.
- Copper weight: TBD.
- Board thickness: TBD.
- Dielectric/impedance requirements: TBD.

## Minimum Trace/Space
- Minimum trace width: TBD.
- Minimum spacing: TBD.
- Preferred design margin: TBD.

## Via Rules
- Minimum drill: TBD.
- Minimum annular ring: TBD.
- Via tenting preference: TBD.
- Filled/capped via rules: TBD.

## Solder Mask Preferences
- Color: TBD.
- Mask expansion: TBD.
- Sliver limits: TBD.

## Silkscreen Preferences
- Color: TBD.
- Minimum text height: TBD.
- Minimum line width: TBD.
- Required labels: connector labels, polarity marks, pin 1 marks, and board revision.

## Stencil Rules
- Stencil required: TBD.
- Thickness: TBD.
- Paste reduction rules: TBD.
- Fiducial requirements: TBD.

## Panelization Rules
- Panelization required: TBD.
- Rail width: TBD.
- Mouse bites/V-score preference: TBD.
- Tooling holes/fiducials: TBD.

## Required Fabrication Outputs
- Gerber files.
- Drill files.
- Board stackup notes.
- Pick-and-place file when assembly is required.
- BOM when assembly is required.
- STEP file for mechanical review when available.
- Fabrication drawing or notes when tolerances, cutouts, or special requirements exist.
- ERC report.
- DRC report.
- Visual review notes.

## COMMAND LINK Fabrication Package Pattern

This pattern was observed in the read-only `COMMAND_LINK_VERIFIED_REFERENCE` review on 2026-04-30. It is a reference package pattern, not a selected board-house default.

- Visible fabrication package included four copper Gerber layers: front copper, inner 1 copper, inner 2 copper, and back copper.
- Visible fabrication package included front/back solder mask, front/back silkscreen, and front/back paste layers.
- Board outline was present as an `Edge_Cuts` Gerber.
- Gerber job metadata was present.
- Drill-related files were present as PTH and NPTH drill Gerber files.
- A fabrication ZIP and a pick-and-place ZIP were present alongside extracted folders.
- PDF and STL reference files were present for visual/mechanical review.
- Standalone Excellon-style `.drl`, `.xln`, or `.txt` drill files were not observed in the visible folder tree. Future fabrication reviews must confirm the selected board house accepts the drill format included in the package.

## 2026-05-07: JLCPCB / PCBWay PCBA File Format Rule

- JLCPCB and PCBWay need separate upload-specific BOM and placement files.
- JLCPCB BOM columns: `Comment,Designator,Footprint,LCSC Part #,Quantity,Manufacturer,Manufacturer Part Number,Notes`.
- JLCPCB CPL columns: `Designator,Mid X,Mid Y,Layer,Rotation`.
- PCBWay BOM columns: `Line #,Quantity Per Part Number,Reference Designator,Part Number,Part Description,Package,Type,Manufacturer Name,Manufacturer Part Number,Distributor Part Number,Notes`.
- PCBWay centroid columns: `Designator,Mid X,Mid Y,Rotation,Layer`.
- Universal BOM/pick-and-place files are allowed for internal review, but upload packages should match the selected fab house.
- Manufacturing outputs remain `NOT_FINAL` until final export gates pass and LJ approves.
