#!/usr/bin/env python3
from validate_kicad_project import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli(["connector_orientation"], "Find connector-like parts that require human orientation review."))
