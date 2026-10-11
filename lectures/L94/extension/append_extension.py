"""Append 25 slides without rewriting any of the preserved 46 slide parts.

Build extension.json with tools/build_lecture.py first. Media files are original
instructor uploads. The final package imports only donor slides 2–26.
"""
from pathlib import Path
import json, hashlib, zipfile, posixpath, subprocess, copy
from lxml import etree as E
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

B = Path(__file__).resolve().parent
S = Path('/workspace/l94-expansion')
OLD = B.parent / 'deliverables/Neuroethology_Lecture94_FA2026_Rio_Revised.pptx'
OUT = B.parent / 'deliverables/Neuroethology_Lecture94_FA2026_Expanded71.pptx'
DONOR = S / 'Extension_With_Movies.pptx'
PNS = 'http://schemas.openxmlformats.org/presentationml/2006/main'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG = 'http://schemas.openxmlformats.org/package/2006/relationships'
CT = 'http://schemas.openxmlformats.org/package/2006/content-types'

records = [
    (47, B.parent/'media/Rio_identity.mp4', 'Cook et al. (2021), Supplementary Video 17.2. Rio performs identity matching.', 'https://doi.org/10.1007/978-3-030-59184-7_17', 'https://link.springer.com/chapter/10.1007/978-3-030-59184-7_17#MOESM2', 'The movie depicts Rio; the accompanying chapter figure identifies Rocky. This footage illustrates matching responses, not a novel-stimulus transfer test.'),
    (57, B/'media/Luca the seal watching dots [ubOdiKRpczA].mp4', 'Instructor-supplied recording. Luca watches a visual dot display.', None, None, 'Instructor-supplied contextual footage. The precise published experiment, filming date and source credit are unverified; do not identify this as footage from Sandow et al. (2025).'),
    (66, B/'media/Moe_Training_Trial_3LEDv_under32MiB.mp4', 'Maaß et al. (2022), article-provided video: Moe Training Trial 3LEDv. Vertical-landmark training.', 'https://doi.org/10.1242/jeb.244544', 'https://osf.io/54vfa/', 'The paper explicitly links its original data and videos to OSF. Two landmarks are illuminated; 3LEDv denotes the 60 cm vertical configuration, not three illuminated landmarks.'),
    (67, B/'media/Baseline_Trial_3LEDh_under32MiB.mp4', 'Maaß et al. (2022), article-provided video: Baseline Trial 3LEDh. Horizontal baseline.', 'https://doi.org/10.1242/jeb.244544', 'https://osf.io/54vfa/', 'Baseline trial in the familiar 60 cm horizontal configuration. This is not footage of a novel-separation probe.'),
    (67, B/'media/Baseline_Trial_5LEDv_under32MiB.mp4', 'Maaß et al. (2022), article-provided video: Baseline Trial 5LEDv. Vertical baseline.', 'https://doi.org/10.1242/jeb.244544', 'https://osf.io/54vfa/', 'Baseline trial in the familiar 90 cm vertical configuration. Baselines measured maintained performance alongside novel-separation tests; this recording is not the novel probe itself.'),
]

def text_box(sl, x, y, w, h, text):
    sh = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    sh.name = 'Article recording credit'
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    r = tf.paragraphs[0].add_run()
    r.text = text
    r.font.name = 'Arial'
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0,0,0)

