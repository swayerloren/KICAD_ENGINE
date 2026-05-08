# PCB Review Checklist

## Footprints

- [ ] Every footprint has verification status.
- [ ] Exact package drawing checked for high-risk parts.
- [ ] Pin 1 and pad numbering checked.
- [ ] 3D model presence and orientation reviewed when used.

## Placement

- [ ] Connectors and mechanical parts reviewed.
- [ ] Polarity-sensitive parts flagged.
- [ ] Decoupling placement reviewed.
- [ ] Power-path placement reviewed.
- [ ] RF/USB/CAN layout flags recorded.

## Routing And Planes

- [ ] Unrouted nets checked.
- [ ] Power and ground return paths reviewed.
- [ ] Differential or sensitive routes reviewed.
- [ ] Zones refilled before DRC.

## Verification

- [ ] DRC run or reason documented.
- [ ] DRC findings interpreted.
- [ ] Remaining risks recorded as `HUMAN_REVIEW_REQUIRED`.
