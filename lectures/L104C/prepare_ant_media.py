from pathlib import Path
import json,hashlib,subprocess,csv,shutil,concurrent.futures,zlib,struct
P=Path('/workspace/scratch/L104C');R=Path('/workspace/NEUROETHOLOGY/lectures/L104C');access=json.load(open(P/'ant_movie_access.json'));meta=list(csv.DictReader(open(P/'OpLan_D1_metadata.csv',encoding='utf-8-sig'),delimiter=';'));rows=json.load(open(R/'media_preparation.json'))
# Independent ZIP checksum validation of the extracted originals.
b=P.joinpath('ant_zip_tail.bin').read_bytes();pos=b.find(b'PK\x01\x02');checks={}
while pos<len(b)-46 and b[pos:pos+4]==b'PK\x01\x02':
 vals=struct.unpack_from('<4s6H3L5H2L',b,pos);nl,el,cl=vals[10:13];name=b[pos+46:pos+46+nl].decode('utf-8','replace');checks[Path(name).name]=vals[7];pos+=46+nl+el+cl
for x in access:
 f=P/'downloads'/x['name'];assert zlib.crc32(f.read_bytes())&0xffffffff==checks[x['name']];x['zip_crc32_verified']=True

def f(x):
 x=dict(x);name=x['name'];src=P/'downloads'/name;stem=Path(name).stem;dst=R/'media/delivery'/(stem+'.mp4');poster=R/'posters'/(stem+'.jpg');start=10;end=100
 subprocess.run(['ffmpeg','-v','error','-ss',str(start),'-i',str(src),'-t',str(end-start),'-map','0:v:0','-map','0:a?','-c:v','libx264','-crf','24','-preset','fast','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart','-y',str(dst)],check=True)
 d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(dst)]));v=next(t for t in d['streams'] if t['codec_type']=='video');subprocess.run(['ffmpeg','-v','error','-ss','10','-i',str(dst),'-frames:v','1','-y',str(poster)],check=True);dec=subprocess.run(['ffmpeg','-v','error','-i',str(dst),'-f','null','-'],capture_output=True,text=True)
 bits=stem.split('_');ant=bits[3];visit=bits[5];md=next(r for r in meta if r['Ant']==ant and r['Visit']==visit)
 x.update({'delivery_file':str(dst.relative_to(R)),'poster':str(poster.relative_to(R)),'start_seconds':start,'end_seconds':end,'duration_seconds':float(d['format']['duration']),'width':v['width'],'height':v['height'],'decode_passed':dec.returncode==0 and not dec.stderr,'delivery_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'license':'CC BY 4.0, as declared by the research data archive','original_identifier':x['source_file'],'credit':'Galante and colleagues, original study data archive','ant_id':ant,'visit':visit,'caffeine_condition':md['Treatment'],'source_metadata':md,'embedded':False,'conversion':'90-second excerpt from 10 to 100 seconds of the original research recording; original dimensions, scene order, playback speed and available audio preserved. Exact slide placement and final contextual interval review pending.'});return x
out=list(concurrent.futures.ThreadPoolExecutor(2).map(f,access));rows=[r for r in rows if not r['name'].startswith('sample_video_ant')]+out;R.joinpath('media_preparation.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');shutil.copy2(P/'ant_movie_access.json',R/'ant_movie_access.json');shutil.copy2(P/'OpLan_D1_metadata.csv',R/'ant_source_metadata.csv');print('Prepared',len(out),'ant excerpts; all decode:',all(x['decode_passed'] for x in out),'; total available originals:',len(rows))
