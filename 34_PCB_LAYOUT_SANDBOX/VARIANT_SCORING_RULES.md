# Variant Scoring Rules

## Purpose

Provide a repeatable scoring system for comparing at least three PCB layout variants before editing a real `.kicad_pcb`.

The score is a structured filter that blocks obviously bad variants, ranks viable candidates, and feeds the sandbox auto-approval decision.

Human review remains available, but generic manual approval is no longer the default gate when objective evidence is sufficient.

## Status Outputs

Every variant must end with exactly one status:

- `PASS`
- `FAIL`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

Project-level selected-variant auto-approval status is handled separately by:

- `AUTO_APPROVAL_STATUS_CODES.md`
- `AUTO_SANDBOX_APPROVAL_RULES.md`

## Score Model

Base score is `0-100` before penalties.

| Category | Range | Pass Intent |
| --- | ---: | --- |
| Mechanical correctness | `0-20` | Shape, dimensions, mounting, connector usability, enclosure logic |
| Connector orientation correctness | `0-20` | USB-C, barrel jack, edge connectors, verified facing direction |
| Antenna/RF keepout correctness | `0-15` | ESP32 antenna clearance, RF edge logic, no blocked keepout |
| Power path quality | `0-15` | Sensible source-to-load flow, compact switching-power grouping |
| USB/data routing quality | `0-10` | Short clean projected data path, ESD placement, low stub risk |
| Component grouping quality | `0-10` | Logical functional clusters, local decoupling, serviceability |
| Routing feasibility | `0-10` | No obvious congestion trap, no forced nonsense routes |

Two penalty channels apply after category scoring:

- DRC/precheck risk penalty
- human uncertainty risk penalty

## DRC / Precheck Risk Penalty

Map DRC/precheck risk to penalty points:

| Risk Level | Penalty |
| --- | ---: |
| `NONE` | `0` |
| `LOW` | `3` |
| `MEDIUM` | `6` |
| `HIGH` | `10` |
| `BLOCKER` | `15` |

## Human Uncertainty Risk Penalty

Map uncertainty risk to penalty points:

| Risk Level | Penalty |
| --- | ---: |
| `NONE` | `0` |
| `LOW` | `2` |
| `MEDIUM` | `5` |
| `HIGH` | `10` |
| `BLOCKER` | `15` |

Total score:

```text
total_score = category_subtotal - drc_precheck_risk_penalty - human_uncertainty_risk_penalty
```

Clamp total score to `0-100`.

## Hard Fail Conditions

Any one of these makes the variant `FAIL` regardless of subtotal:

- required connector missing
- USB-C not on the intended edge when required
- USB-C facing direction wrong
- barrel jack or required input connector wrong or missing
- ESP32 antenna keepout blocked
- mounting holes missing when required
- board dimensions guessed without source
- required footprint missing
- high-risk footprint has no exact package evidence or documented safe candidate
- projected traces cross the antenna keepout
- power path order is nonsensical
- routing feasibility is impossible
- DRC/precheck fail

## Non-Hard-Fail Review Flags

## Missing-Data Block Conditions

Use `AUTO_BLOCKED_MISSING_DATA` when required evidence is incomplete, stale, invalid, or still assumption-only.

Examples:

- category fields missing
- board shape undefined
- board dimensions not source-defined
- connector orientation not fully known
- RF keepout definition missing when the RF module exists

## Status Thresholds

Use these thresholds after hard-fail and missing-data checks:

- `FAIL`
  - any hard fail exists
- `AUTO_BLOCKED_MISSING_DATA`
  - no hard fail exists, but required evidence fields are missing or incomplete
- `AUTO_BLOCKED_BAD_LAYOUT`
  - no hard fail exists
  - no required evidence is missing
  - total score is below `80`
- `PASS`
  - no hard fail exists
  - no required evidence is missing
  - total score is `80+`

## Selection Rule

The selected variant must be:

1. highest score among non-failed variants
2. lowest combined penalty among score ties
3. explicitly justified

The selector must not choose a hard-failed variant, even if it has the highest score.

The selected variant may still be blocked from PCB work by the separate auto-approval engine.

## Optional FreeRouting Support

The `routing_feasibility` category may be supported by an optional FreeRouting dry run.

Allowed use:

- unrouted-net comparison
- via-count comparison
- coarse congestion comparison
- coarse trace-length comparison when reported
- obvious impossible-placement detection

Not allowed:

- automatic approval of USB routing
- automatic approval of RF routing
- automatic approval of buck or switching-node routing
- automatic approval of high-current routing
- final routing approval

When FreeRouting evidence is used:

- label it `REVIEW_ONLY`
- keep human review mandatory for high-risk nets
- treat the result as one supporting signal inside the `routing_feasibility` category, not as a replacement for the rest of the scorecard

## Required Input Fields For Scripts

The scoring scripts consume either:

- a `.json` file, or
- a Markdown file containing one fenced `json` block

Required structured fields:

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
  "drc_precheck_risk_level": "LOW",
  "human_uncertainty_risk_level": "LOW",
  "required_connectors_present": true,
  "connector_orientation_known": true,
  "board_dimensions_known": true,
  "board_shape_defined": true,
  "board_dimensions_guessed_without_source": false,
  "mounting_holes_required": false,
  "mounting_holes_present": true,
  "usb_c_required": true,
  "usb_c_on_intended_edge": true,
  "usb_c_facing_correctly": true,
  "input_connector_required": false,
  "input_connector_present": true,
  "input_connector_facing_correctly": true,
  "barrel_jack_required": false,
  "barrel_jack_placed": true,
  "barrel_jack_facing_correctly": true,
  "esp32_rf_module_present": true,
  "antenna_keepout_defined_if_required": true,
  "esp32_antenna_keepout_blocked": false,
  "all_footprints_assigned": true,
  "high_risk_footprint_exact_package_evidence": true,
  "high_risk_footprint_safe_candidate_documented": false,
  "routing_projection_crosses_antenna_keepout": false,
  "power_path_order_sensible": true,
  "routing_feasibility_impossible": false,
  "drc_precheck_pass": true,
  "notes": "Optional human notes.",
  "uncertainty_notes": "Optional uncertainty notes."
}
```

## Script Usage

Score one variant:

```powershell
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md
```

Compare at least three variants:

```powershell
python 34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md reports/PCB_LAYOUT_SANDBOX_VARIANT_02.md reports/PCB_LAYOUT_SANDBOX_VARIANT_03.md
```

Auto-select the best candidate:

```powershell
python 34_PCB_LAYOUT_SANDBOX/scripts/auto_select_best_variant.py reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md reports/PCB_LAYOUT_SANDBOX_VARIANT_02.md reports/PCB_LAYOUT_SANDBOX_VARIANT_03.md
```

## Scoring Discipline

- Do not inflate scores because a variant looks neat.
- Do not waive hard fails because routing might be fixed later.
- Do not treat a guessed outline as mechanically valid.
- Do not let DRC readiness substitute for placement reasoning.
- Do not use a high score by itself as permission to skip footprint, connector, RF, or routing-feasibility evidence.
- Do not select a lower-ranked variant unless the workflow records an evidence-backed exception outside this scoring rule.
