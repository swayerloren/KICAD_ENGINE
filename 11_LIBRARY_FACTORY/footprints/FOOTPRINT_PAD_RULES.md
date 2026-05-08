# Footprint Pad Rules

## Required Checks

- Pad count matches package drawing.
- Pad numbering matches package drawing.
- Pad shape matches manufacturing intent.
- Pad size matches land pattern or documented calculation.
- Drill size matches lead diameter or mechanical drawing.
- Plated versus non-plated intent is explicit.
- Exposed pad dimensions and paste openings are reviewed.

## SMD Pads

- Check pad width, length, pitch, and row spacing.
- Check solder mask expansion strategy.
- Check paste openings for thermal pads.
- Check toe/heel/side fillets when land pattern guidance is available.

## Through-Hole Pads

- Check drill diameter.
- Check annular ring.
- Check slot dimensions if applicable.
- Check plating intent.
- Check mechanical stress and connector retention.

## AI Rule

Never approve a pad layout from package name alone. Use exact drawings or keep `UNVERIFIED_FOOTPRINT`.

