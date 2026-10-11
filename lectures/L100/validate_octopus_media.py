from pathlib import Path
import subprocess,json
B=Path('lectures/L100');j=json.load(open(B/'media_sources.json'));old=json.load(open(B/'media_validation.json'));old=[m for m in old if m['slide'] not in [34,45]]
for m in j['embedded']:
 if m['doi']!='10.1098/rspb.2023.0640':continue
 def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(B/p)]))
 src=probe(m['original_path']);clip=probe(m['path']);sv=next(s for s in src['streams']if s['codec_type']=='video');cv=next(s for s in clip['streams']if s['codec_type']=='video')
 assert (sv['width'],sv['height'])==(cv['width'],cv['height']);assert sv['r_frame_rate']==cv['r_frame_rate'];assert cv['codec_name']=='h264' and cv['pix_fmt']=='yuv420p'
 subprocess.run(['ffmpeg','-v','error','-i',str(B/m['path']),'-f','null','-'],check=True)
 old.append(dict(slide=m['slide'],full_decode='passed',width=cv['width'],height=cv['height'],frame_rate=cv['r_frame_rate'],audio_track_preserved=any(s['codec_type']=='audio'for s in src['streams'])==any(s['codec_type']=='audio'for s in clip['streams']),temporal_excerpt=True,source_start_seconds=m['source_start_seconds'],source_end_seconds=m['source_end_seconds'],clip_duration_seconds=clip['format']['duration'],conversion=m['conversion']))
 print(m['slide'],'passed',flush=True)
(B/'media_validation.json').write_text(json.dumps(sorted(old,key=lambda m:m['slide']),indent=2)+'\n')
