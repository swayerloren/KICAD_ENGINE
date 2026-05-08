#!/usr/bin/env python3
from validate_kicad_project import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli(["bom_datasheets"], "Check schematic BOM components for datasheet evidence."))
