"""Print every filler-flagged or short body paragraph of one built lecture, with its spec key.

    python scaffolding/specs/flagged_text.py 33
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import check_paragraphs as cp  # noqa: E402
from pptx import Presentation  # noqa: E402

n = int(sys.argv[1])
spec = importlib.util.spec_from_file_location(f"L{n}", Path(__file__).parent / f"L{n}.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
after = sorted(i["after"] for i in m.inserts)
table, b = {}, 1
for orig in range(2, 47):
    b += 1
    table[b] = ("body", orig)
    if orig in after:
        b += 1
        table[b] = ("insert", orig)
prs = Presentation(str(ROOT / "scaffolded" / f"Neuroethology_Lecture{n}_FA2026_SCAFFOLDED.pptx"))
for k, slide in enumerate(prs.slides, 1):
    if k in (1, len(prs.slides)):
        continue
    paras = cp.body_paragraphs(slide)
    if not paras:
        continue
    for i, para in enumerate(paras, 1):
        if cp.filler_hits(para.text):
            print(table.get(k), f"p{i}", "\n   ", para.text)
