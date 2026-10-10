"""Add article recordings while retaining every existing slide element and part.

Usage: python lectures/L71/add_article_media.py INPUT.pptx MEDIA.json OUTPUT.pptx
Only appended shapes, video timing/relationships, appended notes, new media, and
necessary content types are written back into the original OPC package.
"""
import argparse
import copy
import hashlib
import io
import json
import tempfile
import zipfile
from pathlib import Path

from lxml import etree as E
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

def canonical(node):
    return E.tostring(node, method="c14n")

def add_recordings(source, manifest, output):
    config = json.loads(manifest.read_text())
    base = manifest.parent
    original = source.read_bytes()
    prs = Presentation(io.BytesIO(original))
    assert len(prs.slides) == 46
    assert not any(shape.shape_type == 16 for slide in prs.slides for shape in slide.shapes), \
        "Use a fresh baseline without recordings; this deck already contains media."
    additions = {}
    for media in config["embedded"]:
        clip = base / media["path"]
        poster = base / media["poster"]
        assert hashlib.sha256(clip.read_bytes()).hexdigest() == media["sha256"]
        slide = prs.slides[media["slide"] - 1]
        if media.get("overlay_shape_id"):
            picture = next(s for s in slide.shapes if s.shape_id == media["overlay_shape_id"])
            assert poster.read_bytes() == picture.image.blob
            rect = [picture.left, picture.top, picture.width, picture.height]
        else:
            rect = [Inches(x) for x in media["placement"]]
            slide.shapes.add_picture(str(poster), *rect)
        movie = slide.shapes.add_movie(str(clip), *rect,
                    poster_frame_image=str(poster), mime_type="video/mp4")
        movie.name = media["caption"] + " (click to play)"
        caption = slide.shapes.add_textbox(*[Inches(x) for x in media["caption_placement"]])
        caption.name = "Article recording credit"
        frame = caption.text_frame
        frame.word_wrap = True
        frame.margin_top = frame.margin_bottom = frame.margin_left = frame.margin_right = 0
        run = frame.paragraphs[0].add_run()
        run.text = media["caption"]
        run.font.name = "Arial"
        run.font.size = Pt(media.get("caption_font_pt", 9))
        run.font.color.rgb = RGBColor(0, 0, 0)
        additions[media["slide"]] = [
            "Article-provided recording: " + media["caption"],
            "• " + media["teaching_note"],
            "Article DOI: https://doi.org/" + media["doi"],
            "Original media URL: " + media["original_media_url"],
            "Retrieved from: " + media["retrieved_url"],
            "Credit: " + media["credit"],
            "License: " + media["license"],
            "Compatibility: " + media["conversion"],
            "Playback: click the video or its article-figure poster in PowerPoint Slide Show. "
            "The original credited figure remains as a static fallback. The complete media "
            "decode and embedded relationships were verified; interactive PowerPoint "
            "playback was unavailable in this environment."]
    with tempfile.TemporaryDirectory() as tmp:
        saved = Path(tmp) / "with-media.pptx"
        prs.save(saved)
        with zipfile.ZipFile(io.BytesIO(original)) as old, zipfile.ZipFile(saved) as new:
            replacements = {}
            for number, paragraphs in additions.items():
                part = f"ppt/slides/slide{number}.xml"
                root = E.fromstring(old.read(part))
                updated = E.fromstring(new.read(part))
                tree = root.find("p:cSld/p:spTree", NS)
                changed_tree = updated.find("p:cSld/p:spTree", NS)
                # Append only shapes whose IDs did not exist in the supplied slide.
                old_ids = {n.get("id") for n in tree.findall(".//p:cNvPr", NS)}
                for shape in changed_tree:
                    ids = shape.findall(".//p:cNvPr", NS)
                    if ids and ids[0].get("id") not in old_ids:
                        tree.append(copy.deepcopy(shape))
                timing = root.find("p:timing", NS)
                if timing is not None:
                    root.remove(timing)
                timing = updated.find("p:timing", NS)
                assert timing is not None
                # Timing precedes extLst in the PresentationML sequence.
                extension = root.find("p:extLst", NS)
                if extension is None:
                    root.append(copy.deepcopy(timing))
                else:
                    root.insert(list(root).index(extension), copy.deepcopy(timing))
                replacements[part] = E.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
                relpart = f"ppt/slides/_rels/slide{number}.xml.rels"
                old_rels = E.fromstring(old.read(relpart))
                new_rels = E.fromstring(new.read(relpart))
                for rel in old_rels:
                    matched = next(x for x in new_rels if x.get("Id") == rel.get("Id"))
                    assert dict(matched.attrib) == dict(rel.attrib)
                replacements[relpart] = new.read(relpart)
                notespart = f"ppt/notesSlides/notesSlide{number}.xml"
                notes = E.fromstring(old.read(notespart))
                body = next(s for s in notes.findall("p:cSld/p:spTree/p:sp", NS)
                            if s.find("p:nvSpPr/p:nvPr/p:ph", NS) is not None
                            and s.find("p:nvSpPr/p:nvPr/p:ph", NS).get("type") == "body")
                textbody = body.find("p:txBody", NS)
                for text in [""] + paragraphs:
                    paragraph = E.SubElement(textbody, "{" + NS["a"] + "}p")
                    run = E.SubElement(paragraph, "{" + NS["a"] + "}r")
                    E.SubElement(run, "{" + NS["a"] + "}t").text = text
                replacements[notespart] = E.tostring(notes, xml_declaration=True, encoding="UTF-8", standalone=True)
            types = E.fromstring(old.read("[Content_Types].xml"))
            ids = {(x.tag, x.get("Extension"), x.get("PartName")) for x in types}
            for entry in E.fromstring(new.read("[Content_Types].xml")):
                if (entry.tag, entry.get("Extension"), entry.get("PartName")) not in ids:
                    types.append(copy.deepcopy(entry))
            replacements["[Content_Types].xml"] = E.tostring(types, xml_declaration=True, encoding="UTF-8", standalone=True)
            result = io.BytesIO()
            with zipfile.ZipFile(result, "w", zipfile.ZIP_DEFLATED) as dest:
                for item in old.infolist():
                    dest.writestr(item, replacements.get(item.filename, old.read(item.filename)))
                for item in new.infolist():
                    if item.filename not in old.namelist():
                        assert item.filename.startswith("ppt/media/"), item.filename
                        dest.writestr(item, new.read(item.filename))
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(result.getvalue())
    # Verify exact preservation of the original shape XML and all untouched parts.
    with zipfile.ZipFile(io.BytesIO(original)) as old, zipfile.ZipFile(output) as final:
        for name in old.namelist():
            if name not in replacements:
                assert old.read(name) == final.read(name), name
        for n in additions:
            part = f"ppt/slides/slide{n}.xml"
            a = E.fromstring(old.read(part)).find("p:cSld/p:spTree", NS)
            b = E.fromstring(final.read(part)).find("p:cSld/p:spTree", NS)
            for prior, after in zip(a, b):
                assert canonical(prior) == canonical(after), (n, prior.tag)
            notespart = f"ppt/notesSlides/notesSlide{n}.xml"
            previous = E.fromstring(old.read(notespart)).findall(".//a:p", NS)
            following = E.fromstring(final.read(notespart)).findall(".//a:p", NS)
            # Existing note paragraphs are an ordered subsequence of the new notes.
            remaining = iter(following)
            for paragraph in previous:
                assert any(canonical(paragraph) == canonical(candidate) for candidate in remaining)
        hashes = {hashlib.sha256(final.read(n)).hexdigest()
                  for n in final.namelist() if n.endswith(".mp4")}
        assert hashes == {m["sha256"] for m in config["embedded"]}
        for m in config["embedded"]:
            rel = final.read(f"ppt/slides/_rels/slide{m['slide']}.xml.rels").decode()
            assert "/video" in rel and "/media" in rel
    assert len(Presentation(output).slides) == 46
    print(f"Verified {len(additions)} embedded recordings; original slide elements and untouched parts preserved: {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    add_recordings(args.input, args.manifest, args.output)
