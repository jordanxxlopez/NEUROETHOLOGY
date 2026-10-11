from pathlib import Path
import json,subprocess,hashlib,concurrent.futures,shutil,urllib.request
B=Path(__file__).resolve().parent;r=json.loads((B/'research.json').read_text())
data=[
(14,'katydid_calcium','359_2023_1638_MOESM1_ESM.mp4','Movie 1','TN-1 calcium response to a chirp.','A 280 ms conspecific chirp activates TN-1 dendrites; the fluorescence signal rises with the sound and decays after it.'),
(15,'katydid_calcium','359_2023_1638_MOESM2_ESM.mp4','Movie 2','ON-1 calcium response to a chirp.','The original recording tracks calcium signals in dendritic, axonal and spike-generating regions of ON-1 during a chirp.'),
(16,'katydid_calcium','359_2023_1638_MOESM3_ESM.mp4','Movie 3','Frequency-specific calcium signals in TN-1.','Different pure-tone frequencies activate different parts of TN-1 dendrites. The author-provided colors encode measured calcium fluorescence.'),
(26,'katydid_calcium','359_2023_1638_MOESM4_ESM.mp4','Movie 4','Frequency-specific calcium signals in ON-1.','Pure-tone stimulation reveals local dendritic calcium responses in ON-1, whereas axonal responses lack the same spatial frequency map.'),
(38,'bat_onboard','pnas.2407810122.sm01.mp4','Movie S1','Evening emergence of greater mouse-tailed bats.','The original colony recording establishes the crowded emergence context. Individual onboard microphones, rather than this camera alone, measured interference at a focal bat.'),
(8,'croc_spatial','42003_2022_3799_MOESM4_ESM.mp4','Supplementary Movie 1','Field playback with a wild female caiman.','The Pantanal field experiment presents juvenile distress calls with masking noise. Orienting and approaching the target provide the behavioral response.'),
(10,'croc_spatial','42003_2022_3799_MOESM5_ESM.mp4','Supplementary Movie 2','Contact-call playback with Nile crocodiles.','The Crocoparc experiment measures freely moving young Nile crocodiles responding to a contact call against continuous noise.'),
(23,'croc_spatial','42003_2022_3799_MOESM6_ESM.mp4','Supplementary Movie 3','Trained crocodile sound-detection task.','A juvenile Nile crocodile approaches a target speaker following a trained synthetic buzz. Target and masker locations test spatial release without relying on maternal motivation.'),
(42,'frog_gesture','elife-76083-video1.mp4','Video 1','Torrent frog defensive movements toward midges.','Calling little torrent frogs repel parasites with limb movements. Some kinds of movement also increase female preference when added to the same advertisement call.'),
(43,'frog_gesture','elife-76083-video2.mp4','Video 2','A torrent frog moves toward a flying parasite.','The movement supplies a real behavioral origin for a possible visual communication component. The study tested female preference, not a masking threshold.')]

def f(item):
 num,k,name,ident,what,note=item;src=B/'media'/name;original=src.with_name(src.stem+'_original.mp4')
 if not original.exists():
  if src.exists():src.rename(original)
  else:
   pmc=r[k]['record']['pmcid'];original.write_bytes(urllib.request.urlopen('https://pmc-oa-opendata.s3.amazonaws.com/'+pmc+'.1/'+name,timeout=90).read())
 out=src.with_name(src.stem+'_compatible.mp4');subprocess.run(['ffmpeg','-v','error','-threads','2','-i',str(original),'-filter_threads','1','-vf',"scale=w='min(720,iw)':h=-2",'-c:v','libx264','-threads','2','-preset','fast','-crf','29','-c:a','aac','-b:a','96k','-movflags','+faststart','-y',str(out)],check=True)
 j=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(out)]));v=next(s for s in j['streams']if s['codec_type']=='video');duration=float(j['format']['duration']);poster=out.with_suffix('.jpg');t=(3.5 if num==14 else 5.0) if k=='katydid_calcium' else (.2 if num==43 else min(4,duration/3));subprocess.run(['ffmpeg','-v','error','-threads','2','-ss',str(t),'-i',str(out),'-frames:v','1','-q:v','2','-y',str(poster)],check=True)
 subprocess.run(['ffmpeg','-v','error','-threads','2','-i',str(out),'-f','null','-'],check=True)
 author=r[k]['record']['authorString'].split()[0];caption=f"{author} et al. ({r[k]['record']['pubYear']}), {ident}. {what}";pmc=r[k]['record']['pmcid'];u='https://pmc-oa-opendata.s3.amazonaws.com/'+pmc+'.1/'+name
 m=dict(slide=num,paper=k,path=str(out.relative_to(B)),poster=str(poster.relative_to(B)),caption=caption,teaching_note=note,doi=r[k]['doi'],original_identifier=ident,original_filename=name,original_media_url=u,credit=r[k]['record']['authorString'],license='CC BY 4.0, https://creativecommons.org/licenses/by/4.0/',conversion='H.264/AAC compatibility encoding, at most 720 px wide; original scene, frame timing, duration and audio retained; unedited original frame used as poster.',sha256=hashlib.sha256(out.read_bytes()).hexdigest(),original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),duration_seconds=duration,display_aspect=v['width']/v['height'],bytes=out.stat().st_size,decode_verified=True)
 print(num,name,duration,out.stat().st_size,flush=True);return m
with concurrent.futures.ThreadPoolExecutor(3)as p:entries=list(p.map(f,data))
(B/'media_sources.json').write_text(json.dumps(dict(requested=10,embedded=entries,not_embedded=[],note='Ten distinct original article-provided experimental or field recordings; no simulations, generated animations or audio-only clips counted.'),indent=2,ensure_ascii=False)+'\n')
