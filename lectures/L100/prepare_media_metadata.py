from pathlib import Path
import json,hashlib,subprocess,concurrent.futures
B=Path('lectures/L100');j=json.loads((B/'media_sources.json').read_text());spec=json.loads((B/'lecture.json').read_text())
for m in j['embedded']:
 n=m.get('filename',m.get('original_filename'));doi=m['doi'];m.setdefault('license','Article-provided recording; no separate open license verified.')
 if 'rstb20160069_si_002'in n:slide,author,desc=14,'Thomas et al. (2017)','Close-up of unequal squid eyes.'
 elif 'rstb20160069_si_003'in n:slide,author,desc=15,'Thomas et al. (2017)','Histioteuthis heteropsis makes ratcheting turns.'
 elif 'rstb20160069_si_004'in n:slide,author,desc=16,'Thomas et al. (2017)','Stigmatoteuthis dofleini changes orientation.'
 elif 'pnas.'in n:slide,author,desc=19,'Burford & Robison (2020)','Humboldt squid pigmentation during in situ activity.'
 elif 'Video 01_'in n:slide,author,desc=36,'Golikov et al. (2023)','Cirroteuthis muelleri spreads its web near the bottom at 3693 m.'
 elif 'Video 03_'in n:slide,author,desc=37,'Golikov et al. (2023)','Cirroteuthis muelleri contacts the bottom and retreats at 1506 m.'
 elif 'Video S2'in n:slide,author,desc=40,'Stuckless et al. (2023)','Blocking and shared feeding by Ceramaster granularis.'
 elif 'Video S4'in n:slide,author,desc=41,'Stuckless et al. (2023)','Hippasteria phrygiana skirts a neighbor.'
 elif 'Video S7'in n:slide,author,desc=42,'Stuckless et al. (2023)','Henricia lisa taps food with an arm tip.'
 elif 'Video S8'in n:slide,author,desc=43,'Stuckless et al. (2023)','Buccinum scalariforme approaches food.'
 else:raise ValueError(n)
 m.update(slide=slide,caption=f'{author}, {m["identifier"]}. {desc}',credit=author,original_media_url=m.get('url',m.get('original_media_url')),teaching_note=' '.join(spec['slides'][slide-2]['transcript']))
 if doi=='10.1098/rspb.2023.0640':m['teaching_note']+=' This is a temporal excerpt from the original article-linked ROV recording. Source timestamps and conversion details are recorded in media_sources.json; original resolution and playback speed are preserved.'
 if doi=='10.3390/biology12060774':m['teaching_note']+=' This is an author-provided time-lapse record. Recorded speed is preserved, and behavioral durations come from the article rather than the movie playback duration.'
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(B/m['path'])]));v=next(x for x in info['streams']if x['codec_type']=='video');m.update(display_aspect=v['width']/v['height'],duration_seconds=float(info['format']['duration']),width=v['width'],height=v['height'],audio_present=any(x['codec_type']=='audio'for x in info['streams']),sha256=hashlib.sha256((B/m['path']).read_bytes()).hexdigest(),bytes=(B/m['path']).stat().st_size)
 if isinstance(m['license'],dict):m['license']=m['license'].get('name',m['license'].get('id','Source license recorded'))
 if not m.get('license'):m['license']='Article-provided recording; no separate open license verified.'
 m['poster']=str(Path(m['path']).with_suffix('.jpg'));subprocess.run(['ffmpeg','-y','-v','error','-ss',str(min(10,m['duration_seconds']/3)),'-i',str(B/m['path']),'-frames:v','1',str(B/m['poster'])],check=True)
 print(slide,n,m['bytes'],flush=True)
j['not_embedded']=[];(B/'media_sources.json').write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
