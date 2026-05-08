#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OFFER_INSTALL="false"
SKIP_INDEXES="false"
SKIP_HEALTH="false"

for arg in "$@"; do
  case "$arg" in
    --offer-install) OFFER_INSTALL="true" ;;
    --skip-indexes) SKIP_INDEXES="true" ;;
    --skip-health-check) SKIP_HEALTH="true" ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python was not found on PATH. Setup cannot run common helpers." >&2
  exit 2
fi

echo "KiCad Engine macOS setup"
echo "Repo root: $REPO_ROOT"
echo "This script does not install tools unless --offer-install is used and you confirm each install."

if [ "$OFFER_INSTALL" = "true" ]; then
  "$SCRIPT_DIR/install_missing_macos_tools.sh" --apply
fi

"$PYTHON_BIN" "$REPO_ROOT/setup/common/create_repo_folders.py" --repo-root "$REPO_ROOT"

if [ "$SKIP_INDEXES" != "true" ]; then
  "$PYTHON_BIN" "$REPO_ROOT/setup/common/build_indexes.py" --repo-root "$REPO_ROOT"
fi

if [ "$SKIP_HEALTH" != "true" ]; then
  "$PYTHON_BIN" "$REPO_ROOT/health_check.py" --repo-root "$REPO_ROOT"
fi

"$PYTHON_BIN" "$REPO_ROOT/setup/common/write_setup_report.py" --repo-root "$REPO_ROOT"

echo "macOS setup completed. Review reports under 05_OUTPUTS before trusting the environment."
