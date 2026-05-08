# Footprint Common Mistakes

## High-Risk Mistakes

- Approving a footprint because the package name sounds similar.
- Ignoring package suffix differences.
- Ignoring exposed pad size and paste requirements.
- Missing courtyard or assembly clearance.
- Using a generic connector footprint for an exact connector.
- Trusting a 3D model as proof of land-pattern correctness.
- Forgetting polarity/orientation markings.

## Agent Checks

- Compare footprint to exact package drawing.
- Verify pad count, pitch, body size, exposed pad, and pin 1 marker.
- Check courtyard and mechanical clearance.
- Mark unverified footprints as `UNVERIFIED_FOOTPRINT`.
- Require human review for connectors and polarity-sensitive parts.

## Required Human Review

Human review is required for connectors, RF parts, high-power parts, fine-pitch packages, and any package without exact drawing evidence.

