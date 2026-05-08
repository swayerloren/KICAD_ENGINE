#!/usr/bin/env python3
from validate_kicad_project import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli(["unconnected_power", "cli_availability"], "Check static power connectivity signals and ERC availability."))
