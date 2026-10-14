from pathlib import Path
import json,subprocess,shutil,hashlib,concurrent.futures
R=Path('/workspace/NEUROETHOLOGY/lectures/L104B');scratch=Path('/workspace/scratch/L104B');media=R/'media';delivery=media/'delivery';post=R/'posters'
for p in [media,delivery,post]:p.mkdir(exist_ok=True)
refs=json.load(open(R/'reference_verification.json'));access=json.load(open(scratch/'media_access.json'));helpaccess=json.load(open(scratch/'Helping2024_media_access.json'));urlmap={Path(x['path']).name:x['url'] for x in access+helpaccess if 'path' in x}
for p in (scratch/'media').glob('*'):
 if p.suffix.lower() in ['.mp4','.mov'] and not p.name.startswith('Witness'):shutil.copy2(p,media/p.name)
E=[]
def add(sl,k,file,stem,id,desc,start=0,end=None):E.append({'slide':sl,'key':k,'file':'media/'+file,'stem':stem,'original_identifier':id,'description':desc,'start_seconds':start,'end_seconds':end,'article_doi':refs[k]['doi'],'download_url':urlmap.get(file,'https://pmc-oa-opendata.s3.amazonaws.com/PMC12506963.1/sciadv.ady1944_movies_s1_to_s4.zip')})
for sl,tag,st,en,des in [(3,'BV',12,27,'Bee venom paw-directed behavior.'),(4,'Formalin',33,49,'Formalin paw-directed behavior.'),(5,'CFA',52,62,'CFA condition with relatively little spontaneous display.'),(6,'SNI',65,77,'Spared nerve injury condition.')]:add(sl,'Rat2018','Rat2018_Video_1.MP4','Rat2018_'+tag,'Supplemental Video 1',des,st,en)
add(7,'Rat2018','Rat2018_Video_2.MP4','Rat2018_Interaction','Supplemental Video 2','Familiar rat social interaction and injured-paw contact.')
for sl,n,desc in [(22,1,'Standard-reared observer PVT contact-related calcium activity.'),(23,2,'Maternal-separated observer PVT contact-related calcium activity.'),(26,3,'PVT-to-PrL pathway calcium activity during contact.'),(28,4,'Pathway activity after tactile intervention.')]:add(sl,'PVT2025',f'PVT2025_ady1944_movie_s{n}.mp4',f'PVT2025_Movie{n}',f'Movie S{n}',desc)
for sl,n,desc in [(30,1,'General allogrooming toward a partner in pain.'),(31,2,'Targeted allolicking of an injured paw.')]:
 file=Path(helpaccess[n-1]['path']).name;add(sl,'Helping2024',file,f'Helping2024_Video{n}',f'Supplementary Video {n}',desc)
for sl,n,desc in [(36,1,'Spontaneous grooming and injury-directed licking.'),(37,2,'CeM V1aR calcium activity during social investigation.'),(38,3,'CeM V1aR calcium activity during allogrooming.'),(39,4,'CeM V1aR calcium activity during allolicking.'),(44,7,'PVN pathway optogenetic activation recruits care.')]:add(sl,'Care2026',f'Care2026_jci-136-204317-s0{n+10}.mp4',f'Care2026_Video{n}',f'Supplemental Video {n}',desc)
add(40,'Care2026','Care2026_jci-136-204317-s015.mp4','Care2026_Video5_Neutral','Supplemental Video 5','CeM V1aR activation with a neutral cagemate.',0,24)
add(41,'Care2026','Care2026_jci-136-204317-s015.mp4','Care2026_Video5_Pain','Supplemental Video 5','CeM V1aR activation with a melittin-treated cagemate.',25,54.218)
add(42,'Care2026','Care2026_jci-136-204317-s016.mp4','Care2026_Video6_Control','Supplemental Video 6','eGFP control during illumination.',0,23.5)
add(43,'Care2026','Care2026_jci-136-204317-s016.mp4','Care2026_Video6_Inhibit','Supplemental Video 6','GtACR2 inhibition during partner-directed care.',24,52.988)
assert len(E)==20
for x in E:
 x['original_sha256']=hashlib.sha256((R/x['file']).read_bytes()).hexdigest();x['original_credit']=refs[x['key']]['authorString'];x['license']='See original article license; original authors retain credited scientific content';x['genre']='original experimental recording'
def g(x):
 x=dict(x);src=R/x['file'];dest=delivery/(x['stem']+'.mp4');cmd=['ffmpeg','-v','error','-i',str(src)]
 if x['start_seconds']:cmd+=['-ss',str(x['start_seconds'])]
 if x['end_seconds'] is not None:cmd+=['-t',str(x['end_seconds']-x['start_seconds'])]
 cmd+=['-map','0:v:0','-map','0:a?','-vf',"scale='min(1280,iw)':-2",'-c:v','libx264','-crf','26','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart','-y',str(dest)]
 subprocess.run(cmd,check=True);probe=json.loads(subprocess.check_output(['ffprobe','-v','quiet','-show_format','-show_streams','-of','json',str(dest)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');dur=float(probe['format']['duration']);poster=post/(x['stem']+'.jpg');t=min(dur*.3,7)
 subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(dest),'-frames:v','1','-y',str(poster)],check=True)
 x.update({'delivery_file':str(dest.relative_to(R)),'poster':str(poster.relative_to(R)),'delivery_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'duration_seconds':dur,'width':v['width'],'height':v['height'],'poster_seconds':t,'conversion':'H.264/AAC compatibility conversion at original speed; original audio preserved; '+('full recording retained' if x['start_seconds']==0 and x['end_seconds'] is None else f"condition-specific excerpt {x['start_seconds']}–{x['end_seconds']} seconds of original recording")});return x
rows=list(concurrent.futures.ThreadPoolExecutor(3).map(g,E));(R/'media_preparation.json').write_text(json.dumps(rows,indent=2)+'\n');print('Prepared',len(rows),'clips from',len({x['original_sha256'] for x in rows}),'originals;',sum((R/x['delivery_file']).stat().st_size for x in rows),'bytes')
