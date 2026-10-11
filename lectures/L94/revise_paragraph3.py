"""Change only paragraph 3 and its matching transcript on 20 specified slides.
Patch the existing 32-video PPTX without rebuilding or modifying any media.
"""
from pathlib import Path
import json,copy,zipfile,hashlib
from lxml import etree
B=Path(__file__).resolve().parent
spec_path=B/'lecture.json';spec=json.loads(spec_path.read_text());revisions=json.loads((B/'paragraph3_revisions.json').read_text())
source=B/'deliverables/Neuroethology_Lecture94_FA2026_32videos.pptx';output=B/'deliverables/Neuroethology_Lecture94_FA2026_Paragraph3_Revised.pptx'
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'};patches={};audit=[]
with zipfile.ZipFile(source)as original:
 for number,new in revisions.items():
  slide=spec['slides'][int(number)-2];old=slide['body'][2]
  # Repeated execution uses the preserved prior deck, so its original paragraph is authoritative.
  slide_xml=original.read(f'ppt/slides/slide{number}.xml');root=etree.fromstring(slide_xml)
  paragraphs=root.findall('.//a:p',ns)
  old=''.join(t.text or ''for t in paragraphs[3].findall('.//a:t',ns))
  for name in [f'ppt/slides/slide{number}.xml',f'ppt/notesSlides/notesSlide{number}.xml']:
   raw=original.read(name);root=etree.fromstring(raw);found=[]
   for par in root.findall('.//a:p',ns):
    ts=par.findall('.//a:t',ns);text=''.join(t.text or ''for t in ts)
    if text in [old,'• '+old]:found.append((par,ts,text))
   assert len(found)==1,(name,len(found))
   par,ts,text=found[0];before=copy.deepcopy(root);ts[0].text=('• 'if text.startswith('• ')else'')+new
   for t in ts[1:]:t.text=''
   # Restore only the target text nodes and require identical structural XML.
   test=copy.deepcopy(root);p2=test.findall('.//a:p',ns)[root.findall('.//a:p',ns).index(par)]
   for t,original_t in zip(p2.findall('.//a:t',ns),before.findall('.//a:p',ns)[root.findall('.//a:p',ns).index(par)].findall('.//a:t',ns)):t.text=original_t.text
   assert etree.tostring(test)==etree.tostring(before)
   patches[name]=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
  assert len(slide['body'])==3 and len(slide['transcript'])==3
  slide['body'][2]=new;slide['transcript'][2]=new
  audit.append({'slide':int(number),'old_paragraph3':old,'new_paragraph3':new})
 with zipfile.ZipFile(output,'w')as revised:
  for info in original.infolist():revised.writestr(info,patches.get(info.filename,original.read(info.filename)))
with zipfile.ZipFile(source)as original,zipfile.ZipFile(output)as revised:
 changed=[n for n in original.namelist()if original.read(n)!=revised.read(n)];assert set(changed)==set(patches)
 assert all(original.read(n)==revised.read(n)for n in original.namelist()if n.startswith('ppt/media/'))
spec_path.write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'paragraph3_revision_audit.json').write_text(json.dumps({'slides':audit,'changed_package_parts':changed,'all_media_unchanged':True,'source_file':source.name,'output_file':output.name,'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()},indent=2,ensure_ascii=False)+'\n')
print('Only paragraph 3 and matching notes changed on',len(audit),'slides; all other package parts and all media unchanged.')
print(output,output.stat().st_size)
