#!/usr/bin/env bash
set -euo pipefail

apply=0
categories=("kicad" "fab" "visual")

while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply)
      apply=1
      shift
      ;;
    --category)
      categories=("$2")
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tool_root="$repo_root/.tools"
venv_root="$tool_root/venvs"

requirements_for() {
  case "$1" in
    kicad) echo "requirements-kicad-tools.txt" ;;
    fab) echo "requirements-fab-tools.txt" ;;
    visual) echo "requirements-visual-tools.txt" ;;
    *) return 1 ;;
  esac
}

step() {
  local message="$1"
  echo "$message"
  if [[ "$apply" -eq 0 ]]; then
    echo "DRY_RUN: $message"
  fi
}

install_category() {
  local category="$1"
  local requirements_file
  requirements_file="$(requirements_for "$category")"
  local requirements_path="$repo_root/$requirements_file"
  local venv_path="$venv_root/$category"

  [[ -f "$requirements_path" ]] || { echo "Missing $requirements_path" >&2; exit 1; }

  step "Create venv $venv_path"
  if [[ "$apply" -eq 1 ]]; then
    python3 -m venv "$venv_path"
    "$venv_path/bin/python" -m pip install --upgrade pip
    "$venv_path/bin/python" -m pip install -r "$requirements_path"
  fi
}

echo "KiCad Engine optional-tool installer"
echo "Repo root: $repo_root"
echo "Apply mode: $apply"
echo "Categories: ${categories[*]}"
echo "External-only tools remain manual: pcbnew runtime, freerouting, kicad-routing-tools, kicad-component-layout, kicad-library-utils"

if [[ "$apply" -eq 1 ]]; then
  mkdir -p "$venv_root"
fi

for category in "${categories[@]}"; do
  install_category "$category"
done

echo "Verification command: python3 setup/verify_optional_kicad_tools.py --dry-run"
