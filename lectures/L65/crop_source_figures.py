"""Run the repository crop tool using the original PDF crop-box geometry."""
import pathlib,runpy,shutil,sys
d=pathlib.Path(__file__).resolve().parent
which=shutil.which
shutil.which=lambda name,*a,**kw: None if name=="pdftoppm" else which(name,*a,**kw)
sys.argv=["crop_panels.py",str(d/"crops.json")]
runpy.run_path(d.parents[1]/"tools/crop_panels.py",run_name="__main__")
