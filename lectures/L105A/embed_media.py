from pathlib import Path
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.dml.color import RGBColor
import json,hashlib
B=Path(__file__).resolve().parents[1];S=Path(__file__).resolve().parent/'research';refs={}
for fn in ['source_audit.json','extra_audit.json','media_rich_audit.json','more_behavior_audit.json','experience_audit.json','more_development_audit.json','final_source_access.json']:
 for r in json.load(open(S/fn)):
  if r.get('record'):refs[r['key']]=r
refs['PigXlinked']=dict(refs['PigMeCP2'],key='PigXlinked')
def fullref(k):
 x=refs[k]['record'];j=x['journalInfo'];return f"{x['authorString']} ({x['pubYear']}). {x['title']} {j['journal']['title']} {j.get('volume','')}:{x.get('pageInfo','')}. https://doi.org/{refs[k]['doi']}"
def fit(sh,x,y,w,h):
 ratio=sh.width/sh.height;fw=min(w,h*ratio);fh=fw/ratio;sh.left=Inches(x+(w-fw)/2);sh.top=Inches(y+(h-fh)/2);sh.width=Inches(fw);sh.height=Inches(fh)
def label(sl,txt,x,y,w,h,size,name):
 sh=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));sh.name=name;tf=sh.text_frame;tf.word_wrap=True;tf.margin_top=tf.margin_bottom=tf.margin_left=tf.margin_right=0;tf.text=txt
 for p in tf.paragraphs:
  p.space_after=Pt(0);p.line_spacing=1
  for r in p.runs:r.font.name='Arial';r.font.size=Pt(size);r.font.color.rgb=RGBColor(0,0,0)
 return sh
for deck in ['105A']:
 R=B/('L'+deck);P=R/f'Neuroethology_Lecture{deck}_FA2026.pptx';spec=json.load(open(R/'lecture.json'));rows=json.load(open(R/'final_clips.json'));prs=Presentation(P);assert len(prs.slides)==50;assert not any(s.shape_type==MSO_SHAPE_TYPE.MEDIA for sl in prs.slides for s in sl.shapes),'Rebuild the base before embedding again.'
 byslide={};sources=[];photos=[]
 for r in rows:byslide.setdefault(r['slide'],[]).append(r)
 for n,sd in enumerate(spec['slides'],2):
  sl=prs.slides[n-1];body=next(s for s in sl.shapes if s.name=='Body');original_body=body.text;pics=[p for p in sl.shapes if p.shape_type==MSO_SHAPE_TYPE.PICTURE];assert len(pics)==1,(deck,n,len(pics));fig=sd['figure'];w=sd['figure_width'];x=13.333333-.62-w;video=n in byslide;comp=sd.get('companion')
  for sh in [p for p in sl.shapes if p.name=='Figure caption']:sh._element.getparent().remove(sh._element)
  locs=[(x,w)] if not comp else [(x,w-1.6),(x+w-1.4,1.4)]
  h=2.30 if video else 4.65;cap_y=3.72 if video else 6.10;cap_h=.53 if video else .73
  fit(pics[0],locs[0][0],1.36,locs[0][1],h)
  text=fig['caption']
  if fig['kind']=='web':
   text+=' '+fig['credit'].replace('(c) ','').split(',')[0]+'. '+fig['license']+'.';photos.append(dict(slide=n,role='content species image',**fig))
  label(sl,text,locs[0][0],cap_y,locs[0][1],cap_h,8.3 if video else 9,'Figure caption')
  if comp:
   xx,ww=locs[1];pic=sl.shapes.add_picture(str(R/comp['path']),Inches(xx),Inches(1.36));pic.name='Credited companion photograph';fit(pic,xx,1.36,ww,h);credit=comp['credit'].replace('(c) ','').split(',')[0];label(sl,comp['caption']+' '+credit+'. '+comp['license']+'.',xx,cap_y,ww,cap_h,8,'Companion caption');photos.append(dict(slide=n,role='companion image',**comp));sl.notes_slide.notes_text_frame.text+='\n\nImage: '+comp['caption']+' Credit: '+comp['credit']+'. License: '+comp['license']+'. Source: '+comp['source_url']
  vs=byslide.get(n,[]);assert len(vs)<=2,(deck,n,len(vs))
  for j,row in enumerate(vs):
   file=R/row['clip_file'];assert hashlib.sha256(file.read_bytes()).hexdigest()==row['clip_sha256'];ratio=row['width']/row['height'];slotw=(w-.18*(len(vs)-1))/len(vs);mw=min(slotw,1.8*ratio);mh=mw/ratio;mx=x+j*(slotw+.18)+(slotw-mw)/2;my=4.40+(1.8-mh)/2;post=R/row['poster']
   fallback=sl.shapes.add_picture(str(post),Inches(mx),Inches(my),width=Inches(mw),height=Inches(mh));fallback.name='Static recording preview'
   movie=sl.shapes.add_movie(str(file),Inches(mx),Inches(my),Inches(mw),Inches(mh),poster_frame_image=str(post),mime_type='video/mp4');movie.name=row['clip_id'];rec=refs[row['source_key']]['record'];author=rec['authorString'].split()[0];caption=f"{author} ({rec['pubYear']}), {row['original_identifier']}. {row['description']}"
   movie._element.xpath('.//p:cNvPr')[0].set('descr',caption+' Native embedded MP4 recording.')
   for e in sl._element.xpath('.//p:video'):e.set('fullScrn','1')
   label(sl,caption,x+j*(slotw+.18),6.29,slotw,.69,8.0,'Video caption');row=dict(row,caption=caption,embedded=True,display_width=mw,display_height=mh,credit=rec['authorString']);sources.append(row)
   url=row.get('original_download_url',row.get('original_package_url',row.get('source_url','')))
   sl.notes_slide.notes_text_frame.text+='\n\nEmbedded video: '+caption+'\nArticle: '+fullref(row['source_key'])+'\nExact source filename: '+row['original_filename']+'\nOriginal media/source page: '+url+'\nOriginal source hash: '+row['original_sha256']+'\nEmbedded clip hash: '+row['clip_sha256']+f"\nSource recording interval: {row['clip_start_seconds']:.3f}–{row['clip_end_seconds']:.3f} s. Original scientific frames, proportions, author-provided timing and available audio retained. Playback seconds are not necessarily biological elapsed time in source time-lapse/accelerated films.\nLicense: "+row.get('license','Original article-provided recording; consult the source article license.')+'\nNative PPTX movie object with a separate static poster fallback. Desktop PowerPoint GUI playback and Google Slides import have not been tested. Google Slides may require inserting the supplied MP4 from Drive after import.\n'
  # Fix the four measured spacing overruns while preserving font size and all teaching text.
  if n in ({12,30,44} if deck=='105A' else {16}):
   for para in body.text_frame.paragraphs:para.space_after=Pt(4.5)
  assert body.text==original_body
 t=spec['title_image'];prs.slides[0].notes_slide.notes_text_frame.text+='\n\nImage: '+t['caption']+' Credit: '+t['credit']+'. License: '+t['license']+'. Source: '+t['source_url'];photos.append(dict(slide=1,role='title image',**t));prs.save(P)
 report=dict(embedded_video_count=len(sources),distinct_original_recordings=len({r['original_sha256'] for r in sources}),sources=sources);(R/'media_sources.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');(R/'additional_image_placements.json').write_text(json.dumps(photos,indent=2,ensure_ascii=False)+'\n');print(deck,len(sources),'native clips;',len(photos),'photo placements;',round(P.stat().st_size/1048576,1),'MiB',flush=True)
