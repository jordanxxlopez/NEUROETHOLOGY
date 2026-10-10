#!/usr/bin/env python3
"""Insert 14 scaffold slides into a finished lecture deck without touching the original slides.

    python tools/add_scaffold.py <input.pptx> scaffold/specs/<name>.json -o scaffold/output/<name>_SCAFFOLDED.pptx

Rules: scaffold/GUIDELINE.md. The deck is edited at the package (zip) level: every part of the
input is copied byte for byte, new slide / notes parts are added, and only ppt/presentation.xml,
its relationships and [Content_Types].xml are rewritten (to register the new slides and order
them in <p:sldIdLst>). Original slide parts, their notes and their media are never written.

Each new slide is a clone of `template_slide` (same deck): its title, body, citation and
slide-number boxes keep their XML formatting; only the text runs are replaced. The template's
own picture(s) and caption(s) are dropped, and the named picture from `figure.from_slide` is
copied in with its original placement and its original caption shape. Optional
`extra_figures` (same keys as `figure`) copy further pictures the same way, e.g. the anatomy
panel that a run of the deck's own slides carries beside the main figure.
"""
import argparse
import copy
import json
import math
import posixpath
import re
import subprocess
import sys
import zipfile
from pathlib import Path

from lxml import etree

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
}
A, P, R = "{%s}" % NS["a"], "{%s}" % NS["p"], "{%s}" % NS["r"]
REL_T = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/"
SLIDE_CT = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
NOTES_CT = "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"
EMU_PER_PT = 12700


# ------------------------------------------------------------------ package helpers
class Package:
    """Read-only view of a .pptx: parts as bytes, slide order resolved from presentation.xml."""

    def __init__(self, path):
        with zipfile.ZipFile(path) as z:
            self.names = z.namelist()
            self.parts = {n: z.read(n) for n in self.names}
        pres = etree.fromstring(self.parts["ppt/presentation.xml"])
        rels = self.rels("ppt/presentation.xml")
        self.slides = []  # part names in presentation order
        for sid in pres.find("p:sldIdLst", NS):
            self.slides.append(rels[sid.get(R + "id")][1])

    def rels(self, part):
        """{rId: (type, absolute target part name)} for a part."""
        d, b = posixpath.split(part)
        rp = posixpath.join(d, "_rels", b + ".rels")
        out = {}
        if rp not in self.parts:
            return out
        for r in etree.fromstring(self.parts[rp]):
            tgt = r.get("Target")
            if r.get("TargetMode") != "External":
                tgt = posixpath.normpath(posixpath.join(d, tgt))
            out[r.get("Id")] = (r.get("Type").rsplit("/", 1)[-1], tgt)
        return out

    def notes_part(self, slide_part):
        for typ, tgt in self.rels(slide_part).values():
            if typ == "notesSlide":
                return tgt
        return None

    def xml(self, part):
        return etree.fromstring(self.parts[part])


def shape_text(el):
    return "\n".join("".join(t.text or "" for t in p.iter(A + "t")) for p in el.iter(A + "p"))


def notes_lines(pkg, slide_part):
    """Speaker-note text of a slide as a list of lines (paragraphs and line breaks both split)."""
    np_ = pkg.notes_part(slide_part)
    if not np_:
        return []
    root = pkg.xml(np_)
    lines = []
    for sp in root.iter(P + "sp"):
        ph = sp.find(".//p:nvPr/p:ph", NS)
        if ph is None or ph.get("type") != "body":
            continue
        for para in sp.iter(A + "p"):
            cur = ""
            for el in para:
                if el.tag == A + "r":
                    cur += "".join(t.text or "" for t in el.iter(A + "t"))
                elif el.tag == A + "br":
                    lines.append(cur)
                    cur = ""
            lines.append(cur)
    lines = [part for l in lines for part in l.split("\n")]
    return [l.strip() for l in lines if l.strip()]


