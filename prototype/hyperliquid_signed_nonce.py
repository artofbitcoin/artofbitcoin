"""Hyperliquid : nonce strictement croissant."""
import unittest
def valid_nonce(nonce,last): return isinstance(nonce,int) and nonce>last
class Tests(unittest.TestCase):
 def test_next_nonce(self): self.assertTrue(valid_nonce(4,3))
 def test_reuse_rejected(self): self.assertFalse(valid_nonce(3,3))
if __name__=="__main__": unittest.main()
