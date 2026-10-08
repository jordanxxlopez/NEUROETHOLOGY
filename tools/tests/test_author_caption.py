"""An authentic author surname must not trigger generated-image rejection."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from style_rules import MADE_IMAGE_WORDS
from build_lecture import check_image,SpecError
class AuthorCaptionTests(unittest.TestCase):
 def test_original_ai_article(self):
  check_image({'kind':'article','caption':'Ai et al. (2017), Fig. 3A. Recorded vibration responses.','source_url':'https://doi.org/10.1523/JNEUROSCI.0044-17.2017'},'test')
 def test_generated_images_remain_rejected(self):
  for text in ['AI image','ai image','Ai generated image','Ai et al. (2017), Fig. 3. Redrawn traces.','AI-generated diagram','simulated traces']:
   with self.subTest(text=text):self.assertIsNotNone(MADE_IMAGE_WORDS.search(text))
if __name__=='__main__':unittest.main()