def classify(slide_root):
    """Split a content slide's shapes into title, body boxes, pictures, captions, cite, number."""
    sps = [el for el in slide_root.find(".//p:spTree", NS) if el.tag in (P + "sp", P + "pic")]

    def geom(el):
        off = el.find(".//a:xfrm/a:off", NS)
        ext = el.find(".//a:xfrm/a:ext", NS)
        return int(off.get("x")), int(off.get("y")), int(ext.get("cx")), int(ext.get("cy"))

    pics = [el for el in sps if el.tag == P + "pic"]
    texts = [el for el in sps if el.tag == P + "sp" and el.find(".//p:txBody", NS) is not None]
    texts = [el for el in texts if shape_text(el).strip()]
    title = min(texts, key=lambda e: geom(e)[1])
    footer_y = max(geom(e)[1] for e in texts)
    footer = [e for e in texts if geom(e)[1] == footer_y]
    number = max(footer, key=lambda e: geom(e)[0])
    cite = min(footer, key=lambda e: geom(e)[0]) if len(footer) > 1 else None
    rest = [e for e in texts if e is not title and e not in footer]
    captions = [e for e in rest if re.match(r"^[^()]{2,120}?\((?:19|20)\d{2}[a-z]?\),\s*(Fig|Figs|Figure)", shape_text(e))
                or re.match(r"^(Photo|Image|Specimen|Micrograph):", shape_text(e))]
    body = sorted([e for e in rest if e not in captions], key=lambda e: geom(e)[1])
    return dict(title=title, body=body, pics=pics, captions=captions, cite=cite, number=number, geom=geom)


# ------------------------------------------------------------------ text helpers
MARK = re.compile(r"(\*\*.+?\*\*|_[^_]+?_)")


def set_paragraph(p, text, base_rpr, bold_rpr=None):
    """Replace the runs of paragraph p with text; **bold** and _italic_ markup become run attributes."""
    for r in p.findall(A + "r") + p.findall(A + "br") + p.findall(A + "fld"):
        p.remove(r)
    end = p.find(A + "endParaRPr")
    for piece in MARK.split(text):
        if not piece:
            continue
        b, i = base_rpr.get("b", "0"), base_rpr.get("i", "0")
        if piece.startswith("**") and piece.endswith("**"):
            piece, b = piece[2:-2], "1"
        elif piece.startswith("_") and piece.endswith("_") and len(piece) > 2:
            piece, i = piece[1:-1], "1"
        r = etree.Element(A + "r")
        rpr = copy.deepcopy(bold_rpr if (b == "1" and bold_rpr is not None and base_rpr.get("b") != "1") else base_rpr)
        rpr.set("b", b)
        rpr.set("i", i)
        r.append(rpr)
        t = etree.SubElement(r, A + "t")
        t.text = piece
        if end is not None:
            end.addprevious(r)
        else:
            p.append(r)


def set_shape_text(sp, paragraphs, plain_rpr=None, bold_fallback=None):
    """Write paragraphs into a text shape, reusing its first paragraph's pPr and its plain run rPr."""
    body = sp.find(".//p:txBody", NS)
    paras = body.findall(A + "p")
    first = paras[0]
    runs = first.findall(A + "r")
    rprs = [r.find(A + "rPr") for r in body.iter(A + "r") if r.find(A + "rPr") is not None]
    plain_rprs = [x for x in rprs if x.get("b") != "1" and x.get("i") != "1"] or [x for x in rprs if x.get("b") != "1"]
    plain = plain_rprs[0].getparent() if plain_rprs else runs[0]
    rpr = copy.deepcopy(plain_rpr if plain_rpr is not None else plain.find(A + "rPr"))
    bold = next((r for r in body.iter(A + "rPr") if r.get("b") == "1"), None)
    if bold is not None:
        bold = copy.deepcopy(bold)
    elif bold_fallback is not None:  # template has no bold run: plain formatting in the deck's bold color
        bold = copy.deepcopy(rpr)
        bold.set("b", "1")
        fill = bold_fallback.find(A + "solidFill")
        if fill is not None:
            for old_fill in bold.findall(A + "solidFill"):
                bold.remove(old_fill)
            bold.insert(0, copy.deepcopy(fill))
    for extra in paras:
        body.remove(extra)
    for k, text in enumerate(paragraphs):  # paragraph k reuses the template's paragraph k (spacing before/after)
        p = copy.deepcopy(paras[min(k, len(paras) - 1)] if k else first)
        set_paragraph(p, text, rpr, bold)
        body.append(p)


