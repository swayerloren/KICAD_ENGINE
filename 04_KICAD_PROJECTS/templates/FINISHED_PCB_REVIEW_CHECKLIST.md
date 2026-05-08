# Finished PCB Review Checklist

Use this checklist for read-only review of finished PCB reference projects. Original finished PCB folders are reference sources and must not be edited.

## Non-Destructive Rule

- [ ] Confirm the original finished PCB folder is read-only for the review task.
- [ ] If edits, experiments, or generated outputs are needed, work only in a copied review workspace.
- [ ] Mark generated review outputs as `NOT_FINAL`.
- [ ] Do not overwrite original Gerbers, drill files, BOM, pick-and-place files, PDFs, STL files, backups, or KiCad source files.

## Source KiCad File Check

- [ ] Locate `.kicad_pro`.
- [ ] Locate `.kicad_sch`.
- [ ] Locate `.kicad_pcb`.
- [ ] Record project-local libraries, symbol libraries, footprint tables, caches, and backups if present.
- [ ] Record file names, paths, sizes, and modified dates.

## Schematic Check

- [ ] Run ERC against the copied review workspace when safe.
- [ ] Record ERC errors, warnings, exit code, and report path.
- [ ] Check missing symbols, missing footprint links, power labels, net labels, and connector labels.
- [ ] Classify ERC findings as design issue, intentional waiver, or local library/environment issue.

## PCB Check

- [ ] Run DRC against the copied review workspace when safe.
- [ ] Record DRC violations, unconnected items, footprint errors, exit code, and report path.
- [ ] Check courtyard overlap, thermal relief, co-located holes, clearance, board edge clearance, footprint mismatch, and missing library footprints.
- [ ] Classify DRC findings as design issue, intentional waiver, fabrication exception, or local library/environment issue.

## BOM Check

- [ ] Locate BOM file.
- [ ] Count rows, quantity sum, expanded references, and unique references.
- [ ] Check duplicate references.
- [ ] Check missing references.
- [ ] Check missing values.
- [ ] Check missing footprints.
- [ ] Group parts by prefix or category.

## Pick-And-Place Check

- [ ] Locate pick-and-place files or ZIP package.
- [ ] Confirm top and bottom placement files when assembly is required.
- [ ] Confirm required columns such as reference, value, package/footprint, X, Y, rotation, and side.
- [ ] Compare pick-and-place references against BOM references.
- [ ] Document parts in BOM but missing from pick-and-place as manual assembly or unresolved.

## Gerber Check

- [ ] Locate fabrication folder or ZIP.
- [ ] Confirm copper layers.
- [ ] Confirm solder mask layers.
- [ ] Confirm silkscreen layers.
- [ ] Confirm paste layers when assembly is required.
- [ ] Confirm Gerber job file if present.
- [ ] Record layer names exactly as provided.

## Drill Check

- [ ] Locate PTH drill file.
- [ ] Locate NPTH drill file if present.
- [ ] Confirm whether drill data is Excellon, Gerber drill, or another accepted board-house format.
- [ ] Flag missing standalone `.drl`, `.xln`, or drill text files if the board house requires them.

## Board Outline Check

- [ ] Confirm board outline or `Edge_Cuts` file is present.
- [ ] Confirm slots, cutouts, and mounting features are documented when visible.
- [ ] Check board edge clearances during DRC review when source files are available.

## Layer Naming Check

- [ ] Record all layer file names exactly.
- [ ] Confirm front/back copper naming.
- [ ] Confirm inner layer naming for multilayer boards.
- [ ] Confirm front/back mask, silkscreen, and paste naming.
- [ ] Confirm names are understandable to the selected manufacturer.

## PDF/STL Check

- [ ] Locate schematic/assembly PDF if present.
- [ ] Locate STL or STEP mechanical output if present.
- [ ] Treat visual/mechanical files as review aids, not proof of fabrication readiness.

## ERC/DRC Check

- [ ] Record ERC command, report path, exit code, errors, and warnings.
- [ ] Record DRC command, report path, exit code, violations, unconnected items, and footprint errors.
- [ ] Do not call the reference clean if ERC or DRC returns unresolved findings.

## Manufacturer Package Check

- [ ] Confirm fabrication package ZIP or folder exists.
- [ ] Confirm BOM package exists when assembly is required.
- [ ] Confirm pick-and-place package exists when assembly is required.
- [ ] Confirm required outputs match the manufacturer upload requirements.
- [ ] Confirm outputs are not being regenerated or overwritten during review.

## Review Outputs

- [ ] Save inventory report under `02_HISTORY\design_reviews`.
- [ ] Save ERC/DRC report summary under `02_HISTORY\erc_drc_reports`.
- [ ] Save project-specific review report under the copied review workspace `reports` folder.
- [ ] Update project memory only with durable factual findings.

## Completion Rule

A finished PCB reference review is complete only when source files, BOM, pick-and-place, Gerbers, drill data, board outline, PDFs/STL, ERC/DRC status, and manufacturer package completeness have been recorded. A reference review is not fabrication approval.
