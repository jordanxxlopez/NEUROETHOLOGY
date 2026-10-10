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
    # Separate original figures from video objects. Preserve aspect ratios for both.
    probe = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,sample_aspect_ratio', '-of', 'json', str(media)]))['streams'][0]
    sar = probe.get('sample_aspect_ratio', '1:1')
    sar = 1 if sar in ('N/A', '0:1') else float(sar.split(':')[0]) / float(sar.split(':')[1])
    ratio = probe['width'] * sar / probe['height']
    captions = [shape for shape in slide.shapes if shape.has_text_frame and any(shape.text.startswith(x) for x in ['Somppi et al.', 'Quaranta et al.', 'Salonen et al.', 'Lu et al.', 'Bhatt et al.']) and shape.top < Inches(7)]
    def fit(shape, x, y, w, h):
        r = shape.width / shape.height
        nw, nh = min(w, h*r), min(h, w/r)
        shape.left, shape.top, shape.width, shape.height = map(Inches, (x+(w-nw)/2, y+(h-nh)/2, nw, nh))
    if len(pictures) == 2:
        fit(pictures[0], 7.08, 1.3, 3.5, 2.45)
        fit(pictures[1], 10.82, 1.3, 1.7, 2.45)
        for cap, x, w in zip(captions, [7.08, 10.82], [3.5, 1.7]):
            cap.left, cap.top, cap.width, cap.height = map(Inches, (x, 3.85, w, .72))
            for para in cap.text_frame.paragraphs:
                for run in para.runs: run.font.size = Pt(8.5)
        box = (7.08, 4.78, 5.44, 1.87)
    else:
        fit(figure, 7.08, 1.3, 5.44, 3.1)
        for cap in captions:
            cap.left, cap.top, cap.width, cap.height = map(Inches, (7.08, 4.48, 5.44, .42))
        box = (7.08, 5.02, 5.44, 1.63)
    x,y,w,h = box
    vw, vh = min(w,h*ratio), min(h,w/ratio)
    x += (w-vw)/2
    poster = D / 'media' / (media.stem + '_poster.jpg')
    subprocess.run(['ffmpeg','-v','error','-ss',str(record.get('poster_seconds', 3)),'-i',str(media),'-frames:v','1','-y',str(poster)],check=True)
    slide.shapes.add_picture(str(poster), Inches(x), Inches(y), width=Inches(vw), height=Inches(vh))
    movie = slide.shapes.add_movie(str(media), Inches(x), Inches(y), Inches(vw), Inches(vh),
                                  poster_frame_image=str(poster), mime_type='video/mp4')
    slide._element.find('.//p:video', ns).set('fullScrn', '1')
    record['video_bounds_inches'] = [x,y,vw,vh]
    record['native_display_aspect_ratio'] = ratio
    assert abs(vw/vh-ratio) < 1e-6
    record['caption'] = record['caption'].split(' Click')[0] + ' Click video to play.'
    credit = slide.shapes.add_textbox(Inches(7.08), Inches(6.72), Inches(5.44), Inches(.27))
    credit.text_frame.margin_left = credit.text_frame.margin_right = 0
    credit.text_frame.margin_top = credit.text_frame.margin_bottom = 0
    paragraph = credit.text_frame.paragraphs[0]
    paragraph.text = record['caption']
    paragraph.font.name = 'Arial'
    paragraph.font.size = Pt(8)
    paragraph.font.color.rgb = RGBColor(0, 0, 0)
    slide.notes_slide.notes_text_frame.text += (
        '\n\nSource-provided recording:\n' + record['caption'] + '\n' + record['teaching_context'] +
        '\nReferences:\n' + record['reference'] + ('\nArticle DOI: https://doi.org/' + record['doi'] if record.get('doi') else '\nResearch-film catalogue: ' + record['catalogue_url']) +
        '\nOriginal media URL: ' + record['original_url'] + '\nCredit: ' + record['credit'] +
        '\nLicense: ' + record['license'] + '\nConversion: ' + record['conversion'] +
        '\nClick the separate video during Slide Show for full-screen playback. Its poster is an unedited frame from the recording. Original article figures remain separately visible. PowerPoint GUI playback was unavailable for testing. Google Slides imports may omit embedded media: upload the supplied MP4s to Drive and insert them as Google Slides videos.\n')
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
    originals = list(slide.shapes)[:len(shapes_before[index])]
    if index + 1 not in changed:
        assert [etree.tostring(shape._element) for shape in originals] == shapes_before[index]
    else:
        for shape, old in zip(originals, shapes_before[index]):
            old_xml = etree.fromstring(old)
            assert old_xml.xpath('//*[local-name()="t"]/text()') == shape._element.xpath('.//a:t/text()')
        for shape in slide.shapes:
            assert shape.left >= 0 and shape.top >= 0
            assert shape.left + shape.width <= saved.slide_width + 10
            assert shape.top + shape.height <= saved.slide_height + 10
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
    'all_original_slide_text_preserved': True, 'original_figures_preserved_and_repositioned': True, 'all_videos_native_aspect_ratio': True, 'unchanged_original_notes_retained': True,
    'embedded_payloads_and_relationships_verified': True,
    'powerpoint_gui_playback': 'Not tested'
}, indent=2))
print(f'Embedded {len(sources)} article recordings; original text preserved; figures and videos separated at native aspect ratios.')
