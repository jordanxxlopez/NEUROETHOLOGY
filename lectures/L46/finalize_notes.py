"""Apply Arial and plain, readable teaching text to the repository-built notes."""
from pathlib import Path
import sys
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
from build_lecture import plain
path=Path(__file__).with_name('Neuroethology_Lecture46_FA2026.pptx')
prs=Presentation(path)
for index, slide in enumerate(prs.slides):
 if 0 < index < len(prs.slides)-1:
  body = next(s for s in slide.shapes if s.has_text_frame and len(s.text) > 600)
  for paragraph in body.text_frame.paragraphs:
   for run in paragraph.runs:
    if run.font.size and run.font.size.pt > 14.5:
     run.font.size = Pt(14.5)
 for paragraph in slide.notes_slide.notes_text_frame.paragraphs:
  paragraph.text=plain(paragraph.text)
  for run in paragraph.runs:
   run.font.name='Arial'
   run.font.size=Pt(12)
   run.font.color.rgb=RGBColor(0,0,0)
prs.save(path)
print('Applied Arial to all speaker notes and removed literal Markdown emphasis markers.')
