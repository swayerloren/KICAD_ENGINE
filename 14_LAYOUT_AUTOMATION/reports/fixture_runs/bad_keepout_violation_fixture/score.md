# Routing Scorecard

- project: `bad_keepout_violation_fixture`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- total_score: `42`

## Scores

| category | value |
| --- | --- |
| critical_net_completeness | 13 |
| power_path_quality | 15 |
| usb_path_quality | 0 |
| rf_keepout_compliance | 0 |
| via_count_reasonableness | 6 |
| unrouted_net_count | 4 |
| drc_risk | 0 |
| trace_audit_completeness | 5 |
| human_review_risk | 1 |

## Hard Fails

- GND strategy missing
- USB D+/D- incomplete
- critical power net missing
- regulator critical loop not planned
- trace crosses antenna keepout
- unrouted critical net
- via used without reason on critical net

## Blocked Reasons

- 1 unrouted nets remain
- 2 keepout violations detected
- 2 trace audit entries flagged
- GND strategy missing
- USB D+/D- incomplete
- critical power net missing
- regulator critical loop not planned
- routing plan did not pass
- trace crosses antenna keepout
- unrouted critical net
- via used without reason on critical net
