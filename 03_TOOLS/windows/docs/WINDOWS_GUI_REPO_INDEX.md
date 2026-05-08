# Windows GUI Repo Index

Date: 2026-04-30

These repositories were cloned locally for Windows GUI automation reference and future tooling experiments. They were not installed, built, or used to control KiCad. They are optional local-only references, not required for a basic clone-or-ZIP workflow.

Repository root:

`03_TOOLS/windows/repos`

## Safety Rules

- Do not modify third-party repo files.
- Do not build or install these repos unless explicitly requested.
- Do not use these repos to control KiCad until a future gated task approves a specific experiment.
- Prefer passive window discovery and screenshots before any GUI control.
- Keep existing legacy repos under `03_TOOLS\repos`; no existing repos were moved during this clone task.

## Repository Summary

| Repo | Local path | Source URL | Branch | Commit | `.git` | Approx files | Approx folders | Status | Purpose |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| FlaUI | `03_TOOLS\windows\repos\FlaUI` | `https://github.com/FlaUI/FlaUI.git` | `main` | `7d600d5240ff2b8227cfcc829230cefe8116970a` | Yes | 464 | 55 | CLONED_NOT_INSTALLED | .NET UI Automation library reference for structured Windows desktop automation. |
| FlaUInspect | `03_TOOLS\windows\repos\FlaUInspect` | `https://github.com/FlaUI/FlaUInspect.git` | `main` | `c554b6fac19d3486c4fa3cbf6f37bb6d98eed1d9` | Yes | 104 | 19 | CLONED_NOT_INSTALLED | UI Automation inspection tool reference for Windows control-tree exploration. |
| AutoHotkey | `03_TOOLS\windows\repos\AutoHotkey` | `https://github.com/AutoHotkey/AutoHotkey.git` | `alpha` | `7320bfffebf2eb5257990c3c24015499faaab6c8` | Yes | 184 | 9 | CLONED_NOT_BUILT | Windows hotkey and scripting engine source reference. |
| SikuliX1 | `03_TOOLS\windows\repos\SikuliX1` | `https://github.com/RaiMan/SikuliX1.git` | `master` | `17b2f48f5fc38cdea81e6aa0fb336503c5dc0e79` | Yes | 538 | 88 | CLONED_NOT_INSTALLED | Image-driven GUI automation reference for future visual workflow experiments. |

## Git Status

```text
FlaUI:        ## main...origin/main
FlaUInspect: ## main...origin/main
AutoHotkey:  ## alpha...origin/alpha
SikuliX1:    ## master...origin/master
```

No build, install, setup, or GUI control commands were run.
