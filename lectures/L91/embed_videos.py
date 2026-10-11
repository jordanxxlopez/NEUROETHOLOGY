"""Add verified article recordings to the existing deck without rewriting slides."""
from pathlib import Path
import hashlib,json,subprocess
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from lxml import etree
ROOT=Path(__file__).resolve().parent
PPTX=ROOT/'Neuroethology_Lecture91_FA2026.pptx'
base='https://pmc-oa-opendata.s3.amazonaws.com/'
entries=[
 (10,'JEB243085.MovieS1','Milne et al. (2021), Movie 1. Lo explores texture, size, and visual brightness.','10.1242/jeb.243085','https://static-movie-usa.glencoesoftware.com/source/10.1242/861/cf6333a8eda59f3724280a480f4c6d468185fa4d/JEB243085.MovieS1.mp4','CC BY 4.0','Milne, Orton, Black, Jones, Sullivan, and Grant'),
 (12,'Bimbo_balance','Blackpool Zoo (2009). Bimbo balances a ball on land and in water; observational demonstration.','','https://www.youtube.com/watch?v=aoYOyxJu9EM','No open license stated; instructor-provided recording','Blackpool Zoo'),
 (13,'JEB243020.MovieS3','Leahy et al. (2021), Movie 3. A trained sea lion executes a 180° left banking turn.','10.1242/jeb.243020','https://static-movie-usa.glencoesoftware.com/source/10.1242/738/918c6b425b28fbbb9ac7bd4aafad3298129ba4a7/JEB243020.MovieS3.mp4','Copyright The Company of Biologists; no open license stated','Leahy, Fish, Kerr, Zeligs, Skrovan, Cardenas, and Leftwich'),
 (14,'JEB243020.MovieS1','Leahy et al. (2021), Movie 1. A captive sea lion completes a porpoising bout.','10.1242/jeb.243020','https://static-movie-usa.glencoesoftware.com/source/10.1242/738/918c6b425b28fbbb9ac7bd4aafad3298129ba4a7/JEB243020.MovieS1.mp4','Copyright The Company of Biologists; no open license stated','Leahy, Fish, Kerr, Zeligs, Skrovan, Cardenas, and Leftwich'),
 (15,'JEB243020.MovieS2','Leahy et al. (2021), Movie 2. Wild sea lions porpoise in Monterey Bay.','10.1242/jeb.243020','https://static-movie-usa.glencoesoftware.com/source/10.1242/738/918c6b425b28fbbb9ac7bd4aafad3298129ba4a7/JEB243020.MovieS2.mp4','Copyright The Company of Biologists; no open license stated','Leahy, Fish, Kerr, Zeligs, Skrovan, Cardenas, and Leftwich'),
 (17,'UCSC2013_Ronan_feature','Cook et al. (2013), official UCSC study video. Ronan transfers trained synchronization to music.','10.1037/a0032345','https://youtu.be/s4nBevZJMvk','No open license stated; instructor-provided compressed copy and explicit permission for this official study video','UC Santa Cruz; Cook and colleagues'),
 (21,'Rouse_tempo','Rouse et al. (2016), Video 1 excerpt. Persistent +15% interval change.','10.3389/fnins.2016.00257',base+'PMC4891632.1/Video1.MP4','CC BY 4.0','Rouse, Cook, Large, and Reichmuth'),
 (23,'Rouse_phase','Rouse et al. (2016), Video 1 excerpt. +25% phase disturbance.','10.3389/fnins.2016.00257',base+'PMC4891632.1/Video1.MP4','CC BY 4.0','Rouse, Cook, Large, and Reichmuth'),
 (25,'Rouse_doublebob','Rouse et al. (2016), Video 1 excerpt. +25% interval change and extra nod.','10.3389/fnins.2016.00257',base+'PMC4891632.1/Video1.MP4','CC BY 4.0','Rouse, Cook, Large, and Reichmuth'),
 (28,'Rocky_commands','Cook et al. (2021), Video 17.1 excerpt. Rocky follows the LARGE BALL, WATERWING, FETCH sequence.','10.1007/978-3-030-59184-7_17','https://e.video-cdn.net/watch?video-id=Av4gjJyizuXyK9pEqPV3Rs&player-id=-qZL2aSgACrhe2fEUstC_v&channel-id=86512','No open license stated','Cook, Reichmuth, and Hanke'),
 (29,'Rio_identity','Cook et al. (2021), Video 17.2 excerpt. Rio performs visual identity matching.','10.1007/978-3-030-59184-7_17','https://e.video-cdn.net/watch?video-id=6t9bp_2EXpiiKeBUT4Rt3w&player-id=-qZL2aSgACrhe2fEUstC_v&channel-id=86512','No open license stated','Cook, Reichmuth, and Hanke'),
 (30,'Rio_classes','Cook et al. (2021), Video 17.3 excerpt. Rio chooses within a learned stimulus class.','10.1007/978-3-030-59184-7_17','https://e.video-cdn.net/watch?video-id=Dk7Vni8uNuSe-GwX6DwYjE&player-id=-qZL2aSgACrhe2fEUstC_v&channel-id=86512','No open license stated','Cook, Reichmuth, and Hanke'),
 (32,'Hama_commands','Sasaki et al. (2025), learned-command recording excerpt. Hama responds to familiar vocal and hand cues.','10.1007/s10071-025-01971-0','https://www.youtube.com/watch?v=-Kwv_fMeG5w','No open license stated; instructor-provided study recording','Sasaki, Kinoshita, and Konno'),
 (35,'Cook2025_Ronan112','Cook et al. (2025), ESM 2 excerpt. Ronan’s first exposure to 112 bpm snare beats.','10.1038/s41598-025-95279-1','https://www.youtube.com/watch?v=1zZc18B8ZW0','CC BY 4.0; original article supplementary recording','Cook and colleagues'),
 (38,'Cook2025_comparison','Cook et al. (2025), ESM 2 excerpt. Matched sea-lion head and human arm movements.','10.1038/s41598-025-95279-1','https://www.youtube.com/watch?v=1zZc18B8ZW0','CC BY 4.0; original article supplementary recording','Cook and colleagues'),
 (42,'science.adx9367_movie_s1','Cook et al. (2026), Supplementary Movie S1. Reconstructed vocal motor cortex–brainstem pathways in a sea lion.','10.1126/science.adx9367','https://www.science.org/doi/10.1126/science.adx9367#supplementary-materials','Copyright 2026 authors; exclusive license AAAS; instructor-supplied original movie','Cook, Rouse, Sawyer, Miller, and Berns')
]
prs=Presentation(PPTX)
if any(s.shape_type==MSO_SHAPE_TYPE.MEDIA for sl in prs.slides for s in sl.shapes):
 raise SystemExit('Use the pre-video deck to avoid duplicate recordings.')
