import zipfile,posixpath as pp,lxml.etree as E,json,hashlib,os
from pathlib import Path
import urllib.request
HERE=Path(__file__).resolve().parent
CACHE=HERE/'papers'/'source_decks';CACHE.mkdir(parents=True,exist_ok=True)
base=str(CACHE/'latest.pptx');old=str(CACHE/'with_ito.pptx')
for path,sha in [(base,'6c0ae35adcda4f0ff2e1bb5de7cb9009d2e92094'),(old,'bc97bb7af733ffd501e9bd24f1b5b61152187d89')]:
 if not Path(path).exists():
  urllib.request.urlretrieve(f'https://raw.githubusercontent.com/jordanxxlopez/NEUROETHOLOGY/{sha}/lectures/L91/Neuroethology_Lecture91_FA2026.pptx',path)
out=str(HERE/'Neuroethology_Lecture91_FA2026_Expanded_51Slides.pptx')
os.makedirs(pp.dirname(out),exist_ok=True)
B={n:z.read(n) for z in [zipfile.ZipFile(base)] for n in z.namelist()}; O={n:z.read(n) for z in [zipfile.ZipFile(old)] for n in z.namelist()}
R='http://schemas.openxmlformats.org/package/2006/relationships'; P='http://schemas.openxmlformats.org/presentationml/2006/main'; A='http://schemas.openxmlformats.org/drawingml/2006/main'; RR='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
mp={f'ppt/slides/slide{i}.xml':f'ppt/slides/slide{i+6}.xml' for i in range(41,46)}
seen=set(); imported=[]
def relpath(n):return pp.join(pp.dirname(n),'_rels',pp.basename(n)+'.rels')
def xml(x):return E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
def imp(n):
 if n in seen:return mp[n]
 if n not in mp:
  if n in B and O[n]==B[n]:mp[n]=n; return n
  mp[n]=pp.join(pp.dirname(n),'ito_restored_'+pp.basename(n))
 dest=mp[n];seen.add(n);imported.append((n,dest));B[dest]=O[n]
 rel=relpath(n)
 if rel in O:
  root=E.fromstring(O[rel])
  for r in root:
   if r.get('TargetMode')=='External':continue
   target=pp.normpath(pp.join(pp.dirname(n),r.get('Target')))
   nd=imp(target);r.set('Target',pp.relpath(nd,pp.dirname(dest)))
  B[relpath(dest)]=xml(root)
 return dest
for i in range(41,46):imp(f'ppt/slides/slide{i}.xml')
for i in range(41,46):
 n=mp[f'ppt/slides/slide{i}.xml'];r=E.fromstring(B[n])
 for t in r.iter('{'+A+'}t'):
  if t.text==str(i):t.text=str(i+5)
 B[n]=xml(r)
# Correct the original generalization about rat/human movement phase.
n=mp['ppt/slides/slide43.xml'];r=E.fromstring(B[n])
for t in r.iter('{'+A+'}t'):
 if t.text and t.text.startswith('Inspection of the stimulus and motion timing'):
  t.text='Rat movement peaks were more reactive than human peaks, although rising jerk preceded some beats. Shared sensitivity to the musical rate therefore coexisted with differences in phase alignment. In both preparations, listening produced beat-related movement without Ronan’s explicit reinforcement of head bobs.'
B[n]=xml(r)
r=E.fromstring(B['ppt/slides/slide46.xml'])
for t in r.iter('{'+A+'}t'):
 if t.text=='46':t.text='51'
 if t.text=='Experience and comparison':t.text='Comparative rhythm and adaptation'
 if t.text and t.text.lstrip().startswith('An experienced sea lion performed precisely'):
  t.text=' Ronan’s trained synchronization and spontaneous rat movements used different tasks; rat auditory responses favored intermediate rates, which an adaptation model reproduced.'
B['ppt/slides/slide46.xml']=xml(r)
pr=E.fromstring(B['ppt/presentation.xml']);rels=E.fromstring(B['ppt/_rels/presentation.xml.rels']);lst=pr.find('{'+P+'}sldIdLst');take=lst[-1];lst.remove(take)
num=max(int(x.get('Id')[3:]) for x in rels if x.get('Id','').startswith('rId'))
sid=max(int(x.get('id')) for x in lst)+1
for k,i in enumerate(range(41,46),1):
 rid='rId'+str(num+k);E.SubElement(rels,'{'+R+'}Relationship',Id=rid,Type=RR+'/slide',Target=pp.relpath(mp[f'ppt/slides/slide{i}.xml'],'ppt'))
 E.SubElement(lst,'{'+P+'}sldId',id=str(sid+k),attrib={'{'+RR+'}id':rid})
lst.append(take);B['ppt/presentation.xml']=xml(pr);B['ppt/_rels/presentation.xml.rels']=xml(rels)
ct=E.fromstring(B['[Content_Types].xml']);oct=E.fromstring(O['[Content_Types].xml']);types={x.get('PartName'):x.get('ContentType') for x in oct if x.tag.endswith('Override')};exists={x.get('PartName') for x in ct}
for src,dest in imported:
 if '/'+src in types and '/'+dest not in exists:E.SubElement(ct,ct.tag.replace('Types','Override'),PartName='/'+dest,ContentType=types['/'+src])
B['[Content_Types].xml']=xml(ct)
r=E.fromstring(B['docProps/app.xml'])
for t in r:
 if t.tag.endswith('Slides'):t.text='51'
B['docProps/app.xml']=xml(r)
# Keep restored notes consistent with the corrected phase comparison.
for src,dest in imported:
 if src.startswith('ppt/notesSlides/notesSlide43.xml'):
  r=E.fromstring(B[dest])
  for t in r.iter('{'+A+'}t'):
   if t.text and 'Inspection of the stimulus and motion timing' in t.text:
    t.text='• Rat movement peaks were more reactive than human peaks, although rising jerk preceded some beats. Shared sensitivity to the musical rate therefore coexisted with differences in phase alignment. In both preparations, listening produced beat-related movement without Ronan’s explicit reinforcement of head bobs.'
  B[dest]=xml(r)
 if src=='ppt/notesSlides/notesSlide42.xml':
  r=E.fromstring(B[dest])
  for t in r.iter('{'+A+'}t'):
   if t.text and t.text.startswith('Embedded recording:'):
    t.text+=' The freely moving standing-rat preparation included Mozart K.448 and the pop recordings Born This Way (Lady Gaga), Another One Bites the Dust (Queen), Beat It (Michael Jackson), and Sugar (Maroon 5). This preparation differed from the controlled head-accelerometer experiment using altered playback speeds of Mozart.'
  B[dest]=xml(r)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for n,v in B.items():z.writestr(n,v)
# Validate package target integrity and unchanged original content.
from pptx import Presentation
p=Presentation(out);assert len(p.slides)==51
for i in range(1,46):assert B[f'ppt/slides/slide{i}.xml']==zipfile.ZipFile(base).read(f'ppt/slides/slide{i}.xml')
movies=[n for n in B if n.startswith('ppt/media/') and n.endswith('.mp4')];assert len(movies)==20,len(movies)
for n in B:
 if n.endswith('.rels'):
  owner=pp.join(pp.dirname(pp.dirname(n)),pp.basename(n)[:-5]) if n!='_rels/.rels' else ''
  for x in E.fromstring(B[n]):
   if x.get('TargetMode')!='External':
    target=pp.normpath(pp.join(pp.dirname(owner),x.get('Target'))).lstrip('/')
    assert target in B,(n,target)
print(out,os.path.getsize(out),'bytes; 51 slides; 20 embedded MP4 files; original slides 1–45 byte-identical')