def strip_markup(s):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", re.sub(r"(?<!\w)_([^_]+?)_(?!\w)", r"\1", s))


def body_font_pt(sp, default_pt):
    for r in sp.iter(A + "rPr"):
        if r.get("sz"):
            return int(r.get("sz")) / 100
    return default_pt


def line_spacing(sp):
    v = sp.find(".//a:lnSpc/a:spcPct", NS)
    return int(v.get("val")) / 100000 if v is not None else 1.0


def line_height_pt(sp, pt):
    """Height of one text line: an exact spacing (spcPts) if the box sets one, else 1.2 x size x percentage."""
    exact = sp.find(".//a:lnSpc/a:spcPts", NS)
    if exact is not None:
        return int(exact.get("val")) / 100
    return pt * 1.2 * line_spacing(sp)


def estimate_lines(text, width_emu, pt):
    """Lines a paragraph wraps to: rendered Arial body text averages ~0.44 em (0.46 leaves a margin) per character."""
    chars_per_line = max(1, int(width_emu / EMU_PER_PT / (pt * 0.46)))
    words, lines, cur = strip_markup(text).split(), 1, 0
    for w in words:
        add = len(w) + (1 if cur else 0)
        if cur + add > chars_per_line:
            lines, cur = lines + 1, len(w)
        else:
            cur += add
    return lines


# ------------------------------------------------------------------ build
def default_font_pt(pkg):
    pres = pkg.xml("ppt/presentation.xml")
    d = pres.find(".//p:defaultTextStyle/a:lvl1pPr/a:defRPr", NS)
    return int(d.get("sz")) / 100 if d is not None and d.get("sz") else 18.0


def deck_body_bottom(pkg):
    """Lowest body-text edge used on the deck's own content slides (title and takeaways excluded)."""
    bottoms = []
    for part in pkg.slides[1:-1]:
        try:
            c = classify(pkg.xml(part))
        except (ValueError, AttributeError):
            continue
        footer_top = c["geom"](c["number"])[1]
        bottoms += [c["geom"](b)[1] + c["geom"](b)[3] for b in c["body"]
                    if c["geom"](b)[1] + c["geom"](b)[3] < footer_top]
    return max(bottoms) if bottoms else None


