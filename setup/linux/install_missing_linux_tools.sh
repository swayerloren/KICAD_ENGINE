#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
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
Usage: install_missing_linux_tools.sh [--apply]

Default mode is DRY-RUN. The script prints proposed package-manager commands and does not install anything.

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

echo "KiCad Engine Linux optional installer"
echo "Default mode is DRY-RUN. Pass --apply to allow install prompts."
echo "This script asks before each install when --apply is used. It does not collect credentials, modify global KiCad libraries, or install paid tools."
echo "For package managers that require root, run this script as root only after reviewing the commands."
echo ""

if ! DETECTED_MANAGER="$("$SCRIPT_DIR/detect_linux_package_manager.sh" --best-id 2>/dev/null)"; then
  DETECTED_MANAGER=""
fi

manual_instructions() {
  cat <<'EOF'
Manual install references:
- KiCad: https://www.kicad.org/download/linux/
- Git: https://git-scm.com/download/linux
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/
- VS Code: https://code.visualstudio.com/
EOF
}

if [ -z "$DETECTED_MANAGER" ]; then
  echo "No supported package manager was detected."
  manual_instructions
  exit 2
fi

echo "Detected package manager: $DETECTED_MANAGER"

is_command_present() {
  command -v "$1" >/dev/null 2>&1
}

confirm() {
  local label="$1"
  shift
  echo ""
  echo "Proposed install for $label:"
  printf '  %q' "$@"
  echo ""
  if [ "$APPLY" -ne 1 ]; then
    echo "Dry run only. Not installing. Re-run with --apply to allow a confirmation prompt."
    return 1
  fi
  read -r -p "Type YES to run this command: " answer
  [ "$answer" = "YES" ]
}

run_root_command_or_print() {
  local label="$1"
  shift
  if ! confirm "$label" "$@"; then
    echo "Skipped $label."
    return
  fi
  if [ "${EUID:-$(id -u)}" -ne 0 ]; then
    echo "Root privileges are required for this package manager."
    echo "No command was run. Review and run manually if appropriate:"
    printf '  sudo'
    printf ' %q' "$@"
    echo ""
    return
  fi
  "$@"
}

run_user_command() {
  local label="$1"
  shift
  if confirm "$label" "$@"; then
    "$@"
  else
    echo "Skipped $label."
  fi
}

install_package() {
  local label="$1"
  local command_name="$2"
  local apt_pkg="$3"
  local dnf_pkg="$4"
  local yum_pkg="$5"
  local pacman_pkg="$6"
  local flatpak_ref="$7"
  local snap_pkg="$8"

  if is_command_present "$command_name"; then
    echo "$label already appears available: $(command -v "$command_name")"
    return
  fi

  case "$DETECTED_MANAGER" in
    apt)
      run_root_command_or_print "$label update" apt-get update
      run_root_command_or_print "$label" apt-get install -y $apt_pkg
      ;;
    dnf)
      run_root_command_or_print "$label" dnf install -y $dnf_pkg
      ;;
    yum)
      run_root_command_or_print "$label" yum install -y $yum_pkg
      ;;
    pacman)
      run_root_command_or_print "$label" pacman -S --needed --noconfirm $pacman_pkg
      ;;
    flatpak)
      if [ -n "$flatpak_ref" ]; then
        run_user_command "$label" flatpak install --user -y flathub "$flatpak_ref"
      else
        echo "$label is not available through the configured Flatpak fallback. Use manual install instructions."
      fi
      ;;
    snap)
      if [ -n "$snap_pkg" ]; then
        run_root_command_or_print "$label" snap install $snap_pkg
      else
        echo "$label is not available through the configured snap fallback. Use manual install instructions."
      fi
      ;;
    *)
      echo "Unsupported package manager: $DETECTED_MANAGER"
      manual_instructions
      exit 2
      ;;
  esac
}

install_package "KiCad" "kicad-cli" "kicad" "kicad" "kicad" "kicad" "org.kicad.KiCad" "kicad"
install_package "Git" "git" "git" "git" "git" "git" "" "git"
install_package "Python" "python3" "python3" "python3" "python3" "python" "" "python"
install_package "Node.js" "node" "nodejs npm" "nodejs npm" "nodejs npm" "nodejs npm" "" "node --classic"
install_package "npm" "npm" "npm" "npm" "npm" "npm" "" "node --classic"
install_package "Visual Studio Code" "code" "code" "code" "code" "code" "com.visualstudio.code" "code --classic"

echo ""
echo "Optional installer finished. Restart VS Code or your terminal if PATH changed."
