"""Verify native-media delivery and preservation of unaffected slides."""
from pathlib import Path
import hashlib,json,subprocess,zipfile
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
R=Path(__file__).resolve().parent
p=R/'Neuroethology_Lecture91_FA2026.pptx';prs=Presentation(p)
assert len(prs.slides)==46
assert any(x.has_text_frame and x.text=='Key takeaways' for x in prs.slides[-1].shapes)
sources=json.loads((R/'media_sources.json').read_text())
assert sources['qualifying_sea_lion_study_video_count']==12
rows=[]
for source in sources['sources']:
 sl=prs.slides[source['slide']-1];movies=[x for x in sl.shapes if x.shape_type==MSO_SHAPE_TYPE.MEDIA];assert len(movies)==1
 movie=movies[0];rel=movie._element.xpath(".//*[local-name()='media']")[0];rid=rel.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed');blob=sl.part.rels[rid].target_part.blob
 assert hashlib.sha256(blob).hexdigest()==source['sha256']
 path=R/source['file'];v=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(path)]));vid=next(x for x in v['streams'] if x['codec_type']=='video');dar=vid.get('display_aspect_ratio');ratio= float(dar.split(':')[0])/float(dar.split(':')[1]) if dar and dar!='0:1' else vid['width']/vid['height'];assert abs(movie.width/movie.height-ratio)<.002
 subprocess.run(['ffmpeg','-hide_banner','-v','error','-i',str(path),'-f','null','-'],check=True)
 rows.append({'slide':source['slide'],'embedded_sha_verified':True,'decoded_entire_clip':True,'aspect_ratio_verified':True})
baseline=Path('/workspace/scratch/L91/hearing/baseline.pptx')
def fingerprint(sl):
 a=[]
 for x in sl.shapes:
  value=[int(x.shape_type),x.left,x.top,x.width,x.height]
  if x.has_text_frame:value.append(x.text)
  if x.shape_type==MSO_SHAPE_TYPE.PICTURE:value.append(hashlib.sha256(x.image.blob).hexdigest())
  if x.shape_type==MSO_SHAPE_TYPE.MEDIA:
   rid=x._element.xpath(".//*[local-name()='media']")[0].get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed');value.append(hashlib.sha256(sl.part.rels[rid].target_part.blob).hexdigest())
  a.append(value)
 return a
if baseline.exists():
 b=Presentation(baseline)
 for n in [n for n in range(1,47) if n!=44]:
  assert fingerprint(b.slides[n-1])==fingerprint(prs.slides[n-1]),f'Slide {n} changed'
  assert b.slides[n-1].notes_slide.notes_text_frame.text==prs.slides[n-1].notes_slide.notes_text_frame.text,f'Slide {n} notes changed'
assert p.stat().st_size<100*1024*1024, p.stat().st_size
out={'slide_count':46,'content_slide_count':44,'embedded_clip_count':len(rows),'distinct_sea_lion_study_recordings':12,'preserved_slides':[n for n in range(1,47) if n!=44] if baseline.exists() else 'comparison not run; baseline unavailable','size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'powerpoint_GUI_playback':'untested','google_slides_import':'untested; may require separate Drive media insertion','clips':rows}
(R/'delivery_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='clips'},indent=2))
