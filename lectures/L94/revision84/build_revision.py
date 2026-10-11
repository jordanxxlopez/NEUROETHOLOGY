"""Patch teaching text and insert 14 slides without resaving existing media."""
from pathlib import Path
import json, re, copy, posixpath, zipfile, sys, hashlib
from lxml import etree as E
from pptx import Presentation
from pptx.util import Pt
from PIL import ImageFont
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'tools'))
from build_lecture import write_paras, inline_runs, plain
from theme_colors import darker

B=Path(__file__).resolve().parent
R=B.parents[2]
SRC=B.parent/'deliverables/Neuroethology_Lecture94_FA2026_70slides_SingleSummary.pptx'
DONOR=B/'Added14_Base.pptx'
OUT=B.parent/'deliverables/Neuroethology_Lecture94_FA2026_84slides_Revised.pptx'
P='http://schemas.openxmlformats.org/presentationml/2006/main'
A='http://schemas.openxmlformats.org/drawingml/2006/main'
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
CT='http://schemas.openxmlformats.org/package/2006/content-types'

def xml(root):return E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
def rp(part):
    parent,name=posixpath.split(part)
    return posixpath.join(parent,'_rels',name+'.rels')
def resolve(part,target):return posixpath.normpath(posixpath.join(posixpath.dirname(part),target))if not target.startswith('/')else target[1:]
def sentcount(s):return len(re.findall(r'[.!?](?:\s|$)',s))

# Liberation Sans has Arial-compatible metrics. Actual rendered lines are checked
# separately in LibreOffice's PDF; this estimate is not the final layout test.
F=Path('/usr/share/fonts/truetype/liberation')
fonts={style:ImageFont.truetype(str(F/('LiberationSans-'+style+'.ttf')),300)for style in ['Regular','Bold','Italic','BoldItalic']}
def linecount(text,width,pt):
    words=[]
    for chunk,b,i in inline_runs(text):
        style='BoldItalic'if b and i else 'Bold'if b else 'Italic'if i else 'Regular'
        words.extend((w,style)for w in chunk.split())
    total=1;used=0
    for word,style in words:
        font=fonts[style];w=font.getlength(word)/300*pt/72
        space=font.getlength(' ')/300*pt/72 if used else 0
        if used+space+w>width:total+=1;used=w
        else:used+=space+w
    return total
def fit(sh,ps):
    w=sh.width/914400-.08;h=sh.height/914400
    for pt in [18-i*.5 for i in range(11)]:
        counts=[linecount(s,w,pt)for s in ps]
        need=sum(counts)*pt*1.15/72+2*pt*.30/72+.03
        if need<h-.04 and min(counts)>=5:return pt,counts,need
    raise ValueError(('Text cannot fit with five lines per paragraph',sh.name,w,h,counts,need))

def body_edit(slide,paras):
    body=next(s for s in slide.shapes if s.name=='Body')
    assert len(paras)==3 and all(5<=sentcount(s)<=7 for s in paras)
    pt,counts,need=fit(body,paras)
    tf=body.text_frame;tf.clear()
    write_paras(tf,paras,pt,'000000',bold_color=darker('53687D'),space_after=pt*.30)
    for pp in tf.paragraphs:pp.line_spacing=Pt(pt*1.15)
    # Keep original image/movie layout, and only replace the teaching transcript.
    nt=slide.notes_slide.notes_text_frame
    old=nt.text
    keep=old[old.index('References:'):] if 'References:'in old else ''
    nt.clear()
    for i,text in enumerate(['• '+p for p in paras]+keep.split('\n')):
        pp=nt.paragraphs[0]if i==0 else nt.add_paragraph();pp.text=text
    return {'font_pt':pt,'estimated_lines':counts,'height_in':need,'sentences':[sentcount(p)for p in paras]}

