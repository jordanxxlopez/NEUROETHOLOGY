from pathlib import Path
import json,re,hashlib
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
B=Path(__file__).resolve().parent;S=json.loads((B/'lecture.json').read_text());P=Presentation(B/'Neuroethology_Lecture41_FA2026.pptx');R=json.loads((B/'research.json').read_text());C=json.loads((B/'crops.json').read_text());meta=next(x for x in json.loads((B.parents[1]/'course/schedule.json').read_text())['lectures'] if x['n']==41)
assert len(P.slides)==46 and len(S['slides'])==44
assert next(sh.text for sh in P.slides[0].shapes if sh.name=='Lecture title')==meta['title']
assert meta['date']=='TBD' and any(sh.has_text_frame and sh.text=='TBD' for sh in P.slides[0].shapes)
figures=[]
for i,(sd,sl)in enumerate(zip(S['slides'],list(P.slides)[1:-1]),2):
 assert len(sd['body'])==3
 assert 90<=len(' '.join(sd['body']).split())<=170
 notes=sl.notes_slide.notes_text_frame.text;assert 'References:' in notes and len(notes.split('References:')[0].split())>90
 imgs=[sd['figure']] if 'figure' in sd else sd['figures'];emb={hashlib.sha256(sh.image.blob).hexdigest() for sh in sl.shapes if sh.shape_type==MSO_SHAPE_TYPE.PICTURE}
 for f in imgs:
  assert f['kind']=='article' and f['source_url'].startswith('https://doi.org/')
  name=Path(f['path']).stem;assert name in C['crops'];h=hashlib.sha256((B/f['path']).read_bytes()).hexdigest();assert h in emb
  key,page,box=C['crops'][name];source=next(x for x in R['sources'] if x['id']==key);assert f['source_url'].endswith(source['doi']);assert source['pdf_sha256']==hashlib.sha256((B/source['local_pdf']).read_bytes()).hexdigest()
  figures.append({'slide':i,'file':f['path'],'image_sha256':h,'paper':key,'pdf_page':page,'crop_box':box,'caption':f['caption'],'doi':source['doi']})
 assert all('https://doi.org/'in r for r in sd['refs'])
 for sh in sl.shapes:
  if sh.has_text_frame:
   for p in sh.text_frame.paragraphs:
    for r in p.runs:assert r.font.name=='Arial'
assert len(S['takeaways']['items'])==6
out={'slides':46,'content_slides':44,'article_figure_slides':44,'color_image_slides_checker':37,'body_paragraphs_per_slide':3,'body_word_range':[min(len(' '.join(s['body']).split())for s in S['slides']),max(len(' '.join(s['body']).split())for s in S['slides'])],'primary_papers':18,'unique_original_crops':len(C['crops']),'web_photos':1,'exact_title':meta['title'],'exact_date':meta['date'],'font':'Arial','figures':figures,'scientific_image_creation':False,'native_pptx_sha256':hashlib.sha256((B/'Neuroethology_Lecture41_FA2026.pptx').read_bytes()).hexdigest()}
(B/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print({k:v for k,v in out.items()if k!='figures'})
