# Pick And Place Rules

## Required Inputs

- KiCad board file.
- Footprint side and reference designator.
- Component centroid.
- Rotation convention for the target assembler.
- DNP/exclude-from-position-file status.

## Review Steps

- Verify every polarized part orientation.
- Verify connectors and mechanical parts are included or excluded intentionally.
- Verify top/bottom side.
- Verify rotations against assembly viewer or vendor expectation.
- Check for parts that should be hand-assembled.

## Common Mistakes

- Assuming KiCad rotation equals assembler rotation.
- Including hand-solder or DNP parts accidentally.
- Missing bottom-side rotation differences.
- Trusting PNP without visual assembly review.

## Human Review Gate

PNP files require manual review before assembly ordering.

