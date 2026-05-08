# USB Trace Rules

## Purpose

Define routing rules for USB data and support traces.

## Rules

- Route USB D+/D- after the power core but before low-risk nets.
- Keep D+/D- short, clean, and paired where practical.
- Avoid obvious stubs.
- Keep ESD protection local to the connector.
- Keep CC and series parts on a clean local path.
- Avoid unnecessary vias on D+/D- unless the board geometry truly requires them.

## Review Triggers

- unequal-looking pair path
- long pair detours
- connector-to-ESD distance that is obviously too long
- USB path crossing switching or RF-sensitive regions