def build_slide(pkg, spec_slide, slide_w, default_pt, body_floor=None):
    tpart = pkg.slides[spec_slide["template_slide"] - 1]
    root = copy.deepcopy(pkg.xml(tpart))
    parts = classify(root)
    geom = parts["geom"]
    tree = root.find(".//p:spTree", NS)

    # title
    set_shape_text(parts["title"], [spec_slide["title"]])

    deck_bold = None
    for part in pkg.slides[1:-1]:
        try:
            for bx in classify(pkg.xml(part))["body"]:
                deck_bold = next((r for r in bx.iter(A + "rPr") if r.get("b") == "1"), None)
                if deck_bold is not None:
                    break
        except (ValueError, AttributeError):
            continue
        if deck_bold is not None:
            break
    # body: one paragraph per template body box (boxes restacked to fit), or, when the template
    # keeps all paragraphs in one box, every paragraph in that box with its own paragraph spacing
    boxes = parts["body"]
    paras = spec_slide["body"]
    if spec_slide.get("source_line"):  # older decks print the full reference in a line under the title
        set_shape_text(boxes[0], [spec_slide["source_line"]])
        boxes = boxes[1:]
    top = geom(boxes[0])[1]
    bottom = max(geom(b)[1] + geom(b)[3] for b in boxes)
    if body_floor:  # body text may extend as low as the deck's own content slides place it,
        # keeping a quarter inch clear of the footer
        bottom = max(bottom, min(body_floor, geom(parts["number"])[1] - 228600))
    if len(boxes) == 1 and len(paras) > 1:
        b = boxes[0]
        pt = body_font_pt(b, default_pt)
        aft = b.find(".//a:pPr/a:spcAft/a:spcPts", NS)
        after = int(aft.get("val")) / 100 * EMU_PER_PT if aft is not None else 0
        tparas = list(b.iter(A + "p"))
        bef = tparas[1].find("./a:pPr/a:spcBef/a:spcPts", NS) if len(tparas) > 1 else None
        after += int(bef.get("val")) / 100 * EMU_PER_PT if bef is not None else 0
        h = sum(int(math.ceil(estimate_lines(t, geom(b)[2], pt) * line_height_pt(b, pt) * EMU_PER_PT)) for t in paras)
        h += int(after * (len(paras) - 1))
        print(f"  {spec_slide['footer_number']:>4}: body {h / 914400:.2f} of {(bottom - top) / 914400:.2f} in")
        if h > bottom - top:
            raise SystemExit(f"slide {spec_slide['footer_number']}: body text does not fit "
                             f"({(h - bottom + top) / 914400:.2f} in over); shorten it")
        set_shape_text(b, paras, bold_fallback=deck_bold)
        b.find(".//a:xfrm/a:ext", NS).set("cy", str(h))
    else:
        if len(paras) > len(boxes):
            raise SystemExit(f"slide {spec_slide['footer_number']}: {len(paras)} paragraphs but template "
                             f"slide {spec_slide['template_slide']} has {len(boxes)} body boxes")
        for extra in boxes[len(paras):]:
            tree.remove(extra)
        boxes = boxes[:len(paras)]
        heights = []
        for b, text in zip(boxes, paras):
            pt = body_font_pt(b, default_pt)
            n = estimate_lines(text, geom(b)[2], pt)
            heights.append(int(math.ceil(n * line_height_pt(b, pt) * EMU_PER_PT)))
        free = bottom - top - sum(heights)
        print(f"  {spec_slide['footer_number']:>4}: body {sum(heights) / 914400:.2f} of {(bottom - top) / 914400:.2f} in")
        if free < 0:
            raise SystemExit(f"slide {spec_slide['footer_number']}: body text does not fit "
                             f"({-free / 914400:.2f} in over); shorten it")
        gap = free / max(1, len(boxes) - 1) if len(boxes) > 1 else 0
        gap = min(gap, 0.45 * 914400)
        y = top
        for b, text, h in zip(boxes, paras, heights):
            set_shape_text(b, [text], bold_fallback=deck_bold)
            b.find(".//a:xfrm/a:off", NS).set("y", str(int(y)))
            b.find(".//a:xfrm/a:ext", NS).set("cy", str(h))
            y += h + gap

    # figures: drop the template's pictures and captions, copy the named picture(s) with their captions;
    # a text-only slide (figure null, for decks whose content slides carry no figures) keeps the
    # template's own decorative icon, exactly as the deck's text slides do
    figs = ([spec_slide["figure"]] if spec_slide.get("figure") else []) + spec_slide.get("extra_figures", [])
    if figs:
        for el in parts["pics"] + parts["captions"]:
            tree.remove(el)
    anchor = parts["cite"] if parts["cite"] is not None else parts["number"]
    images = {}  # temporary rId -> media part
    if not figs:  # kept template icons point at the template's own relationships
        trels_ = pkg.rels(tpart)
        for pic in parts["pics"]:
            for blip in pic.iter(A + "blip"):
                tmp = f"keep_{blip.get(R + 'embed')}"
                images[tmp] = trels_[blip.get(R + "embed")][1]
                blip.set(R + "embed", tmp)
    for k, fig in enumerate(figs):
        src_part = pkg.slides[fig["from_slide"] - 1]
        fparts = classify(pkg.xml(src_part))
        pic = next((e for e in fparts["pics"] if e.find(".//p:cNvPr", NS).get("name") == fig["picture"]), None)
        if pic is None:
            raise SystemExit(f"picture '{fig['picture']}' not on slide {fig['from_slide']}")
        cap = next((e for e in fparts["captions"] if shape_text(e) == fig["caption"]), None)
        if cap is None:
            raise SystemExit(f"caption not found on slide {fig['from_slide']}: {fig['caption']!r}")
        pic, cap = copy.deepcopy(pic), copy.deepcopy(cap)
        frels = pkg.rels(src_part)
        for blip in pic.iter(A + "blip"):
            tmp = f"tmp{k}_{blip.get(R + 'embed')}"
            images[tmp] = frels[blip.get(R + "embed")][1]
            blip.set(R + "embed", tmp)
        anchor.addprevious(pic)
        anchor.addprevious(cap)

    # footer: citation and "24a" slide number; widen boxes leftward/rightward as the text needs
    def footer_text(sp, text):
        set_shape_text(sp, [text])
        x, y_, w, h = geom(sp)
        pt = body_font_pt(sp, default_pt)
        need = int(len(text) * pt * 0.56 * EMU_PER_PT) + 2 * EMU_PER_PT
        if need > w:
            off = sp.find(".//a:xfrm/a:off", NS)
            ext = sp.find(".//a:xfrm/a:ext", NS)
            if sp is parts["number"]:
                off.set("x", str(x + w - need))
            ext.set("cx", str(need))

    if parts["cite"] is not None and spec_slide.get("cite"):  # null keeps the deck's own footer label
        footer_text(parts["cite"], spec_slide["cite"])
    footer_text(parts["number"], spec_slide["footer_number"])

    # unique shape ids
    for n, c in enumerate(root.iter(P + "cNvPr"), start=1):
        c.set("id", str(n))
    return root, images, pkg.rels(tpart)


