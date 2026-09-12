"""HyperEVM : validation d une commande CoreWriter."""
import unittest
def valid(action,nonce): return bool(action) and isinstance(nonce,int) and nonce>=0
class Tests(unittest.TestCase):
 def test_valid_command(self): self.assertTrue(valid("transfer",0))
 def test_empty_action(self): self.assertFalse(valid("",0))
if __name__=="__main__": unittest.main()
