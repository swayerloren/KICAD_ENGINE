# Routing Feasibility Scripts

Status: `OPTIONAL_REVIEW_ONLY`

## Purpose

Provide a small first-party script layer for optional FreeRouting-based routing-feasibility experiments.

This folder does not implement production autorouting. It provides dry-run helpers for:

- staging `.dsn` inputs
- running an optional FreeRouting dry run
- parsing coarse routing metrics
- converting those metrics into a routing-feasibility score
- staging `.ses` results for human review only

## Rules

- FreeRouting output is not final routing.
- Any autorouted result must be labeled `REVIEW_ONLY`.
- Never overwrite a real `.kicad_pcb` from these scripts.
- USB, RF, switching-regulator, and high-current paths still require engineering review.
- If FreeRouting is not installed or not available locally, the scripts must fail safely or return `UNAVAILABLE`.

## Files

- `export_dsn_for_feasibility.ps1`
- `run_freerouting_dry_run.py`
- `parse_unrouted_and_vias.py`
- `score_routing_feasibility.py`
- `import_route_result_for_review.py`

## Typical Flow

1. Stage a `.dsn`:

```powershell
powershell -ExecutionPolicy Bypass -File 03_TOOLS/scripts/routing_feasibility/export_dsn_for_feasibility.ps1 -BoardPath path\to\candidate.kicad_pcb -ManualDsnPath path\to\candidate.dsn -OutputDsnPath path\to\review\candidate.dsn
```

2. Run FreeRouting dry run:

```powershell
python 03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py --dsn path\to\review\candidate.dsn --output-dir path\to\review\freerouting_run --freerouting-jar C:\tools\freerouting.jar
```

3. Parse coarse metrics:

```powershell
python 03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py --log path\to\review\freerouting_run\freerouting.stdout.log --dsn path\to\review\candidate.dsn --ses path\to\review\freerouting_run\candidate.ses
```

4. Score routing feasibility:

```powershell
python 03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py path\to\review\freerouting_run\run_manifest.json
```

5. Stage review bundle:

```powershell
python 03_TOOLS/scripts/routing_feasibility/import_route_result_for_review.py --ses path\to\review\freerouting_run\candidate.ses --run-manifest path\to\review\freerouting_run\run_manifest.json --destination-dir path\to\review\bundle
```

## Output Discipline

Outputs are for:

- sandbox reports
- comparison scorecards
- human review bundles

They are not for:

- direct production board overwrite
- final routing approval
- fabrication export decisions
