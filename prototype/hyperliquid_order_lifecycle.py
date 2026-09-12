"""Hyperliquid : transitions explicites d un ordre."""
import unittest
T={"new":{"accepted","cancelled"},"accepted":{"filled","cancelled"},"filled":set(),"cancelled":set()}
def allowed(a,b): return b in T.get(a,set())
class Tests(unittest.TestCase):
 def test_fill(self): self.assertTrue(allowed("accepted","filled"))
 def test_reopen_rejected(self): self.assertFalse(allowed("filled","accepted"))
if __name__=="__main__": unittest.main()
