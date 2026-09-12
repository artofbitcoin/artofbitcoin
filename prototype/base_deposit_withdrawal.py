"""Base : états déterministes d un dépôt/retrait."""
import unittest
STATES={"initiated":{"proven","failed"},"proven":{"minted"},"minted":set(),"failed":set()}
def allowed(old,new): return new in STATES.get(old,set())
class Tests(unittest.TestCase):
 def test_deposit_progresses(self): self.assertTrue(allowed("initiated","proven"))
 def test_minted_cannot_reinitiate(self): self.assertFalse(allowed("minted","initiated"))
if __name__=="__main__": unittest.main()
