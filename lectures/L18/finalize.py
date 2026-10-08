"""Preserve the title as one character-exact paragraph after the course builder."""
import json
from pathlib import Path
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
p=HERE/'Neuroethology_Lecture18_FA2026.pptx';prs=Presentation(p)
meta=next(x for x in json.loads((ROOT/'course/schedule.json').read_text())['lectures'] if x['n']==18)
sh=next(x for x in prs.slides[0].shapes if x.name=='Lecture title');sh.text_frame.clear();pa=sh.text_frame.paragraphs[0];pa.space_after=Pt(0);pa.line_spacing=1.08;r=pa.add_run();r.text=meta['title'];r.font.name='Arial';r.font.size=Pt(24);r.font.bold=True;r.font.color.rgb=RGBColor.from_string('1E3448')
assert sh.text==meta['title']
spec=json.loads((HERE/'lecture.json').read_text())
prs.slides[-1].notes_slide.notes_text_frame.text='\n'.join('• '+i['lead']+'. '+i['text'] for i in spec['takeaways']['items'])+'\n\nReferences:\n'+'\n'.join(spec['takeaways']['refs'])
prs.save(p)
print('Preserved exact title and completed takeaway notes.')
# Give every cited image a full reference and clickable source DOI in the notes.
import re
refs=json.loads((HERE/'references.json').read_text())
nt=prs.slides[0].notes_slide.notes_text_frame
nt.text=nt.text+'\n\nReferences:\n'+refs['k78']
for sl in prs.slides:
 tf=sl.notes_slide.notes_text_frame
 for pa in tf.paragraphs:
  txt=pa.text;pa.clear()
  for chunk in re.split(r'(https://doi\.org/[^\s]+)',txt):
   if not chunk:continue
   run=pa.add_run();run.text=chunk;run.font.name='Arial';run.font.size=Pt(12)
   if chunk.startswith('https://doi.org/'):run.hyperlink.address=chunk
prs.save(p)
print('Notes use Arial and DOI links are clickable.')
