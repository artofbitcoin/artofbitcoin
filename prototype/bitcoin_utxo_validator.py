"""Bitcoin : validation minimale d une entrée UTXO."""
import unittest
def valid_input(value,signature,script): return value>0 and bool(signature) and bool(script)
class Tests(unittest.TestCase):
 def test_valid_input(self): self.assertTrue(valid_input(100,"sig","pk"))
 def test_zero_value_rejected(self): self.assertFalse(valid_input(0,"sig","pk"))
if __name__=="__main__": unittest.main()
