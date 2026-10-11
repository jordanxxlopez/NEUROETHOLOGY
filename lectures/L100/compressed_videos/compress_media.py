from pathlib import Path
import json,subprocess,concurrent.futures,time
B=Path('lectures/L100');D=B/'compressed_videos'
allmedia=json.load(open(B/'media_sources.json'))['embedded']+json.load(open(B/'additional_videos/media_sources.json'))['added']
selected=[m for m in allmedia if m['bytes']>100000000]
def encode(m):
 src=B/m['path'];out=D/src.name
 command=['ffmpeg','-y','-v','error','-i',str(src),'-map','0:v:0','-map','0:a?','-c:v','libx264','-preset','medium','-crf','21','-threads','2','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(out)]
 t=time.time();subprocess.run(command,check=True);print(src.name,src.stat().st_size,'->',out.stat().st_size,'seconds',round(time.time()-t),flush=True)
 return dict(source_path=m['path'],compressed_path=str(out.relative_to(B)),source_bytes=src.stat().st_size,compressed_bytes=out.stat().st_size,crf=21,preset='medium',audio='copied without re-encoding')
with concurrent.futures.ThreadPoolExecutor(max_workers=2)as ex:results=list(ex.map(encode,selected))
(D/'compression.json').write_text(json.dumps(results,indent=2)+'\n')
