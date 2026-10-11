"""Embed verified, original article recordings in the repository-built deck.
Run build_lecture.py first, then this script. Never apply twice to the same deck.
"""
from pathlib import Path
import hashlib,json,shutil,subprocess,zipfile
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
BASE=Path(__file__).resolve().parent
research=json.loads((BASE/'research.json').read_text())
media=json.loads((BASE/'media_sources.json').read_text())
deck=BASE/'Neuroethology_Lecture89_FA2026.pptx'
prs=Presentation(deck)
assert len(prs.slides)==46
assert not any(s.shape_type==16 for slide in prs.slides for s in slide.shapes), 'Rebuild the baseline before embedding.'
from collections import defaultdict
groups=defaultdict(list)
for m in media['embedded']:groups[m['slide']].append(m)
for number, recordings in groups.items():
 slide=prs.slides[number-1]
 pictures=[sh for sh in slide.shapes if sh.shape_type==13]
 captions=[sh for sh in slide.shapes if sh.name=='Figure caption']
 assert len(pictures)==len(captions)
 # Preserve every original figure and caption; two figures share the upper row.
 cells=len(pictures);cell_width=5.7/cells
 for i,(picture,caption) in enumerate(zip(pictures,captions)):
  ratio=picture.width/picture.height
  width=min(cell_width-.08,2.15*ratio);height=width/ratio
  left=7.01+i*cell_width+(cell_width-width)/2
  picture.left=Inches(left);picture.top=Inches(1.35)
  picture.width=Inches(width);picture.height=Inches(height)
  caption.left=Inches(7.01+i*cell_width);caption.width=Inches(cell_width-.05)
  caption.top=Inches(1.35+height+.07);caption.height=Inches(.63)
  for p in caption.text_frame.paragraphs:
   for r in p.runs:r.font.size=Pt(9)
 for i,m in enumerate(recordings):
  clip=BASE/m['path'];poster=BASE/m['poster']
  assert hashlib.sha256(clip.read_bytes()).hexdigest()==m['sha256']
  cell_width=5.7/len(recordings);ratio=m['display_aspect']
  width=min(cell_width-.06,2.35*ratio);height=width/ratio
  left=7.01+i*cell_width+(cell_width-width)/2;top=4.23+(2.35-height)/2
  fallback=slide.shapes.add_picture(str(poster),Inches(left),Inches(top),Inches(width),Inches(height))
  fallback.name='Unedited article-recording frame: '+m['caption']
  movie=slide.shapes.add_movie(str(clip),Inches(left),Inches(top),Inches(width),Inches(height),poster_frame_image=str(poster),mime_type='video/mp4')
  movie.name=m['caption']+' (click to play)'
  c=slide.shapes.add_textbox(Inches(7.01+i*cell_width),Inches(6.58),Inches(cell_width-.06),Inches(.46))
  c.name='Article recording credit';tf=c.text_frame;tf.word_wrap=True
  tf.margin_top=tf.margin_bottom=tf.margin_left=tf.margin_right=0
  r=tf.paragraphs[0].add_run();r.text=m['caption'];r.font.name='Arial';r.font.size=Pt(8.5);r.font.color.rgb=RGBColor(0,0,0)
  tf=slide.notes_slide.notes_text_frame
  for text in ['', 'Article-provided recording: '+m['caption'],'• '+m['teaching_note'],'Article DOI: https://doi.org/'+m['doi'],'Original media URL: '+m['original_media_url'],'Credit: '+m['credit'],'License: '+m['license'],'Compatibility: '+m['conversion'],'Playback: click the recording in PowerPoint Slide Show. The credited original article figure remains a static fallback. Full media decode and embedded relationships were checked; interactive PowerPoint playback was unavailable in this environment.']:
   tf.add_paragraph().text=text
for m in media['not_embedded']:
 tf=prs.slides[m['slide']-1].notes_slide.notes_text_frame
 tf.add_paragraph().text='Optional article recording, not embedded: '+m['reason']+' Original media URL: '+m['original_media_url']+' Article DOI: https://doi.org/'+m['doi']
prs.save(deck)
with zipfile.ZipFile(deck) as z:
 hashes={hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.endswith('.mp4')}
 assert hashes=={m['sha256']for m in media['embedded']}
 for m in media['embedded']:
  rel=z.read(f"ppt/slides/_rels/slide{m['slide']}.xml.rels").decode()
  assert '/video' in rel and '/media' in rel
  assert b'<p:timing>' in z.read(f"ppt/slides/slide{m['slide']}.xml")
assert len(Presentation(deck).slides)==46
print('Verified embedded recordings:',len(media['embedded']))
