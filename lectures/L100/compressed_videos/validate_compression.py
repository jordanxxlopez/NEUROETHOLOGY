from pathlib import Path
import subprocess,json,hashlib,re,concurrent.futures
B=Path(__file__).resolve().parent.parent;D=B/'compressed_videos'
rows=json.loads((D/'compression.json').read_text())
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
def validate(row):
 a=B/row['source_path'];b=B/row['compressed_path'];ja=probe(a);jb=probe(b);va=next(s for s in ja['streams']if s['codec_type']=='video');vb=next(s for s in jb['streams']if s['codec_type']=='video')
 for key in ['width','height','r_frame_rate']:assert va[key]==vb[key],(a,key,va[key],vb[key])
 assert vb['codec_name']=='h264' and vb['pix_fmt']=='yuv420p';assert abs(float(ja['format']['duration'])-float(jb['format']['duration']))<.05
 def timestamps(p):
  r=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','frame=best_effort_timestamp_time','-of','csv=p=0',str(p)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True);assert not r.stderr,r.stderr.decode();text=r.stdout.decode()
  return [float(line.split(',')[0])for line in text.splitlines()if line and line.split(',')[0].strip()]
 ta=timestamps(a);tb=timestamps(b);assert len(ta)==len(tb);vb['nb_read_frames']=str(len(tb))
 max_timing_difference=max(abs((x-ta[0])-(y-tb[0]))for x,y in zip(ta,tb));assert max_timing_difference<.002,(a,max_timing_difference)
 aa=[s for s in ja['streams']if s['codec_type']=='audio'];ab=[s for s in jb['streams']if s['codec_type']=='audio'];assert len(aa)==len(ab)
 if aa:
  def audio_hash(p):return subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:a','-c','copy','-f','hash','-hash','sha256','-']).decode().strip()
  assert audio_hash(a)==audio_hash(b)
 # ffprobe frame enumeration above fully decodes each video once.
 start=5 if float(ja['format']['duration'])>10 else 0
 cmd=['ffmpeg','-v','info','-ss',str(start),'-i',str(a),'-ss',str(start),'-i',str(b),'-t','3','-lavfi','[0:v][1:v]ssim','-an','-f','null','-']
 r=subprocess.run(cmd,stderr=subprocess.PIPE,stdout=subprocess.DEVNULL,check=True);matches=re.findall(r'All:([0-9.]+)',r.stderr.decode());score=float(matches[-1]);assert score>.95,(a,score)
 result={'file':b.name,'width':vb['width'],'height':vb['height'],'frame_rate':vb['r_frame_rate'],'frames':vb['nb_read_frames'],'duration_seconds':jb['format']['duration'],'audio_packets_identical':True,'maximum_relative_frame_timing_difference_seconds':max_timing_difference,'full_decode':'passed','three_second_sample_ssim':score,'source_sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'compressed_sha256':hashlib.sha256(b.read_bytes()).hexdigest()};print(b.name,'passed','SSIM',score,flush=True);return result
with concurrent.futures.ThreadPoolExecutor(max_workers=2)as ex:results=list(ex.map(validate,rows))
(D/'validation.json').write_text(json.dumps(results,indent=2)+'\n')
