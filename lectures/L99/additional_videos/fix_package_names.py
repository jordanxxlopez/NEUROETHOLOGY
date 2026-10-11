"""Normalize the extensionless movie part without changing slide or media bytes."""
from pathlib import Path
import zipfile,json,hashlib,posixpath,collections
from lxml import etree
B=Path(__file__).resolve().parents[1]
src=B/'deliverables/Neuroethology_Lecture99_FA2026_21Videos.pptx';out=B/'deliverables/Neuroethology_Lecture99_FA2026_21Videos_Fixed.pptx'
old='ppt/media/media18.';new='ppt/media/media18.mp4';changes=[];names=[]
with zipfile.ZipFile(src) as a,zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as b:
 assert old in a.namelist() and new not in a.namelist()
 for info in a.infolist():
  data=a.read(info);name=info.filename
  if name=='[Content_Types].xml':data=data.replace(('/'+old+'"').encode(),('/'+new+'"').encode())
  elif name.endswith('.rels'):data=data.replace(b'../media/media18."',b'../media/media18.mp4"')
  if name==old:name=new
  if data!=a.read(info) or name!=info.filename:changes.append({'before':info.filename,'after':name,'bytes_unchanged':data==a.read(info)})
  info.filename=name;b.writestr(info,data)
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','p14':'http://schemas.microsoft.com/office/powerpoint/2010/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with zipfile.ZipFile(src) as a,zipfile.ZipFile(out) as b:
 assert b.testzip() is None
 assert len(set(b.namelist()))==len(b.namelist())
 assert all(all(s and not s.endswith('.') and s not in ('.','..') for s in n.split('/')) for n in b.namelist())
 changed_files={x['before'] for x in changes};assert changed_files=={old,'[Content_Types].xml','ppt/slides/_rels/slide4.xml.rels'},changed_files
 for name in a.namelist():
  if name not in changed_files:assert a.read(name)==b.read(name),name
 assert a.read(old)==b.read(new)
 movie_count=0;relationship_count=0
 for name in b.namelist():
  if name.endswith(('.xml','.rels')):root=etree.fromstring(b.read(name))
  if name.endswith('.rels'):
   ids=[r.get('Id') for r in root];assert len(set(ids))==len(ids),name
   base=posixpath.dirname(posixpath.dirname(name))
   for r in root:
    if r.get('TargetMode')=='External':continue
    t=r.get('Target');target=t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(base,t));assert target in b.namelist(),(name,target);relationship_count+=1
  if name.startswith('ppt/slides/slide') and name.endswith('.xml'):
   ids=root.xpath('.//p:cNvPr/@id',namespaces=ns);assert len(ids)==len(set(ids)),name
   tids=root.xpath('.//p:cTn/@id',namespaces=ns);assert len(tids)==len(set(tids)),name
   for spid in root.xpath('.//p:spTgt/@spid',namespaces=ns):assert spid in ids,(name,spid)
   relname=posixpath.dirname(name)+'/_rels/'+posixpath.basename(name)+'.rels';rels={r.get('Id'):r.get('Target') for r in etree.fromstring(b.read(relname))}
   for video in root.findall('.//a:videoFile',ns):
    movie_count+=1;target=rels[video.get('{'+ns['r']+'}link')];assert target.endswith('.mp4'),(name,target)
   for media in root.findall('.//p14:media',ns):assert rels[media.get('{'+ns['r']+'}embed')].endswith('.mp4')
 assert movie_count==21
report=dict(file=str(out),cause='Embedded movie part ppt/media/media18. had a trailing period and no extension. Rename to media18.mp4 and update both slide-4 references and content-type entry.',changes=changes,all_slide_xml_byte_identical=True,all_notes_and_layouts_byte_identical=True,all_original_media_byte_identical=True,package_names_canonical=True,zip_crc='passed',xml_parsing='passed',relationships=relationship_count,movies=movie_count,slides=46,bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest(),desktop_powerpoint_test='Not available; actual repair-free opening cannot be confirmed in this environment.')
(B/'additional_videos/repair_fix_validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
