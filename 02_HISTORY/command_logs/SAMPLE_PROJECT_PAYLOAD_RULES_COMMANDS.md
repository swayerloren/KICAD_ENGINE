# Command Log - Sample Project Payload Rules

Date: `2026-05-06`

## Commands Run

### Inspect release folder

```powershell
Get-ChildItem -Force 17_RELEASE_BUILD | Select-Object Mode,Length,LastWriteTime,Name
```

Result: release folder existed; `PAYLOAD_ALLOWLIST.md`,
`PAYLOAD_EXCLUDE_RULES.md`, `PUBLIC_PAYLOAD_MANIFEST.md`, and
`build_public_payload.py` were missing.

### Read required sample and license context

```powershell
Get-Content -Raw '32_OPEN_KICAD_SAMPLE_INTAKE\INDEX.md'
Get-Content -Raw '19_TEST_PROJECTS\SAMPLE_PROJECTS_INDEX.md'
Get-Content -Raw '19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\ORIGINAL_SOURCE_ATTRIBUTION.md'
Get-Content -Raw '19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\GOLDEN_PATH_DEMO_STATUS.md'
Get-Content -Raw '21_LICENSE_ATTRIBUTION\LICENSE_AUDIT.md'
Get-Content -Raw '17_RELEASE_BUILD\PUBLIC_RELEASE_EXCLUSION_MANIFEST.md'
```

Result: files read. The ATtiny85 sample has MIT license evidence but remains
`PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW` and
`BLOCKED_UNTIL_HUMAN_REVIEW`.

### Inspect builder status

```powershell
if (Test-Path '17_RELEASE_BUILD\build_public_payload.py') { Get-Content -Raw '17_RELEASE_BUILD\build_public_payload.py' } else { 'MISSING: 17_RELEASE_BUILD\build_public_payload.py' }
Get-Content -Raw 'installer\payload\build_payload.py'
```

Result: public payload builder missing. Installer payload builder exists but is
not the requested public sample payload builder and has no dry-run flag.

### Failed validation attempts

```powershell
$paths = @(...); foreach ($p in $paths) { [pscustomobject]@{Path=$p; Exists=(Test-Path $p)} } | Format-Table -AutoSize
```

Result: failed due PowerShell empty pipe element after a `foreach` statement.
Rerun with `$results = foreach (...) { ... }; $results | Format-Table`.

```powershell
rg -n "<secret-assignment-regex>" 17_RELEASE_BUILD FOR\ CHAT\ GPT.MD
```

Result: failed due PowerShell quoting. Rerun with a PowerShell `$pattern`
variable and `Select-String`.

```powershell
git status --short -- '17_RELEASE_BUILD' '05_OUTPUTS/release_readiness' '02_HISTORY/sessions' '02_HISTORY/command_logs' 'FOR CHAT GPT.MD'
```

Result: failed because this checkout does not expose `.git` metadata to the
current shell: `fatal: not a git repository`.

### Presence validation rerun

```powershell
$paths = @(
  '17_RELEASE_BUILD\PAYLOAD_ALLOWLIST.md',
  '17_RELEASE_BUILD\PAYLOAD_EXCLUDE_RULES.md',
  '17_RELEASE_BUILD\PUBLIC_PAYLOAD_MANIFEST.md',
  '17_RELEASE_BUILD\PUBLIC_RELEASE_EXCLUSION_MANIFEST.md',
  '17_RELEASE_BUILD\SAMPLE_PROJECT_PAYLOAD_POLICY.md',
  '17_RELEASE_BUILD\build_public_payload.py',
  '05_OUTPUTS\release_readiness',
  '02_HISTORY\sessions',
  '02_HISTORY\command_logs'
)
$results = foreach ($p in $paths) { [pscustomobject]@{Path=$p; Exists=(Test-Path $p)} }
$results | Format-Table -AutoSize
```

Result: required policy/report folders exist; `build_public_payload.py` is
missing.

### Targeted secret scan

```powershell
$pattern = '<secret-assignment-regex>'
Get-ChildItem '17_RELEASE_BUILD' -File -Filter '*.md' | Select-String -Pattern $pattern
Select-String -Path 'FOR CHAT GPT.MD' -Pattern $pattern
```

Result: no matches.

### Read-only KiCad sample source inventory

```powershell
$sample = '19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board'
Get-ChildItem -Recurse -File $sample -Include *.kicad_pro,*.kicad_sch,*.kicad_pcb,*.kicad_mod |
  Select-Object @{Name='Path';Expression={$_.FullName.Replace((Get-Location).Path + '\','')}},LastWriteTime,Length |
  Sort-Object Path | Format-Table -AutoSize
```

Result: read-only inventory only; no KiCad design files were edited.

### Public payload dry-run

```powershell
if (Test-Path '17_RELEASE_BUILD\build_public_payload.py') { 'PUBLIC_BUILDER_EXISTS' } else { 'PUBLIC_BUILDER_MISSING_NO_DRY_RUN_EXECUTED' }
if (Test-Path 'installer\payload\build_payload.py') { 'INSTALLER_PAYLOAD_BUILDER_EXISTS_NO_DRY_RUN_FLAG_CONFIRMED_BY_READ' }
```

Result: no public dry-run builder exists; no dry-run payload build executed.

### Current known problems refresh

```powershell
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
python -m py_compile 03_TOOLS\scripts\indexing\build_known_problems.py
```

Result: completed successfully. `00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md`
now references the open issue
`02_HISTORY\issue_logs\SAMPLE_PROJECT_PUBLIC_PAYLOAD_BLOCKED_PENDING_REVIEW.md`.

### Final targeted secret scan

```powershell
Select-String -Path <changed-files> -Pattern <secret-assignment-regex>
```

Result: no matches after replacing literal regex text in this command log with
a placeholder to avoid false positive matches.

### Failed-attempt record and known-problems refresh

```powershell
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
```

Result: completed successfully after creating
`02_HISTORY\failed_attempts\SAMPLE_PROJECT_PAYLOAD_RULES_VALIDATION_COMMAND_FAILURES.md`.