before=[[s.text for s in sl.shapes if s.has_text_frame] for sl in prs.slides]
original_images=[[hashlib.sha256(s.image.blob).hexdigest() for s in sl.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE] for sl in prs.slides]
def fit(shape,x,y,w,h):
 ratio=shape.width/shape.height
 sw=min(w,h*ratio);sh=sw/ratio
 shape.left=Inches(x+(w-sw)/2);shape.top=Inches(y+(h-sh)/2);shape.width=Inches(sw);shape.height=Inches(sh)
def caption(sl,text,x,y,w,h):
 box=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
 tf=box.text_frame;tf.word_wrap=True;tf.margin_left=tf.margin_right=0;tf.margin_top=tf.margin_bottom=0
 tf.text=text
 for p in tf.paragraphs:
  for r in p.runs:r.font.name='Arial';r.font.size=Pt(9);r.font.color.rgb=RGBColor(0,0,0)
 return box
segments={x['file']:x for x in json.loads((ROOT/'segment_audit.json').read_text())}
sources=[]
for num,stem,cap,doi,url,license,credit in entries:
 sl=prs.slides[num-1];pic=next(s for s in sl.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE)
 figcap=next(s for s in sl.shapes if s.has_text_frame and 'Fig.' in s.text)
 path=ROOT/'media'/f'{stem}.mp4';poster=ROOT/'posters'/f'{stem}.png'
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]))
 v=next(s for s in probe['streams'] if s['codec_type']=='video');ratio=(float(v['display_aspect_ratio'].split(':')[0])/float(v['display_aspect_ratio'].split(':')[1])) if v.get('display_aspect_ratio') not in (None,'0:1') else v['width']/v['height']
 if num==43:
  fit(pic,7.11,1.4,2.6,2.5);figcap.left=Inches(7.11);figcap.top=Inches(4.0);figcap.width=Inches(2.6);figcap.height=Inches(.85)
  w=2.7;h=w/ratio;x=9.95;y=1.4
  caption(sl,cap,9.95,y+h+.12,2.7,.8)
 else:
  fit(pic,7.11,1.35,5.6,2.1);figcap.left=Inches(7.11);figcap.top=Inches(3.5);figcap.width=Inches(5.6);figcap.height=Inches(.42)
  h=min(2.35,5.6/ratio);w=h*ratio;x=7.11+(5.6-w)/2;y=4.02
  caption(sl,cap,7.11,6.48,5.6,.35)
 fallback=sl.shapes.add_picture(str(poster),Inches(x),Inches(y),width=Inches(w),height=Inches(h))
 fallback.name='Static video fallback'
 movie=sl.shapes.add_movie(str(path),Inches(x),Inches(y),Inches(w),Inches(h),poster_frame_image=str(poster),mime_type='video/mp4')
 for el in movie._element.xpath('.//p:cNvPr'):el.set('descr',cap+' Click to play the embedded original study recording.')
 # PowerPoint supports full-screen video playback while preserving the native ratio.
 for el in sl._element.xpath('.//p:video'):el.set('fullScrn','1')
 sl.notes_slide.notes_text_frame.text+='\nEmbedded recording: '+cap+'\nSource URL: '+url+('\nArticle DOI: https://doi.org/'+doi if doi else '\nSource: observational zoo recording; no article DOI')+'\nCredit: '+credit+'. License: '+license+'.\nDiscuss the displayed behavior and compare it with the adjacent published measurements. Original timing and audio retained; poster is an unedited frame. The embedded MP4 preserves native display proportions, original timing, scene order, and audio; compatibility conversion details are recorded in media_conversion_audit.json when applicable. Desktop PowerPoint playback and Google Slides import were not tested.\n'
 if str(path.relative_to(ROOT)) in segments:
  seg=segments[str(path.relative_to(ROOT))]
  sl.notes_slide.notes_text_frame.text+='\nInstructor-authorized excerpt: '+str(seg['start_seconds'])+' to '+str(seg['start_seconds']+seg['duration_seconds'])+' seconds. '+seg['conversion']+'. Spatial crop: '+str(seg['spatial_crop'])+'. This excerpt retains the source behavior and sound sequence; omitted sections are outside the selected task.\n'
 sources.append(dict(slide=num,file=str(path.relative_to(ROOT)),caption=cap,doi=doi,original_url=url,credit=credit,license=license,width=v['width'],height=v['height'],duration_seconds=float(probe['format']['duration']),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),display_aspect_ratio=v.get('display_aspect_ratio'),counts_toward_study_target=(stem not in ('UCSC2013_Ronan_feature','Bimbo_balance')),segment=segments.get(str(path.relative_to(ROOT)))))