def notes_xml(pkg, template_slide_part, spec_slide):
    """Clone the template slide's notes part and write the transcript, then References."""
    root = copy.deepcopy(pkg.xml(pkg.notes_part(template_slide_part)))
    body = None
    for sp in root.iter(P + "sp"):
        ph = sp.find(".//p:nvPr/p:ph", NS)
        if ph is not None and ph.get("type") == "body":
            body = sp.find(".//p:txBody", NS)
    paras = body.findall(A + "p")
    first_rpr = next(body.iter(A + "rPr"), None)
    rpr = copy.deepcopy(first_rpr) if first_rpr is not None else etree.Element(A + "rPr", lang="en-US")
    ppr = paras[0].find(A + "pPr")
    typed_bullets = any("".join(t.text or "" for t in p.iter(A + "t")).startswith(("• ", "– ")) for p in paras)
    for p in paras:
        body.remove(p)

    def para(text, lvl=None):
        if typed_bullets:  # the deck writes "• " and "– " as text in plain paragraphs
            p = etree.SubElement(body, A + "p")
            if text:
                r = etree.SubElement(p, A + "r")
                r.append(copy.deepcopy(rpr))
                etree.SubElement(r, A + "t").text = ({0: "• ", 1: "– "}.get(lvl, "")) + strip_markup(text)
            return
        p = etree.SubElement(body, A + "p")
        pp = copy.deepcopy(ppr) if ppr is not None else etree.Element(A + "pPr")
        for child in list(pp):
            if child.tag in (A + "buNone", A + "buChar", A + "buAutoNum", A + "buFont", A + "buSzPts"):
                pp.remove(child)
        if lvl is None:
            pp.set("marL", "0")
            pp.set("indent", "0")
            pp.set("lvl", "0")
            etree.SubElement(pp, A + "buNone")
        else:
            pp.set("lvl", str(lvl))
            pp.set("marL", str(342900 + lvl * 342900))
            pp.set("indent", "-228600")
            etree.SubElement(pp, A + "buChar").set("char", "•" if lvl == 0 else "–")
        p.append(pp)
        r = etree.SubElement(p, A + "r")
        r.append(copy.deepcopy(rpr))
        etree.SubElement(r, A + "t").text = strip_markup(text)

    for item in spec_slide["transcript"]:
        if isinstance(item, str):
            para(item, 0)
        else:
            para(item[0], 0)
            for sub in item[1]:
                para(sub, 1)
    para("")
    para("References:")
    for ref in spec_slide["refs"]:
        para(ref)
    return root


