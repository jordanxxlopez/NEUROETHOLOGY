#!/usr/bin/env python3
"""Verify a scaffolded deck against scaffold/GUIDELINE.md section 10.

    python tools/check_scaffold.py <input.pptx> <output.pptx> scaffold/specs/<name>.json [--pdf out.pdf] [--json scores.json]

Checks: count, integrity of every original slide (XML, relationships, media, notes), non-redundancy
of each scaffold slide against all original slides, teaching moves, sources (numbers and
citations), language (tools/style_rules.py plus the scaffold word list), format, and PDF page
count. Prints a per-slide table and exits non-zero on any failure. Visual inspection (section
10.8) still has to be done by eye on the rendered pages.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_scaffold import NS, A, P, R, Package, classify, notes_lines, shape_text  # noqa: E402
from style_rules import framing_problems, stats_problems  # noqa: E402

MOVES = {"mechanism", "consequence", "integration", "method_logic", "distinction", "foundation"}
STOP = set("""a about above after again against all also am an and any are as at be been before being below between
both but by can could did do does doing down during each either else even ever every few for from further had has have
having he her here hers him his how however i if in into is it its itself just less like made make makes many may me
might more most much must my neither no nor not now of off on once one only onto or other others otherwise our ours out
over own per rather same several she should since so some such than that the their theirs them themselves then there
therefore these they this those though through thus to too toward towards under until up upon us very was we were what
when where whereas whether which while who whom whose why will with within without would yet you your its it's than
cannot can't does doesn't don't isn't wasn't weren't""".split())
BANNED_WORDS = [r"\billustrat\w*", r"\bdemonstrat\w*", r"\bshows? that\b", r"\bturn to\b", r"\bnext\b", r"\bkey point\b",
                r"\bas you can see\b", r"\bremember\w*", r"\bnote that\b", r"\bputting it together\b", r"\bcheckpoint\b",
                r"\bsummary\b", r"\brecap\b", r"\bteaching transcript\b", r"\blecture\s+\d+", r"\boverview\b",
                r"\bnow let'?s\b", r"\bnext we have\b", r"\bthis is important to understand\b"]
BANNED_TITLES = re.compile(r"putting it together|summary|recap|review|checkpoint|overview|key concepts|where this leads|"
                           r"how to read|introduction to|part \d+ of \d+", re.I)
CITE_RX = re.compile(r"\b([A-Z][A-Za-zÀ-ž'’-]+(?: (?:et al\.|& [A-Z][A-Za-zÀ-ž'’-]+|and [A-Z][A-Za-zÀ-ž'’-]+))?) \((1[89]\d\d|20\d\d)[a-z]?\)")
NUM_RX = re.compile(r"\d+(?:[.,]\d+)*")


def words(text):
    return re.findall(r"[a-z0-9µ°]+(?:['’][a-z]+)?", text.lower().replace("–", " ").replace("-", " "))


def content(ws, extra_stop=()):
    return [w for w in ws if w not in STOP and w not in extra_stop and len(w) > 1]


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9_*“\"(])", text) if s.strip()]


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a and b else 0.0


def longest_run(ws, ref_ngrams_by_n):
    """Longest run of consecutive words in ws that also occurs consecutively in the reference text."""
    best = 0
    n = 1
    while n <= len(ws):
        grams = ref_ngrams_by_n(n)
        if any(tuple(ws[i:i + n]) in grams for i in range(len(ws) - n + 1)):
            best = n
            n += 1
        else:
            break
    return best


def canon(xml_bytes):
    return etree.tostring(etree.fromstring(xml_bytes), method="c14n")


def slide_text(pkg, part):
    root = pkg.xml(part)
    return [shape_text(sp) for sp in root.iter(P + "sp") if sp.find(".//p:txBody", NS) is not None]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("spec")
    ap.add_argument("--pdf")
    ap.add_argument("--json", help="write per-slide scores here (for scaffold/REPORT.md)")
    a = ap.parse_args()

    spec = json.loads(Path(a.spec).read_text())
    src, out = Package(a.input), Package(a.output)
    new = spec["new_slides"]
    fails, warns = [], []

    def fail(msg):
        fails.append(msg)

    # 1. COUNT -------------------------------------------------------------------------
    n_orig = len(src.slides)
    if len(new) != 14:
        fail(f"COUNT: spec has {len(new)} scaffold slides, not 14")
    if len(out.slides) != n_orig + 14:
        fail(f"COUNT: output has {len(out.slides)} slides, expected {n_orig + 14}")
    if n_orig != 46:
        warns.append(f"COUNT: input has {n_orig} slides (not 46); output total {len(out.slides)}")

    # expected order: originals in order, each followed by its scaffold slides in spec order
    order = []
    for pos in range(1, n_orig + 1):
        order.append(("orig", pos))
        order += [("new", s) for s in new if s["after"] == pos]
    if len(order) != len(out.slides):
        fail("COUNT: slide order cannot be matched")
        order = order[:len(out.slides)]
    for s in new:
        if s["after"] < 1 or s["after"] >= n_orig:
            fail(f"PLACEMENT {s['footer_number']}: must follow a slide between the title and Key takeaways")

    # 2. INTEGRITY ---------------------------------------------------------------------
    integrity_ok = True
    for (kind, ref), opart in zip(order, out.slides):
        if kind != "orig":
            continue
        ipart = src.slides[ref - 1]
        if canon(src.parts[ipart]) != canon(out.parts[opart]):
            fail(f"INTEGRITY: original slide {ref} XML changed")
            integrity_ok = False
        irels, orels = src.rels(ipart), out.rels(opart)
        if set(irels) != set(orels):
            fail(f"INTEGRITY: original slide {ref} relationships changed")
            integrity_ok = False
            continue
        for rid, (typ, itgt) in irels.items():
            otyp, otgt = orels[rid]
            if typ != otyp:
                fail(f"INTEGRITY: slide {ref} {rid} type changed")
                integrity_ok = False
            elif typ == "notesSlide":
                if canon(src.parts[itgt]) != canon(out.parts[otgt]):
                    fail(f"INTEGRITY: original slide {ref} notes changed")
                    integrity_ok = False
            elif itgt in src.parts and src.parts[itgt] != out.parts.get(otgt):
                fail(f"INTEGRITY: original slide {ref} {typ} part {itgt} changed")
                integrity_ok = False

    # reference text of the originals
    orig = []
    for pos, part in enumerate(src.slides, start=1):
        texts = slide_text(src, part)
        notes = notes_lines(src, part)
        orig.append({"pos": part, "n": pos, "text": "\n".join(texts), "notes": "\n".join(notes), "lines": notes})
    all_orig = "\n".join(o["text"] + "\n" + o["notes"] for o in orig)
    orig_words = [words(o["text"] + " " + o["notes"]) for o in orig]
    orig_body_words = [words(o["text"]) for o in orig]
    ref_sents = []
    for o in orig:
        for s in sentences(o["text"].replace("\n", " ")) + sentences(o["notes"].replace("\n", " ")):
            ref_sents.append((o["n"], s))
    # unavoidable technical terms: spec list plus words used on at least a quarter of original slides
    df = {}
    for ws in orig_body_words:
        for w in set(content(ws)):
            df[w] = df.get(w, 0) + 1
    tech = {w for w, c in df.items() if c >= max(3, n_orig // 4)}
    tech |= {w.lower() for t in spec.get("technical_terms", []) for w in words(t)}
    gram_cache = {}

    def grams(n):
        if n not in gram_cache:
            g = set()
            for ws in orig_words:
                g.update(tuple(ws[i:i + n]) for i in range(len(ws) - n + 1))
            gram_cache[n] = g
        return gram_cache[n]

    orig_captions = set()
    for part in src.slides:
        orig_captions.update(shape_text(c) for c in classify(src.xml(part))["captions"])
    orig_refs = set()
    for o in orig:
        orig_refs.update(o["lines"])
    deck_cites = {m.group(0) for m in CITE_RX.finditer(all_orig)}
    deck_numbers = set(NUM_RX.findall(all_orig))

    # 3-7 per scaffold slide --------------------------------------------------------------
    rows = []
    used_figures = {}
    new_parts = {id(s): opart for (kind, s), opart in zip(order, out.slides) if kind == "new"}
    for s in new:
        tag = s["footer_number"]
        body = " ".join(s["body"])
        plain_body = re.sub(r"\*\*|(?<!\w)_|_(?!\w)", "", body)
        notes_items = []
        for it in s["transcript"]:
            if isinstance(it, str):
                notes_items.append(it)
            else:
                notes_items.append(it[0])
                notes_items += list(it[1])
        notes = " ".join(notes_items)
        bw, nw = words(s["title"] + " " + plain_body), words(notes)

        # 3. non-redundancy
        run = max(longest_run(bw, grams), longest_run(nw, grams))
        if run >= 8:
            fail(f"REDUNDANCY {tag}: {run}-word run copied from an original slide")
        max_sim, worst = 0.0, None
        for sent in sentences(plain_body) + sentences(notes):
            cw = content(words(sent))
            if len(cw) < 4:
                continue
            for n, rs in ref_sents:
                j = jaccard(cw, content(words(rs)))
                if j > max_sim:
                    max_sim, worst = j, (n, sent[:70])
        if max_sim >= 0.6:
            fail(f"REDUNDANCY {tag}: sentence similarity {max_sim:.2f} with original slide {worst[0]}: {worst[1]!r}")
        mine = set(content(bw, tech))
        overlap, best_slide = 0.0, None
        for o, ws in zip(orig, orig_body_words):
            ov = len(mine & set(content(ws, tech))) / len(mine) if mine else 0
            if ov > overlap:
                overlap, best_slide = ov, o["n"]
        if overlap > 0.40:
            fail(f"REDUNDANCY {tag}: {overlap:.0%} of content words also on original slide {best_slide}")
        self_sim = 0.0
        for ns_ in sentences(notes):
            for bs in sentences(plain_body):
                self_sim = max(self_sim, jaccard(content(words(ns_)), content(words(bs))))
        if self_sim >= 0.6:
            fail(f"REDUNDANCY {tag}: a notes sentence repeats a slide sentence ({self_sim:.2f})")

        # 4. teaching moves
        moves = [m for m in s.get("moves", []) if m in MOVES]
        bad = set(s.get("moves", [])) - MOVES
        if bad:
            fail(f"MOVES {tag}: unknown move(s) {sorted(bad)}")
        if len(set(moves)) < 3:
            fail(f"MOVES {tag}: {len(set(moves))} teaching moves listed; at least 3 required")
        if "integration" in moves and len(set(s.get("integrates", []))) < 2:
            fail(f"MOVES {tag}: integration needs two or more original slides in 'integrates'")

        # 5. sources
        allowed_nums = set(deck_numbers) | {str(x) for x in s.get("paper_numbers", {})}
        for num in NUM_RX.findall(plain_body + " " + notes + " " + s["title"]):
            if num not in allowed_nums:
                fail(f"SOURCE {tag}: number {num} is not in the deck (list it in 'paper_numbers' with its source)")
        for m in CITE_RX.finditer(plain_body + " " + notes + " " + s["cite"]):
            if m.group(0) not in deck_cites:
                fail(f"SOURCE {tag}: citation {m.group(0)!r} is not in the deck")
        if re.search(r"(?<![<>≤≥])=|\b[a-z]\s*[\^]\s*\d", plain_body + notes):
            fail(f"SOURCE {tag}: equation-like text")
        for ref in s["refs"]:
            if ref not in orig_refs:
                fail(f"SOURCE {tag}: reference not copied exactly from the original notes: {ref[:60]!r}")

        # 6. language
        for text, where in ((s["title"], "title"), (plain_body, "body"), (notes, "notes")):
            for why, hit in framing_problems(text):
                fail(f"LANGUAGE {tag} {where}: {why}: {hit!r}")
            for hit in stats_problems(text):
                fail(f"LANGUAGE {tag} {where}: statistics clutter {hit!r}")
            for rx in BANNED_WORDS:
                m = re.search(rx, text, re.I)
                if m:
                    fail(f"LANGUAGE {tag} {where}: {m.group(0)!r}")
            for sent in sentences(text):
                if re.match(r"[\"“(]?because\b", sent, re.I):
                    fail(f"LANGUAGE {tag} {where}: sentence begins with 'Because': {sent[:50]!r}")
        if notes_items and re.match(r"teaching transcript", notes_items[0], re.I):
            fail(f"LANGUAGE {tag}: notes start with a label")

        # 7. format
        if len(s["title"]) > 62 or s["title"].endswith("."):
            fail(f"FORMAT {tag}: title over 62 characters or ends with a period")
        if BANNED_TITLES.search(s["title"]):
            fail(f"FORMAT {tag}: banned title wording")
        nwords = len(plain_body.split())
        if not 3 <= len(s["body"]) <= 5:
            fail(f"FORMAT {tag}: {len(s['body'])} paragraphs (3-5 required)")
        if not 90 <= nwords <= 170:
            fail(f"FORMAT {tag}: {nwords} body words (90-170 required)")
        if not re.fullmatch(rf"{s['after']}[a-z]", tag):
            fail(f"FORMAT {tag}: footer number must be the original slide number plus a letter ({s['after']}a)")
        fig = s["figure"]
        if fig["from_slide"] == 1:
            fail(f"FORMAT {tag}: title-slide photo reused")
        if fig["caption"] not in orig_captions:
            fail(f"FORMAT {tag}: caption is not an original caption, character for character")
        key = (fig["from_slide"], fig["picture"])
        if key in used_figures:
            fail(f"FORMAT {tag}: figure already used on scaffold slide {used_figures[key]}")
        used_figures[key] = tag
        opart = new_parts.get(id(s))
        if opart:
            root = out.xml(opart)
            parts = classify(root)
            if not parts["pics"]:
                fail(f"FORMAT {tag}: no figure on the slide")
            if [shape_text(c) for c in parts["captions"]] != [fig["caption"]]:
                fail(f"FORMAT {tag}: slide caption does not match the spec caption")
            if shape_text(parts["number"]) != tag:
                fail(f"FORMAT {tag}: footer number box reads {shape_text(parts['number'])!r}")
            if shape_text(parts["title"]) != s["title"]:
                fail(f"FORMAT {tag}: title text mismatch")
            for rpr in root.iter(A + "rPr"):
                if rpr.get("sz") and int(rpr.get("sz")) < 1300 and any(rpr in b.iter(A + "rPr") for b in parts["body"]):
                    fail(f"FORMAT {tag}: body text below 13 pt")
            ol = notes_lines(out, opart)
            if not ol or "References:" not in ol:
                fail(f"FORMAT {tag}: notes lack References:")
            elif ol[ol.index("References:") + 1:] != s["refs"]:
                fail(f"FORMAT {tag}: notes references do not match the spec")
        rows.append({"footer": tag, "after": s["after"], "title": s["title"], "moves": moves,
                     "integrates": s.get("integrates", []), "longest_run": run, "max_sentence_sim": round(max_sim, 2),
                     "content_overlap": round(overlap, 2), "overlap_slide": best_slide, "words": nwords,
                     "figure": fig, "cited_papers_used": s.get("cited_papers_used", [])})

    # placement: no two scaffold slides in a row unless the spec says so
    afters = [s["after"] for s in new]
    for pos in set(afters):
        if afters.count(pos) > 1 and not all(s.get("consecutive_ok") for s in new if s["after"] == pos):
            warns.append(f"PLACEMENT: {afters.count(pos)} scaffold slides in a row after slide {pos}")

    # 9. PDF ---------------------------------------------------------------------------
    if a.pdf:
        info = subprocess.run(["pdfinfo", a.pdf], capture_output=True, text=True).stdout
        pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
        if pages != len(out.slides):
            fail(f"PDF: {pages} pages, expected {len(out.slides)}")

    # report -----------------------------------------------------------------------------
    print(f"{Path(a.output).name}: {len(out.slides)} slides; integrity {'identical' if integrity_ok else 'CHANGED'}")
    print(f"{'#':>5}  {'moves':<46} {'run':>3} {'sim':>5} {'ovl':>5} {'wds':>4}  title")
    for r in rows:
        print(f"{r['footer']:>5}  {','.join(r['moves']):<46} {r['longest_run']:>3} {r['max_sentence_sim']:>5.2f} "
              f"{r['content_overlap']:>5.2f} {r['words']:>4}  {r['title']}")
    for w in warns:
        print("WARN", w)
    for f in fails:
        print("FAIL", f)
    if a.json:
        Path(a.json).write_text(json.dumps({"slides": len(out.slides), "integrity": integrity_ok, "rows": rows,
                                            "fails": fails, "warnings": warns}, indent=1, ensure_ascii=False))
    print("PASS" if not fails else f"{len(fails)} failure(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
