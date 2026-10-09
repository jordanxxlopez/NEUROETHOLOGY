"""Fit the unusually long scheduled title and complete note hyperlinks."""
import json,re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
D=Path(__file__).parent
spec=json.loads((D/'lecture.json').read_text())
path=D/'Neuroethology_Lecture45_FA2026.pptx'
p=Presentation(path)
schedule=json.loads((D.parent.parent/'course/schedule.json').read_text())
# The builder already reads the exact special-topic title into the first notes line.
exact=p.slides[0].notes_slide.notes_text_frame.text.splitlines()[0]
for s in p.slides[0].shapes:
 if s.has_text_frame and s.name=='Lecture title':
  s.top=Inches(2.4);s.height=Inches(3.05);s.text_frame.clear()
  para=s.text_frame.paragraphs[0];para.space_after=Pt(0);para.line_spacing=1.05
  run=para.add_run();run.text=exact;run.font.name='Arial';run.font.size=Pt(26);run.font.bold=True;run.font.color.rgb=RGBColor.from_string('FFFFFF')
 elif s.has_text_frame and s.text=='Date TBD':s.top=Inches(5.85)
 elif s.has_text_frame and s.text.startswith('Jordan Lopez'):s.top=Inches(6.5)
last=p.slides[-1].notes_slide.notes_text_frame
last.text='\n'.join('• '+x['lead']+' '+x['text'] for x in spec['takeaways']['items'])+'\n\nReferences:\n'+'\n\n'.join(spec['takeaways']['refs'])
for s in p.slides:
 for para in s.notes_slide.notes_text_frame.paragraphs:
  text=para.text;para.clear()
  for chunk in re.split(r'(https://doi\.org/\S+)',text):
   if not chunk:continue
   run=para.add_run();run.text=chunk;run.font.name='Arial';run.font.size=Pt(12)
   if chunk.startswith('https://doi.org/'):run.hyperlink.address=chunk
p.save(path)
print('Exact scheduled title, title fit, full teaching notes and DOI hyperlinks finalized.')
