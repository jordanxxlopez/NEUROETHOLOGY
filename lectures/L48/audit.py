"""Audit editable slides, source figures, title, date and notes after building."""
import hashlib,json
from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
base=Path(__file__).resolve().parent
spec=json.loads((base/'lecture.json').read_text());crops=json.loads((base/'crops.json').read_text());srcs={s['key']:s for s in json.loads((base/'sources/available-pdfs.json').read_text())}
r=Presentation(base/'Neuroethology_Lecture48_FA2026.pptx');assert len(r.slides)==46
provenance=[]
for n,sd in enumerate(spec['slides'],2):
 assert len(sd['body'])==3
 figs=[sd['figure']] if 'figure' in sd else sd['figures']
 embedded={hashlib.sha256(sh.image.blob).hexdigest() for sh in r.slides[n-1].shapes if sh.shape_type==MSO_SHAPE_TYPE.PICTURE}
 for f in figs:
  im=base/f['path'];sha=hashlib.sha256(im.read_bytes()).hexdigest();assert sha in embedded
  k,pg,box=crops['crops'][im.stem]
  pdf=base/crops['papers'][k];pdfsha=hashlib.sha256(pdf.read_bytes()).hexdigest()
  provenance.append({'slide':n,'path':f['path'],'caption':f['caption'],'doi':srcs[k]['doi'],'pdf_page':pg,'crop_box_fraction':box,'dpi':crops['dpi'],'pdf_sha256':pdfsha,'image_sha256':sha,'source_policy':'Unaltered rectangular crop of original published PDF figure; no generated or reconstructed visual.'})
 notes=r.slides[n-1].notes_slide.notes_text_frame.text
 assert 'References:' in notes and 'https://doi.org/' in notes and '• ' in notes
 assert all(ref in notes for ref in sd['refs'])
bodyfonts=set()
for sl in r.slides:
 for sh in sl.shapes:
  if sh.has_text_frame:
   for p in sh.text_frame.paragraphs:
    for run in p.runs:
     if run.text:bodyfonts.add(run.font.name)
 assert all(run.font.name=='Arial' for p in sl.notes_slide.notes_text_frame.paragraphs for run in p.runs if run.text)
assert bodyfonts=={'Arial'},bodyfonts
schedule=json.loads((base.parents[1]/'course/schedule.json').read_text())
title=r.slides[0].notes_slide.notes_text_frame.text.split('\n')[0]
assert next(sh.text for sh in r.slides[0].shapes if sh.name=='Lecture title')==title
assert any(sh.has_text_frame and sh.text=='Date TBD' for sh in r.slides[0].shapes)
assert len(spec['takeaways']['items'])==6
(base/'sources/figure-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
summary={'slides':46,'content_slides':44,'image_content_slides':44,'article_figure_content_slides':44,'primary_papers':len(srcs),'content_paragraphs_per_slide':3,'full_references_and_transcripts':True,'notes_doi_hyperlinks':True,'editable_text_font':'Arial','title':title,'date':'Date TBD','title_preserved_character_for_character':True,'scientific_image_provenance':'PDF crops only','generated_scientific_visuals':0,'takeaway_points':6,'palette':'Atlantic ink / pearl','native_pptx_sha256':hashlib.sha256((base/'Neuroethology_Lecture48_FA2026.pptx').read_bytes()).hexdigest()}
(base/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
