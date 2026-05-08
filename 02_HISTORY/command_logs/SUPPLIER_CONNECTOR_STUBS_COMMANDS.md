# Supplier Connector Stubs Commands

Date: 2026-05-03

Status: `RECORDED`

## Commands Run

### Startup And Inspection

```powershell
Get-Content -Raw AGENTS.md
Get-Content -Raw 00_CODEX_START\START_HERE.md
Get-Content -Raw 28_SUPPLIER_INGESTION\README.md
Get-Content -Raw 28_SUPPLIER_INGESTION\API_KEY_HANDLING.md
Get-Content -Raw 28_SUPPLIER_INGESTION\SUPPLIER_CONNECTOR_STANDARD.md
Get-ChildItem -Force -Recurse -Depth 2 28_SUPPLIER_INGESTION\connectors\digikey,28_SUPPLIER_INGESTION\connectors\mouser,28_SUPPLIER_INGESTION\connectors\jlcpcb,28_SUPPLIER_INGESTION\connectors\lcsc
Get-ChildItem -Force 28_SUPPLIER_INGESTION\scripts
```

Result: `PASS`

### Syntax Validation

```powershell
python -B -m py_compile 28_SUPPLIER_INGESTION\connectors\digikey\digikey_connector.py 28_SUPPLIER_INGESTION\connectors\mouser\mouser_connector.py 28_SUPPLIER_INGESTION\connectors\jlcpcb\jlcpcb_connector.py 28_SUPPLIER_INGESTION\connectors\lcsc\lcsc_connector.py 28_SUPPLIER_INGESTION\scripts\test_connectors_dry_run.py
```

Result: `PASS`

### Targeted Secret Pattern Scan

```powershell
rg -n --hidden -S "sk-[A-Za-z0-9_-]{20,}|api[_-]?key\s*=|token\s*=|password\s*=|client_secret\s*=" 28_SUPPLIER_INGESTION\connectors\digikey 28_SUPPLIER_INGESTION\connectors\mouser 28_SUPPLIER_INGESTION\connectors\jlcpcb 28_SUPPLIER_INGESTION\connectors\lcsc 28_SUPPLIER_INGESTION\scripts\test_connectors_dry_run.py README_GPT.md "FOR CHAT GPT.MD"
```

Result: `PASS_NO_MATCHES`

### Bytecode Cleanup

```powershell
$root = (Resolve-Path '.').Path
$targets = Get-ChildItem -Force -Recurse 28_SUPPLIER_INGESTION\connectors\digikey,28_SUPPLIER_INGESTION\connectors\mouser,28_SUPPLIER_INGESTION\connectors\jlcpcb,28_SUPPLIER_INGESTION\connectors\lcsc,28_SUPPLIER_INGESTION\scripts | Where-Object { $_.PSIsContainer -and $_.Name -eq '__pycache__' }
foreach ($target in $targets) {
  $resolved = (Resolve-Path -LiteralPath $target.FullName).Path
  if (-not $resolved.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) { throw "Refusing to remove outside repo: $resolved" }
  Remove-Item -LiteralPath $resolved -Recurse -Force
}
```

Result: `PASS`

### Optional Git Diff Check

```powershell
git diff --name-only
```

Result: `FAILED_NON_BLOCKING`

Reason: current folder did not present as a Git repository to Git. This did not affect the requested connector stub work.

### Closeout Index Rebuild

```powershell
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
```

Result: `PASS`

## Commands Not Run

- No live supplier API commands.
- No connector dry-run execution.
- No package manager install.
- No KiCad CLI command.
- No KiCad design-file command.
