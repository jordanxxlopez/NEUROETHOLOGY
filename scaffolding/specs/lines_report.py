"""Rendered line counts for the body and insert texts of one lecture spec (scaffolding/RULES.md).

    python scaffolding/specs/lines_report.py 31
Prints the paragraphs that fall outside 5-7 lines, keyed by the original slide number.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import scaffold_deck as sd  # noqa: E402

PT = 15.0
BODY_W = int(5.99 * 914400 * sd.WRAP_FACTOR)     # left-column box width at 15 pt
INS_W = int(5.99 * 914400 * sd.WRAP_FACTOR)


def count(text, width=BODY_W):
    return sd.wrap_lines(sd.PLAIN.sub("", text), width, PT)


def main(n):
    sys.path.insert(0, str(Path(__file__).parent))
    body = importlib.import_module(f"body_L{n}").body
    spec = importlib.util.spec_from_file_location(f"L{n}", Path(__file__).parent / f"L{n}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for k in sorted(body):
        for i, t in enumerate(body[k], 1):
            lines = count(t)
            if not 5 <= lines <= 7:
                print(f"body {k} p{i}: {lines} lines, {len(t.split())} words")
    for ins in m.inserts:
        for i, t in enumerate(ins["paragraphs"], 1):
            lines = count(t)
            if not 5 <= lines <= 7:
                print(f"insert after {ins['after']} p{i}: {lines} lines, {len(t.split())} words")


if __name__ == "__main__":
    main(int(sys.argv[1]))
