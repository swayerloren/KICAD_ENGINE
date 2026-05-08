# Generic Gerber And Drill Rules

## Required Files

- Copper layers.
- Solder mask layers.
- Silkscreen layers.
- Paste layers when assembly is needed.
- Board outline layer.
- Excellon drill files.
- Drill map or report when useful.

## Review Steps

- Open Gerbers in an independent viewer when possible.
- Check board outline and cutouts.
- Check layer count and layer naming.
- Check plated versus non-plated holes.
- Check slots and mounting holes.
- Check solder mask openings.
- Check silkscreen readability and clearance.

## KiCad Engine Rules

- Generated Gerbers and drills are `NOT_FINAL` until reviewed.
- Do not overwrite prior exports without a timestamped output folder.
- Keep export command logs under `02_HISTORY/` or `05_OUTPUTS/`.

## Stop Conditions

Stop if board outline, drill intent, layer stack, or DRC status is unclear.

