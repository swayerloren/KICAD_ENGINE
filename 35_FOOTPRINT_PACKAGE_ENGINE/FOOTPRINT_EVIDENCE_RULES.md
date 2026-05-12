# Footprint Evidence Rules

## Minimum Proof

A footprint is only considered verified when the project records:

- the exact physical symbol reference
- the exact KiCad footprint name
- package or land-pattern evidence
- a source link or local datasheet path
- a risk classification
- explicit review state for high-risk parts

## Acceptable Evidence

- manufacturer datasheet package drawing
- official mechanical drawing
- official land-pattern recommendation
- trusted KiCad-library QA record with the exact package
- reviewed project-local footprint copy with matching source evidence

## Not Enough

- footprint name looks similar
- package code seems close
- another project used it
- DRC is clean
- 3D model roughly fits
- symbol default footprint field exists

## Required Result Labels

- `VERIFIED`
- `UNVERIFIED`
- `BLOCKED_UNTIL_HUMAN_REVIEW`

## Source References

Source evidence may be:

- `https://...`
- `http://...`
- a repo-relative datasheet path
- an approved local document path captured in the lock notes

Missing source evidence means the footprint remains unverified.

## Canonical Migration References

For component/datasheet/vendor migration evidence, use:

- `08_COMPONENT_DATABASE/COMPONENT_EVIDENCE_RULES.md`
- `29_FOOTPRINT_GAP_ANALYSIS/LAND_PATTERN_SOURCE_INDEX.md`
- `30_SUPPLIER_FOOTPRINT_MATCHES/SUPPLIER_CAD_MODEL_RULES.md`

These surfaces record source-backed candidate evidence without treating vendor
portals or CAD libraries as final proof.
