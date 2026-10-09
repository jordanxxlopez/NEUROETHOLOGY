"""Finalize the long exact title, note typography and clickable DOI references."""
import json,re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
base=Path(__file__).resolve().parent;path=base/'Neuroethology_Lecture48_FA2026.pptx'
r=Presentation(path);schedule=json.loads((base.parents[1]/'course/schedule.json').read_text())
spec=json.loads((base/'lecture.json').read_text())
# Use the title already taken verbatim from the authoritative schedule by the builder.
title=r.slides[0].notes_slide.notes_text_frame.text.split('\n')[0]
for sh in r.slides[0].shapes:
 if sh.name=='Lecture title':
  sh.left=Inches(.75);sh.top=Inches(2.5);sh.width=Inches(5.166);sh.height=Inches(3.0)
  tf=sh.text_frame;tf.clear();tf.word_wrap=True;p=tf.paragraphs[0];p.text=title;p.line_spacing=1.06;p.space_after=Pt(0)
  for run in p.runs:run.font.name='Arial';run.font.size=Pt(24);run.font.bold=True;run.font.color.rgb=RGBColor.from_string('FFFFFF')
 elif sh.has_text_frame and sh.text=='Date TBD':sh.top=Inches(5.85)
 elif sh.has_text_frame and sh.text.startswith(schedule['instructor']):sh.top=Inches(6.5)
last=r.slides[-1].notes_slide.notes_text_frame
last.text='\n'.join('• '+q['lead']+' '+q['text'] for q in spec['takeaways']['items'])+'\n\nReferences:\n'+'\n'.join(spec['takeaways']['refs'])
for sl in r.slides:
 tf=sl.notes_slide.notes_text_frame
 for p in tf.paragraphs:
  content=p.text
  # Rebuild each paragraph with hyperlink runs while retaining natural teaching text.
  p.clear()
  for part in re.split(r'(https://doi\.org/\S+)',content):
   if not part:continue
   run=p.add_run();run.text=part;run.font.name='Arial';run.font.size=Pt(12)
   if part.startswith('https://doi.org/'):run.hyperlink.address=part
r.save(path)
print('Exact title, complete notes and DOI hyperlinks finalized')
