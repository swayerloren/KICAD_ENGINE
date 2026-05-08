# {representative_part} Package And Footprint Notes

Date: {date}
Status: `NEEDS_HUMAN_REVIEW`

This file records package and footprint evidence for `{representative_part}`. It starts with no approved footprint.

## Evidence Labels

{evidence_labels}

## Candidate Package/Footprint

| Item | Candidate | Evidence | Status |
| --- | --- | --- | --- |
| orderable part | `{representative_part}` | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| package | `UNKNOWN_REQUIRES_SOURCE` | exact datasheet/order-code table required | `NEEDS_HUMAN_REVIEW` |
| KiCad symbol | `UNKNOWN_REQUIRES_SOURCE` | local/project library search required | `UNVERIFIED` |
| KiCad footprint | `UNKNOWN_REQUIRES_SOURCE` | exact package drawing required | `NEEDS_HUMAN_REVIEW` |
| KiCad 3D model | `UNKNOWN_REQUIRES_SOURCE` | mechanical/orientation review required | `NEEDS_HUMAN_REVIEW` |

## Verification Required Before PCB

- Check package/order-code table.
- Check package drawing dimensions, pin 1, pitch, tolerances, and body/lead geometry.
- Inspect symbol pin numbers and hidden pins against datasheet.
- Inspect footprint pads, courtyard, fab outline, silkscreen, and pin-1 marker.
- Confirm 3D model orientation and mechanical fit.
