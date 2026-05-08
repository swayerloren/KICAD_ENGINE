# Windows GUI Repos Cloned Commands

Date: 2026-04-30

## Scope

Cloned Windows GUI automation helper repositories into:

`C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos`

No installs, builds, setup scripts, KiCad GUI control, KiCad project edits, existing repo moves, or MCP permission changes were performed.

## Clone Commands

### FlaUI

```powershell
git clone https://github.com/FlaUI/FlaUI.git C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\FlaUI
```

Result:

```text
Exit code: 0
Cloning into 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\FlaUI'...
```

### FlaUInspect

```powershell
git clone https://github.com/FlaUI/FlaUInspect.git C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\FlaUInspect
```

Result:

```text
Exit code: 0
Cloning into 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\FlaUInspect'...
```

### AutoHotkey

```powershell
git clone https://github.com/AutoHotkey/AutoHotkey.git C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\AutoHotkey
```

Result:

```text
Exit code: 0
Cloning into 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\AutoHotkey'...
```

### SikuliX1

```powershell
git clone https://github.com/RaiMan/SikuliX1.git C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\SikuliX1
```

Result:

```text
Exit code: 0
Cloning into 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\repos\SikuliX1'...
```

## Inspection Commands

For each repo, the following safe inspection commands were run:

```powershell
Test-Path <repo>\.git
git -C <repo> remote get-url origin
git -C <repo> rev-parse --abbrev-ref HEAD
git -C <repo> rev-parse HEAD
git -C <repo> log -1 --pretty=%s
git -C <repo> status --short --branch
Get-ChildItem <repo> -Force -Recurse excluding .git for approximate file/folder counts
```

## Inspection Results

| Repo | `.git` exists | Remote | Branch | Commit | Status | Approx files | Approx folders |
| --- | --- | --- | --- | --- | --- | ---: | ---: |
| FlaUI | True | `https://github.com/FlaUI/FlaUI.git` | `main` | `7d600d5240ff2b8227cfcc829230cefe8116970a` | `## main...origin/main` | 464 | 55 |
| FlaUInspect | True | `https://github.com/FlaUI/FlaUInspect.git` | `main` | `c554b6fac19d3486c4fa3cbf6f37bb6d98eed1d9` | `## main...origin/main` | 104 | 19 |
| AutoHotkey | True | `https://github.com/AutoHotkey/AutoHotkey.git` | `alpha` | `7320bfffebf2eb5257990c3c24015499faaab6c8` | `## alpha...origin/alpha` | 184 | 9 |
| SikuliX1 | True | `https://github.com/RaiMan/SikuliX1.git` | `master` | `17b2f48f5fc38cdea81e6aa0fb336503c5dc0e79` | `## master...origin/master` | 538 | 88 |

## Commit Subjects

- FlaUI: `fix unsupporedexception (#704)`
- FlaUInspect: `Update image path in README for FlaUInspect`
- AutoHotkey: `Changed built-ins to return unset by default in v2.1 mode.`
- SikuliX1: `Update link for getting SikuliX ready to use`
