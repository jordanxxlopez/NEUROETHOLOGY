"""Create a sub-40 MB delivery copy; preserve all original slide/figure parts.
Higher-compression H.264 videos retain original resolution, timing and audio.
"""
import subprocess,json,zipfile,hashlib
from lxml import etree
from pathlib import Path
import tempfile
base=Path(__file__).resolve().parent
work=tempfile.TemporaryDirectory(prefix='neur83-compact-')
out=Path(work.name)
m=json.load(open(base/'media_sources.json'));replacement={}
for i,item in enumerate(m['embedded']):
 src=base/item['path'];dst=out/src.name
 bitrate={5:'150k',6:'220k',23:'350k',27:'400k',38:'400k'}[item['slide']]
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-map','0:v:0','-map','0:a?','-c:v','libx264','-preset','slow','-b:v',bitrate,'-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart',str(dst)],check=True)
 subprocess.run(['ffmpeg','-v','error','-i',str(dst),'-f','null','-'],check=True)
 def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
 a=probe(src);b=probe(dst);av=next(s for s in a['streams']if s['codec_type']=='video');bv=next(s for s in b['streams']if s['codec_type']=='video')
 assert (av['width'],av['height'])==(bv['width'],bv['height'])
 assert abs(float(a['format']['duration'])-float(b['format']['duration']))<.06
 replacement[hashlib.sha256(src.read_bytes()).hexdigest()]=dst
 print(src.name,src.stat().st_size,'->',dst.stat().st_size,flush=True)
source=base/'Neuroethology_Lecture83_FA2026.pptx';target=base/'Neuroethology_Lecture83_FA2026_under40MB.pptx'
with zipfile.ZipFile(source) as zin,zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED)as zout:
 for item in zin.infolist():
  data=zin.read(item.filename)
  if item.filename.endswith('.mp4'):data=replacement[hashlib.sha256(data).hexdigest()].read_bytes()
  if item.filename.startswith('ppt/notesSlides/notesSlide') and item.filename.endswith('.xml'):
   root=etree.fromstring(data)
   for t in root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
    if t.text and t.text.startswith('Compatibility:'):
     t.text='Compatibility: This download copy uses more compressed H.264 MP4 media to stay below 40 MB. Original dimensions, full scene, timing, and audio where present are retained. Compression may soften video details; original article figures and source-frame posters remain unchanged.'
   data=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
  zout.writestr(item,data)
assert target.stat().st_size<40_000_000,target.stat().st_size
print('Verified PPTX bytes',target.stat().st_size,flush=True)

work.cleanup()
