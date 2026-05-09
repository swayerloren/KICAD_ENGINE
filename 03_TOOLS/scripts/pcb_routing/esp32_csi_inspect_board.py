import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR)
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
if str(LAYOUT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(LAYOUT_SCRIPTS))

from _kicad_pcb_bridge_common import require_pcbnew_for_cli  # type: ignore  # noqa: E402


pcbnew = require_pcbnew_for_cli()


def mm(value):
    return pcbnew.ToMM(value)


def main():
    board_path = Path(sys.argv[1])
    board = pcbnew.LoadBoard(str(board_path))
    for fp in sorted(board.GetFootprints(), key=lambda f: f.GetReference()):
        pos = fp.GetPosition()
        print(f"{fp.GetReference():<4} {fp.GetValue():<24} at {mm(pos.x):7.3f},{mm(pos.y):7.3f} rot={fp.GetOrientationDegrees():7.2f} fp={fp.GetFPID().GetLibItemName()}")
        for pad in sorted(fp.Pads(), key=lambda p: p.GetNumber()):
            p = pad.GetPosition()
            print(f"  pad {pad.GetNumber():<4} {pad.GetNetname():<32} {mm(p.x):7.3f},{mm(p.y):7.3f}")


if __name__ == "__main__":
    main()
