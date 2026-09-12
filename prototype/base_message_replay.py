"""Base : identifiants de messages cross-chain anti-rejeu."""
import unittest
def accept(message,used): return bool(message) and message not in used
class Tests(unittest.TestCase):
 def test_fresh_message(self): self.assertTrue(accept("m1",set()))
 def test_replayed_message(self): self.assertFalse(accept("m1",{"m1"}))
if __name__=="__main__": unittest.main()
