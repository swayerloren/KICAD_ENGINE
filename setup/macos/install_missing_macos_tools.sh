#!/usr/bin/env bash
set -euo pipefail

APPLY=0
for arg in "$@"; do
  case "$arg" in
    --apply)
      APPLY=1
      ;;
    --dry-run)
      APPLY=0
      ;;
    -h|--help)
      cat <<'EOF'
Usage: install_missing_macos_tools.sh [--apply]

Default mode is DRY-RUN. The script prints proposed Homebrew commands and does not install anything.

Use --apply to allow install prompts. Even with --apply, each install requires typing YES.
EOF
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 2
      ;;
  esac
done

echo "KiCad Engine macOS optional installer"
echo "Default mode is DRY-RUN. Pass --apply to allow install prompts."
echo "This script asks before each install when --apply is used. It does not store API keys, collect AI credentials, modify KiCad app bundles, or install paid tools."
echo ""

if ! command -v brew >/dev/null 2>&1; then
  cat <<'EOF'
Homebrew was not found.

No tools were installed.

Manual install references:
- KiCad: https://www.kicad.org/download/macos/
- Git: https://git-scm.com/download/mac
- Python: https://www.python.org/downloads/macos/
- Node.js: https://nodejs.org/
- VS Code: https://code.visualstudio.com/
- Homebrew, optional: https://brew.sh/
EOF
  exit 2
fi

is_kicad_present() {
  command -v kicad-cli >/dev/null 2>&1 && return 0
  [ -e "/Applications/KiCad/KiCad.app" ] && return 0
  [ -x "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli" ] && return 0
  [ -e "/Applications/KiCad.app" ] && return 0
  [ -x "/Applications/KiCad.app/Contents/MacOS/kicad-cli" ] && return 0
  return 1
}

is_vscode_present() {
  command -v code >/dev/null 2>&1 && return 0
  [ -e "/Applications/Visual Studio Code.app" ] && return 0
  return 1
}

install_with_brew() {
  local name="$1"
  shift
  echo ""
  echo "Missing: $name"
  echo "Proposed command: brew install $*"
  if [ "$APPLY" -ne 1 ]; then
    echo "Dry run only. Not installing. Re-run with --apply to allow a confirmation prompt."
    return
  fi
  read -r -p "Type YES to install $name with Homebrew: " answer
  if [ "$answer" != "YES" ]; then
    echo "Skipped $name."
    return
  fi
  brew install "$@"
}

if is_kicad_present; then
  echo "KiCad appears installed."
else
  install_with_brew "KiCad" --cask kicad
fi

if command -v git >/dev/null 2>&1; then
  echo "Git appears available: $(command -v git)"
else
  install_with_brew "Git" git
fi

if command -v python3 >/dev/null 2>&1 || command -v python >/dev/null 2>&1; then
  echo "Python appears available."
else
  install_with_brew "Python" python
fi

if command -v node >/dev/null 2>&1; then
  echo "Node.js appears available: $(command -v node)"
else
  install_with_brew "Node.js" node
fi

if command -v npm >/dev/null 2>&1; then
  echo "npm appears available: $(command -v npm)"
elif command -v node >/dev/null 2>&1; then
  echo "Node.js is present but npm was not found. Review your Node installation before installing more tools."
else
  install_with_brew "npm via Node.js" node
fi

if is_vscode_present; then
  echo "VS Code appears installed."
else
  install_with_brew "Visual Studio Code" --cask visual-studio-code
fi

echo ""
echo "Optional installer finished. Restart VS Code or your terminal if PATH changed."
