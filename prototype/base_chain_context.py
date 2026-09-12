"""Base : contexte réseau L1/L2 explicite."""
import unittest
def valid(chain,l1,l2): return chain==8453 and l1>=0 and l2>=0
class Tests(unittest.TestCase):
 def test_valid(self): self.assertTrue(valid(8453,1,2))
 def test_wrong_chain(self): self.assertFalse(valid(1,1,2))
if __name__=="__main__": unittest.main()
