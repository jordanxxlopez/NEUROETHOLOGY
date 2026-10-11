"""Add instructor-requested EVE excerpts after build_lecture.py and embed_media.py.
Original ten movie shapes and all existing text are retained without modification.
Only article figure geometry on slides receiving excerpts is adjusted for space.
"""
from pathlib import Path
import json,hashlib,zipfile
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
B=Path(__file__).resolve().parent
meta=json.loads((B/'media_sources.json').read_text());deck=B/'Neuroethology_Lecture94_FA2026.pptx'
p=Presentation(deck)
assert len(p.slides)==46
assert sum(s.shape_type==16 for slide in p.slides for s in slide.shapes)==10,'Apply only after embedding the ten original complete recordings.'
original_text=[[s.text for s in slide.shapes if s.has_text_frame]for slide in p.slides]
original_movies=[(i,s.name,s.left,s.top,s.width,s.height)for i,slide in enumerate(p.slides)for s in slide.shapes if s.shape_type==16]
for m in meta['eve_excerpts']:
 slide=p.slides[m['slide']-1];has_movie=any(s.shape_type==16 for s in slide.shapes)
 pictures=[s for s in slide.shapes if s.shape_type==13 and not s.name.startswith('Unedited article-recording frame:')]
 captions=[s for s in slide.shapes if s.name.startswith('Figure caption')]
 assert len(pictures)==1 and len(captions)==1
 pic=pictures[0];cap=captions[0];ratio=pic.width/pic.height
 # Existing video on slides 12 and 14 stays at its exact original position.
 # Add the new excerpt beside the article figure in the upper right column.
 cell=2.75 if has_movie else 5.7;figleft=7.01;figheight=2.2 if has_movie else 2.5
 w=min(cell,figheight*ratio);h=w/ratio
 pic.left=Inches(figleft+(cell-w)/2);pic.top=Inches(1.35);pic.width=Inches(w);pic.height=Inches(h)
 cap.left=Inches(figleft);cap.width=Inches(cell);cap.top=Inches(1.35+h+.07);cap.height=Inches(.7 if has_movie else .43)
 for para in cap.text_frame.paragraphs:
  for r in para.runs:r.font.size=Pt(8 if has_movie else 9)
 left=9.96 if has_movie else 7.01;top=1.35 if has_movie else 4.23
 w=min(cell,2.35*m['display_aspect']);h=w/m['display_aspect'];x=left+(cell-w)/2
 f=B/m['path'];poster=B/m['poster'];assert hashlib.sha256(f.read_bytes()).hexdigest()==m['sha256']
 fallback=slide.shapes.add_picture(str(poster),Inches(x),Inches(top),Inches(w),Inches(h));fallback.name='Unedited EVE excerpt source frame'
 movie=slide.shapes.add_movie(str(f),Inches(x),Inches(top),Inches(w),Inches(h),poster_frame_image=str(poster),mime_type='video/mp4');movie.name=m['caption']+' (click to play)'
 box=slide.shapes.add_textbox(Inches(left),Inches(top+h+.08),Inches(cell),Inches(.6));box.name='EVE excerpt credit';tf=box.text_frame;tf.word_wrap=True
 tf.margin_top=tf.margin_bottom=tf.margin_left=tf.margin_right=0
 r=tf.paragraphs[0].add_run();r.text='Click to play. '+m['caption'];r.font.name='Arial';r.font.size=Pt(9);r.font.color.rgb=RGBColor(0,0,0)
 notes=slide.notes_slide.notes_text_frame
 for t in ['', 'Article-provided EVE excerpt: '+m['caption'],'• '+m['teaching_note'],'Original filename: '+m['original_filename'],'Source interval: '+str(m['source_start_s'])+'–'+str(m['source_end_s'])+' seconds; complete source remains embedded on slide 2.','Article DOI: https://doi.org/'+m['doi'],'Original media URL: '+m['original_media_url'],'Credit: '+m['credit'],'License: '+m['license'],'Editing: '+m['conversion']]:notes.add_paragraph().text=t
for i,slide in enumerate(p.slides):
 assert [s.text for s in slide.shapes if s.has_text_frame][:len(original_text[i])]==original_text[i]
for i,name,left,top,w,h in original_movies:
 s=next(s for s in p.slides[i].shapes if s.name==name);assert(s.left,s.top,s.width,s.height)==(left,top,w,h)
p.save(deck)
with zipfile.ZipFile(deck)as z:
 movies=[n for n in z.namelist()if n.endswith('.mp4')]
 assert len(movies)==17
 assert {hashlib.sha256(z.read(n)).hexdigest()for n in movies}=={m['sha256']for m in meta['embedded']+meta['eve_excerpts']}
 for m in meta['eve_excerpts']:
  assert b'<p:timing>'in z.read(f"ppt/slides/slide{m['slide']}.xml")
  assert b'/video'in z.read(f"ppt/slides/_rels/slide{m['slide']}.xml.rels")
assert deck.stat().st_size<100*1024*1024
print('Added seven EVE excerpts; retained all ten original movie shapes, all original text, and 46 slides. Bytes:',deck.stat().st_size)
