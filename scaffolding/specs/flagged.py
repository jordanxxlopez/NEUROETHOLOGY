"""Print the text of every paragraph the build flagged (built slide numbers), for one lecture.

    python scaffolding/specs/flagged.py 32
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import scaffold_deck as sd  # noqa: E402
from pptx import Presentation  # noqa: E402

n = int(sys.argv[1])
log = Path(sys.argv[2]) if len(sys.argv) > 2 else None
text = log.read_text() if log else ""
prs = Presentation(str(ROOT / "scaffolded" / f"Neuroethology_Lecture{n}_FA2026_SCAFFOLDED.pptx"))
for m in re.finditer(r"built slide (\d+): paragraph (\d+): (\d+) lines", text):
    k, p = int(m.group(1)), int(m.group(2))
    c = sd.classify(prs.slides[k - 1])
    paras = [q.text for q in c["body"][0].text_frame.paragraphs if q.text.strip()]
    print(f"slide {k} p{p} ({m.group(3)} lines): {paras[p - 1]}")
