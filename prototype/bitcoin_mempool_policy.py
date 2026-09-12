"""Bitcoin : politique locale de mempool, distincte du consensus."""
import unittest
def relayable(fee_rate,min_rate): return fee_rate>=min_rate
class Tests(unittest.TestCase):
 def test_fee_policy_accepts(self): self.assertTrue(relayable(5,2))
 def test_low_fee_policy_rejects(self): self.assertFalse(relayable(1,2))
if __name__=="__main__": unittest.main()
