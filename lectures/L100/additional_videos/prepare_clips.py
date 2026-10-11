"""Preserve source resolution, speed and audio when preparing the two excerpts."""
from pathlib import Path
import subprocess
B=Path(__file__).resolve().parent.parent;D=B/'additional_videos';S=B/'papers/original_media'
subprocess.run(['ffmpeg','-y','-v','error','-ss','48','-i',str(S/'Supplementary Video 02_HACON21-ROV019-Video2.mp4'),'-t','22','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(D/'Golikov_Video02_compatible.mp4')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-ss','25','-i',str(S/'Supplementary Video 04_037ROV02-tROVobs-LowerHD.mp4'),'-t','60','-c','copy','-movflags','+faststart',str(D/'Golikov_Video04_excerpt.mp4')],check=True)