def embed():
    p = Presentation(S/'Extension_Base.pptx')
    metadata = []
    for actual in range(47,72):
        sl = p.slides[actual-46]
        for sh in sl.shapes:
            if sh.name == 'Slide number':
                sh.text_frame.paragraphs[0].runs[0].text = str(actual)
        rr = [r for r in records if r[0]==actual]
        if not rr:
            continue
        pic = next(sh for sh in sl.shapes if sh.shape_type==13)
        cap = next(sh for sh in sl.shapes if sh.name=='Figure caption')
        limit = 1.65 if len(rr)==2 else 2.5
        ratio = pic.width/pic.height
        fw = min(5.7, limit*ratio); fh=fw/ratio
        pic.left=Inches(7.01+(5.7-fw)/2);pic.top=Inches(1.35)
        pic.width=Inches(fw);pic.height=Inches(fh)
        cap.top=Inches(1.35+fh+.05);cap.height=Inches(.45)
        for par in cap.text_frame.paragraphs:
            for r in par.runs:r.font.size=Pt(9)
        for k, (_,src,caption,doi,url,description) in enumerate(rr):
            info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(src)]))
            video=next(s for s in info['streams']if s['codec_type']=='video')
            poster=B/'media'/(src.stem+'_poster.png')
            subprocess.run(['ffmpeg','-v','error','-ss','0.5','-i',str(src),'-frames:v','1','-y',str(poster)],check=True)
            height=1.45 if len(rr)==2 else 2.35
            width=height*video['width']/video['height']
            x=7.01+(5.7-width)/2;y=3.56+k*1.73 if len(rr)==2 else 4.23
            fallback=sl.shapes.add_picture(str(poster),Inches(x),Inches(y),Inches(width),Inches(height))
            fallback.name='Unedited supplied recording frame'
            movie=sl.shapes.add_movie(str(src),Inches(x),Inches(y),Inches(width),Inches(height),poster_frame_image=str(poster),mime_type='video/mp4')
            movie.name=caption+' (click to play)'
            text_box(sl,7.01,y+height+.035,5.7,.38 if len(rr)==1 else .27,'Click to play. '+caption)
            for line in ['', 'Embedded recording: '+caption, description, 'Article DOI: '+str(doi or 'unverified'), 'Original media repository: '+str(url or 'Instructor upload; source unverified'), 'License: instructor-supplied copy; no separate video license supplied.', 'File: '+src.name, 'Editing: supplied bytes retained exactly; no trimming, cropping, re-encoding, compression, resolution reduction, speed change or audio removal.', 'Playback: H.264/AAC source decoding and embedded relationships checked. Interactive desktop PowerPoint playback untested.']:
                sl.notes_slide.notes_text_frame.add_paragraph().text=line
            metadata.append({'slide':actual,'file':src.name,'caption':caption,'doi':doi,'original_repository':url,'description':description,'bytes':src.stat().st_size,'MB':src.stat().st_size/1e6,'MiB':src.stat().st_size/1048576,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'width':video['width'],'height':video['height'],'duration_s':float(info['format']['duration']),'audio_present':any(s['codec_type']=='audio'for s in info['streams']),'editing':'None; supplied file bytes embedded unchanged.'})
    p.save(DONOR)
    (B/'media_manifest.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n')
    return metadata

def relpath(part):
    parent, name=posixpath.split(part)
    return posixpath.join(parent,'_rels',name+'.rels')

