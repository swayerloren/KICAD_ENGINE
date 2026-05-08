import sys
from pathlib import Path

import pcbnew


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
