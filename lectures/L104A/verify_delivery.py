"""Check embedded original media, native ratios, teaching text, and scoped counts."""
from pathlib import Path
import hashlib,json,subprocess,zipfile,re
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
R=Path(__file__).resolve().parent;p=R/'Neuroethology_Lecture104A_FA2026.pptx';prs=Presentation(p);spec=json.loads((R/'lecture.json').read_text());sources=json.loads((R/'media_sources.json').read_text());assert len(prs.slides)==46;assert sources['embedded_video_count']==20;assert sources['distinct_original_recordings']==20
movie_count=sum(x.shape_type==MSO_SHAPE_TYPE.MEDIA for sl in prs.slides for x in sl.shapes);assert movie_count==20
for n,sd in enumerate(spec['slides'],2):
 sl=prs.slides[n-1];body=next(x for x in sl.shapes if x.name=='Body');clean=lambda t:re.sub(r'_([^_]+)_',r'\1',re.sub(r'\*\*(.*?)\*\*',r'\1',t))
 assert [x.text for x in body.text_frame.paragraphs]==[clean(t) for t in sd['body']],f'Teaching text differs on slide {n}'
 assert len(sd['body'])==3
 for para in sd['body']:assert 5<=len(re.findall(r'[.!?](?:\s|$)',para))<=7
 assert all(r.font.name=='Arial' for shape in sl.shapes if shape.has_text_frame for pa in shape.text_frame.paragraphs for r in pa.runs)
extra=sum(f.get('role')=='additional animal or anatomical image' for sd in spec['slides'] for f in sd.get('figures',[]));assert extra==35
checks=[]
for x in sources['sources']:
 sl=prs.slides[x['slide']-1];movie=next(s for s in sl.shapes if s.name==Path(x['file']).stem);rel=movie._element.xpath(".//*[local-name()='media']")[0];rid=rel.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed');blob=sl.part.rels[rid].target_part.blob;assert hashlib.sha256(blob).hexdigest()==x['delivery_sha256'];assert abs(movie.width/movie.height-x['native_aspect_ratio'])<.002
 assert hashlib.sha256((R/x['file']).read_bytes()).hexdigest()==x['original_sha256']
 def probe(f):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]))
 orig=probe(R/x['file']);deliver=probe(R/x['delivery_file']);assert abs(float(orig['format']['duration'])-float(deliver['format']['duration']))<.15
 oa=[s for s in orig['streams'] if s['codec_type']=='audio'];da=[s for s in deliver['streams'] if s['codec_type']=='audio'];assert bool(oa)==bool(da)
 subprocess.run(['ffmpeg','-v','error','-i',str(R/x['delivery_file']),'-f','null','-'],check=True)
 checks.append({'slide':x['slide'],'source_identifier':x['original_identifier'],'embedded_sha_verified':True,'native_aspect_verified':True,'entire_recording_decoded':True,'duration_preserved':True,'audio_presence_preserved':True})
assert p.stat().st_size<100*1024*1024,p.stat().st_size
out={'slide_count':46,'content_slide_count':44,'embedded_recordings':20,'distinct_original_recordings':20,'experimental_recordings':17,'author_figure_presentations':3,'additional_companion_images':extra,'teaching_text_matches_spec':True,'paragraphs_per_content_slide':3,'sentences_per_paragraph':'5–7','size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'desktop_powerpoint_GUI_playback':'untested','google_slides_import':'untested; may require separate Drive media insertion','media_checks':checks}
(R/'delivery_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='media_checks'},indent=2))
