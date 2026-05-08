# REAL_KICAD_PCB_ROUTING_BRIDGE_HASH_RECHECK_COMMAND_WRAPPER

Date: `2026-05-07`

## Failure

The first closeout hash recheck wrapped PowerShell commands in a here-string that was printed instead of executed.

## Fix

Reran the hash check with direct `Get-FileHash` commands.

## Status

Resolved.
