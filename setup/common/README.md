# Common Setup Scripts

These scripts are cross-platform helpers for preparing a local KiCad Engine checkout.

## Scripts

- `create_repo_folders.py` creates missing expected repo directories. It never deletes files.
- `build_indexes.py` creates local metadata indexes under `05_OUTPUTS/setup_indexes`. It does not download datasheets.
- `write_setup_report.py` writes a setup report under `05_OUTPUTS/setup_reports`.

## Safety

- No script installs tools.
- No script modifies KiCad project source files.
- No script writes into an installed KiCad application folder.
- No script stores API keys, passwords, tokens, or license keys.
- Generated reports are local review artifacts only.

## Typical Use

From the repo root:

```bash
python setup/common/create_repo_folders.py
python setup/common/build_indexes.py
python setup/common/write_setup_report.py --include-health-check
```

If your platform uses `python3`, replace `python` with `python3`.
