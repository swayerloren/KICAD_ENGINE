# Trace By Trace Audit

- project: `bad_keepout_violation_fixture`
- status: `AUTO_BLOCKED_BAD_LAYOUT`

## Trace Audit

| net | critical | segments | vias | issues |
| --- | --- | --- | --- | --- |
| USB_D+ | True | 1 | 1 | trace_crosses_antenna_keepout,vias_without_reason |
| EN | True | 2 | 0 | right_angle_turn,trace_crosses_antenna_keepout |

## Hard Fails

- trace crosses antenna keepout
- via used without reason on critical net