def append():
    with zipfile.ZipFile(OLD)as old,zipfile.ZipFile(DONOR)as donor:
        added={};mapping={}; overrides={}
        types=E.fromstring(donor.read('[Content_Types].xml'))
        dtype={x.get('PartName').lstrip('/'):x.get('ContentType')for x in types if x.tag.endswith('Override')}
        def clone(part):
            if part in mapping:return mapping[part]
            parent,name=posixpath.split(part)
            dest=posixpath.join(parent,'extension_'+name)
            mapping[part]=dest
            added[dest]=donor.read(part)
            if part in dtype:overrides[dest]=dtype[part]
            rp=relpath(part)
            if rp in donor.namelist():
                rel=E.fromstring(donor.read(rp))
                for r in rel:
                    if r.get('TargetMode')=='External':continue
                    target=r.get('Target')
                    full=posixpath.normpath(posixpath.join(parent,target))if not target.startswith('/')else target.lstrip('/')
                    r.set('Target',posixpath.relpath(clone(full),posixpath.dirname(dest)))
                added[relpath(dest)]=E.tostring(rel,xml_declaration=True,encoding='UTF-8',standalone=True)
            return dest
        pres=E.fromstring(old.read('ppt/presentation.xml'))
        rels=E.fromstring(old.read('ppt/_rels/presentation.xml.rels'))
        sids=pres.find('{'+PNS+'}sldIdLst')
        sid=max(int(x.get('id'))for x in sids)
        rid=max(int(x.get('Id')[3:])for x in rels if x.get('Id').startswith('rId'))
        def relation(target,kind):
            nonlocal rid
            rid+=1;rr='rId'+str(rid)
            E.SubElement(rels,'{'+PKG+'}Relationship',Id=rr,Type=RNS+'/'+kind,Target=posixpath.relpath(target,'ppt'))
            return rr
        for n in range(2,27):
            dest=clone(f'ppt/slides/slide{n}.xml');sid+=1
            x=E.SubElement(sids,'{'+PNS+'}sldId',id=str(sid));x.set('{'+RNS+'}id',relation(dest,'slide'))
        for key, dest in list(mapping.items()):
            kind = 'sldMaster' if key.startswith('ppt/slideMasters/') and key.endswith('.xml') else 'notesMaster' if key.startswith('ppt/notesMasters/') and key.endswith('.xml') else None
            if kind:
                lst=pres.find('{'+PNS+'}'+kind+'IdLst')
                if lst is None:
                    lst=E.Element('{'+PNS+'}'+kind+'IdLst');pres.insert(1,lst)
                x=E.SubElement(lst,'{'+PNS+'}'+kind+'Id')
                if kind=='sldMaster':x.set('id',str(max([int(q.get('id'))for q in lst if q.get('id')]or[2147483647])+1))
                x.set('{'+RNS+'}id',relation(dest,'slideMaster'if kind=='sldMaster'else'notesMaster'))
        ct=E.fromstring(old.read('[Content_Types].xml'))
        defs={x.get('Extension')for x in ct if x.tag.endswith('Default')}
        for x in types:
            if x.tag.endswith('Default')and x.get('Extension')not in defs:ct.append(copy.deepcopy(x));defs.add(x.get('Extension'))
        for part,mime in overrides.items():E.SubElement(ct,'{'+CT+'}Override',PartName='/'+part,ContentType=mime)
        changed={'ppt/presentation.xml':E.tostring(pres,xml_declaration=True,encoding='UTF-8',standalone=True),'ppt/_rels/presentation.xml.rels':E.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True),'[Content_Types].xml':E.tostring(ct,xml_declaration=True,encoding='UTF-8',standalone=True)}
        if 'docProps/app.xml'in old.namelist():
            app=E.fromstring(old.read('docProps/app.xml'))
            for x in app.iter():
                if x.tag.endswith('}Slides'):x.text='71'
            changed['docProps/app.xml']=E.tostring(app,xml_declaration=True,encoding='UTF-8',standalone=True)
        with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED)as z:
            for info in old.infolist():z.writestr(info,changed.get(info.filename,old.read(info.filename)))
            for name,data in added.items():z.writestr(name,data)
    with zipfile.ZipFile(OLD)as old,zipfile.ZipFile(OUT)as new:
        unchanged=[n for n in old.namelist()if n not in changed]
        for n in unchanged:assert old.read(n)==new.read(n),n
        assert new.testzip() is None
    p=Presentation(OUT)
    assert len(p.slides)==71
    assert sum(s.shape_type==16 for sl in p.slides for s in sl.shapes)==38
    rio=hashlib.sha256((B.parent/'media/Rio_identity.mp4').read_bytes()).hexdigest()
    placements=[]
    for i,sl in enumerate(p.slides,1):
        for r in sl.part.rels.values():
            if r.reltype.endswith('/video')and hashlib.sha256(r.target_part.blob).hexdigest()==rio:placements.append(i)
    assert placements==[32,35,47],placements
    manifest=json.loads((B/'media_manifest.json').read_text())
    for m in manifest:
        rr=[r for r in p.slides[m['slide']-1].part.rels.values()if r.reltype.endswith('/video')]
        assert m['sha256']in[hashlib.sha256(r.target_part.blob).hexdigest()for r in rr]
    report={'slides':71,'appended_slides':25,'preserved_slides':46,'unchanged_original_package_parts':len(unchanged),'changed_original_package_parts':list(changed),'embedded_movie_placements':38,'Rio_placements':placements,'bytes':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'all_five_supplied_videos_embedded':True,'native_uploaded_media_bytes_preserved':True,'interactive_PowerPoint_playback':'untested'}
    (B/'package_validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    embed();append()
