#!/usr/bin/env python3
from validate_kicad_project import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli(["missing_3d_models"], "Check KiCad PCB 3D model references."))
