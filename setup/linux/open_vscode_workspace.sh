#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
WORKSPACE_PATH="${1:-$REPO_ROOT}"

if [ ! -d "$WORKSPACE_PATH" ]; then
  echo "Workspace path does not exist: $WORKSPACE_PATH" >&2
  exit 2
fi

if command -v code >/dev/null 2>&1; then
  code "$WORKSPACE_PATH"
  exit 0
fi

if command -v xdg-open >/dev/null 2>&1; then
  echo "VS Code command was not found. Opening folder with xdg-open."
  xdg-open "$WORKSPACE_PATH"
  exit 0
fi

cat <<EOF
VS Code was not found and xdg-open is unavailable.

Open this folder manually after installing VS Code:
$WORKSPACE_PATH

Manual install URL:
https://code.visualstudio.com/
EOF
exit 1
