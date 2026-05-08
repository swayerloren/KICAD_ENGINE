# RF Feedline Rules

Date: 2026-05-02

Status: rule snippet for AI-assisted RF layout review.

## Selection Rules

- Confirm the target impedance, usually from the radio, module, antenna, or connector source document.
- Determine the actual PCB stackup before calculating trace width and clearance.
- Verify dielectric constant, dielectric thickness, copper thickness, soldermask effect, and reference plane continuity.
- Choose feedline topology deliberately: microstrip, grounded coplanar waveguide, stripline, or vendor-specified geometry.

## Layout Rules

- Keep RF feedlines short and direct.
- Maintain a continuous reference plane under controlled-impedance traces unless the vendor layout forbids it.
- Stitch ground near grounded coplanar waveguide edges and RF connector grounds according to stackup and fab capability.
- Avoid 90 degree bends, unnecessary vias, neckdowns, and long stubs.
- Keep digital, switch-mode power, crystal, and high-current traces away from RF feedlines.
- Do not place copper, silkscreen, vias, or mechanical features in antenna keepouts unless source documents permit it.

## KiCad Review Checklist

- Board setup includes the intended stackup and constraints.
- RF net classes identify width, clearance, via limits, and length-sensitive areas.
- Connector footprint orientation matches the antenna cable or edge-launch direction.
- Ground pads on RF connectors have low-inductance via stitching.
- Matching network pads are present if the reference design expects tuning.

## AI Warnings

- Do not invent a 50 ohm trace width from memory.
- Do not treat "U.FL" and "IPEX" as interchangeable without exact mechanical series verification.
- Do not claim RF performance without stackup, layout, enclosure, and tuning review.
