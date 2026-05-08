# Hallucination Risk Log - Test Examples Benchmarks Setup

Date: 2026-05-03

Risk label: `LOW_RISK`

## Risk

Future agents could mistake examples, planning-only fixtures, or benchmark task definitions for completed benchmark results or approved engineering designs.

## Mitigation

- Planning sample files are marked `EXAMPLE_ONLY_PLANNING_ONLY`.
- Example folders are marked `EXAMPLE_ONLY`.
- Benchmark results folder remains empty except for its README.
- Audit states no real KiCad projects or fabrication outputs were created.

## Human Review Required

Required before adding real sample KiCad projects, publishing benchmark results, or using examples as project templates.