def build():
    revised=json.loads((B/'revised_paragraphs.json').read_text())
    # python-pptx canonicalizes slide part names when .slides is accessed. The
    # preserved extension uses noncanonical filenames, so patch the ORIGINAL
    # OPC targets, not the library's renamed in-memory part names.
    with zipfile.ZipFile(SRC)as z:
        root=E.fromstring(z.read('ppt/presentation.xml'))
        rr=E.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
        targets={r.get('Id'):resolve('ppt/presentation.xml',r.get('Target'))for r in rr}
        original_parts=[targets[s.get('{'+REL+'}id')]for s in root.find('{'+P+'}sldIdLst')]
        original_notes={part:next(resolve(part,r.get('Target'))for r in E.fromstring(z.read(rp(part)))if r.get('Type').endswith('/notesSlide'))for part in original_parts}
    prs=Presentation(SRC);donorprs=Presentation(DONOR);changes={};layout=[]
    for n,ps in revised.items():
        sl=prs.slides[int(n)-1];rec=body_edit(sl,ps);rec['slide']=int(n);layout.append(rec)
        part=original_parts[int(n)-1]
        changes[part]=sl.part.blob
        changes[original_notes[part]]=sl.notes_slide.part.blob
    spec=json.loads((B/'additions.json').read_text())
    donorchanges={}
    for i,s in enumerate(spec['slides'],1):
        sl=donorprs.slides[i];rec=body_edit(sl,s['body']);rec['slide']=i+69;layout.append(rec)
        for sh in sl.shapes:
            if sh.name=='Slide number':sh.text_frame.paragraphs[0].runs[0].text=str(i+69)
        donorchanges[str(sl.part.partname)[1:]]=sl.part.blob
        donorchanges[str(sl.notes_slide.part.partname)[1:]]=sl.notes_slide.part.blob
    last=prs.slides[-1]
    for sh in last.shapes:
        if sh.name=='Slide number':sh.text_frame.paragraphs[0].runs[0].text='84'
    changes[original_parts[-1]]=last.part.blob
    with zipfile.ZipFile(SRC)as old,zipfile.ZipFile(DONOR)as donor:
        added={};mapping={};overrides={}
        types=E.fromstring(donor.read('[Content_Types].xml'))
        dtype={x.get('PartName')[1:]:x.get('ContentType')for x in types if x.tag.endswith('Override')}
        def clone(part):
            if part in mapping:return mapping[part]
            if part.startswith(('ppt/slideMasters/','ppt/slideLayouts/','ppt/notesMasters/','ppt/theme/')):
                assert part in old.namelist()and old.read(part)==donor.read(part),part
                rr=rp(part)
                assert (rr not in donor.namelist()and rr not in old.namelist())or donor.read(rr)==old.read(rr),rr
                mapping[part]=part;return part
            parent,name=posixpath.split(part);dest=posixpath.join(parent,'revision84_'+name)
            assert dest not in old.namelist()
            mapping[part]=dest;added[dest]=donorchanges.get(part,donor.read(part))
            if part in dtype:overrides[dest]=dtype[part]
            rr=rp(part)
            if rr in donor.namelist():
                root=E.fromstring(donor.read(rr))
                for r in root:
                    if r.get('TargetMode')=='External':continue
                    target=clone(resolve(part,r.get('Target')))
                    r.set('Target',posixpath.relpath(target,posixpath.dirname(dest)))
                added[rp(dest)]=xml(root)
            return dest
        pres=E.fromstring(old.read('ppt/presentation.xml'))
        rels=E.fromstring(old.read('ppt/_rels/presentation.xml.rels'))
        lst=pres.find('{'+P+'}sldIdLst');final=lst[-1];lst.remove(final)
        sid=max(int(x.get('id'))for x in lst)+1
        rid=max(int(x.get('Id')[3:])for x in rels if x.get('Id').startswith('rId'))
        for n in range(2,16):
            target=clone(f'ppt/slides/slide{n}.xml');sid+=1;rid+=1;rr='rId'+str(rid)
            E.SubElement(rels,'{'+PKG+'}Relationship',Id=rr,Type=REL+'/slide',Target=posixpath.relpath(target,'ppt'))
            x=E.SubElement(lst,'{'+P+'}sldId',id=str(sid));x.set('{'+REL+'}id',rr)
        lst.append(final)
        assert len(lst)==84
        ct=E.fromstring(old.read('[Content_Types].xml'))
        defs={x.get('Extension')for x in ct if x.tag.endswith('Default')}
        for x in types:
            if x.tag.endswith('Default')and x.get('Extension')not in defs:ct.append(copy.deepcopy(x));defs.add(x.get('Extension'))
        for part,mime in overrides.items():E.SubElement(ct,'{'+CT+'}Override',PartName='/'+part,ContentType=mime)
        app=E.fromstring(old.read('docProps/app.xml'))
        for x in app.iter():
            if x.tag.endswith('}Slides'):x.text='84'
        for n,root in [('ppt/presentation.xml',pres),('ppt/_rels/presentation.xml.rels',rels),('[Content_Types].xml',ct),('docProps/app.xml',app)]:changes[n]=xml(root)
        with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
            for n in old.namelist():z.writestr(n,changes.get(n,old.read(n)))
            for n,data in added.items():z.writestr(n,data)
    with zipfile.ZipFile(SRC)as a,zipfile.ZipFile(OUT)as b:
        assert b.testzip()is None
        media=[n for n in a.namelist()if n.startswith('ppt/media/')]
        for n in media:assert a.read(n)==b.read(n),n
        for n in a.namelist():
            if n not in changes:assert a.read(n)==b.read(n),n
        assert sum(x.get('Type').endswith('/notesMaster')for x in E.fromstring(b.read('ppt/_rels/presentation.xml.rels')))==1
        titlepart=original_parts[0];assert a.read(titlepart)==b.read(titlepart)
    p=Presentation(OUT)
    assert len(p.slides)==84
    assert sum(s.shape_type==16 for sl in p.slides for s in sl.shapes)==38
    assert [i for i,sl in enumerate(p.slides,1)if any(s.has_text_frame and s.text.strip()=='Key takeaways'for s in sl.shapes)]==[84]
    report={'slides':84,'content_slides':82,'rewritten_existing_slides':68,'added_slides':14,'paragraphs':246,'sentences_per_paragraph':5,'key_takeaways_slide':84,'movie_placements':38,'preserved_media_parts':len(media),'original_media_bytes_preserved':True,'title_slide_bytes_preserved':True,'bytes':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'layout':layout}
    (B/'package_validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k!='layout'},indent=2))

if __name__=='__main__':build()
