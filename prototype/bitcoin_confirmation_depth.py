"""Bitcoin : profondeur de confirmations et reorganisation."""
import unittest
def sufficiently_confirmed(tip,height,required): return tip>=height and tip-height+1>=required
class Tests(unittest.TestCase):
 def test_required_depth(self): self.assertTrue(sufficiently_confirmed(105,100,6))
 def test_shallow_depth(self): self.assertFalse(sufficiently_confirmed(104,100,6))
if __name__=="__main__": unittest.main()