def rels_xml(entries):
    root = etree.Element("{%s}Relationships" % NS["rel"], nsmap={None: NS["rel"]})
    for rid, typ, tgt in entries:
        etree.SubElement(root, "{%s}Relationship" % NS["rel"], Id=rid, Type=REL_T + typ, Target=tgt)
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def ser(root):
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def paragraph_text(p):
    return "".join(t.text or "" for t in p.iter(A + "t"))


def apply_original_edits(pkg, spec):
    """Replace single named paragraphs on original slides (spec "original_edits", used when the instructor
    asks for caveat paragraphs to be rewritten). Every other byte of the slide stays as it was; the edited
    paragraph keeps its own paragraph and run formatting. Returns the edited part names."""
    edited = []
    for e in spec.get("original_edits", []):
        part = pkg.slides[e["slide"] - 1]
        root = pkg.xml(part)
        hits = [p for p in root.iter(A + "p") if paragraph_text(p) == e["old"]]
        if len(hits) != 1:
            raise SystemExit(f"original slide {e['slide']}: paragraph to replace found {len(hits)} times")
        p = hits[0]
        rprs = [r.find(A + "rPr") for r in p.findall(A + "r") if r.find(A + "rPr") is not None]
        if not rprs:
            raise SystemExit(f"original slide {e['slide']}: paragraph has no run formatting")
        base = next((x for x in rprs if x.get("b") != "1" and x.get("i") != "1"), rprs[0])
        bold = next((x for x in rprs if x.get("b") == "1"), None)
        set_paragraph(p, e["new"], copy.deepcopy(base), copy.deepcopy(bold) if bold is not None else None)
        pkg.parts[part] = ser(root)
        edited.append(part)
    return edited


