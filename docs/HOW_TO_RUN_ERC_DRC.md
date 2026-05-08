# How To Run ERC And DRC

ERC and DRC are KiCad checks that should be part of every serious review.

## ERC

ERC checks schematic electrical-rule issues.

VS Code task:

```text
KiCad Engine: Run ERC
```

PowerShell wrapper:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\03_TOOLS\scripts\run_erc.ps1 -ProjectPath "C:\path\to\project"
```

## DRC

DRC checks PCB design-rule issues.

VS Code task:

```text
KiCad Engine: Run DRC
```

PowerShell wrapper:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\03_TOOLS\scripts\run_drc.ps1 -ProjectPath "C:\path\to\project"
```

## Limits

ERC does not prove pinouts, datasheet values, power budgets, or connector orientation.

DRC does not prove footprint correctness, mechanical fit, controlled impedance, assembly polarity, or fab readiness.

Use ERC and DRC as important evidence, not final approval.
