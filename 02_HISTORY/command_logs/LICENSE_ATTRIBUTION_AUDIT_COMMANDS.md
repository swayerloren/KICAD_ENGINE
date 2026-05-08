# License Attribution Audit Commands

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Startup And Inventory

Commands were run read-only to inspect startup files, repo folders, third-party repositories, local license files, datasheet PDFs, sample projects, generated outputs, screenshots, and generated KiCad library indexes.

Important observations:

- `git status --short` could not be used because this workspace did not expose a `.git` directory.
- Third-party Git remotes and local license files were found under `03_TOOLS/repos` and `03_TOOLS/windows/repos`.
- Two Espressif PDFs were found under `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/`.
- Generated and copied artifacts were found under `05_OUTPUTS/`.

## Created Files

Validation command:

```powershell
$files = @(
  'LEGAL_AND_LICENSE_AUDIT.md',
  'THIRD_PARTY_TOOLS_ATTRIBUTION.md',
  'DATASHEET_REDISTRIBUTION_AUDIT.md',
  'PUBLIC_REPO_RISK_REGISTER.md',
  '02_HISTORY\sessions\LICENSE_ATTRIBUTION_AUDIT_SESSION.md'
)
foreach ($f in $files) {
  if (Test-Path -LiteralPath $f) { Write-Output "PASS exists $f" }
  else { Write-Output "FAIL missing $f" }
}
```

Result:

```text
PASS exists LEGAL_AND_LICENSE_AUDIT.md
PASS exists THIRD_PARTY_TOOLS_ATTRIBUTION.md
PASS exists DATASHEET_REDISTRIBUTION_AUDIT.md
PASS exists PUBLIC_REPO_RISK_REGISTER.md
PASS exists 02_HISTORY\sessions\LICENSE_ATTRIBUTION_AUDIT_SESSION.md
```

## Required Wording Check

Command:

```powershell
rg -n "requires human review|link-only recommended|Redistribution status|Recommended action|Safe public release status" LEGAL_AND_LICENSE_AUDIT.md THIRD_PARTY_TOOLS_ATTRIBUTION.md DATASHEET_REDISTRIBUTION_AUDIT.md PUBLIC_REPO_RISK_REGISTER.md
```

Result: required wording and table fields were found across the audit documents.

## Protected KiCad File Guard

Command:

```powershell
$since = [datetime]'2026-05-02T19:50:00'
Get-ChildItem -Path 04_KICAD_PROJECTS -Recurse -File -Include *.kicad_sch,*.kicad_pcb,*.kicad_pro,*.kicad_sym,*.kicad_mod -ErrorAction SilentlyContinue |
  Where-Object { $_.LastWriteTime -gt $since } |
  Select-Object FullName,LastWriteTime
```

Result: no KiCad project/source/library files were reported as modified during the audit window.

## ASCII Check

Command:

```powershell
rg -n "[^\x00-\x7F]" LEGAL_AND_LICENSE_AUDIT.md THIRD_PARTY_TOOLS_ATTRIBUTION.md DATASHEET_REDISTRIBUTION_AUDIT.md PUBLIC_REPO_RISK_REGISTER.md 02_HISTORY\sessions\LICENSE_ATTRIBUTION_AUDIT_SESSION.md
```

Result: no non-ASCII matches were reported.

## Health Check

Command:

```powershell
python health_check.py --no-write
```

Result:

```text
KiCad Engine Health Check
Repo root: C:\Users\LJ\GitHub\KICAD_ENGINE
PASS=97 WARN=0 FAIL=0
```
