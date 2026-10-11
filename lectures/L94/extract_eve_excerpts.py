"""Extract the seven instructor-authorized slide-specific EVE intervals. Requires ffmpeg.
Run before add_eve_excerpts.py; does not modify the complete original recording.
"""
import subprocess,json,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent;m=json.loads((b/'media_sources.json').read_text());src=m['embedded'][0];clips=[]
items=[(9,0,13,1,'Brief button contact','Nearby targets reinforce brief contact with a directional button.'),(10,15,30,2,'Restricted directional movement','Walls restrict cursor movement while one available direction leads to the target.'),(11,45,65,3,'Sustained directional contact','Longer button contact continues cursor movement toward a more distant target.'),(12,74,95,4,'Stopping at interior targets','Targets lie inside the display rather than at its outer boundary, requiring termination of directional input.'),(13,120,145,5,'Switching directions','Opposing targets require selection of different directional buttons across target locations.'),(14,160,180,6,'Precise target placement','A single small target changes position while the directional button mapping remains fixed.'),(15,200,220,6,'Phase 6 with feeder','The authors label this section PHASE 6 WITH FEEDER. The sea lion operates the directional controller and turns toward the feeder outlet after completing a target response.')]
for slide,start,end,phase,label,note in items:
 f=b/f'media/EVE_slide{slide}_excerpt.mp4';poster=f.with_name(f.stem+'_poster.png')
 subprocess.run(['ffmpeg','-y','-v','error','-ss',str(start),'-i',str(b/src['path']),'-t',str(end-start),'-c:v','libx264','-preset','slow','-crf','25','-maxrate','550k','-bufsize','1100k','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(f)],check=True)
 subprocess.run(['ffmpeg','-y','-v','error','-ss','2','-i',str(f),'-frames:v','1',str(poster)],check=True)
 from PIL import Image
 jpg=poster.with_suffix('.jpg');Image.open(poster).convert('RGB').save(jpg,quality=95,subsampling=0);poster.unlink();poster=jpg
 p=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(f)]));v=next(s for s in p['streams']if s['codec_type']=='video')
 c={k:src[k]for k in ['doi','credit','license','original_media_url','original_filename','original_duration_s','original_sha256']}
 c.update(slide=slide,path=str(f.relative_to(b)),poster=str(poster.relative_to(b)),source_start_s=start,source_end_s=end,duration_s=float(p['format']['duration']),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),display_aspect=v['width']/v['height'],width=v['width'],height=v['height'],audio_present=any(s['codec_type']=='audio'for s in p['streams']),caption=f'Winship et al. (2023), EVE excerpt {start//60}:{start%60:02d}–{end//60}:{end%60:02d}. {label}.',teaching_note=note,conversion='Instructor-authorized temporal excerpt only. Full original 854 × 480 scene, frame rate and playback speed retained; H.264 compatibility encoding, original AAC packets retained. No spatial crop, overlays, recoloring, inserted frames or added audio.',instructor_authorization='Extract slide-specific segments from only this EVE video; keep the full source recording and all other lecture content and recordings unchanged.')
 clips.append(c);print(slide,f.stat().st_size)
m['eve_excerpts']=clips;m['excerpt_policy']='Seven scientifically selected EVE excerpts explicitly requested by the instructor, added after the original ten complete recordings. Excerpts are not counted as distinct source recordings.'
(b/'media_sources.json').write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