for i,sl in enumerate(prs.slides):
 assert [s.text for s in sl.shapes if s.has_text_frame][:len(before[i])]==before[i],f'Text changed on slide {i+1}'
 assert [hashlib.sha256(s.image.blob).hexdigest() for s in sl.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE and s.name!='Static video fallback']==original_images[i]
for n in (28,29,30):
 prs.slides[n-1].notes_slide.notes_text_frame.text+='\nThe chapter supplement records the trained task. It is not identified as a trial from the earlier article; numerical findings refer to that cited article.\n'
prs.slides[31].notes_slide.notes_text_frame.text+='\nThis recording contains familiar command responses, not the delayed-Go imitation test.\n'
prs.slides[11].notes_slide.notes_text_frame.text+='\nBimbo is a zoo demonstration, not a participant in the adjacent Milne and Grant measurements.\n'
prs.save(PPTX)
study=[x for x in sources if x['counts_toward_study_target']]
sea=study
unique=lambda xs:len({x['original_url']+(':'+x['file'] if x['slide'] in (13,14,15,41,42,43) else '') for x in xs})
(ROOT/'media_sources.json').write_text(json.dumps(dict(embedded_video_count=len(sources),qualifying_sea_lion_study_video_count=unique(sea),required_count=10,featured_video_count=1,observational_demo_count=1,qualifying_study_video_count=unique(study),study_target_shortfall=max(0,10-unique(sea)),sources=sources),indent=2)+'\n')
print('Embedded',len(sources),'clips;',unique(sea),'distinct sea-lion study recordings, excluding Ronan feature and zoo demonstration.')
