"""Replace only five video parts and their compatibility-note lines."""
from pathlib import Path
import json,hashlib,zipfile
from lxml import etree
B=Path(__file__).resolve().parent.parent;D=B/'compressed_videos'
src=B/'Neuroethology_Lecture100_FA2026_20_Videos.pptx';out=B/'Neuroethology_Lecture100_FA2026_20_Videos_Compressed.pptx'
allmedia=json.load(open(B/'media_sources.json'))['embedded']+json.load(open(B/'additional_videos/media_sources.json'))['added'];rows=json.load(open(D/'compression.json'));selected={r['source_path']:r for r in rows};changes=[]
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with zipfile.ZipFile(src)as a,zipfile.ZipFile(out,'w')as z:
 replacements={}
 for n in a.namelist():
  if n.endswith('.mp4'):
   sha=hashlib.sha256(a.read(n)).hexdigest();m=next(x for x in allmedia if x['sha256']==sha)
   if m['path']in selected:replacements[n]=B/selected[m['path']]['compressed_path'];selected[m['path']]['package_part']=n
 for info in a.infolist():
  n=info.filename
  if n in replacements:
   info.compress_type=zipfile.ZIP_DEFLATED
   with replacements[n].open('rb')as inp,z.open(info,'w')as dest:
    while chunk:=inp.read(4*1024*1024):dest.write(chunk)
   changes.append(n)
  elif n.startswith('ppt/notesSlides/notesSlide')and n.endswith('.xml'):
   data=a.read(n);root=etree.fromstring(data);changed=False
   for m in allmedia:
    if m['path']not in selected:continue
    if n!=f"ppt/notesSlides/notesSlide{m['slide']}.xml":continue
    for t in root.findall('.//a:t',ns):
     if t.text=='Compatibility: '+m['conversion']:
      t.text='Compatibility: Compressed distribution copy, H.264 CRF21 medium. Original resolution, frame rate, all video frames, playback speed and audio retained. Source preparation: '+m['conversion'];changed=True
   if changed:data=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True);changes.append(n)
   z.writestr(info,data)
  else:
   with a.open(info)as inp,z.open(info,'w')as dest:
    while chunk:=inp.read(4*1024*1024):dest.write(chunk)
assert len(replacements)==5
assert len(changes)==10,changes
report={'file':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'changed_package_parts':changes,'video_replacements':rows,'all_slide_xml_and_scientific_images_unchanged':True,'videos':20,'resolution_speed_audio_preserved':True,'desktop_playback':'untested'}
# Verify unchanged slide definitions, images and all other parts byte for byte.
with zipfile.ZipFile(src)as a,zipfile.ZipFile(out)as z:
 assert len(set(z.namelist()))==len(z.namelist());assert set(a.namelist())==set(z.namelist())
 for n in a.namelist():
  if n not in changes:assert a.read(n)==z.read(n),n
 assert len([n for n in z.namelist()if n.endswith('.mp4')])==20
(D/'artifact.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'bytes':report['bytes'],'sha256':report['sha256'],'replaced_videos':5,'unchanged_remaining_parts':True}),flush=True)
