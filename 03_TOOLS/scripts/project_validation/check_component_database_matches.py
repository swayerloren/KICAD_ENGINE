#!/usr/bin/env python3
from validate_kicad_project import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli(["component_database_matches"], "Check schematic component values against the component database."))
