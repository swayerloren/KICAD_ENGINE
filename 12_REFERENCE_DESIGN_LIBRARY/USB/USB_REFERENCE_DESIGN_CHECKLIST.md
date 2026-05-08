# USB Reference Design Checklist

## Source And License

- Source owner identified.
- License and redistribution status recorded.
- Connector drawing source recorded.

## Technical Review

- USB role identified: host, device, dual-role, or power-only.
- Connector exact MPN and footprint reviewed.
- CC pins reviewed for USB-C.
- D+ and D- routing reviewed.
- ESD protection placement reviewed.
- VBUS power path and sense reviewed.
- Shield/shell behavior reviewed.

## Reuse Warnings

- Do not use a connector footprint from a different MPN.
- Do not copy USB2 pair width/spacing without stackup.
- Do not call a power-only USB-C design compliant without CC/current review.

## Human Review Needed

- Connector orientation.
- CC implementation.
- ESD placement.
- VBUS current path.

