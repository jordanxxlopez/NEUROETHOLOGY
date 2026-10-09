"""Use the current repository builder with a long special-topic title layout."""
import sys,json
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parents[1]/'tools'))
import build_lecture as b
from pptx.util import Pt

def special_title(self):
 s=self.new_slide();t=self.t;img=self.spec['title_image'];b.check_image(img,'title slide');b.rect(s,0,0,b.W/2,b.H,t['title_bg'])
 def text(x,y,w,h,value,pt,col,name=None,bold=False):
  _,tf=b.textbox(s,x,y,w,h,name);b.write_paras(tf,[value],pt,col,space_after=0)
  for p in tf.paragraphs:
   for r in p.runs:r.font.bold=bold
 text(.65,.65,5.5,.4,self.course['course'],12,'000000')
 text(.65,1.25,5.5,.45,'Lecture 41 · Special topic',18,'000000')
 text(.65,2.05,5.35,3.35,self.meta['title'],25,t['title_text'],'Lecture title',True)
 text(.65,5.70,5.5,.35,self.meta['date'],16,'000000')
 text(.65,6.25,5.5,.6,self.course['instructor']+'\n'+self.course['instructor_title'],12,'000000')
 b.picture_contain(s,self.path(img['path']),7.05,1.1,5.55,5.1);self.caption(s,7.05,6.4,5.55,img['caption'])
 s.notes_slide.notes_text_frame.text=self.meta['title']+'\nLecture 41. '+self.meta['date']+'\n\nImage: '+img['caption']+' Credit: '+img['credit']+'. License: '+img['license']+'. Source: '+img['source_url']+'\n\nReferences:\n'+'\n'.join(self.spec['title_refs'])
b.Deck.title_slide=special_title
sys.argv=[str(BASE.parents[1]/'tools/build_lecture.py'),str(BASE/'lecture.json')]
b.main()
