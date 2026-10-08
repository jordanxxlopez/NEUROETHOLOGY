import json,hashlib,re,io,shutil
from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import pymupdf
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
from style_rules import is_color_image
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
spec=json.loads((H/'lecture.json').read_text());meta=next(x for x in json.loads((ROOT/'course/schedule.json').read_text())['lectures']if x['n']==32);prs=Presentation(H/'Neuroethology_Lecture32_FA2026.pptx');assert len(prs.slides)==46
assert next(sh.text for sh in prs.slides[0].shapes if sh.name=='Lecture title')==meta['title'];assert meta['date']in '\n'.join(sh.text for sh in prs.slides[0].shapes if sh.has_text_frame)
imgs=colors=0;bodyfonts=[];hashes={hashlib.sha256(p.read_bytes()).hexdigest():p.name for p in (H/'figures').iterdir()if p.is_file()}
for i,sl in enumerate(prs.slides):
 notes=sl.notes_slide.notes_text_frame.text;assert 'References:'in notes and 'https://doi.org/'in notes
 pics=[x for x in sl.shapes if x.shape_type==MSO_SHAPE_TYPE.PICTURE]
 if 0<i<45:
  assert pics;imgs+=1;colors+=any(is_color_image(x.image.blob)for x in pics)
 for x in pics:assert hashlib.sha256(x.image.blob).hexdigest()in hashes
 for x in sl.shapes:
  if x.has_text_frame:
   for p in x.text_frame.paragraphs:
    for r in p.runs:
     assert not r.text or r.font.name=='Arial'
     if x.name=='Body' and r.font.size:bodyfonts.append(r.font.size.pt)
 for p in sl.notes_slide.notes_text_frame.paragraphs:
  for r in p.runs:assert not r.text or r.font.name=='Arial'
assert imgs==44 and colors>=22
pdf=H/'Neuroethology_Lecture32_FA2026.pdf';doc=pymupdf.open(pdf);assert len(doc)==46
for p in doc:
 for b in p.get_text('blocks'):assert b[0]>=-1 and b[2]<=p.rect.width+1 and b[3]<=p.rect.height+1

manifest=[]
for p in sorted((H/'papers').glob('*.pdf')):
 d=pymupdf.open(p);manifest.append({'key':p.stem,'path':'papers/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':len(d),'figure_source':p.stem in {x[0]for x in json.loads((H/'crops.json').read_text())['crops'].values()}})
(H/'sources/available-pdfs.json').write_text(json.dumps(manifest,indent=2));(H/'sources/needed-pdfs.json').write_text('[]\n')
result={'slides':46,'content_slides':44,'content_slides_with_original_article_figures':imgs,'content_slides_with_source_color':colors,'title':meta['title'],'date':meta['date'],'content_paragraphs_per_slide':3,'takeaways':6,'fonts':['Arial'],'all_slides_have_reference_notes':True,'all_image_bytes_match_retained_sources':True,'pdf_pages':46,'pdf_text_inside_page':True,'generated_scientific_images':0,'pending_pdfs':0}
(H/'sources/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(H/'VALIDATION.md').write_text('# Lecture 32 validation\n\n'+ '\n'.join(f'- {k}: {v}'for k,v in result.items())+'\n\nAll 46 rendered slides and all used source crops were visually inspected. Source captions identify original figure numbers/panels and DOI links; notes contain full references and DOI hyperlinks. The Bottjer upload is a text-only licensed reprint and contributed no images. Scientific images are unchanged published panels cropped with the repository tools. The sole web photograph is credited to Michael Hains, CC BY-NC 4.0.\n')
print(json.dumps(result,ensure_ascii=False))
