# Footprint Verify Workflow

## Steps

1. Identify exact manufacturer part number.
2. Collect package drawing or land pattern.
3. Resolve KiCad footprint file path.
4. Compare pad count, numbering, pitch, pad size, body outline, courtyard, pin 1, and mechanical orientation.
5. Check 3D model path and orientation if available.
6. Record evidence and status.
7. Copy into project-local library if stability or modification is required.

## Exit Criteria

Use `FOOTPRINT_VERIFIED_AGAINST_DRAWING` only when exact evidence is recorded. Otherwise use `UNVERIFIED_FOOTPRINT`.
## Mandatory Accuracy Gate

Footprint verification must compare KiCad pads, numbering, orientation, courtyard, fab outline, silkscreen, drills, and 3D model alignment against exact source evidence. Record unresolved items in a claim/evidence matrix and uncertainty log.
