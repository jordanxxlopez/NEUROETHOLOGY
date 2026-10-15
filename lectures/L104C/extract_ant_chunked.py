from pathlib import Path
import requests,json,concurrent.futures,struct,zlib,time,subprocess,hashlib
P=Path('/workspace/scratch/L104C');idx=json.load(open(P/'ant_video_archive_index.json'));url='https://zenodo.org/records/10894114/files/sample_videos.zip?download=1';chunkdir=P/'ant_chunks';chunkdir.mkdir(exist_ok=True)
names=['sample_video_ant_40_visit_4.mp4','sample_video_ant_40_visit_5.mp4','sample_video_ant_140_visit_2.mp4','sample_video_ant_140_visit_5.mp4'];rows=[r for r in idx['files'] if Path(r['name']).name in names];jobs=[]
for row in rows:
 begin=row['offset'];end=begin+row['compressed_bytes']+512
 for st in range(begin,end+1,4*1024*1024):jobs.append((st,min(end,st+4*1024*1024-1)))
def get(t):
 st,en=t;dest=chunkdir/f'{st}_{en}.bin'
 if dest.exists() and dest.stat().st_size==en-st+1:return dest
 for attempt in range(2):
  try:
   r=requests.get(url,headers={'Range':f'bytes={st}-{en}'},timeout=45);assert r.status_code==206 and r.headers.get('Content-Range','').startswith(f'bytes {st}-'),(r.status_code,r.headers.get('Content-Range'));assert len(r.content)==en-st+1;dest.write_bytes(r.content);return dest
  except Exception:
   if attempt:raise
with concurrent.futures.ThreadPoolExecutor(8) as pool:
 for i,p in enumerate(pool.map(get,jobs)):print('chunk',i+1,'/',len(jobs),flush=True)
access=[]
for row in rows:
 st=row['offset'];en=st+row['compressed_bytes']+512;parts=[chunkdir/f'{a}_{min(en,a+4*1024*1024-1)}.bin' for a in range(st,en+1,4*1024*1024)];b=b''.join(x.read_bytes() for x in parts);assert b[:4]==b'PK\x03\x04';v=struct.unpack_from('<4s5H3L2H',b);off=30+v[-2]+v[-1];data=zlib.decompress(b[off:off+row['compressed_bytes']],-15);assert len(data)==row['bytes'];name=Path(row['name']).name;dest=P/'downloads'/name;dest.write_bytes(data);access.append({'name':name,'source_file':row['name'],'url':url,'saved':True,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'article_doi':'10.1016/j.isci.2024.109935','dataset_doi':'10.5281/zenodo.10894114'});print('EXTRACTED',name,len(data),flush=True)
P.joinpath('ant_movie_access.json').write_text(json.dumps(access,indent=2))
