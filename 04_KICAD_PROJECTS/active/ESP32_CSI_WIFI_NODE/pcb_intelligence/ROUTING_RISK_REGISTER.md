# Routing Risk Register

## 1. USB D+/D- test pads create stub risk and crowd the USB path.

- Severity: `MEDIUM`
- Status: `OPEN`

## 2. USB shield policy remains human-review required.

- Severity: `MEDIUM`
- Status: `OPEN`

## 3. U2 pad 41 drill-size violation needs footprint, rule, or fab review.

- Severity: `HIGH`
- Status: `OPEN`

## 4. Crude 90-degree or acute-angle rerouting could regress the board even when DRC passes.

- Severity: `HIGH`
- Status: `OPEN`

## 5. USB routing can be forced into awkward pathing if the local USB cluster is not adjusted.

- Severity: `MEDIUM`
- Status: `OPEN`

## 6. RF keepout could be violated during USB or later low-speed routing if geometry is prioritized over placement.

- Severity: `MEDIUM`
- Status: `OPEN`

## 7. Copper zones remain intentionally deferred; local ground-return assumptions still need later review when zones are added.

- Severity: `MEDIUM`
- Status: `OPEN`

## 8. Overall routing remains incomplete after Stage 1/2 cleanup; USB and remaining low-speed nets still require clean completion.

- Severity: `HIGH`
- Status: `OPEN`
