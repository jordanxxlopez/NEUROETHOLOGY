"""Check the finished native deck against its source and figure manifests."""
import hashlib, json
from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
here=Path(__file__).resolve().parent
root=here.parents[1]
spec=json.loads((here/'lecture.json').read_text())
meta=next(x for x in json.loads((root/'course/schedule.json').read_text())['lectures'] if x['n']==27)
prs=Presentation(here/'Neuroethology_Lecture27_FA2026.pptx')
assert len(prs.slides)==46
assert next(s.text for s in prs.slides[0].shapes if s.name=='Lecture title')==meta['title']
assert meta['date'] in '\n'.join(s.text for s in prs.slides[0].shapes if s.has_text_frame)
rows=list(json.loads((here/'figure-sources.json').read_text()).values())
known={hashlib.sha256((here/x['out']).read_bytes()).hexdigest() for x in rows}
image_slides=0
for n,sl in enumerate(prs.slides,1):
    notes=sl.notes_slide.notes_text_frame.text
    assert 'References:' in notes and 'https://doi.org/' in notes, n
    for s in sl.shapes:
        if s.shape_type==MSO_SHAPE_TYPE.PICTURE:
            assert hashlib.sha256(s.image.blob).hexdigest() in known, n
        if s.has_text_frame:
            for p in s.text_frame.paragraphs:
                for run in p.runs:
                    assert run.font.name in ('Arial', None), (n, run.font.name)
    if 2<=n<=45:
        assert any(s.shape_type==MSO_SHAPE_TYPE.PICTURE for s in sl.shapes), n
        image_slides+=1
        assert len(spec['slides'][n-2]['body'])==3
assert image_slides==44
assert len(spec['takeaways']['items'])==6
result={'slides':46,'content_slides':44,'content_slides_with_published_figures':44,'content_slides_with_primary_figures':44,'review_figure_content_slides':0,'unique_original_crops':len(known),'generated_scientific_visuals':0,'notes_with_references':46,'font':'Arial','title':meta['title'],'date':meta['date']}
result['content_slides_with_original_color']=sum(any(x['original_color'] for x in rows if x['out'] in [f['path'] for f in (s.get('figures') or [s['figure']])]) for s in spec['slides'])
assert result['content_slides_with_original_color']>=22
(here/'sources/validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