def build(input_path, spec_path, out_path):
    spec = json.loads(Path(spec_path).read_text())
    pkg = Package(input_path)
    edited = apply_original_edits(pkg, spec)
    slides = spec["new_slides"]
    n_orig = len(pkg.slides)
    if len(slides) != 14:
        raise SystemExit(f"spec has {len(slides)} new slides; exactly 14 are required")
    for s in slides:
        for key in ("after", "template_slide"):
            if not 1 <= s[key] <= n_orig:
                raise SystemExit(f"{s['footer_number']}: {key} {s[key]} outside 1-{n_orig}")
        if s["after"] == n_orig:
            raise SystemExit(f"{s['footer_number']}: nothing may follow the Key takeaways slide")
    default_pt = default_font_pt(pkg)
    pres = pkg.xml("ppt/presentation.xml")
    slide_w = int(pres.find("p:sldSz", NS).get("cx"))
    floor = deck_body_bottom(pkg)

    new_parts = {}
    existing = set(pkg.parts)

    def free_name(stem, ext):
        k = 1
        while f"{stem}{k}{ext}" in existing or f"{stem}{k}{ext}" in new_parts:
            k += 1
        return f"{stem}{k}{ext}"

    pres_rels_part = "ppt/_rels/presentation.xml.rels"
    prels = etree.fromstring(pkg.parts[pres_rels_part])
    used_rids = {r.get("Id") for r in prels}
    ct = etree.fromstring(pkg.parts["[Content_Types].xml"])
    sld_lst = pres.find("p:sldIdLst", NS)
    next_id = max(int(s.get("id")) for s in sld_lst) + 1
    orig_ids = list(sld_lst)
    inserted = {}  # original position -> [new sldId elements in spec order]

    for s in slides:
        root, images, trels = build_slide(pkg, s, slide_w, default_pt, floor)
        slide_part = free_name("ppt/slides/slide", ".xml")
        new_parts[slide_part] = None
        notes_part = free_name("ppt/notesSlides/notesSlide", ".xml")
        new_parts[notes_part] = None
        sdir = "ppt/slides"
        rel_entries = []
        layout = next(t for typ, t in trels.values() if typ == "slideLayout")
        rel_entries.append(("rId1", "slideLayout", posixpath.relpath(layout, sdir)))
        rel_entries.append(("rId2", "notesSlide", posixpath.relpath(notes_part, sdir)))
        remap = {}
        for k, (old, target) in enumerate(sorted(images.items()), start=3):
            remap[old] = f"rId{k}"
            rel_entries.append((f"rId{k}", "image", posixpath.relpath(target, sdir)))
        for blip in root.iter(A + "blip"):
            blip.set(R + "embed", remap[blip.get(R + "embed")])
        new_parts[slide_part] = ser(root)
        new_parts[posixpath.join(sdir, "_rels", posixpath.basename(slide_part) + ".rels")] = rels_xml(rel_entries)

        nroot = notes_xml(pkg, pkg.slides[s["template_slide"] - 1], s)
        tnotes = pkg.notes_part(pkg.slides[s["template_slide"] - 1])
        master = next(t for typ, t in pkg.rels(tnotes).values() if typ == "notesMaster")
        ndir = "ppt/notesSlides"
        new_parts[notes_part] = ser(nroot)
        new_parts[posixpath.join(ndir, "_rels", posixpath.basename(notes_part) + ".rels")] = rels_xml(
            [("rId1", "notesMaster", posixpath.relpath(master, ndir)),
             ("rId2", "slide", posixpath.relpath(slide_part, ndir))])

        k = 1
        while f"rId{k}" in used_rids:
            k += 1
        rid = f"rId{k}"
        used_rids.add(rid)
        etree.SubElement(prels, "{%s}Relationship" % NS["rel"], Id=rid, Type=REL_T + "slide",
                         Target=posixpath.relpath(slide_part, "ppt"))
        for part, ctype in ((slide_part, SLIDE_CT), (notes_part, NOTES_CT)):
            etree.SubElement(ct, "{%s}Override" % NS["ct"], PartName="/" + part, ContentType=ctype)
        el = etree.Element(P + "sldId", nsmap=None)
        el.set("id", str(next_id))
        el.set(R + "id", rid)
        next_id += 1
        inserted.setdefault(s["after"], []).append(el)

    for el in list(sld_lst):
        sld_lst.remove(el)
    for pos, el in enumerate(orig_ids, start=1):
        sld_lst.append(el)
        for new in inserted.get(pos, []):
            sld_lst.append(new)

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    changed = {"ppt/presentation.xml": ser(pres), pres_rels_part: ser(prels), "[Content_Types].xml": ser(ct)}
    changed.update({part: pkg.parts[part] for part in edited})
    with zipfile.ZipFile(input_path) as zin, zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = changed.get(info.filename, zin.read(info.filename))
            zout.writestr(info, data)
        for name, data in new_parts.items():
            zout.writestr(name, data)
    return out_path


def to_pdf(pptx):
    pptx = Path(pptx)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(pptx.parent), str(pptx)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    return pptx.with_suffix(".pdf")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("input")
    ap.add_argument("spec")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    if Path(a.input).resolve() == Path(a.output).resolve():
        sys.exit("refusing to overwrite the input deck")
    if "_SCAFFOLDED" in Path(a.input).name:
        sys.exit("build from the original input deck, never from a _SCAFFOLDED output")
    out = build(a.input, a.spec, a.output)
    print(f"wrote {out}")
    if not a.no_pdf:
        print(f"wrote {to_pdf(out)}")


if __name__ == "__main__":
    main()
