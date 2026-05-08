# Routing Geometry Hard Fail Test Report

Date: `2026-05-08`
Branch: `hardening/execution-contract`
Task type: `DOCS_ONLY`

## Scope

Validate the new routing geometry hard-fail layer without editing KiCad design
files.

## Aggregate Geometry Checker Results

| Fixture | Exit | Status | Hard Fail Statuses |
| --- | --- | --- | --- |
| `good_45_degree_route` | `0` | `PASS` | `_none_` |
| `bad_90_degree_route` | `1` | `AUTO_BLOCKED_BAD_LAYOUT` | `RIGHT_ANGLE_FOUND` |
| `bad_acute_jog_route` | `1` | `AUTO_BLOCKED_BAD_LAYOUT` | `ACUTE_JOG_FOUND` |
| `bad_pad_entry_route` | `1` | `AUTO_BLOCKED_BAD_LAYOUT` | `PAD_ENTRY_GEOMETRY_POOR` |
| `bad_zigzag_route` | `1` | `AUTO_BLOCKED_BAD_LAYOUT` | `UNNECESSARY_ZIGZAG_FOUND` |

## Focused Detector Results

| Detector | Fixture | Exit | Status |
| --- | --- | --- | --- |
| `detect_right_angle_traces.py` | `bad_90_degree_route` | `1` | `RIGHT_ANGLE_FOUND` |
| `detect_acute_jogs.py` | `bad_acute_jog_route` | `1` | `ACUTE_JOG_FOUND` |
| `detect_bad_pad_entry.py` | `bad_pad_entry_route` | `1` | `PAD_ENTRY_GEOMETRY_POOR` |
| `detect_unnecessary_zigzags.py` | `bad_zigzag_route` | `1` | `UNNECESSARY_ZIGZAG_FOUND` |

## Trace Audit / Scorecard Integration

| Fixture | Routing Plan Exit | Trace Audit Exit | Score Exit | Score Status | Geometry Hard Fails |
| --- | --- | --- | --- | --- | --- |
| `good_45_degree_route` | `0` | `0` | `0` | `PASS` | `_none_` |
| `bad_90_degree_route` | `0` | `1` | `1` | `AUTO_BLOCKED_BAD_LAYOUT` | `RIGHT_ANGLE_FOUND` |

## Conclusion

- The standalone geometry checker now fails bad geometry fixtures.
- The focused detector wrappers return the expected hard-fail status codes.
- The existing trace audit now surfaces geometry hard-fail statuses.
- The routing scorecard now blocks pass status when bad geometry is present.
- Routing work can no longer pass with ugly right-angle geometry hidden behind a
  clean or irrelevant DRC snapshot.
