"""Extract only the instructor-authorized intervals from the three uploaded sources.
Supply the original filenames under papers/uploaded_videos before regenerating.
Checked-in compatible excerpts can be embedded without regenerating them.
"""
from pathlib import Path
import subprocess,json,hashlib,shutil
from PIL import Image
B=Path(__file__).resolve().parent;m=json.loads((B/'media_sources.json').read_text());R=json.loads((B/'research.json').read_text())
paths=[B/'papers'/'uploaded_videos'/name for name in ['Examples_of_Defined_Strategies_HD (1).mp4','Navy_Sea_Lions_HD.mp4','Meet_EVE_HD (1).mp4']]
items=[(4,1,6,18,'Controller contact','Four-button controller contact and the separate visual display.'),(6,2,84,101,'Response and trainer reward','The sea lion operates the controller and subsequently receives a trainer-delivered reward. This is observed delivery, not evidence for an automatic feeder.'),(21,2,53,59,'Maze gameplay','Cursor movement occurs along the maze platforms. This short excerpt concerns maze gameplay, not the distinct matching rule.'),(22,2,70,84,'Sample and choice display','Cursor control occurs with shape displays used in EVE. The footage supplies apparatus and task context; the exact trial stage and performance measurements are established by the cited paper.'),(23,0,11,14.5,'Staircase strategy','The authors identify this section as Staircase. Alternating directional inputs produce a stepped cursor route.'),(23,0,20.5,25.5,'Targeting strategy','The authors identify this section as Targeting. The animal directs cursor movement toward the target.'),(24,0,26.5,31.5,'Wall surfing strategy','The authors identify this section as Wall Surfing. The cursor route uses the display boundary.'),(25,0,6,10.5,'Diagonal strategy','The authors identify this section as Diagonal. Combined directional input produces diagonal cursor movement. This example does not establish a before-and-after change in strategy duration.')]
source=[]
for k,f in enumerate(paths):
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(f)]));p=B/'papers'/'uploaded_videos'/f.name;p.parent.mkdir(exist_ok=True);
 if f.resolve()!=p.resolve():shutil.copyfile(f,p)
 source.append(dict(original_filename=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),duration_s=float(info['format']['duration']),path=str(p.relative_to(B)),provenance='Instructor-uploaded recording explicitly authorized for extraction and embedding.',publication_status='Verified Roberts et al. (2023) Supplementary Video S1, exact title Examples of Defined Strategies.' if k==0 else 'Instructor-supplied contextual recording. Exact publication linkage and producer not independently verified; not labeled as an original article supplement.',source_url='https://www.mdpi.com/article/10.3390/jzbg4010021/s1'if k==0 else None))
clips=[]
for j,(slide,k,start,end,label,note)in enumerate(items):
 src=source[k];f=B/f'media/upload_excerpt_{j+1}_slide{slide}.mp4';png=f.with_suffix('.png');poster=f.with_suffix('.jpg')
 subprocess.run(['ffmpeg','-y','-v','error','-ss',str(start),'-i',str(paths[k]),'-t',str(end-start),'-vf','scale=854:480:flags=lanczos','-c:v','libx264','-preset','slow','-crf','24','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart',str(f)],check=True)
 subprocess.run(['ffmpeg','-y','-v','error','-ss',str(min(1,(end-start)/2)),'-i',str(f),'-frames:v','1',str(png)],check=True)
 Image.open(png).convert('RGB').save(poster,quality=95,subsampling=0);png.unlink()
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(f)]))
 c=dict(slide=slide,path=str(f.relative_to(B)),poster=str(poster.relative_to(B)),source_index=k,source_start_s=start,source_end_s=end,duration_s=float(info['format']['duration']),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),source_sha256=src['sha256'],original_filename=src['original_filename'],publication_status=src['publication_status'],original_media_url=src['source_url'],audio_present=any(s['codec_type']=='audio'for s in info['streams']),display_aspect=854/480,width=854,height=480,teaching_note=note,caption=(f'Roberts et al. (2023), Video S1, {start}–{end} s. {label}.'if k==0 else f'{paths[k].stem.replace(" (1)","")}, {start}–{end} s. {label}.'),credit='Roberts DL, Eskelinen HC, Winship KA, Ramos AM, Xitco MJ (2023)'if k==0 else 'Instructor-supplied video; producer credit not independently verified.',license='CC BY 4.0, as stated in uploaded article'if k==0 else 'Instructor-supplied; separate reuse license not established.',doi='10.3390/jzbg4010021'if k==0 else None,conversion='Instructor-authorized temporal excerpt. Entire displayed scene retained, resized to compatible 854 × 480 H.264/AAC MP4. Correct source display orientation, original frame rate, normal timing and audio retained; no added overlays, music, frames, recoloring or speed changes.')
 clips.append(c);print(j+1,slide,f.stat().st_size,flush=True)
m['additional_uploaded_sources']=source;m['additional_uploaded_excerpts']=clips
m['not_embedded']=[c for c in m['not_embedded']if c.get('doi')!='10.3390/jzbg4010021']
(B/'media_sources.json').write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
