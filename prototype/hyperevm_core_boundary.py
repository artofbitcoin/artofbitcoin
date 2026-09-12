"""HyperEVM : distinguer EVM et confirmation HyperCore."""
import unittest
def confirmed(layer,finalized): return layer=="hypercore" and finalized
class Tests(unittest.TestCase):
 def test_evm_is_not_core(self): self.assertFalse(confirmed("evm",True))
 def test_core_confirmation(self): self.assertTrue(confirmed("hypercore",True))
if __name__=="__main__": unittest.main()
