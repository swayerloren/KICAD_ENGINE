# STM32 Source Link Research Commands

Date: 2026-05-03

## Commands/Tools Used

- Read required startup and STM32 context files with PowerShell.
- Used official ST web search/open results for STM32 portfolio, family pages, Nucleo/Discovery/EVAL pages, ST-LINK tools, STM32CubeMX, and representative Nucleo/product pages.
- Ran `python 03_TOOLS/scripts/datasheets/build_stm32_source_link_indexes.py --repo-root .`.
- Ran validation checks for CSV/header existence, PDF count, secret patterns, and script syntax.
- Rebuilt repo, memory, history, known-problems, and AI-quality indexes.

## Validation Notes

- Initial CSV validation command failed because it used Bash heredoc syntax in PowerShell. The check was rerun with a PowerShell here-string and passed.
- `git status` could not verify KiCad design-file cleanliness because this folder is not currently visible as a Git worktree to Git. No commands targeted `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, `.kicad_sym`, or `.kicad_mod` files.
- Final CSV validation: `STM32_OFFICIAL_SOURCE_LINKS.csv` rows `111`, `STM32_PART_NUMBER_INDEX.csv` rows `194`, `STM32_DEV_BOARD_INDEX.csv` rows `17`; required header matched all three CSV files.
- Final family document validation: `76` expected per-family documents found, `0` missing.
- Final PDF check: `0` PDF files found under the STM32 datasheet tree.
- Final targeted secret scan: `0` matches.
- Final script syntax validation: passed.
- Index rebuild commands completed successfully.

No install, clone, PDF download, KiCad CLI edit, or KiCad design-file modification commands were run.
