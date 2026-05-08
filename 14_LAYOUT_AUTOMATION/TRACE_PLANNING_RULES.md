# Trace Planning Rules

## Purpose

Define the planning rules used before any routing work is treated as acceptable.

## Rules

- Plan by net criticality, not by random ratsnest order.
- Decide width, layer intent, and via tolerance before routing.
- Project return-path and keepout implications before routing sensitive nets.
- Route short, obvious critical paths first.
- Do not defer switching-loop or USB thought until late cleanup.

## Required Inputs

- net name
- net role
- width target
- layer preference
- keepout constraints
- whether pairing is required
- whether vias are allowed

## Failure Conditions

- critical nets missing from the plan
- width not assigned to power or USB nets
- keepout constraints missing for RF-sensitive paths
- via usage undefined for critical nets
