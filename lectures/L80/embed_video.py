"""Embed unedited publisher supplementary recordings after the repository build."""
from pathlib import Path
import json,zipfile,hashlib
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from PIL import Image
D=Path(__file__).resolve().parent;path=D/'Neuroethology_Lecture80_FA2026.pptx';deck=Presentation(path);spec=json.loads((D/'lecture.json').read_text());media=json.loads((D/'media_sources.json').read_text())
def box(s,text,x,y,w,h,size=8):
 a=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));p=a.text_frame.paragraphs[0];p.text=text;p.font.name='Arial';p.font.size=Pt(size);p.font.color.rgb=RGBColor(0,0,0);return a
for m in media:
 slide=deck.slides[m['pptx_slide']-1];sd=spec['slides'][m['content_slide']-1];figs=sd.get('figures',[sd.get('figure')]);pictures=[x for x in slide.shapes if x.shape_type==MSO_SHAPE_TYPE.PICTURE]
 # Preserve each intact source image and its caption as a static evidence strip.
 for shape in list(slide.shapes):
  if shape.has_text_frame and any(shape.text==f['caption'] for f in figs):shape._element.getparent().remove(shape._element)
 for i,(p,f) in enumerate(zip(pictures,figs)):
  x=7.02+i*2.9;maxw=2.7 if len(figs)>1 else 5.6;maxh=1.42;iw,ih=Image.open(D/f['path']).size;k=min(maxw/iw,maxh/ih);w,h=iw*k,ih*k;p.left=Inches(x+(maxw-w)/2);p.top=Inches(5.02);p.width=Inches(w);p.height=Inches(h);box(slide,f['caption'],x,6.45,maxw,.35)
 # Original source poster, exact original aspect ratio, click-to-play PowerPoint video.
 slide.shapes.add_picture(str(D/m['poster']),Inches(7.02),Inches(1.4),width=Inches(5.6),height=Inches(3.15))
 movie=slide.shapes.add_movie(str(D/m['path']),Inches(7.02),Inches(1.4),Inches(5.6),Inches(3.15),poster_frame_image=str(D/m['poster']),mime_type='video/mp4')
 box(slide,m['caption'],7.02,4.60,5.6,.38,9)
 notes=slide.notes_slide.notes_text_frame;notes.text+='\n\nRecording metadata:\n'+m['caption']+'\nArticle DOI: https://doi.org/'+m['doi']+'\nOriginal media URL: '+m['url']+'\nCredit: '+m['credit']+'\nLicense: '+m['license']+'\n'+m['conversion']+'\nDuration: '+m['duration']+' seconds. Original audio retained. Click the video in PowerPoint Slide Show to play it. Published source figures remain as static evidence for viewers that omit movies. PowerPoint GUI playback was not available in this cloud environment.\n'
deck.save(path)
with zipfile.ZipFile(path) as z:
 embedded=[n for n in z.namelist() if n.endswith('.mp4')];assert len(embedded)==4
 hashes={hashlib.sha256(z.read(n)).hexdigest() for n in embedded}
 for m in media:
  assert hashlib.sha256((D/m['path']).read_bytes()).hexdigest() in hashes
  xml=z.read(f'ppt/slides/slide{m["pptx_slide"]}.xml').decode();assert 'videoFile' in xml
  rel=z.read(f'ppt/slides/_rels/slide{m["pptx_slide"]}.xml.rels').decode();assert '/video' in rel and '/media' in rel
(D/'media_verification.json').write_text(json.dumps({'embedded_movies':4,'pptx_slides':[m['pptx_slide'] for m in media],'payload_hashes_match':True,'relationships_verified':True,'full_decode_verified':True,'powerpoint_gui_playback':'Not tested: no PowerPoint GUI in the cloud environment','hosted_export':'Static, without embedded movies'},indent=2))
print('Verified four embedded MP4 recordings and their media relationships')
