from pathlib import Path
from pptx import Presentation
B=Path('lectures/L100');deck=B/'Neuroethology_Lecture100_FA2026.pptx';p=Presentation(deck)
for slide in p.slides:
 for shape in list(slide.shapes):
  if shape.shape_type==16:
   el=shape._element;el.getparent().remove(el)
for slide in p.slides:
 for rid, rel in list(slide.part.rels.items()):
  if rel.reltype.rsplit('/',1)[-1] in ('video','media','audio'):
   slide.part.drop_rel(rid)
 for el in list(slide._element):
  if el.tag.endswith('}timing'):slide._element.remove(el)
# A separate static copy retains scientific figures and unedited recording posters.
p.save(B/'Neuroethology_Lecture100_FA2026_static_preview.pptx')
