# Footprint Requirements Extraction

## Required Source Evidence

Extract footprint requirements only from:

- Exact package drawing.
- Exact connector drawing.
- Vendor land pattern.
- Package section in the datasheet.
- User-confirmed mechanical requirement.

## Extract Fields

- Package name/code.
- Pin or pad count.
- Pitch.
- Pad dimensions.
- Drill sizes.
- Slot dimensions.
- Exposed pad dimensions.
- Body outline.
- Courtyard or keepout.
- Pin 1 orientation.
- Mounting pads or shell pads.
- Height.
- 3D model requirements.

## Connector Rule

Connector footprints require exact manufacturer drawing and human orientation review.

## Unknown Rule

If any dimension is not extracted from source, keep it `Unknown - requires source verification`.

## Related Standards

- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_CREATION_STANDARD.md`
- `11_LIBRARY_FACTORY/footprints/CONNECTOR_FOOTPRINT_RULES.md`
- `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md`

