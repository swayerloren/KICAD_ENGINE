# PCB Variant Scorecard

Project:

Variant ID:

Board shape:

Board dimensions:

Primary connector edge plan:

## Human Scorecard

| Category | Max | Score | Notes |
| --- | ---: | ---: | --- |
| Mechanical correctness | 20 |  |  |
| Connector orientation correctness | 20 |  |  |
| Antenna/RF keepout correctness | 15 |  |  |
| Power path quality | 15 |  |  |
| USB/data routing quality | 10 |  |  |
| Component grouping quality | 10 |  |  |
| Routing feasibility | 10 |  |  |

## Human-Review Risk

- Risk level: `NONE | LOW | MEDIUM | HIGH | BLOCKER`
- Risk penalty:
- Risk notes:

## Hard Fail Checklist

- USB-C on intended edge:
- USB-C facing correctly:
- Barrel jack placed when required:
- Barrel jack facing correctly:
- ESP32 antenna keepout blocked:
- Mounting holes present when required:
- High-risk connector orientation reviewed:
- All footprints assigned:
- High-risk connector footprint tied to exact package/manufacturer drawing:
- Routing projection crosses antenna keepout:
- Power path sensible:
- Board dimensions known:
- Board dimensions guessed anyway:

## Variant Status

- Subtotal:
- Penalty:
- Total:
- Status: `PASS | FAIL | NEEDS_HUMAN_REVIEW`

## Optional FreeRouting Feasibility Evidence

- Evidence mode: `MANUAL_ONLY | FREEROUTING_DRY_RUN`
- Review-only status: `REVIEW_ONLY`
- Run status: `UNAVAILABLE | COMPLETED | ERROR | TIMEOUT`
- Routed percent:
- Unrouted net count:
- Via count:
- Congestion mentions:
- Notes:

## Notes

- Main strengths:
- Main risks:
- Why this variant should or should not survive comparison:

## Machine Score Input

Use this fenced JSON block as script input for `score_layout_variant.py` or `compare_layout_variants.py`.

```json
{
  "project": "PROJECT_NAME",
  "variant_id": "VARIANT_01",
  "mechanical_correctness": 18,
  "connector_orientation_correctness": 19,
  "antenna_rf_keepout_correctness": 15,
  "power_path_quality": 13,
  "usb_data_routing_quality": 8,
  "component_grouping_quality": 9,
  "routing_feasibility": 8,
  "routing_feasibility_evidence_mode": "MANUAL_ONLY",
  "freerouting_review_only": true,
  "freerouting_run_status": "UNAVAILABLE",
  "freerouting_routed_pct": 0.0,
  "freerouting_unrouted_net_count": 0,
  "freerouting_via_count": 0,
  "freerouting_congestion_mentions": 0,
  "human_review_risk_level": "LOW",
  "board_dimensions_known": true,
  "board_dimensions_guessed_anyway": false,
  "mounting_holes_required": false,
  "mounting_holes_present": true,
  "usb_c_required": true,
  "usb_c_on_intended_edge": true,
  "usb_c_facing_correctly": true,
  "barrel_jack_required": false,
  "barrel_jack_placed": true,
  "barrel_jack_facing_correctly": true,
  "esp32_antenna_keepout_blocked": false,
  "high_risk_connector_orientation_reviewed": true,
  "all_footprints_assigned": true,
  "high_risk_connector_footprints_tied_to_exact_package": true,
  "routing_projection_crosses_antenna_keepout": false,
  "power_path_sensible": true,
  "notes": "Optional notes.",
  "human_review_notes": "Optional risk notes."
}
```
