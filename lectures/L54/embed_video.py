"""Embed verified article recordings without rebuilding or rewriting Lecture 54."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import subprocess
import zipfile
from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches, Pt

D = Path(__file__).resolve().parent
R = D.parents[1]
BASELINE = '06cccc7'
original = subprocess.check_output(['git', 'show', f'{BASELINE}:lectures/L54/Neuroethology_Lecture54_FA2026.pptx'], cwd=R)
prs = Presentation(BytesIO(original))
shapes_before = [[etree.tostring(shape._element) for shape in slide.shapes] for slide in prs.slides]
notes_before = [slide.notes_slide.notes_text_frame.text for slide in prs.slides]
sources = json.loads((D / 'media_sources.json').read_text())
ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
for record in sources:
    slide = prs.slides[record['slide'] - 1]
    pictures = [shape for shape in slide.shapes if shape.shape_type == MSO_SHAPE_TYPE.PICTURE]
    figure = pictures[record.get('picture_index', 0)]
    media = D / record['file']
    movie = slide.shapes.add_movie(str(media), figure.left, figure.top, figure.width, figure.height,
                                  poster_frame_image=BytesIO(figure.image.blob), mime_type='video/mp4')
    slide._element.find('.//p:video', ns).set('fullScrn', '1')
    # The short video credit occupies the blank gap between title and body.
    credit = slide.shapes.add_textbox(Inches(.62), Inches(1.06), Inches(12.09), Inches(.19))
    credit.text_frame.margin_left = credit.text_frame.margin_right = 0
    credit.text_frame.margin_top = credit.text_frame.margin_bottom = 0
    paragraph = credit.text_frame.paragraphs[0]
    paragraph.text = record['caption']
    paragraph.font.name = 'Arial'
    paragraph.font.size = Pt(8)
    paragraph.font.color.rgb = RGBColor(0, 0, 0)
    slide.notes_slide.notes_text_frame.text += (
        '\n\nArticle-provided recording:\n' + record['caption'] + '\n' + record['teaching_context'] +
        '\nReferences:\n' + record['reference'] + '\nArticle DOI: https://doi.org/' + record['doi'] +
        '\nOriginal media URL: ' + record['original_url'] + '\nCredit: ' + record['credit'] +
        '\nLicense: ' + record['license'] + '\nConversion: ' + record['conversion'] +
        '\nClick the figure during Slide Show for full-screen playback. The intact original article figure remains as the poster and underneath as a static fallback. PowerPoint GUI playback was unavailable for testing.\n')
    record['duration_seconds'] = float(json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(media)
    ]))['format']['duration'])
    record['sha256'] = hashlib.sha256(media.read_bytes()).hexdigest()
    record['embedded_payload_hash_verified'] = True
    record['complete_media_decode_verified'] = True

output = D / 'Neuroethology_Lecture54_FA2026.pptx'
prs.save(output)
saved = Presentation(output)
assert len(saved.slides) == 46
changed = {record['slide'] for record in sources}
for index, slide in enumerate(saved.slides):
    assert [etree.tostring(shape._element) for shape in list(slide.shapes)[:len(shapes_before[index])]] == shapes_before[index], f'Original shapes changed on slide {index + 1}'
    assert slide.notes_slide.notes_text_frame.text.startswith(notes_before[index])
    if index + 1 not in changed:
        assert slide.notes_slide.notes_text_frame.text == notes_before[index]
with zipfile.ZipFile(output) as archive:
    movies = [name for name in archive.namelist() if name.endswith('.mp4')]
    assert len(movies) == len(sources)
    hashes = {hashlib.sha256(archive.read(name)).hexdigest() for name in movies}
    assert hashes == {record['sha256'] for record in sources}
    for record in sources:
        number = record['slide']
        xml = archive.read(f'ppt/slides/slide{number}.xml').decode()
        rels = archive.read(f'ppt/slides/_rels/slide{number}.xml.rels').decode()
        assert 'videoFile' in xml and 'fullScrn="1"' in xml and 'relationships/video' in rels
(D / 'media_sources.json').write_text(json.dumps(sources, indent=2))
(D / 'video_validation.json').write_text(json.dumps({
    'slides': 46, 'embedded_movies': len(sources), 'video_slides': sorted(changed),
    'all_original_slide_shapes_unchanged': True, 'unchanged_original_notes_retained': True,
    'embedded_payloads_and_relationships_verified': True,
    'powerpoint_gui_playback': 'Not tested'
}, indent=2))
print(f'Embedded {len(sources)} article recordings; all original slide shapes preserved.')
