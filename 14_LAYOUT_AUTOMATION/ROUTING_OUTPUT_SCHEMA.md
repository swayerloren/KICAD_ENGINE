# Routing Output Schema

## Purpose

Define the normalized JSON output format produced by the routing-planning and routing-audit scripts.

## Common Fields

Every routing-engine JSON output should include:

- `schema_version`
- `project`
- `tool`
- `status`
- `summary`

Optional:

- `errors`
- `warnings`
- `hard_fails`
- `review_required`

## Allowed Status Values

- `PASS`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

## Routing Plan Output

Required:

- `routing_order`
- `critical_net_names`
- `power_net_names`
- `usb_net_names`
- `rf_keepout_risk_nets`
- `antenna_keepout_risk_nets`

Each `routing_order` entry should include:

- `name`
- `role`
- `stage_name`
- `stage_index`
- `routing_priority`
- `critical`
- `power`
- `usb`
- `net_class`
- `width_mm`
- `clearance_mm`
- `preferred_layers`
- `allowed_layers`
- `via_allowed`
- `via_reason_required`
- `routing_status`

## Critical-Net Plan Output

Required:

- `critical_nets`
- `critical_net_count`
- `missing_critical_nets`
- `review_required`

## Unrouted-Net Report Output

Required:

- `unrouted_nets`
- `unrouted_count`
- `unrouted_critical_nets`
- `unrouted_power_nets`
- `hard_fails`

## Keepout-Violation Report Output

Required:

- `violations`
- `violation_count`
- `rf_or_antenna_violation_count`
- `hard_fails`

Each violation entry should include:

- `net`
- `keepout`
- `keepout_type`
- `segment`

## Trace Audit Output

Required:

- `trace_count`
- `flagged_count`
- `audit_complete`
- `traces`
- `hard_fails`

Each trace-audit entry should include:

- `net`
- `critical`
- `routing_status`
- `segment_count`
- `via_count`
- `via_reason`
- `widths_mm`
- `angles_deg`
- `issues`
- `review_required`

## Score Output

Required:

- `total_score`
- `status`
- `scores`
- `hard_fails`
- `blocked_reasons`
- `readiness`

`scores` must include:

- `critical_net_completeness`
- `power_path_quality`
- `usb_path_quality`
- `rf_keepout_compliance`
- `via_count_reasonableness`
- `unrouted_net_count`
- `drc_risk`
- `trace_audit_completeness`
- `human_review_risk`

`readiness` should include:

- `ready_for_real_kicad_test`
- `exact_blockers`
