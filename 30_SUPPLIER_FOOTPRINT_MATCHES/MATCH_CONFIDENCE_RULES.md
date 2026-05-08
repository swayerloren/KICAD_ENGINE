# Match Confidence Rules

Status: confidence rules for supplier-to-KiCad footprint matches.

## Confidence Levels

| Level | Meaning | Can Approve Footprint? |
| --- | --- | --- |
| `VERIFIED_EXACT_PACKAGE_DRAWING` | KiCad footprint was compared to exact manufacturer package or connector drawing. | Maybe, if symbol/pinout/orientation and human review also pass. |
| `VERIFIED_VENDOR_FOOTPRINT` | Vendor provides an official footprint or EDA model and it was inspected. | Maybe, after local KiCad and human review. |
| `MATCHED_BY_PACKAGE_NAME_ONLY` | Supplier package text matches a generic KiCad package name. | No. |
| `MATCHED_BY_GENERIC_FOOTPRINT` | Generic KiCad footprint is plausible but not exact. | No. |
| `UNVERIFIED` | Evidence is missing or incomplete. | No. |
| `REJECTED` | Mismatch or unacceptable risk found. | No. |

## Hard Downgrade Rules

No connector, PMOS, ESD array, MCU module, or regulator footprint may be marked verified from package name only.

If any of these are true, confidence must be `UNVERIFIED`, `MATCHED_BY_PACKAGE_NAME_ONLY`, `MATCHED_BY_GENERIC_FOOTPRINT`, or `REJECTED`:

- Exact package drawing source is missing.
- KiCad footprint candidate is generic.
- Supplier package name is the only evidence.
- Pinout/pad mapping has not been checked.
- Connector orientation or mating connector is unknown.
- PMOS source/gate/drain mapping is not verified.
- ESD array pinout, polarity, or flow-through layout is not verified.
- MCU/module land pattern or keepout is not verified.
- Regulator thermal pad, exposed pad, or power-loop layout requirements are unknown.

## Verified Match Requirements

To use `VERIFIED_EXACT_PACKAGE_DRAWING`, the record must include:

- Exact MPN.
- Exact package name/code.
- Exact package drawing source.
- KiCad footprint library and footprint name.
- Pad count and pad numbering comparison.
- Pin 1/orientation review.
- Courtyard, fab, silkscreen, mask, paste, drill, and exposed-pad review as applicable.
- 3D/mechanical review if fit matters.
- Human review flag resolved or explicitly accepted.

## Vendor Footprint Requirements

`VERIFIED_VENDOR_FOOTPRINT` requires the vendor footprint source, revision/date if available, local KiCad import/review status, and human review. Vendor EDA models are not automatically correct.

