# ESP32_CSI_WIFI_NODE PCB Routing Plan Select-String Quoting

Status: `FAILED_NON_BLOCKING`

Date: 2026-05-03

## Attempt

Run a PowerShell `Select-String` validation command using double-quoted patterns containing Markdown backticks.

## Result

PowerShell returned a parser error because the quoted string was not terminated correctly.

## Impact

Non-blocking. The validation was rerun with single-quoted simpler patterns and succeeded.

## Future Action

Avoid PowerShell double-quoted validation patterns that include Markdown backticks. Prefer single-quoted patterns or simpler status strings.

