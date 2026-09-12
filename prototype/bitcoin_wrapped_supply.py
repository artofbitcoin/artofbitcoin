"""Actif Bitcoin représenté : invariant de supply."""
import unittest
def supply_ok(locked,minted,burned): return locked>=0 and minted>=burned and minted-burned<=locked
class Tests(unittest.TestCase):
 def test_parity(self): self.assertTrue(supply_ok(100,100,0))
 def test_overmint_is_rejected(self): self.assertFalse(supply_ok(100,101,0))
if __name__=="__main__": unittest.main()
