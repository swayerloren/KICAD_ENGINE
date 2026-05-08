# ESP32-C5-REPRESENTATIVE_PART_REQUIRES_SOURCE Boot And Debug Notes

Date: 2026-05-03
Status: `AI_PLANNING_CHECKLIST`

Use this file to record boot, programming, and debug guidance for `ESP32-C5-REPRESENTATIVE_PART_REQUIRES_SOURCE`. All entries start unverified.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## Programming And Debug Method

| Method | Pins / Connector | Evidence Status | Notes |
| --- | --- | --- | --- |
| `UNKNOWN_REQUIRES_SOURCE` | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` | Add official programming/debug source. |

## Boot Pins Or Configuration Pins

| Signal | Default State | Recovery Access | Status |
| --- | --- | --- | --- |
| `UNKNOWN_REQUIRES_SOURCE` | `UNKNOWN_REQUIRES_SOURCE` | `UNKNOWN_REQUIRES_SOURCE` | `NEEDS_HUMAN_REVIEW` |

## Agent Rules

- Do not repurpose debug pins without a documented recovery path.
- Do not infer bootloader interfaces from another family.
- Do not claim programming support until source evidence or user confirmation exists.
